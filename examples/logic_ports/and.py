from cmath import tan
import sys
import os
import numpy as np

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from v1.network.Network import Network
from v1.layer.FCLayer import FCLayer
from v1.layer.ActivationLayer import ActivationLayer
from v1.activation.Activation import tanh, tanhPrime
from v1.loss.Loss import mse, msePrime

# dados de treino
x_test = np.array([ [[1,0]], [[1,1]], [[0,0]], [[0,1]] ])
x_train = np.array([ [[0,0]], [[0,1]], [[1,0]], [[1,1]] ])
y_train = np.array([ [[0]], [[0]], [[0]], [[1]] ])

# criando a rede
net = Network()
net.add(FCLayer(2, 3))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FCLayer(3, 1))
net.add(ActivationLayer(tanh, tanhPrime))

# trainando rede
net.use(mse, msePrime)
net.fit(x_train, y_train, 1000, learningRate = 0.15)

# testando rede
out = net.predict(x_test)
print(out)