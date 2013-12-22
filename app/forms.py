from app import app
import os

from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired

def get_file_options():
    static_file_loc = os.path.join(app.config['APP_ROOT'], 'static/sample_docs')
    sample_corpus_loc = os.path.join(app.config['PLAGCOMPS_LOC'], 'plagcomps/sample_corpus')

    # Grab document options from both the plagapp static sample docs
    # and the sample corpus directory in the plagcomps repo
    local_file_options = os.listdir(static_file_loc)
    sample_corpus_options = os.listdir(sample_corpus_loc)
    file_options = local_file_options + sample_corpus_options

    full_paths = [os.path.join(static_file_loc, f) for f in local_file_options] + \
                 [os.path.join(sample_corpus_loc, f) for f in sample_corpus_options]
                 
    return zip(full_paths, file_options)

class PlagSelection(Form):
    file_options = get_file_options()
    print file_options
    file_name = SelectField('File Name', choices=file_options)