# Import the actual Flask app
from app import app

from flask import render_template, redirect, jsonify, request, url_for
import sys
import os

from forms import PlagSelection
from plag_detector import PlagDetector
from util import get_file_to_full_paths, get_file_options

@app.route('/index/')
@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/select_doc/', methods=['GET', 'POST'])
def select_doc():
    form = PlagSelection()

    # If file has been selected, perform detection and display results
    if form.validate_on_submit():
        kwargs = {
            form.doc_name.name : form.doc_name.data,
            form.features.name : form.features.data,
            form.atom.name : form.atom.data,
            form.cluster_method.name : form.cluster_method.data,
            form.k.name : form.k.data
        }
        
        return redirect(url_for('view_doc', **kwargs))
    elif len(form.errors) > 0:
        # TODO Make a nice error msg
        return str(form.errors)
    else:
        # Otherwise display options
        return render_template('select_doc.html',
                    form = form)

@app.route('/view_doc/<doc_name>', methods=['GET'])
def view_doc(doc_name):
    file_to_full_path = get_file_to_full_paths()
    if doc_name in file_to_full_path:
        full_path = file_to_full_path[doc_name]
    else:
        # TODO Make a nice error msg
        return 'some error'

    atom_type = request.args.get('atom')
    features = request.args.getlist('features')
    cluster_method = request.args.get('cluster_method')
    k = int(request.args.get('k'))

    all_passages = PlagDetector().get_passages(atom_type, features, cluster_method, k, full_path)
    feature_names = all_passages[0].features.keys()

    return render_template('view_doc.html',
        atom_type = atom_type,
        cluster_method = cluster_method,
        k = k,
        passages = all_passages,
        features = feature_names,
        doc_name = doc_name)
    

#@app.route('/view_source_doc/<doc_name>', methods=['GET'])
#def view_source_doc(doc_name):
@app.route('/test_source_doc')
def view_source_doc():
    full_path = os.path.join(app.config['APP_ROOT'], 'static/sample_docs/test2.txt')
    xml_path = os.path.join(app.config['APP_ROOT'], 'static/sample_docs/test2.xml')

    atom_type = 'paragraph'

    passages = PlagDetector().get_ground_truth_passages(atom_type, full_path, xml_path)
    
    return render_template('view_source_doc.html',
        passages = passages,
        atom_type = atom_type)




@app.route('/sample/')
def show_sample():
    '''
    Use a pickled file of passage objects parsed from static/training_sample.txt
    to sample the front-end
    '''
    #all_passages = PlagDetector().get_passages('pickle')
    all_passages = PlagDetector().get_passages()
    features = all_passages[0].features.keys()

    return render_template('view_doc.html',
        doc_name = 'Sample',
        passages = all_passages,
        features = features)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, port=port)