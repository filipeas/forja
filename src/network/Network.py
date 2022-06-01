from unittest import result


class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.lossPrime = None
    
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
    def fit(self, xTrain, yTrain, epochs, learningRate):
        samples = len(xTrain)

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