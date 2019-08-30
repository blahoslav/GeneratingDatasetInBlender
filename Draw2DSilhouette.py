#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:55:22 2019

@author: blahoslav
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pdb
import matplotlib.image as mpimg

def project_pts(pts, K, R, t):
  """Projects 3D points.
  :param pts: nx3 ndarray with the 3D points.
  :param K: 3x3 ndarray with an intrinsic camera matrix.
  :param R: 3x3 ndarray with a rotation matrix.
  :param t: 3x1 ndarray with a translation vector.
  :return: nx2 ndarray with 2D image coordinates of the projections.
  """
  assert (pts.shape[1] == 3)
  P = K.dot(np.hstack((R, t)))
  pts_h = np.hstack((pts, np.ones((pts.shape[0], 1))))
  pts_im = P.dot(pts_h.T)
  pts_im /= pts_im[2, :]
  return pts_im[:2, :].T

with open("/home/blahoslav/Documents/Image308/duck/points.xyz", "r") as ins:
    UCoordinates = []
    VCoordinates = []
    WCoordinates = []
    UVWCoordinate = []
    for line in ins:
        pointCoordinates = line.split()
        UCoordinates.append(pointCoordinates[0])
        VCoordinates.append(pointCoordinates[1])
        WCoordinates.append(pointCoordinates[2])
        UVWCoordinate.append(pointCoordinates[0])
        UVWCoordinate.append(pointCoordinates[1])
        UVWCoordinate.append(pointCoordinates[2])
      #  UVWCoordinates.append(UVWCoordinate)

UCoordinates = np.array(UCoordinates)
VCoordinates = np.array(VCoordinates)
WCoordinates = np.array(WCoordinates)
# 000308-color.png -> duck
R = np.array( [[0.851779997349, 0.202316999435, -0.483258992434, 0.0076962755993],
             [-0.313771009445, -0.541687011719, -0.779823005199, 0.00826022215188],
             [-0.41954600811, 0.815869987011, -0.397915989161, 0.743500173092],
             [0.0, 0.0, 0.0, 1.0]] ) 
    
R_simple = np.array( [[0.851779997349, 0.202316999435, -0.483258992434],
             [-0.313771009445, -0.541687011719, -0.779823005199],
             [-0.41954600811, 0.815869987011, -0.397915989161]] )
    
#    R_simple = np.array( [[0.851779997349, 0.202316999435, -0.483258992434],
#             [0.313771009445, 0.541687011719, 0.779823005199],
#             [0.41954600811, -0.815869987011, 0.397915989161]] )
#R_simple_2 = np.array( [[-0.41954600811, 0.815869987011, -0.397915989161],
#             [-0.313771009445, -0.541687011719, -0.779823005199],
#             [0.851779997349, 0.202316999435, -0.483258992434]] )
        
T = np.array([[0.0076962755993], 
              [0.00826022215188], 
              [0.743500173092]]) 
K = np.array( [[572.4114, 0.0, 325.2611, 0.0],
             [0.0, 573.57043, 242.04899, 0.0],
             [ 0.0, 0.0, 1.0, 0.0]] )
KSimple = np.array( [[572.4114, 0.0, 325.2611],
             [0.0, 573.57043, 242.04899],
             [ 0.0, 0.0, 1.0]] )
    
uCoordinates = []
vCoordinates = []
UVWCoordinates = []
for i in range(0, len(UCoordinates)):
    worldCoordinates = np.array( [[UCoordinates[i].astype(float)],
                                   [VCoordinates[i].astype(float)],
                                   [WCoordinates[i].astype(float)],
                                   [1]])
    UVWCoordinates.append(np.array([UCoordinates[i].astype(float), VCoordinates[i].astype(float), WCoordinates[i].astype(float)]))
    cameraCoordinates = R @ worldCoordinates
    filmCoordinates = K @ cameraCoordinates
    uCoordinates.append((filmCoordinates[0][0])/filmCoordinates[2][0])
    vCoordinates.append((filmCoordinates[1][0])/filmCoordinates[2][0]) 
UVWCoordinates = np.array(UVWCoordinates)
vysledek = project_pts(UVWCoordinates, KSimple, R_simple, T)
# plt.plot(uCoordinates, vCoordinates, 'ro')
uCoordinates, vCoordinates = zip(*vysledek)
plt.plot(uCoordinates, vCoordinates, 'ro')
plt.axis([0, 640, 480, 0])
img=mpimg.imread('/home/blahoslav/Documents/Image308/duck/09 - duck/000308-color.png')
imgplot = plt.imshow(img)
plt.show()