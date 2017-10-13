#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import matplotlib.animation as anime

up = 5
down = -5

fig = plt.figure()
ims = []

a = npr.rand(100,100) * 255
#b = np.zeros((100,100))
b = a

for ii in range(40):
    #im = plt.imshow(a, 'gray', interpolation="none")
    #ims.append([im])
    for i in range(1,99):
        for k in range(1,99):
            av = np.mean(a[i-1:i+2,k-1:k+2])
            if av > 127.5:
                b[i,k] = a[i,k] + up
            if av <= 127.5:
                b[i,k] = a[i,k] + down
    b[b > 255] = 255
    b[b < 0] = 0
    a = b
    #plt.cla()
    im = plt.imshow(a, 'gray', interpolation="none")
    ims.append([im])
    plt.pause(0.3)

#ani = anime.ArtistAnimation(fig, ims, interval=300)
ani = anime.ArtistAnimation(fig, ims)
ani.save('anime.gif', writer="imagemagick")
#plt.show()
# print(len(ims))

