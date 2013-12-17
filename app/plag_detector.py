from app import app
import sys
import os
import cPickle

sys.path.append(app.config['PLAGCOMPS_LOC'])

from plagcomps.controller import Controller

class PlagDetector:
    '''
    Class used (for the moment) to interact with the detection
    module. Should be removed later once the detection module
    has been nicely packaged.
    '''

    def get_passages(self, filename=None):
        if filename is None:
            filename = os.path.join(app.config['APP_ROOT'], 'static/head_training_sample.txt')
        elif filename == 'pickle':
            pickle_file = os.path.join(app.config['APP_ROOT'], 'static/passages.dat')
            f = file(pickle_file, 'rb')
            passages = cPickle.load(f)
            f.close()
        else:

            c = Controller(filename)

            features = [
                'averageWordLength',
                'averageSentenceLength',
                'get_avg_word_frequency_class',
                'get_punctuation_percentage',
                'get_stopword_percentage'
            ]
            print 'created a controller, runnign the sucker'
            passages = c.test('paragraph', features, 'kmeans', 2, display_output=True)

        return passages



