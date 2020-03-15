# Tests that the environment works correctly

import tensorflow
import keras
import matplotlib
import sklearn
import pandas
import requests
import scipy
import numpy

from eli5 import explain_prediction, format_as_image

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Activation
from keras.layers.core import Dense
from keras.utils import np_utils

from skimage.io import imread
from skimage.transform import resize

from sklearn.model_selection import train_test_split

import torch


def test_keras():
    """Trains a small network on MNIST with Keras"""
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.astype('float32') / 255
    trainvectors = X_train.reshape(60000, 784)
    Y_train = np_utils.to_categorical(y_train, 10)
    model = Sequential()
    model.add(Dense(10, input_shape=(784,)))
    model.add(Activation('softmax'))
    model.summary()
    model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    model.fit(trainvectors, Y_train, epochs=1)



def test_requests():
    """Tries to perform a request to a public server"""
    r = requests.get('http://www.google.com/search?q=deep+learning')
    print(r.text)
