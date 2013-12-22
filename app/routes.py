# Import the actual Flask app
from app import app

from flask import render_template, redirect, jsonify, request, url_for
import sys
import os

from forms import PlagSelection
from plag_detector import PlagDetector

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
        return redirect(url_for('view_doc', doc_name=form.file_name.data))

    # Otherwise display options
    return render_template('select_doc.html',
                form = form)

@app.route('/view_doc', methods=['GET'])
def view_doc():
    doc_name = request.args['doc_name']
    print 'Using', doc_name
    all_passages = PlagDetector().get_passages(doc_name)
    features = all_passages[0].features.keys()
    print 'Got is features!', features

    return render_template('view_doc.html',
        doc_name = 'some doc',
        passages = all_passages,
        features = features)
    

# TODO write this to process an AJAX request for information
# about a given passage.
# How will we access the passages??
@app.route('/_get_features')
def get_features():
    print 'got args', request.args
    return jsonify(key='it worked!')

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