import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src")
sys.path.append(ROOT_DIR)

from v2.network import Network
from v2.optimizer import Adam
from v2.loss import CrossEntropy
from v2.layer import Dense, Activation
from v2.utils import to_categorical

def main():
    # data = datasets.load_digits()
    # X = data.data
    # y = data.target

    # print('X = ', X[0].shape)

    # # Convert to one-hot encoding
    # y = to_categorical(y.astype("int"))
    
    # print('y = ', y[0].shape)

    # n_samples, n_features = X.shape
    # n_hidden = 512

    # dados de treino
    x_test = np.array([ [[1,0]], [[1,1]], [[0,0]], [[0,1]] ])
    y_test = np.array([ [[0]], [[1]], [[0]], [[1]] ])
    x_train = np.array([ [[0,0]], [[0,1]], [[1,0]], [[1,1]] ])
    y_train = np.array([ [[0]], [[0]], [[0]], [[1]] ])

    print(x_test.shape, y_test.shape)
    print(x_train.shape, y_train.shape)

    optimizer = Adam()
    net = Network(optimizer, CrossEntropy, validation_data=(x_test, y_test))
    net.add(Dense(3, input_shape=(2,3)))
    net.add(Activation('tanh'))
    net.add(Dense(3, input_shape=(3,1)))
    net.add(Activation('tanh'))

    print()
    net.summary('Model')

    train_err, val_err = net.fit(X=x_train, y=y_train, n_epochs=100, batch_size=64)

    # Training and validation error plot
    # n = len(train_err)
    # training, = plt.plot(range(n), train_err, label="Training Error")
    # validation, = plt.plot(range(n), val_err, label="Validation Error")
    # plt.legend(handles=[training, validation])
    # plt.title("Error Plot")
    # plt.ylabel('Error')
    # plt.xlabel('Iterations')
    # plt.show()

if __name__ == "__main__":
    main()