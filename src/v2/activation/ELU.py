import numpy as np

class ELU():
    def __init__(self, alpha=0.1):
        self.alpha = alpha
    
    def __call__(self, x):
        return np.where(x >= 0.0, x, self.alpha * (np.exp(x) - 1))
    
    def gradient(self, x):
        return np.where(x >= 0.0, 1, self.__call__(x) + self.alpha)