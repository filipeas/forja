from __future__ import division
import numpy as np
import math
import sys

def accuracyScore(y_true, y_pred):
    # compare y_true to y_pred and return the accuracy
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy

def determinePadding(filter_shape, output_shape='same'):
    """
    Method which calculates the padding based on the 
    specified output shape and the shape of the filters.
    """
    # no padding
    if output_shape == 'valid':
        return (0, 0), (0, 0)
    elif output_shape == 'same':
        filter_height, filter_width = filter_shape
        
        # derived from:
        # output_height = (height + pad_h - filter_heigth) / stride + 1
        # in this case output_height = height and stride = 1.
        # this gives the expression for the padding below.
        pad_h1 = int(math.floor((filter_height - 1) / 2))
        pad_h2 = int(math.ceil((filter_height - 1) / 2))
        pad_w1 = int(math.floor((filter_width - 1) / 2))
        pad_w2 = int(math.ceil((filter_width - 1) / 2))
        
        return (pad_h1, pad_h2), (pad_w1, pad_w2)

def imageToColumn(images, filter_shape, stride, output_shape='same'):
    """
    Method which turns the image shaped input to column shape.
    Used during the forward pass.
    """
    filter_height, filter_width = filter_shape
    
    pad_h, pad_w = determinePadding(filter_shape, output_shape)
    
    # add padding to the image