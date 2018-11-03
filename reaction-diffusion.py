import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
import scipy.signal as signal

height = 100
width = 100

f = .055  #feed
k = .062  #kill
D_X = 1.  #diffusion X , Y
D_Y = .5

#substance A
X = np.ones((height, width))

#substance B
Y = np.zeros((height, width))
Y[20:22, 20:22] = 1.

#discrete laplacian
laplFilt = np.array([[.05, .2, .05], [.2, -1, .2], [.05, .2, .05]])

theFig = plt.figure()


def nextStep(arg):
    global X, Y
    for _ in range(20):
        laplX = signal.convolve2d(X, laplFilt, 'same', 'wrap')
        laplY = signal.convolve2d(Y, laplFilt, 'same', 'wrap')

        #Gray-Scott model
        X = X + (D_X * laplX - (X * Y**2) + f * (1 - X))
        Y = Y + (D_Y * laplY + (X * Y**2) - (k + f) * Y)

    img = plt.imshow(X)

    return img,


animate = matplotlib.animation.FuncAnimation(theFig, nextStep, interval=1)
plt.show()