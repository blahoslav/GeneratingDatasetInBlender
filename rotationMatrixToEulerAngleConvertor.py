#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:23:11 2019

@author: https://www.learnopencv.com/rotation-matrix-to-euler-angles/
"""
import numpy as np
import math
R = np.array( [[0.969546020031, -0.242716997862, -0.0326980985701],
             [-0.244435995817, -0.967307984829, -0.0675733014941],
             [-0.0152278998867, 0.073508001864, -0.997178018093]] )
Rt = np.transpose(R)
shouldBeIdentity = np.dot(Rt, R)
I = np.identity(3, dtype = R.dtype)
n = np.linalg.norm(I - shouldBeIdentity)
print(n)
# assert(isRotationMatrix(R))

sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
singular = sy < 1e-6
 
if  not singular :
     x = math.atan2(R[2,1] , R[2,2]) * (180 / math.pi)
     y = math.atan2(-R[2,0], sy) * (180 / math.pi)
     z = math.atan2(R[1,0], R[0,0]) * (180 / math.pi)
else :
     x = math.atan2(-R[1,2], R[1,1])
     y = math.atan2(-R[2,0], sy)
     z = 0
 