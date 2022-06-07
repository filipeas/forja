from __future__ import print_function, division
import math
import numpy as np
import copy
from v2.activation import Sigmoid, ReLU, SoftPlus, LeakyReLU
from v2.activation import TanH, ELU, SELU, Softmax
from v2.layer.Layer import Layer

class Conv2D(Layer):
    """
    A 2D convolutional layer.
    
    Parameters:
    -----------
    n_filters: 
        int
        The number of filters that will convolve over the input matrix.
        The number of channels of the output shape.
    filter_shape:
        tuple
        A tuple (filter_height, filter_width).
    input_shape:
        tuple
        (batch_size, chanels, heigh, width)
        The shape of the expected input of the layer.
        Only needs to be specified for first layer in the network.
    padding:
        string
        Either 'same' or 'valid'.
        'same' results in padding being added so that the output height and width
        matches the input height and width. For 'valid' no padding is added.
    stride:
        int
        The stride length of the filters during the convolution over the input.
    """
    def __init__(self, n_filters, filter_shape, input_shape=None, padding='same', stride=1):
        self.n_filters = n_filters
        self.filter_shape = filter_shape
        self.padding = padding
        self.stride = stride
        self.input_shape = input_shape
        self.trainable = True
    
    def initialize(self, optimizer):
        # initialize the weights
        filter_height, filter_width = self.filter_shape
        channels = self.input_shape[0]
        limit = 1 / math.sqrt(np.prod(self.filter_shape))
        self.W = np.random.uniform(-limit, limit, size=(self.n_filters, channels, filter_height, filter_width))
        self.w0 = np.zeros((self.n_filters, 1))
        
        # weight optimizers
        self.W_opt = copy.copy(optimizer)
        self.w0_opt = copy.copy(optimizer)
    
    def parameters(self):
        return np.prod(self.W.shape) + np.prod(self.w0.shape)
    
    def forwardPass(self, X, training=True):
        batch_size, channels, height, width = X.shape
        self.layer_input = X
        
        # turn image shape into column shape
        # (enables dot product between input and weights)
        self.X_col = imageToColumn(X, self.filter_shape, stride=self.stride, output_shape=self.padding)