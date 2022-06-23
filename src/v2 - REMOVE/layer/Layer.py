class Layer(object):
    def setInputShape(self, shape):
        """
        Sets the shape that the layer expects of the input
        in the forward pass method.
        """
        self.input_shape = shape
    
    def layerName(self):
        """
        The name of the layer. Used in model summary.
        """
        return self.__class__.__name__
    
    def parameters(self):
        """
        The number of trainable parameters used by the layer.
        """
        return 0
    
    def forwardPass(self, X, training):
        """
        Propagates the signal forward in the network.
        """
        raise NotImplementedError()
    
    def backwardPass(self, accum_grad):
        """
        Propagates the accumulated gradient backwards in the network.
        If the has trainable weights then these weights are also tuned
         in this method.
        
        As input (accum_grad) it receives the gradient with respect to 
        the output of the layer and return the gradient with respect to 
        the output of the previous layer.
        """
        raise NotImplementedError()
    
    def outputShape(self):
        """
        The shape of the output produced by forwardPass() function.
        """
        raise NotImplementedError()