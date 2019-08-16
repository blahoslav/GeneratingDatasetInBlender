#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:55:22 2019

@author: blahoslav
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
print("One")
with open("/home/blahoslav/Documents/Image308/duck/points.xyz", "r") as ins:
    xCoordinates = []
    yCoordinates = []
    zCoordinates = []
    for line in ins:
        pointCoordinates = line.split()
        xCoordinates.append(pointCoordinates[0])
        yCoordinates.append(pointCoordinates[1])
        zCoordinates.append(pointCoordinates[2])
    print("Stage 1")

xCoordinates = np.array(xCoordinates)
yCoordinates = np.array(yCoordinates)
zCoordinates = np.array(zCoordinates)
R = np.array( [[-0.0152278998867, 0.073508001864, -0.997178018093],
             [-0.244435995817, -0.967307984829, -0.0675733014941],
             [0.969546020031, -0.242716997862, -0.0326980985701]] )
K = np.array( [[572.4114, 0.0, 325.2611],
             [0.0, 573.57043, 242.04899],
             [ 0.0, 0.0, 1.0]] )
uCoordinates = []
vCoordinates = []
for i in range(0, len(xCoordinates)):
    pointOnTheObject = np.array( [[xCoordinates[i].astype(float)],
                                   [yCoordinates[i].astype(float)],
                                   [zCoordinates[i].astype(float)]] )
    resulting_point = R @ K @ pointOnTheObject
    uCoordinates.append(resulting_point[0][0])
    vCoordinates.append(resulting_point[1][0])    
# for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
# ax.plot_surface(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), color='b')
  #  ax.scatter(xCoordinates, yCoordinates, zCoordinates, marker=m)


# surf = ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)
# ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# surf = ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)

# [572.4114, 0.0, 325.2611, 0.0, 573.57043, 242.04899, 0.0, 0.0, 1.0]

plt.plot(uCoordinates, vCoordinates, 'ro')
plt.axis([-50, 60, -50, 60])



plt.show()
