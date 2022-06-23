from __future__ import print_function, division
import math
from tkinter.tix import Tree
import numpy as np
import copy
from REMOVER.layer.Layer import Layer

class BatchNormalization(Layer):
    """
    Batch normalization
    """
    def __init__(self, momentum=0.99):
        self.momentum = momentum
        self.trainable = True
        self.eps = 0.01
        self.running_mean = None
        self.running_var = None
    
    def initialize(self, optimizer):
        # initialize the parameters
        self.gamma = np.ones(self.input_shape)
        self.beta = np.zeros(self.input_shape)
        # parameter optimizers
        self.gamma_opt = copy.copy(optimizer)
        self.beta_opt = copy.copy(optimizer)
    
    def parameters(self):
        return np.prod(self.gamma.shape) + np.prod(self.beta.shape)
    
    def forwardPass(self, X, training=True):
        # initialize running mean and variance if first run
        if self.running_mean is None:
            self.running_mean = np.mean(X, axis=0)
            self.running_var = np.var(X, axis=0)
        
        if training and self.trainable:
            mean = np.mean(X, axis=0)
            var = np.var(X, axis=0)
            self.running_mean = self.momentum * self.running_mean + (1 - self.momentum) * mean
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var
        else:
            mean = self.running_mean
            var = self.running_var
        
        # statistics saved for backward pass
        self.X_centered = X - mean
        self.stddev_inv = 1 / np.sqrt(var + self.eps)

        X_norm = self.X_centered * self.stddev_inv
        output = self.gamma * X_norm + self.beta

        return output
    
    def backwardPass(self, accum_grad):
        # save parameters used during the forward pass
        gamma = self.gamma

        # if the layer is traineble the parameters are updated
        if self.trainable:
            X_norm = self.X_centered * self.stddev_inv
            grad_gamma = np.sum(accum_grad * X_norm, axis=0)
            grad_beta = np.sum(accum_grad, axis=0)

            self.gamma = self.gamma_opt.update(self.gamma, grad_gamma)
            self.beta = self.beta_opt.update(self.beta, grad_beta)
        
        batch_size = accum_grad.shape[0]

        # the gradient of the loss with respect to the layer inputs 
        # (use weights and statistics from forward pass)
        accum_grad = (1 / batch_size) * gamma * self.stddev_inv * (batch_size * accum_grad - np.sum(accum_grad, axis=0) - self.X_centered * self.stddev_inv**2 * np.sum(accum_grad * self.X_centered, axis=0))

        return accum_grad
    
    def outputShape(self):
        return self.input_shape