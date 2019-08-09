#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:55:22 2019

@author: blahoslav
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
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
# for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
# ax.plot_surface(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), color='b')
  #  ax.scatter(xCoordinates, yCoordinates, zCoordinates, marker=m)

surf = ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)
# surf = ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)
ax.plot_trisurf(xCoordinates.astype(float), yCoordinates.astype(float), zCoordinates.astype(float), linewidth=0, antialiased=False)


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
