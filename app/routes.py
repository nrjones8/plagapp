# Import the actual Flask app
from app import app

from flask import render_template, jsonify, request
import sys
import os

from plag_detector import PlagDetector

@app.route('/index/')
@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/<docname>')
def single_doc(docname):
    content = 'here is some content to display'

    return render_template('view_doc.html',
                doc_name = docname,
                doc_content = content)


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
    all_passages = PlagDetector().get_passages('pickle')
    features = all_passages[0].features.keys()

    return render_template('view_doc.html',
        doc_name = 'Sample',
        passages = all_passages,
        features = features)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, port=port)