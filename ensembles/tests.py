# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas
import scipy
import numpy
import ete3
import graphviz

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from graphviz import Source


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


def buildtree(X, y):
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf


# Tests

def test_tree():
    """Trains a Tree"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = buildtree(X, y)
    clf.predict([[2., 2.]])


def plot_tree():
    """Plots a Tree"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = buildtree(X, y)
    plottree(clf)
