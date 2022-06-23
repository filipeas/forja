from __future__ import division
import numpy as np
from .Loss import Loss
from REMOVER.utils import accuracyScore

class CrossEntropy(Loss):
    def __init__(self): pass

    def loss(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        return - y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred)
    
    def gradient(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        return - (y_true / y_pred) + (1 - y_pred) / (1 - y_pred)
    
    def acc(self, y_true, y_pred):
        return accuracyScore(np.argmax(y_true, axis=1), np.argmax(y_pred, axis=1))