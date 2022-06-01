class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def forwardPropagation(self, input):
        raise NotImplementedError
    
    def backwardPropagation(self, outputError, learningRate):
        raise NotImplementedError