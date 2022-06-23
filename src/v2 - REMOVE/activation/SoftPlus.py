import numpy as np

class SoftPlus():
    def __call__(self, x):
        return np.log(1 + np.exp(x))
    
    def gradient(self, x):
        return 1 / (1 + np.exp(-x))