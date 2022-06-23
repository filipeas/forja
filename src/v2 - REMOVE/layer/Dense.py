from __future__ import print_function, division
import math
import numpy as np
import copy
from REMOVER.layer.Layer import Layer

class Dense(Layer):
    """
    A fully-connected NN layer.
    
    Parameters:
    -----------
    n_units: 
        int
        The number of neurons in the layer.
    input_shape:
        tuple
        The expected input shape of the layer. For dense layers a single digit specifying
        the number of features of the input. Must be specified if it is the first layer in the network.
    """
    def __init__(self, n_units, input_shape=None):
        self.layer_input = None
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
        self.W = None
        self.w0 = None
    
    def initialize(self, optimizer):
        # inicialize the weights
        limit = 1 / math.sqrt(self.input_shape[0])
        self.W = np.random.uniform(-limit, limit, (self.input_shape[0], self.n_units))
        self.w0 = np.zeros((1, self.n_units))
        # weight optimizers
        self.W_opt = copy.copy(optimizer)
        self.w0_opt = copy.copy(optimizer)
    
    def parameters(self):
        return np.prod(self.W.shape) + np.prod(self.w0.shape)
    
    def forwardPass(self, X, training=True):
        self.layer_input = X
        return X.dot(self.W) + self.w0
    
    def backwardPass(self, accum_grad):
        # save weights used during forwards pass
        W = self.W
        
        if self.trainable:
            # calculate gradient w.r.t layer weights
            grad_w = self.layer_input.T.dot(accum_grad)
            grad_w0 = np.sum(accum_grad, axis=0, keepdims=True)
            
            # update the layer weights
            self.W = self.W_opt.update(self.W, grad_w)
            self.w0 = self.w0_opt.update(self.w0, grad_w0)
        
        # return accumulated gradient for next layer
        # calculated based on the weights used during the forward pass
        accum_grad = accum_grad.dot(W.T)
        return accum_grad
    
    def outputShape(self):
        return (self.n_units, )