import numpy as np
from REMOVER.layer.Layer import Layer

class Flatten(Layer):
    """
    Turn a multidimensional matrix into two-dimensional.
    """
    def __init__(self, input_shape=None):
        self.prev_shape = None
        self.trainable = True
        self.input_shape = input_shape
    
    def forwardPass(self, X, training=True):
        self.prev_shape = X.shape
        return X.reshape((X.shape[0], -1))
    
    def backwardPass(self, accum_grad):
        return accum_grad.reshape(self.prev_shape)
    
    def outputShape(self):
        return (np.prod(self.input_shape),)