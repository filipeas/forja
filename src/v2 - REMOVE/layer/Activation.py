import numpy as np
from REMOVER.layer.Layer import Layer
from REMOVER.activation.ReLU import ReLU
from REMOVER.activation.Sigmoid import Sigmoid
from REMOVER.activation.SELU import SELU
from REMOVER.activation.ELU import ELU
from REMOVER.activation.Softmax import Softmax
from REMOVER.activation.LeakyReLU import LeakyReLU
from REMOVER.activation.TanH import TanH
from REMOVER.activation.SoftPlus import SoftPlus

activation_functions = {
    'relu': ReLU,
    'sigmoid': Sigmoid,
    'selu': SELU,
    'elu': ELU,
    'softmax': Softmax,
    'leaky_relu': LeakyReLU,
    'tanh': TanH,
    'softplus': SoftPlus
}

class Activation(Layer):
    """
    A layer that applies an activation operation to the input.
    
    Parameters:
    -----------
    name:
        string
        The name of the activation function that will be used.
    """
    def __init__(self, name):
        self.activation_name = name
        self.activation_func = activation_functions[name]()
        self.trainable = True
    
    def layerName(self):
        return "Activation (%s)" % (self.activation_func.__class__.__name__)
    
    def forwardPass(self, X, training=True):
        self.layer_input = X
        return self.activation_func(X)
    
    def backwardPass(self, accum_grad):
        return accum_grad * self.activation_func.gradient(self.layer_input)
    
    def outputShape(self):
        return self.input_shape