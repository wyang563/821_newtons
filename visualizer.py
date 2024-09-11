import numpy as np
import matplotlib.pyplot as plt


def plot_polynomial(p, left, right):
    num_samples = 50
    xs = np.arange(left, right, (right - left) / num_samples)
    ys = list(map(p, xs))
    plt.plot(xs, ys)
    plt.axhline(0, color='black')
    plt.show()


