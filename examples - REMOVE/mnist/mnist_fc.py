"""
Exemplo de mnist usando somente camada totalmente conectada
"""

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

from keras.datasets import mnist
from keras.utils import np_utils

# lendo base de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train)
# print(y_train)

# reshape e normalizacao de dados de traino (60000 imagens)
x_train = x_train.reshape(x_train.shape[0], 1, 28*28)
x_train = x_train.astype('float32')
x_train /= 255

# encode da saida para converter em vetor (ex: 3 vai se tornar [0 0 1 0 0 0 0 0 0 0])
y_train = np_utils.to_categorical(y_train)

x_test = x_test.reshape(x_test.shape[0], 1, 28*28)
x_test = x_test.astype('float32')
x_test /= 255

y_test = np_utils.to_categorical(y_test)

# montando rede
net = Network()

net.add(FCLayer(28*28, 100))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(FCLayer(100, 50))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(FCLayer(50, 10))
net.add(ActivationLayer(tanh, tanhPrime))

net.use(mse, msePrime)
net.fit(x_train[0:6000], y_train[0:6000], epochs = 100, learningRate = 0.1)

# testando 3 exemplos
out = net.predict(x_test[0:3])
print("\n")
print("Valores preditos : ")
print(out, end="\n")
print("Valores verdadeiros : ")
print(y_test[0:3])