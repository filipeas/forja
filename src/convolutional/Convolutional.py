import sys
import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from layer.Layer import Layer
import numpy as np
from scipy import signal

class ConvLayer(Layer):
    """
    inputShape: (i, j, d)
    kernelShape: (m, n)
    layerDepth: outputDepth
    """
    def __init__(self, inputShape, kernelShape, layerDepth):
        self.inputShape = inputShape
        self.inputDepth = inputShape[2]
        self.kernelShape = kernelShape
        self.layerDepth = layerDepth
        
        self.outputShape = (inputShape[0] - kernelShape[0] + 1, inputShape[1] - kernelShape[1] + 1, layerDepth)
        self.weights = np.random.rand(kernelShape[0], kernelShape[1], self.inputShape[1], self.inputDepth, layerDepth) - 0.5
        self.bias = np.random.rand(layerDepth) - 0.5
    
    def forwardPropagation(self, input):
        self.input = input
        self.output = np.zeros(self.outputShape)