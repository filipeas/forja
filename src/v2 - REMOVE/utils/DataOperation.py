from __future__ import division
import numpy as np
import math
import sys

def calculate_entropy(y):
    """
    Calculate the entropy of label array y
    """
    log2 = lambda x: math.log(x) / math.log(2)
    unique_labels = np.unique(y)
    entropy = 0
    for label in unique_labels:
        count = len(y[y == label])
        p = count / len(y)
        entropy += -p * log2(p)
    return entropy


def mean_squared_error(y_true, y_pred):
    """
    Returns the mean squared error between y_true and y_pred
    """
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse

def calculate_variance(X):
    """
    Return the variance of the features in dataset X
    """
    mean = np.ones(np.shape(X)) * X.mean(0)
    n_samples = np.shape(X)[0]
    variance = (1 / n_samples) * np.diag((X - mean).T.dot(X - mean))
    
    return variance

def calculate_std_dev(X):
    """
    Calculate the standard deviations of the features in dataset X
    """
    std_dev = np.sqrt(calculate_variance(X))
    return std_dev

def euclidean_distance(x1, x2):
    """
    Calculates the l2 distance between two vectors
    """
    distance = 0
    # Squared distance between each coordinate
    for i in range(len(x1)):
        distance += pow((x1[i] - x2[i]), 2)
    return math.sqrt(distance)


def accuracy_score(y_true, y_pred):
    """
    Compare y_true to y_pred and return the accuracy
    """
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy

def calculate_covariance_matrix(X, Y=None):
    """
    Calculate the covariance matrix for the dataset X.
    """
    if Y is None:
        Y = X
    n_samples = np.shape(X)[0]
    covariance_matrix = (1 / (n_samples - 1)) * (X - X.mean(axis=0)).T.dot(Y - Y.mean(axis=0))
    
    return np.array(covariance_matrix, dtype=float)

def calculate_correlation_matrix(X, Y=None):
    """
    Calculate the correlation matrix for the dataset X
    """
    if Y is None:
        Y = X
    n_samples = np.shape(X)[0]
    covariance = (1 / n_samples) * (X - X.mean(0)).T.dot(Y - Y.mean(0))
    std_dev_X = np.expand_dims(calculate_std_dev(X), 1)
    std_dev_y = np.expand_dims(calculate_std_dev(Y), 1)
    correlation_matrix = np.divide(covariance, std_dev_X.dot(std_dev_y.T))
    
    return np.array(correlation_matrix, dtype=float)

def accuracyScore(y_true, y_pred):
    # compare y_true to y_pred and return the accuracy
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy

def determinePadding(filter_shape, output_shape='same'):
    """
    Method which calculates the padding based on the 
    specified output shape and the shape of the filters.
    """
    # no padding
    if output_shape == 'valid':
        return (0, 0), (0, 0)
    elif output_shape == 'same':
        filter_height, filter_width = filter_shape
        
        # derived from:
        # output_height = (height + pad_h - filter_heigth) / stride + 1
        # in this case output_height = height and stride = 1.
        # this gives the expression for the padding below.
        pad_h1 = int(math.floor((filter_height - 1) / 2))
        pad_h2 = int(math.ceil((filter_height - 1) / 2))
        pad_w1 = int(math.floor((filter_width - 1) / 2))
        pad_w2 = int(math.ceil((filter_width - 1) / 2))
        
        return (pad_h1, pad_h2), (pad_w1, pad_w2)

def getIm2ColIndices(images_shape, filter_shape, padding, stride=1):
    #first figure out what the size of the output should be
    batch_size, channels, height, width = images_shape
    filter_height, filter_width = filter_shape
    pad_h, pad_w = padding
    out_height = int((height + np.sum(pad_h) - filter_height) / stride + 1)
    out_width = int((width + np.sum(pad_w) - filter_width) / stride + 1)
    
    i0 = np.repeat(np.arange(filter_height), filter_width)
    i0 = np.tile(i0, channels)
    i1 = stride * np.repeat(np.arange(out_height), out_width)
    j0 = np.tile(np.arange(filter_width), filter_height * channels)
    j1 = stride * np.tile(np.arange(out_width), out_height)
    i = i0.reshape(-1, 1) + i1.reshape(1, -1)
    j = j0.reshape(-1, 1) + j1.reshape(1, -1)
    
    k = np.repeat(np.arange(channels), filter_height * filter_width).reshape(-1, 1)
    
    return (k, i, j)

def imageToColumn(images, filter_shape, stride, output_shape='same'):
    """
    Method which turns the image shaped input to column shape.
    Used during the forward pass.
    """
    filter_height, filter_width = filter_shape
    
    pad_h, pad_w = determinePadding(filter_shape, output_shape)
    
    # add padding to the image
    images_padded = np.pad(images, ((0, 0), (0, 0), pad_h, pad_w), mode='constant')
    
    # calculate the indices where the dot product are to be 
    # applied betwenn weights and the image.
    k, i, j = getIm2ColIndices(images.shape, filter_shape, (pad_h, pad_w), stride)
    
    # get content from image at those indices
    cols = images_padded[:, k, i, j]
    channels = images.shape[1]
    #reshape content into column shape
    cols = cols.transpose(1, 2, 0).reshape(filter_height * filter_width * channels, -1)
    return cols

def columnToImage(cols, images_shape, filter_shape, stride, output_shape='same'):
    """
    Method which turns the column shaped input to image shape.
    Used during the backward pass.
    """
    batch_size, channels, height, width = images_shape
    pad_h, pad_w = determinePadding(filter_shape, output_shape)
    height_padded = height + np.sum(pad_h)
    width_padded = width + np.sum(pad_w)
    images_padded = np.zeros((batch_size, channels, height_padded, width_padded))
    
    # calculate the indices where the dot products are applied between weights
    # and the image
    k, i, j = getIm2ColIndices(images_shape, filter_shape, (pad_h, pad_w), stride)
    
    cols = cols.reshape(channels * np.prod(filter_shape), -1, batch_size)
    cols = cols.transpose(2, 0, 1)
    # add column content to the images at the indices
    np.add.at(images_padded, (slice(None), k, i, j), cols)
    
    # return image without padding
    return images_padded[:, :, pad_h[0]:height+pad_h[0], pad_w[0]:width+pad_w[0]]