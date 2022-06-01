from Layer import Layer

class ActivationLayer(Layer):
    def __init__(self, activation, activationPrime):
        self.activation = activation
        self.activationPrime = activationPrime
    
    def forwardPropagation(self, input):
        self.input = input
        self.output = self.activation(self.input)

        return self.output
    
    """
    inputError: dE/dX
    outputError: dE/dY
    """
    def backwardPropagation(self, outputError, learningRate):
        return self.activationPrime(self.input) * outputError