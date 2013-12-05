from flask import Flask, render_template

app = Flask(__name__)
#app.config.from_object()
# TODO put this in a config file

@app.route('/')
def main_page():
    return "Let's detect some plag"

@app.route('/<docname>')
def single_doc(docname):
    # f = file('static/' + docname + '.txt', 'r')
    # content = f.read().decode('utf8')
    # f.close()
    content = 'here is some content to display'

    return render_template('view_doc.html',
                doc_name = docname,
                doc_content = content)



if __name__ == '__main__':
    app.run(debug = True)
    print