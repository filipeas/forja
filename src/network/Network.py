# import numba
import numpy as np
import json

class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.lossPrime = None

        self.epochs = 0
    
    """
    Function for add layer to network
    """
    def add(self, layer):
        self.layers.append(layer)
    
    """
    Function for set loss to use
    """
    def use(self, loss, lossPrime):
        self.loss = loss
        self.lossPrime = lossPrime
    
    """
    Function for predict output for given input
    """
    # @numba.jit(forceobj=True)
    def predict(self, input):
        samples = len(input)
        result = []

        for i in range(samples):
            output = input[i]
            for layer in self.layers:
                output = layer.forwardPropagation(output)
            result.append(output)
        
        return result
    
    """
    Function for train the network
    """
    # @numba.jit(forceobj=True)
    def fit(self, xTrain, yTrain, epochs, learningRate):
        samples = len(xTrain)

        self.epochs = epochs

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = xTrain[j]
                for layer in self.layers:
                    output = layer.forwardPropagation(output)
                
                err += self.loss(yTrain[j], output)

                error = self.lossPrime(yTrain[j], output)
                for layer in reversed(self.layers):
                    error = layer.backwardPropagation(error, learningRate)
            
            err /= samples
            print('[epoch %d/%d   error = %f]' % (i + 1, epochs, err))
    
    def layers(self):
        return self.layers
    
    def summary(self):
        print("your model: ")
        print("[ \t nº layer \t | \t type \t | \t shape \t]: ")
        for i, layer in enumerate(self.layers):
            print("[\t" + str(i) + "\t|\t" + layer.name + "\t|\t" + str(np.array(layer.output).shape) + "]", end="\n")
    
    def save(self):
        networkJson = json.dumps({'network': self.__dict__})
        print(networkJson)