import sys
import os
import numpy as np
import matplotlib.pyplot as plt

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from network.Network import Network
from convolutional.Convolutional import ConvLayer
from layer.ActivationLayer import ActivationLayer
from activation.Activation import tanh, tanhPrime
from loss.Loss import mse, msePrime

x_data = np.random.rand(10,10,1)
x_train = [x_data]
y_data = np.random.rand(4,4,1)
y_train = [y_data]

# criando rede
net = Network()
net.add(ConvLayer((10,10,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(ConvLayer((8,8,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(ConvLayer((6,6,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))

# treinando
net.use(mse, msePrime)
net.fit(x_train, y_train, epochs=1000, learningRate=0.3)

# testando
out = net.predict(x_train)
print("predito = ", out)
print("experado = ", y_train)

out = out.pop(0)
out_img = np.array(out)
plt.imshow(out_img, interpolation='nearest')
plt.show()

y_train = y_train.pop(0)
y_img = np.array(y_train)
plt.imshow(y_img, interpolation='nearest')
plt.show()