# Tests that the environment works correctly

import matplotlib
import sklearn
import pandas
import scipy
import numpy

from scipy.misc import imread

from sklearn import svm

def test_svm():
    """Trains a SVM"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    clf.predict([[2., 2.]])

