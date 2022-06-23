import numpy as np
from REMOVER.layer.Layer import Layer

class Dropout(Layer):
    """
    A layer that randomly sets a fraction p of the output units of the previous layer to zero.
    
    Parameters:
    -----------
    p:
        float
        The probabilit that unit x is set to zero.
    """
    def __init__(self, p=0.2):
        self.p = p
        self._mask = None
        self.input_shape = None
        self.n_units = None
        self.pass_through = True
        self.trainable = True
    
    def forwardPass(self, X, training=True):
        c = (1 - self.p)
        if training:
            self._mask = np.random.uniform(size=X.shape) > self.p
            c = self._mask
        return X * c
    
    def backwardPass(self, accum_grad):
        return accum_grad * self._mask
    
    def outputShape(self):
        return self.input_shape