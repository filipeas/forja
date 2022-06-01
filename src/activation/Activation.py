import numpy as np

def tanh(x):
    return np.tanh(x)

def tanhPrime(x):
    return 1 - np.tanh(x)**2