# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas
import scipy
import numpy
import seaborn
import spacy
import gensim
import subprocess

from sklearn import svm

from sklearn.decomposition import LatentDirichletAllocation


def test_svm():
    """Trains a SVM"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    clf.predict([[2., 2.]])


def test_spacy_nlp():
    """Runs an NLP pipeline in spaCy"""
    subprocess.run(["python", "-m" ,"spacy", "download", "en"])
    nlp = spacy.load('en')
    sentence = "The black cat sat peacefully on the mat."
    nlp(sentence)
