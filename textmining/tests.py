# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas
import scipy
import numpy

from sklearn import svm

from matplotlib.figure import Figure
from matplotlib.contour import ContourSet
from matplotlib.lines import Line2D


def test_svm():
    """Trains a SVM"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    clf.predict([[2., 2.]])

