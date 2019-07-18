#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:38:34 2019

@author: blahoslav
"""
import sys
sys.path.append('/home/blahoslav/Documents/BlenderDatasetPreparation/')
import DataReader
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 

class NetworkTrainer:
    nameList = []
    def __init__(self, inputShape):
        self.__InputShape = inputShape
    def prepareVGG16Model(self):
        model = Sequential([Conv2D(64, (3, 3), input_shape=self.__InputShape, padding='same', activation='relu'),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        Conv2D(128, (3, 3), activation='relu', padding='same',),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        Conv2D(256, (3, 3), activation='relu', padding='same',),
        Conv2D(256, (3, 3), activation='relu', padding='same',),
        Conv2D(256, (3, 3), activation='relu', padding='same',),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        Conv2D(512, (3, 3), activation='relu', padding='same',),
        MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        Flatten(),
        Dense(4096, activation='relu'),
        Dense(4096, activation='relu'),
        Dense(8, activation='softmax')])
        return model
    def prepareTrainingImagesAndData(self, cadFolder, imgFolder, metadataFolder):
        reader = DataReader.DataReader(cadFolder, imgFolder, metadataFolder)
        cadImageNames, cadImages, imgImageNames, imgImages = reader.ReadImages()
        nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates = reader.ReadMetadata()
        cadTrainImages = []
        cadPointOCoordinates = []
        cadPointXCoordinates = []
        cadPointYCoordinates = []
        cadPointZCoordinates = []
        cadNames = []
        imgTrainImages = []
        imgPointOCoordinates = []
        imgPointXCoordinates = []
        imgPointYCoordinates = []
        imgPointZCoordinates = []
        imgNames = []
        for x in range(0, len(cadImageNames)):
            cadPicture = cadImages[x]
            for o in range(0, len(nameList)):
                if(cadImageNames[x] == nameList[o]):
                    cadPointOCoordinates.append(originCoordinates[o])
                    cadPointXCoordinates.append(pointXCoordinates[o])
                    cadPointYCoordinates.append(pointYCoordinates[o])
                    cadPointZCoordinates.append(pointZCoordinates[o])
                    cadTrainImages.append(cadImages[x])
                    cadNames.append(cadImageNames[x])
            for k in range(0, len(imgImageNames)):
                if(cadImageNames[x].replace("cube_cad_", "") == imgImageNames[k].replace("cube_img_", "")):
                    imgTrainImages.append(imgImages[k])
                    imgNames.append(imgImageNames[k])
                    for c in range(0, len(nameList)):
                        if (imgImageNames[k] == nameList[c]):
                            imgPointOCoordinates.append(originCoordinates[c])
                            imgPointXCoordinates.append(pointXCoordinates[c])
                            imgPointYCoordinates.append(pointYCoordinates[c])
                            imgPointZCoordinates.append(pointZCoordinates[c])
        trainImages = []
        for p in range (0, len(cadNames)):
            cadImage = np.array(cadImages[p])
            imgImage = np.array(imgImages[p])
            combinedImage = np.concatenate((cadImage, imgImage), axis=2)
        
        
                            
vggNetwork = NetworkTrainer((64, 64, 3))
vggNetwork.prepareTrainingImagesAndData("/home/blahoslav/Documents/BlenderDatasetPreparation/cad", "/home/blahoslav/Documents/BlenderDatasetPreparation/img", "/home/blahoslav/Documents/BlenderDatasetPreparation")
#model = vggNetwork.prepareVGG16Model()
#model.compile(loss=keras.losses.categorical_crossentropy, optimizer='adam', metrics=["accuracy"]) 

        

# Preparing dataset for training
#picture1 = np.array(cadImages[5])
#picture2 = np.array(imgImages[5])
#combinedImages = np.concatenate((picture1, picture2), axis=2)
#plt.imshow(combinedImages)
#print(combinedImages)