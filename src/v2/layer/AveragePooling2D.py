from __future__ import print_function, division

import numpy as np
from v2.layer.PoolingLayer import PoolingLayer

class AveragePooling2D(PoolingLayer):
    def _pool_forward(self, X_col):
        output = np.mean(X_col, axis=0)
        return output
    
    def _pool_backward(self, accum_grad):
        accum_grad_col = np.zeros((np.prod(self.pool_shape), accum_grad.size))
        accum_grad_col[:, range(accum_grad.size)] = 1. / accum_grad_col.shape[0] * accum_grad
        return accum_grad_col