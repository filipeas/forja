import sys
import os
import numpy as np

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from network.Network import Network
from layer.FCLayer import FCLayer
from layer.Convolutional import ConvLayer
from layer.Flatten import FlattenLayer
from layer.ActivationLayer import ActivationLayer
from activation.Activation import tanh, tanhPrime
from loss.Loss import mse, msePrime

from keras.datasets import mnist
from keras.utils import np_utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# reshape e normalizando dados de entrada
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_train = x_train.astype('float32')
x_train /= 255
y_train = np_utils.to_categorical(y_train)

# reshape e normalizando dados de saida
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_test = x_test.astype('float32')
x_test /= 255
y_test = np_utils.to_categorical(y_test)

# criando rede
net = Network()
net.add(ConvLayer((28,28,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))
net.add(FlattenLayer())

net.add(FCLayer(26*26*1, 100))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(FCLayer(100,10))
net.add(ActivationLayer(tanh, tanhPrime))

net.use(mse, msePrime)
net.fit(x_train[0:1000], y_train[0:1000], epochs=100, learningRate=0.1)

out = net.predict(x_test[0:3])

print("\n")

print("valores preditos: ")
print(out, end="\n")
print("valores verdadeiros: ")
print(y_test[0:3])