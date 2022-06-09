import progressbar
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import numpy as np

from v2.utils.DataOperation import calculate_covariance_matrix
from v2.utils.DataOperation import calculate_correlation_matrix
from v2.utils.DataManipulation import standardize

bar_widgets = [
    'Training: ', 
    progressbar.Percentage(), 
    ' ', 
    progressbar.Bar(marker="-", left="[", right="]"),
    ' ', 
    progressbar.ETA()
]

class Plot():
    def __init__(self):
        self.cmap = plt.get_cmap('viridis')
    
    def _transform(self, X, dim):
        covariance = calculate_correlation_matrix(X)
        eigenvalues = eigenvectors = np.linalg.eig(covariance)
        # sort eigenvalues and eigenvector by largest eigenvalues
        idx = eigenvalues.argsort()[::-1]