from v2.layer.Layer import Layer

class Reshape(Layer):
    """
    Reshapes the input tensor into specified shape.
    
    Parameters:
    -----------
    shape:
        tuple
        The shape which the input shall be reshaped to.
    """
    def __init__(self, shape, input_shape=None):
        self.prev_shape = None
        self.trainable = True
        self.shape = shape
        self.input_shape = input_shape
    
    def forwardPass(self, X, training=True):
        self.prev_shape = X.shape
        return X.reshape((X.shape[0], ) + self.shape)
    
    def backwardPass(self, accum_grad):
        return accum_grad.reshape(self.prev_shape)
    
    def outputShape(self):
        return self.shape