from Layer import Layer
import numpy as np

class FCLayer(Layer):
    def __init__(self, inputSize, outputSize):
        self.weights = np.random.rand(inputSize, outputSize) - 0.5
        self.bias = np.random.rand(1, outputSize) - 0.5
    
    def forwardPropagation(self, input):
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output
    
    def backwardPropagation(self, outputError, learningRate):
        inputError = np.dot(outputError, self.weights.T)
        weightsError = np.dot(self.input.T, outputError)

        self.weights -= learningRate * weightsError
        self.bias -= learningRate * outputError

        return inputError