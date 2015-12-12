import nltk
import nltk.tag, nltk.data
from nltk.tag.brill import BrillTagger
from nltk.tag.perceptron import PerceptronTagger


class TextTagger(object):
    def __init__(self):
        pass
        
    def pos_tag(self, sentences, tagger):

        pos = map(tagger.tag, sentences)       

        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]

        return pos