import sys
import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from layer.Layer import Layer

class FlattenLayer(Layer):
    def forwardPropagation(self, input):
        self.input = input
        self.output = input.flatten().reshape((1,-1))
        return self.output
    
    def backwardPropagation(self, outputError, learningRate):
        return outputError.reshape(self.input.shape)