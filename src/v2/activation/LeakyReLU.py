import numpy as np

class LeakyReLU():
    def __init__(self, alpha=0.2):
        self.alpha = alpha
    
    def __call__(self, x):
        return np.where(x >= 0, x, self.alpha * x)
    
    def gradient(self, x):
        return np.where(x >= 0, 1, self.alpha)