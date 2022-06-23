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
net.add(ConvLayer((500, 390, 1), (5,5), 32))
net.add(ActivationLayer(tanh, tanhPrime))

# net.add(ConvLayer((496, 386, 32), (5,5), 32))
# net.add(ActivationLayer(tanh, tanhPrime))

# net.add(ConvLayer((492, 382, 32), (15,15), 64))
# net.add(ActivationLayer(tanh, tanhPrime))

# treinando
net.use(mse, msePrime)
# net.fit(folha_resposta, y_train, epochs=1, learningRate=0.3)

"""
verificando camadas
"""
# retornar uma lista de todas as camadas criadas. Cada camada é convertida para array numpy para plot
layer_outputs = [np.array(layer.output) for layer in net.layers] # esse exemplo retorna uma lista com 6 camadas (exatamente a qtd de camadas criadas)
# print(len(layer_outputs))

"""
plotando sumário da rede
"""
net.summary()

"""
salvar modelo
"""
# net.save()


# """
# plots
# """
# for i in range(len(layer_outputs)):
#     for j in range(32):
#         plt.imsave('plots/conv'+str(i)+'_channel'+str(j)+'.jpg', layer_outputs[i][:, :, j])