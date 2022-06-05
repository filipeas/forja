class Layer:
    def __init__(self):
        self.name = ""
        self.input = None
        self.output = None
    
    def forwardPropagation(self, input):
        raise NotImplementedError
    
    def backwardPropagation(self, outputError, learningRate):
        raise NotImplementedError
    
    def input(self):
        return self.input
    
    def output(self):
        return self.output
    
    def name(self):
        return self.name