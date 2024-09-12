import numpy as np
import matplotlib.pyplot as plt

def plot_method(p, guesses):
    x_samples = [x for x, _ in guesses]
    interval_width = (max(x_samples) - min(x_samples)) 
    left = -2 # min(x_samples) - interval_width
    right = 2 # max(x_samples) + interval_width
    num_samples = 50
    xs = np.arange(left, right, (right - left) / num_samples)
    ys = list(map(p, xs))
    plt.plot(xs, ys)
    plt.scatter(x_samples, [y for _, y in guesses])
    plt.axhline(0, color='black')
    plt.show()

def plot_scatter(data):
    plt.scatter(data[0], data[1])
    plt.show()
