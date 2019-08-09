#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:23:11 2019

@author: https://www.learnopencv.com/rotation-matrix-to-euler-angles/
"""
import numpy as np
import math
R = np.array( [[0.851779997349,0.202316999435,-0.483258992434],
             [-0.313771009445,-0.541687011719,-0.779823005199],
             [-0.41954600811,0.815869987011,-0.397915989161]] )


Rt = np.transpose(R)
shouldBeIdentity = np.dot(Rt, R)
I = np.identity(3, dtype = R.dtype)
n = np.linalg.norm(I - shouldBeIdentity)
print(n)


# assert(isRotationMatrix(R))
     
sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
     
singular = sy < 1e-6
 
if  not singular :
     x = math.atan2(R[2,1] , R[2,2])
     y = math.atan2(-R[2,0], sy)
     z = math.atan2(R[1,0], R[0,0])
else :
     x = math.atan2(-R[1,2], R[1,1])
     y = math.atan2(-R[2,0], sy)
     z = 0
 