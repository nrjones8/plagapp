from app import app
import sys
import os
import cPickle

sys.path.append(app.config['PLAGCOMPS_LOC'])

from plagcomps.intrinsic import get_plagiarism_passages

class PlagDetector:
    '''
    Class used (for the moment) to interact with the detection
    module. Should be removed later once the detection module
    has been nicely packaged.
    '''

    def get_passages(self, atom_type, features, cluster_method, k, filename=None):
        if filename == 'pickle':
            pickle_file = os.path.join(app.config['APP_ROOT'], 'static/sample_docs/passages.dat')
            f = file(pickle_file, 'rb')
            passages = cPickle.load(f)
            f.close()

            return passages
        elif filename is None:
            filename = os.path.join(app.config['APP_ROOT'], 'static/sample_docs/head_training_sample.txt')
    
        f = file(filename, 'rb')
        content = f.read()
        f.close()
        
        passages = get_plagiarism_passages(content, atom_type, features, cluster_method, k)

        return passages



