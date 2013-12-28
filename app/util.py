from app import app
import os
import glob

def get_file_options():
    static_file_loc = os.path.join(app.config['APP_ROOT'], 'static/sample_docs')
    sample_corpus_loc = os.path.join(app.config['PLAGCOMPS_LOC'], 'plagcomps/sample_corpus')

    # Grab document options from both the plagapp static sample docs
    # and the sample corpus directory in the plagcomps repo
    local_file_options = glob.glob(static_file_loc + '/*.txt')
    sample_corpus_options = glob.glob(sample_corpus_loc + '/*.txt')
    file_options = [os.path.basename(f) for f in local_file_options + sample_corpus_options]
    without_extensions = [os.path.splitext(f)[0] for f in file_options]

    full_paths = [os.path.join(static_file_loc, f) for f in local_file_options] + \
                 [os.path.join(sample_corpus_loc, f) for f in sample_corpus_options]

    return full_paths, without_extensions

def get_file_short_names():
    full_paths, file_names = get_file_options()

    return zip(file_names, file_names)

def get_file_to_full_paths():
    full_paths, file_names = get_file_options()

    return {name : full for name, full in zip(file_names, full_paths)}

def get_feature_options():
    '''
    '''
    options = [
        'average_word_length',
        'average_sentence_length',
        'stopword_percentage',
        'punctuation_percentage',
        'syntactic_complexity',
        'avg_internal_word_freq_class',
        'avg_external_word_freq_class'
    ]

    return zip(options, options)

def get_atom_options():
    options = [
        'paragraph',
        'sentence',
        'word'
    ]

    return zip(options, options)

def get_cluster_options():
    options = [
        'kmeans',
        'agglom',
        'hmm'
    ]

    return zip(options, options)