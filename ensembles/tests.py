# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas as pd
import scipy
import numpy as np
import ete3
import skopt

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from skopt import BayesSearchCV


def getdata():
    X = np.array([[0, 0], [1, 1]])
    y = [0, 1]
    return X, y


def buildtree(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf


# Tests

def test_tree():
    """Trains a Tree"""
    X, y = getdata()
    clf = buildtree(X, y)
    clf.predict([[2., 2.]])


def test_xgb():
    """Trains an XGB model"""
    X, y = getdata()
    clf = XGBClassifier()
    clf.fit(X, y)
    clf.predict([[2., 2.]])
