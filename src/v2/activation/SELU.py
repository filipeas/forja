import numpy as np

class SELU():
    def __init__(self):
        # Reference : https://arxiv.org/abs/1706.02515
        self.alpha = 1.6732632423543772848170429916717
        self.scale = 1.0507009873554804934193349852946 
    
    def __call__(self, x):
        return self.scale * np.where(x >= 0.0, x, self.alpha * (np.exp(x) - 1))
    
    def gradient(self, x):
        return self.scale * np.where(x >= 0.0, 1, self.alpha * np.exp(x))