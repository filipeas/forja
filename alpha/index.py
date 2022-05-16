import os
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image, ImageDraw, ImageFilter
import glob
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

cwd = os.getcwd()

BATCH_SIZE = 64
EPOCH_SIZE = 64

def gabarito_gen(batch_size = 64):
    # pasta das imagens de gabaritos
    source_path = cwd + "\\tests\\"
    image_files = [f for f in glob.glob(source_path + '*.png')]

    while True:
        # gerando imagens pretas no tamanho desejado
        X = np.zeros((batch_size, 1024, 768, 3))
        Y = np.zeros((batch_size, 3))

        # preenchendo imagens
        for i in range(batch_size):
            for filepath in image_files:
                # lendo imagem e fazendo resize para (64, 64) e depois convertendo para array de numpy
                gabarito = Image.open(filepath)
                gabarito = gabarito.resize((156, 349))
                imgGabarito = np.asarray(gabarito)
                #plt.imshow(imgGabarito)

                # resize no gabarito
                # size = np.random.randint(32, 64)
                temp_gabarito = gabarito.resize((156, 349)) # (size, size)
                imgGabarito = np.asarray(temp_gabarito) / 255.
                gabarito_x, gabarito_y, _ = imgGabarito.shape

                # criar fundo preto da imagem
                bg = Image.new('RGB', (768, 1024))

                # processo de geracao
                x1 = np.random.randint(1, 1024 - gabarito_x)
                y1 = np.random.randint(1, 768 - gabarito_y)

                # colar imagem do gabarito sobre o fundo preto
                bg.paste(temp_gabarito, (x1, y1))
                # transformando em array de numpy
                gabarito = np.asarray(bg) / 255.
                X[i] = gabarito

                Y[i, 0] = x1 / 1024.
                Y[i, 1] = y1 / 768.
                Y[i, 2] = gabarito_x / 1024.
        yield X, Y

# chamando funcao de gerar gabaritos
x, y = next(gabarito_gen())

vgg = tf.keras.applications.VGG16(input_shape=[768, 1024, 3], include_top=False, weights='imagenet')
x = Flatten()(vgg.output)
x = Dense(3, activation='sigmoid')(x)
model2 = Model(vgg.input, x)
model2.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001))
model2.summary()

model2.fit_generator(gabarito_gen(), steps_per_epoch = EPOCH_SIZE, epochs = 5)