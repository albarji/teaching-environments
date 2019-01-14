# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas as pd
import scipy
import numpy as np
import ete3
import graphviz
import skopt

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from graphviz import Source
from xgboost import XGBClassifier
from skopt import BayesSearchCV


# Auxiliary functions
def plottree(decisiontree, features_names=None, class_names=None):
    """Returns a graphviz visualization of a scikit-learn decision tree

    Inputs
        - decisiontree: tree to visualize
        - feature_names: iterable with the names of the features present in the data.
        - class_names: iterable with the names of the classes present in the data, in increasing order.

    If the call to this function is the last line of a notebook cell, the tree is rendered automatically.
    """
    dot_data = tree.export_graphviz(
        decisiontree,
        out_file=None,
        filled=True,
        rounded=True,
        rotate=True,
        feature_names=features_names,
        class_names=class_names
    )
    return Source(dot_data)


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


def plot_tree():
    """Plots a Tree"""
    X, y = getdata()
    clf = buildtree(X, y)
    plottree(clf)


def test_xgb():
    """Trains an XGB model"""
    X, y = getdata()
    clf = XGBClassifier()
    clf.fit(X, y)
    clf.predict([[2., 2.]])
