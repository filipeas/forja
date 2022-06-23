from cmath import tan
import sys
import os
import numpy as np

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from network.Network import Network
from layer.FCLayer import FCLayer
from layer.ActivationLayer import ActivationLayer
from activation.Activation import tanh, tanhPrime
from loss.Loss import mse, msePrime

# dados de treino
x_test = np.array([ [[1]], [[0]] ])
x_train = np.array([ [[0]], [[1]] ])
y_train = np.array([ [[1]], [[0]] ])

# criando a rede
net = Network()
net.add(FCLayer(1, 2))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FCLayer(2, 1))
net.add(ActivationLayer(tanh, tanhPrime))

# trainando rede
net.use(mse, msePrime)
net.fit(x_train, y_train, 1000, learningRate = 0.15)

# testando rede
out = net.predict(x_test)
print(out)