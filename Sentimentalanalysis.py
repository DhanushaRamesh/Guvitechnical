import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
def word_feats(words):
    return dict((word,True)for word in words)
positive_vocab=['awesome','outstanding','fantastic',')']
negative_vocab=['bad','terrible','hate','(']
neutral_vocab=['move','the','sound','was','is']
positive_features=[(word_feats(pos),'pos')for pos in positive_vocab]
negative_features=[(word_feats(neg),'neg')for neg in negative_vocab]
neutral_features=[(word_feats(neu),'neu')for neu in neutral_vocab]
train_set=negative_features+positive_features+neutral_features
classifier=NaiveBayesClassifier.train(train_set)
neg=0
pos=0
