from __future__ import division
from itertools import combinations_with_replacement
from matplotlib.pyplot import axis
import numpy as np
import math
import sys

def batch_iterator(X, y=None, batch_size=64):
    """
    Simple batch generator
    """
    n_samples = X.shape[0]
    for i in np.arange(0, n_samples, batch_size):
        begin, end = i, min(i + batch_size, n_samples)
        if y is not None:
            yield X[begin:end], y[begin:end]
        else:
            yield X[begin:end]

def standardize(X):
    """
    Standardize the dataset X
    """
    X_std = X
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    for col in range(np.shape(X)[1]):
        if std[col]:
            X_std[:, col] = (X_std[:, col] - mean[col]) / std[col]
    return X_std