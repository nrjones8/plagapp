from flask import Flask, render_template
import sys
import os

# NOTE Terribly hacky right now. This should NOT live in plagapp,
# but should instead be imported from the actual plagcomps repo
from passage import Passage
# NOTE this should be removed later too
import cPickle as pickle

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/index/')
@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/<docname>')
def single_doc(docname):
    # f = file('static/' + docname + '.txt', 'r')
    # content = f.read().decode('utf8')
    # f.close()
    content = 'here is some content to display'

    return render_template('view_doc.html',
                doc_name = docname,
                doc_content = content)


# TODO write this to process an AJAX request for information
# about a given passage.
# How will we access the passages??
@app.route('/_get_feautures')
def get_features():
    pass

@app.route('/sample/')
def show_sample():
    '''
    Use a pickled file of passage objects parsed from static/training_sample.txt
    to sample the front-end
    '''
    passage_pickle = file(os.path.join(APP_ROOT, 'static/passages.dat'), 'rb')
    all_passages = pickle.load(passage_pickle)
    passage_pickle.close()

    return render_template('view_doc.html',
        doc_name = 'Sample',
        passages = all_passages)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(debug = True, port=port)
    print