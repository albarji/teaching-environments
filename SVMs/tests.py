# Tests that the environment works correctly

import matplotlib
matplotlib.use('TkAgg')
import sklearn
import pandas
import scipy
import numpy as np

from scipy.misc import imread
from sklearn.externals.six.moves import xrange

from sklearn import svm

import tkinter as Tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.contour import ContourSet
from matplotlib.lines import Line2D

import prox_tv as ptv


def test_svm():
    """Trains a SVM"""
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)  
    clf.predict([[2., 2.]])


def test_proxtv():
    """Tests proxTV"""
    N = 1000
    s = np.zeros((N,1))
    s[int(N/4):int(N/2)] = 1
    s[int(N/2):int(3*N/4)] = -1
    s[int(3*N/4):int(-N/8)] = 2

    n = s + 0.5*np.random.rand(*np.shape(s))

    lam=20
    f = ptv.tv1_1d(n,lam)

