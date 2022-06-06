import numpy as np

class TanH():
    def __call__(self, x):
        return 2 / (1 + np.exp(-2 * x)) - 1
    
    def gradient(self, x):
        return 1 - np.power(self.__call__(x), 2)