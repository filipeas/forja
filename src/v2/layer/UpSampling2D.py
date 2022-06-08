from v2.layer.Layer import Layer

class UpSampling2D(Layer):
    """
    Nearest neighbor ip sampling of the input. Repeats the rows and
    columns of the data by size[0] and size[1] respectively.
    
    Parameters:
    -----------
    size:
        tuple
        (size_y, size_x) - The number of times each axis will be repeated.
    """
    def __init__(self, size=(2,2), input_shape=None):
        self.prev_shape = None
        self.traibable = True
        self.size = size
        self.input_shape = input_shape
    
    def forwardPass(self, X, training=True):
        self.prev_shape = X.shape
        # repeat each axis as specified by size
        X_new = X.repeat(self.size[0], axis=2).repeat(self.size[1], axis=3)
        return X_new
    
    def backwardPass(self, accum_grad):
        # down sample input to previous shape
        accum_grad = accum_grad[:, :, ::self.size[0], ::self.size[1]]
        return accum_grad
    
    def outputShape(self):
        channels, height, width = self.input_shape
        return channels, self.size[0] * height, self.size[1] * width