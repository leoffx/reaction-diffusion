import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import scipy.signal as signal

height = 100
width = 500

np.random.seed(1)

X = np.random.rand(height, width)
X[X > .9] = 1
X[X <= .9] = 0

#discrete laplacian
neighbCount = np.array([[1., 1., 1.], [1., 0, 1.], [1., 1., 1.]])

theFig = plt.figure()


def nextStep(arg):
    global X

    for _ in range(20):
        neighbNum = signal.convolve2d(X, neighbCount, 'same', 'wrap')
        X[(X == 1) & (neighbNum < 2)] = 0
        X[(X == 1) & ((neighbNum == 2) | (neighbNum == 3))] = 1
        X[(X == 1) & (neighbNum > 3)] = 0
        X[(X == 0) & (neighbNum == 3)] = 1

    plt.clf()
    img = plt.imshow(X)

    return img,


animate = matplotlib.animation.FuncAnimation(theFig, nextStep, interval=1)
plt.show()
