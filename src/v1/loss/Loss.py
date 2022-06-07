import numpy as np

def mse(yTrue, yPred):
    return np.mean(np.power(yTrue - yPred, 2))

def msePrime(yTrue, yPred):
    return 2 * (yPred - yTrue) / yTrue.size