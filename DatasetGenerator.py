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

for number_of_image in range(0, number_of_images):
    originOfCube.rotation_euler[2] = radians(number_of_image * (360.0 / number_of_images))
    bpy.data.scenes["Scene"].render.filepath = '/home/blahoslav/Documents/BlenderDatasetPreparation/cube_%d.jpg' % number_of_image
    bpy.ops.render.render(write_still=True)     
# bpy.data.scenes["Scene"].render.filepath = '/home/user/VR/vr_shot_%d.jpg' % number_of_images
    
    