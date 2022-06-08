from __future__ import print_function, division
import numpy as np
from v2.layer.ConstantPadding2D import ConstantPadding2D

class ZeroPadding2D(ConstantPadding2D):
    """
    Adds rows and columns of zero values to the input.
    Expects the input to be of shape (batch_size, channels, height, width)
    
    Parameters:
    -----------
    padding:
        tuple
        The amount of padding along the height and width dimension of the input.
        If (pad_h, pad_w) the same symmetric padding is applied along height and width dimension.
        If((pad_h0, pad_h1), (pad_w0, pad_w1)) the specified padding is added to beginning and end of
        the height and width dimension.
    """
    def __init__(self, padding):
        self.padding = padding
        if isinstance(padding[0], int):
            self.padding = ((padding[0], padding[0]), padding[1])
        if isinstance(padding[1], int):
            self.padding = (self.padding[0], (padding[1], padding[1]))
        self.padding_value = 0