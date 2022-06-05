import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from network.Network import Network
from layer.Convolutional import ConvLayer
from layer.FCLayer import FCLayer
from layer.Flatten import FlattenLayer
from layer.ActivationLayer import ActivationLayer
from activation.Activation import tanh, tanhPrime
from loss.Loss import mse, msePrime

# lendo imagem de teste
folha_resposta = cv2.imread('folha-resposta_resize.jpg')
# convertendo para escala de cinza
folha_resposta = cv2.cvtColor(folha_resposta, cv2.COLOR_RGB2GRAY)
# reshape e normalize da imagem teste
folha_resposta = folha_resposta.reshape(1, 500, 390, 1)
folha_resposta = folha_resposta.astype('float32')
folha_resposta /= 255

# print(folha_resposta.shape)
# plt.matshow(folha_resposta[:,:,0])
# plt.matshow(folha_resposta[:,:,1])
# plt.matshow(folha_resposta[:,:,2])
# plt.show()

y_data = np.random.rand(496,386,32)
y_train = [y_data]
# y_train = [1]

# criando rede
net = Network()

"""
lendo modelo salvo
"""
net = net.load('checkout')

net.summary()