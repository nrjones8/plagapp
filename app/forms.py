from app import app
import os
from util import get_file_short_names, get_feature_options, get_atom_options, get_cluster_options

from flask_wtf import Form
from wtforms import SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class PlagSelection(Form):
    file_options = get_file_short_names()
    doc_name = SelectField('Doc Name', choices=file_options)

    feature_options = get_feature_options()
    features = SelectMultipleField('Features (Select Multiple)', choices=feature_options)

    atom_options = get_atom_options()
    atom = SelectField('Atom Type', choices=atom_options)

    cluster_options = get_cluster_options()
    cluster_method = SelectField('Cluster Method', choices=cluster_options)

    k_options = [2, 3, 4, 5]
    k = SelectField('k', choices=zip(k_options, k_options), coerce=int)
