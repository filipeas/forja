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
        self.name = "convolutional"
        self.inputShape = inputShape
        self.inputDepth = inputShape[2]
        self.kernelShape = kernelShape
        self.layerDepth = layerDepth
        
        self.outputShape = (inputShape[0] - kernelShape[0] + 1, inputShape[1] - kernelShape[1] + 1, layerDepth)
        self.weights = np.random.rand(kernelShape[0], kernelShape[1], self.inputDepth, layerDepth) - 0.5
        self.bias = np.random.rand(layerDepth) - 0.5
    
    def forwardPropagation(self, input):
        self.input = input
        self.output = np.zeros(self.outputShape)

        print("input shape: " + str(self.input.shape), end="\n")
        print("output shape: " + str(self.output.shape), end="\n")
        print("weight shape: " + str(self.weights.shape), end="\n")

        for k in range(self.layerDepth):
            for d in range(self.inputDepth):
                self.output[:,:,k] += signal.correlate2d(self.input[:,:,d], self.weights[:,:,d,k], 'valid') + self.bias[k]
        
        return self.output
    
    """
    calcula dE/dW, dE/dB para um dado outputError = dE/dY.
    retorna inputError = dE/dX
    """
    def backwardPropagation(self, outputError, learningRate):
        inError = np.zeros(self.inputShape)
        dWeights = np.zeros((self.kernelShape[0], self.kernelShape[1], self.inputDepth, self.layerDepth))
        dBias = np.zeros(self.layerDepth)

        for k in range(self.layerDepth):
            for d in range(self.inputDepth):
                inError[:,:,d] += signal.convolve2d(outputError[:,:,k], self.weights[:,:,d,k], 'full')
                dWeights[:,:,d,k] = signal.correlate2d(self.input[:,:,d], outputError[:,:,k], 'valid')
            dBias[k] = self.layerDepth * np.sum(outputError[:,:,k])
        
        self.weights -= learningRate * dWeights
        self.bias -= learningRate * dBias
        return inError