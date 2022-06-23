from __future__ import print_function, division
from REMOVER.utils import imageToColumn, columnToImage
from REMOVER.layer.Layer import Layer

class PoolingLayer(Layer):
    """
    A parent class of MaxPooling2D and AveragePooling2D
    """
    def __init__(self, pool_shape=(2, 2), stride=1, padding=0):
        self.pool_shape = pool_shape
        self.stride = stride
        self.padding = padding
        self.trainable = True
    
    def forwardPass(self, X, training=True):
        self.layer_input = X

        batch_size, channels, height, width = X.shape

        _, out_height, out_width = self.outputShape()

        X = X.reshape(batch_size * channels, 1, height, width)
        X_col = imageToColumn(X, self.pool_shape, self.stride, self.padding)

        # maxpool or averagepool specific method
        output = self._pool_forward(X_col)

        output = output.reshape(out_height, out_width, batch_size, channels)
        output = output.transpose(2, 3, 0, 1)

        return output
    
    def backwardPass(self, accum_grad):
        batch_size, _, _, _ = accum_grad.shape
        channels, height, width = self.input_shape
        accum_grad = accum_grad.transpose(2, 3, 0, 1).ravel()

        # maxpool or averagepool specific method
        accum_grad_col = self._pool_backward(accum_grad)

        accum_grad = columnToImage(accum_grad_col, (batch_size * channels, 1, height, width), self.pool_shape, self.stride, 0)
        accum_grad = accum_grad.reshape((batch_size,) + self.input_shape)

        return accum_grad
    
    def outputShape(self):
        channels, height, width = self.input_shape
        out_height = (height - self.pool_shape[0]) / self.stride + 1
        out_width = (width - self.pool_shape[1]) / self.stride + 1
        assert out_height % 1 == 0
        assert out_width % 1 == 0
        return channels, int(out_height), int(out_width)