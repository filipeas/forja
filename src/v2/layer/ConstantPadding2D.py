from __future__ import print_function, division
import math
import numpy as np
import copy
from v2.utils import imageToColumn, columnToImage
from v2.layer.Layer import Layer
from v2.utils.DataOperation import determinePadding

class ConstantPadding2D(Layer):
    """
    Adds rows and columns of constant values to the input.
    """