import sys
import os
import numpy as np
import matplotlib.pyplot as plt

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src")
sys.path.append(ROOT_DIR)

from network.Network import Network
from layer.Convolutional import ConvLayer
from layer.ActivationLayer import ActivationLayer
from activation.Activation import tanh, tanhPrime
from loss.Loss import mse, msePrime

x_data = np.random.rand(10,10,1)
x_train = [x_data]
y_data = np.random.rand(4,4,2)
y_train = [y_data]

# criando rede
net = Network()
net.add(ConvLayer((10,10,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(ConvLayer((8,8,1), (3,3), 1))
net.add(ActivationLayer(tanh, tanhPrime))

net.add(ConvLayer((6,6,1), (3,3), 2))
net.add(ActivationLayer(tanh, tanhPrime))

# treinando
net.use(mse, msePrime)
net.fit(x_train, y_train, epochs=1000, learningRate=0.3)

# executando predict do modelo
out = net.predict(x_train)
# print("predito = ", out)
# print("experado = ", y_train)

"""
verificando camadas
"""
# retornar uma lista de todas as camadas criadas. Cada camada é convertida para array numpy para plot
layer_outputs = [np.array(layer.output) for layer in net.layers] # esse exemplo retorna uma lista com 6 camadas (exatamente a qtd de camadas criadas)
print(len(layer_outputs))

"""
plots
"""
# # plot da saida predita
# out = np.array(out)
# print(out.shape)
# plt.matshow(out[0, :, :, 0], cmap ='viridis')
# plt.matshow(out[0, :, :, 1], cmap ='viridis')

# # plot da saida de treino (desejada)
# y_img = np.array(y_train)
# plt.matshow(y_img[0, :, :, 0], cmap ='viridis')
# plt.matshow(y_img[0, :, :, 1], cmap ='viridis')
# plt.show()

# plot da primeira camada convolucional
plt.matshow(layer_outputs[0], cmap ='viridis')
# plot da primeira camada de ativação
plt.matshow(layer_outputs[1], cmap ='viridis')
# plot da segunda camada convolucional
plt.matshow(layer_outputs[2], cmap ='viridis')
# plot da segunda camada de ativação
plt.matshow(layer_outputs[3], cmap ='viridis')
# plot da terceira camada convolucional
plt.matshow(layer_outputs[4][:, :, 0], cmap ='viridis')
plt.matshow(layer_outputs[4][:, :, 1], cmap ='viridis')
# plot da terceira camada de ativação
plt.matshow(layer_outputs[5][:, :, 0], cmap ='viridis')
plt.matshow(layer_outputs[5][:, :, 1], cmap ='viridis')
plt.show()