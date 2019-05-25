import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

height = 50
width = 50

class point:
    def __init__(self):
        self.pos=np.array([height/2,width/2])
        self.vel=np.random.rand(2,)*2
        self.acc=np.zeros((0,0))
    
    def upd(self):
        self.vel=np.random.rand(2,)*2 -1
        self.pos += self.vel

walker = point()


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], '-', animated=True)

def setup():
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    return ln,

def draw(frame):
    walker.upd()
    xdata.append(walker.pos[0])
    ydata.append(walker.pos[1])
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, draw,
                    init_func=setup, blit=True)
plt.show()
