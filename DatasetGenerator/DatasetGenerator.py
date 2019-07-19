#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:18:00 2019
@author: blahoslav
"""
import bpy
import bpy_extras
import sys
sys.path.append('/home/blahoslav/Documents/BlenderDatasetPreparation/')
import ImageCoordinateConvertor
import FileWriter
from mathutils import Matrix, Vector

# Function to add background image - code from https://blender.stackexchange.com/questions/76054/render-scene-with-background-jpg-in-python 
def addBackgroundImage(filepath):
    img = bpy.data.images.load(filepath)
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            space_data = area.spaces.active
            bg = space_data.background_images.new()
            bg.image = img
            space_data.show_background_images = True
            break

    texture = bpy.data.textures.new("TextureKensington", 'IMAGE')
    texture.image = img
    bpy.data.worlds['World'].active_texture = texture
    bpy.context.scene.world.texture_slots[0].use_map_horizon = True

#addBackgroundImage('/home/blahoslav/Documents/BlenderDatasetPreparation/kensingtonBackgroundImage.jpg')
number_of_images = 4
originOfCube = bpy.data.objects['cube_1']
imageNames = []
pointXCoordinates = []
pointYCoordinates = []
pointZCoordinates = []
pointOCoordinates = []
cam = bpy.data.objects['Camera']
P, K, RT = ImageCoordinateConvertor.get3x4PMatrixFromBlender(cam)

for number_of_image in range(0, number_of_images):
    originOfCube.rotation_euler[2] = radians(number_of_image * (360.0 / number_of_images))
    bpy.data.scenes["Scene"].render.filepath = '/home/blahoslav/Documents/BlenderDatasetPreparation/cube_%d.png' % number_of_image
    bpy.ops.render.render(write_still=True)     
    imageNames.append("cube_" + str(number_of_image) + ".png")
    e1 = ImageCoordinateConvertor.getWorldVectorCoordinateOfObjectOnScene('point_x')
    print("abcd")
    p1 = P * e1
    p1 /= p1[2]
    pointXCoordinates.append(p1)
    e2 = ImageCoordinateConvertor.getWorldVectorCoordinateOfObjectOnScene('point_y')
    p2 = P * e2
    p2 /= p2[2]
    pointYCoordinates.append(p2)
    e3 = ImageCoordinateConvertor.getWorldVectorCoordinateOfObjectOnScene('point_z')
    p3 = P * e3
    p3 /= p3[2]
    pointZCoordinates.append(p3)
    e4 = ImageCoordinateConvertor.getWorldVectorCoordinateOfObjectOnScene('cube_1')
    p4 = P * e4
    p4 /= p4[2]
    pointOCoordinates.append(p4)
writer = FileWriter("/home/blahoslav/Documents/BlenderDatasetPreparation");
writer.WriteMetadataIntoFile(imageNames, pointOCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates)
    
    
# bpy.data.scenes["Scene"].render.filepath = '/home/user/VR/vr_shot_%d.jpg' % number_of_images
    
    
