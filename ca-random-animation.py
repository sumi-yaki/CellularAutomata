#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import matplotlib.animation as anime

up = 5
down = -5

fig = plt.figure()

a = npr.rand(100,100) * 255
#b = np.zeros((100,100))
b = a

def avav(data):
    global a
    global b
    im = plt.imshow(a, 'gray', interpolation="none")

    for i in range(1,99):
        for k in range(1,99):
            av = np.mean(a[i-1:i+2,k-1:k+2])
            if av > 125:
                b[i,k] = a[i,k] + up
            if av <= 125:
                b[i,k] = a[i,k] + down

    b[b > 255] = 255
    b[b < 0] = 0
    a = b
    return im
    #plt.cla()

ani = anime.FuncAnimation(fig, avav, interval=100)
plt.show()

