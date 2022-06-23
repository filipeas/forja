from __future__ import print_function, division
import numpy as np
from REMOVER.layer.Layer import Layer

class ConstantPadding2D(Layer):
    """
    Adds rows and columns of constant values to the input.
    Expects the input to be of shape (batch_size, channels, height, width)
    
    Parameters:
    -----------
    padding:
        tuple
        The amount of padding along the height and width dimension of the input.
        If (pad_h, pad_w) the same symmetric padding is applied along height and width dimension.
        If((pad_h0, pad_h1), (pad_w0, pad_w1)) the specified padding is added to beginning and end of
        the height and width dimension.
    padding_value:
        int or tuple
        The value the is added as padding.
    """
    def __init__(self, padding, padding_value=0):
        self.padding = padding
        self.trainable = True
        if not isinstance(padding[0], tuple):
            self.padding = ((padding[0], padding[0]), padding[1])
        if not isinstance(padding[1], tuple):
            self.padding = (self.padding[0], (padding[1], padding[1]))
        self.padding_value = padding_value
    
    def forwardPass(self, X, training=True):
        output = np.pad(X, 
                        pad_width=((0,0), (0,0), self.padding[0], self.padding[1]), 
                        mode="constant", 
                        constant_values=self.padding_value
                        )
        return output
    
    def backwardPass(self, accum_grad):
        pad_top, pad_left = self.padding[0][0], self.padding[1][0]
        height, width = self.input_shape[1], self.input_shape[2]
        accum_grad = accum_grad[:, :, pad_top:pad_top + height, pad_left:pad_left + width]
        return accum_grad
    
    def outputShape(self):
        new_height = self.input_shape[1] + np.sum(self.padding[0])
        new_width = self.input_shape[2] + np.sum(self.padding[1])
        return (self.input_shape[0], new_height, new_width)