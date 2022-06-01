import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
# sys.path.append(os.path.dirname(SCRIPT_DIR))

import numpy as np

# from Network import Network
# from FCLayer import FCLayer
# from ActivationLayer import ActivationLayer
# from Activation import tanh, tanhPrime
# from Loss import mse, msePrime