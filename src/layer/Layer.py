class Layer:
    def __init__(self):
        self.name = ""
        self.input = None
        self.output = None
    
    def forwardPropagation(self, input):
        raise NotImplementedError
    
    def backwardPropagation(self, outputError, learningRate):
        raise NotImplementedError
    
    def output():
        return self.output
    
    def name():
        return self.name