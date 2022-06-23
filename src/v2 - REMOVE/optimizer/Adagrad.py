import numpy as np
from REMOVER.utils import make_diagonal, normalize

class Adagrad():
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.G = None # Sum of squares of the gradients
        self.eps = 1e-8

    def update(self, w, grad_wrt_w):
        # If not initialized
        if self.G is None:
            self.G = np.zeros(np.shape(w))
        # Add the square of the gradient of the loss function at w
        self.G += np.power(grad_wrt_w, 2)
        # Adaptive gradient with higher learning rate for sparse data
        return w - self.learning_rate * grad_wrt_w / np.sqrt(self.G + self.eps)