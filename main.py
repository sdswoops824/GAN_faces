import numpy as np
from numpy import random
from matplotlib import pyplot as plt


# Drawing function
def view_samples(samples, m, n):
    fig, axes = plt.subplots(figsize=(10, 10), nrows=m, ncols=n, sharey=True, sharex=True)
    for ax, img in zip(axes.flatten(), samples):
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        im = ax.imshow(1-img.reshape((2,2)), cmap='Greys_r')
    return fig, axes


# Examples of faces
faces = [np.array([1, 0, 0, 1]),
         np.array([0.9, 0.1, 0.2, 0.8]),
         np.array([0.9, 0.2, 0.1, 0.8]),
         np.array([0.8, 0.1, 0.2, 0.9]),
         np.array([0.8, 0.2, 0.1, 0.9])]

view_samples(faces, 1, 4)