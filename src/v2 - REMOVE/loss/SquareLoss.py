from __future__ import division
import numpy as np
from .Loss import Loss

class SquareLoss(Loss):
    def __init__(self): pass

    def loss(self, y_true, y_pred):
        return 0.5 * np.power((y_true - y_pred), 2)
    
    def gradient(self, y_true, y_pred):
        return -(y_true - y_pred)