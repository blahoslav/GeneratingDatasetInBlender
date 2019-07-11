#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:18:00 2019

@author: blahoslav
"""
import bpy
import sys
sys.path.append('/home/blahoslav/Documents/BlenderDatasetPreparation/')
import ImageCoordinateConvertor

cam = bpy.data.objects['Camera']
originOfCube = bpy.data.objects['cube_1']

number_of_images = 32

for number_of_image in range(0, number_of_images):
    originOfCube.rotation_euler[2] = radians(number_of_image * (360.0 / number_of_images))
    bpy.data.scenes["Scene"].render.filepath = '/home/blahoslav/Documents/BlenderDatasetPreparation/cube_%d.jpg' % number_of_image
    bpy.ops.render.render( write_still=True )

# bpy.data.scenes["Scene"].render.filepath = '/home/user/VR/vr_shot_%d.jpg' % number_of_images

