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
    def prepareTrainTestImagesAndData(self, cadFolder, imgFolder, metadataFolder, proportionOfTestImages):
        reader = DataReader.DataReader(cadFolder, imgFolder, metadataFolder)
        cadImageNames, cadImages, imgImageNames, imgImages = reader.ReadImages()
        nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates = reader.ReadMetadata()
        cadTrainImages = []
        cadTrainPointOCoordinates = []
        cadTrainPointXCoordinates = []
        cadTrainPointYCoordinates = []
        cadTrainPointZCoordinates = []
        cadTrainNames = []
        imgTrainImages = []
        imgTrainPointOCoordinates = []
        imgTrainPointXCoordinates = []
        imgTrainPointYCoordinates = []
        imgTrainPointZCoordinates = []
        imgTrainNames = []
        for x in range(0, len(cadImageNames)):
            for o in range(0, len(nameList)):
                if(cadImageNames[x] == nameList[o]):
                    cadTrainPointOCoordinates.append(originCoordinates[o])
                    cadTrainPointXCoordinates.append(pointXCoordinates[o])
                    cadTrainPointYCoordinates.append(pointYCoordinates[o])
                    cadTrainPointZCoordinates.append(pointZCoordinates[o])
                    cadTrainImages.append(cadImages[x])
                    cadTrainNames.append(cadImageNames[x])
            for k in range(0, len(imgImageNames)):
                if(cadImageNames[x].replace("cube_cad_", "") == imgImageNames[k].replace("cube_img_", "")):
                    imgTrainImages.append(imgImages[k])
                    imgTrainNames.append(imgImageNames[k])
                    for c in range(0, len(nameList)):
                        if (imgImageNames[k] == nameList[c]):
                            imgTrainPointOCoordinates.append(originCoordinates[c])
                            imgTrainPointXCoordinates.append(pointXCoordinates[c])
                            imgTrainPointYCoordinates.append(pointYCoordinates[c])
                            imgTrainPointZCoordinates.append(pointZCoordinates[c])
        trainImages = []
        print("Data")
        print(np.shape(cadTrainImages))
        print(np.shape(imgTrainImages))
        print(len(cadTrainNames))
        for p in range (0, len(cadTrainNames)):
            cadImage = np.array(cadTrainImages[p])
            imgImage = np.array(imgTrainImages[p])
            trainImages.append(np.concatenate((cadImage, imgImage), axis=2))
        return trainImages, cadTrainPointOCoordinates, cadTrainPointXCoordinates, cadTrainPointYCoordinates, cadTrainPointZCoordinates, cadTrainNames, imgTrainPointOCoordinates, imgTrainPointXCoordinates, imgTrainPointYCoordinates, imgTrainPointZCoordinates, imgTrainNames
            
            
vggNetwork = NetworkTrainer((64, 64, 3))
trainImages, cadPointOCoordinates, cadPointXCoordinates, cadPointYCoordinates, cadPointZCoordinates, cadNames, imgPointOCoordinates, imgPointXCoordinates, imgPointYCoordinates, imgPointZCoordinates, imgImageNames = vggNetwork.prepareTrainTestImagesAndData("/home/blahoslav/Documents/BlenderDatasetPreparation/cad", "/home/blahoslav/Documents/BlenderDatasetPreparation/img", "/home/blahoslav/Documents/BlenderDatasetPreparation", 0.75)
#model = vggNetwork.prepareVGG16Model()
#model.compile(loss=keras.losses.categorical_crossentropy, optimizer='adam', metrics=["accuracy"]) 

# fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)
# model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=64)   

# Preparing dataset for training
#picture1 = np.array(cadImages[5])
#picture2 = np.array(imgImages[5])
#combinedImages = np.concatenate((picture1, picture2), axis=2)
#plt.imshow(combinedImages)
#print(combinedImages)