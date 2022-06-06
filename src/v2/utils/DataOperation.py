from __future__ import division
import numpy as np
import math
import sys

def accuracyScore(y_true, y_pred):
    # compare y_true to y_pred and return the accuracy
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy