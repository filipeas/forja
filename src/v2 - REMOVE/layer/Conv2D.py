from __future__ import print_function, division
import math
import numpy as np
import copy
from REMOVER.utils import imageToColumn, columnToImage
from REMOVER.layer.Layer import Layer
from REMOVER.utils.DataOperation import determinePadding

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
        # turn weights into column shape
        self.W_col = self.W.reshape((self.n_filters, -1))
        # calculate output
        output = self.W_col.dot(self.X_col) + self.w0
        # reshape into (n_filters, out_height, out_width, batch_size)
        output = output.reshape(self.outputShape() + (batch_size, ))
        # redistribute axises so that batch size comes first
        return output.transpose(3, 0, 1, 2)
    
    def backwardPass(self, accum_grad):
        # reshape accumulated gradient into column shape
        accum_grad = accum_grad.transpose(1, 2, 3, 0).reshape(self.n_filters, -1)
        
        if self.trainable:
            # Take dot product between column shaped accum. gradient and column shape
            # layer input to determine the gradient at the layer with respect to layer weights
            grad_w = accum_grad.dot(self.X_col.T).reshape(self.W.shape)
            #the gradient with respect to bias term is the sum similarly to in dense layer
            grad_w0 = np.sum(accum_grad, axis=1, keepdims=True)
            
            # update the layers weights
            self.W = self.W_opt.update(self.W, grad_w)
            self.w0 = self.w0_opt.update(self.w0, grad_w0)
        
        # recalculate the gradient wich will be propagated back to prev layer
        accum_grad = self.W_col.T.dot(accum_grad)
        # reshape from column shape to image shape
        accum_grad = columnToImage(accum_grad, self.layer_input.shape, self.filter_shape, stride=self.stride, output_shape=self.padding)
        
        return accum_grad
    
    def outputShape(self):
        channels, height, width = self.input_shape
        pad_h, pad_w = determinePadding(self.filter_shape, output_shape=self.padding)
        output_height = (height + np.sum(pad_h) - self.filter_shape[0]) / self.stride + 1
        output_width = (width + np.sum(pad_w) - self.filter_shape[1]) / self.stride + 1
        return self.n_filters, int(output_height), int(output_width)