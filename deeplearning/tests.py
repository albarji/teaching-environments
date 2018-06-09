# Tests that the environment works correctly

import tensorflow
import keras
import matplotlib
import sklearn
import pandas

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Activation
from keras.layers.core import Dense
from keras.utils import np_utils


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

