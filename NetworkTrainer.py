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
from PIL import Image

class NetworkTrainer:
    nameList = []
    def __init__(self, inputShape):
        self.__InputShape = inputShape

    def prepareLabels(self, cadPointOr, cadPointX, cadPointY, cadPointZ, imgPointO, imgPointX, imgPointY, imgPointZ):
        labels = []
        for l in range(0, len(cadPointOr)):
            label = []
            for p in range(0, len(cadPointOr[l])):
                label.append(np.array(cadPointOr[l][p]) - np.array(imgPointO[l][p]))
            for p in range(0, len(cadPointX[l])):
                label.append(np.array(cadPointX[l][p]) - np.array(imgPointX[l][p]))
            for p in range(0, len(cadPointY[l])):
                label.append(np.array(cadPointY[l][p]) - np.array(imgPointY[l][p]))
            for p in range(0, len(cadPointZ[l])):
                label.append(np.array(cadPointZ[l][p]) - np.array(imgPointZ[l][p]))
#            for p in range(0, len(imgPointO[l])):
#                label.append(imgPointO[l][p])
#            for p in range(0, len(imgPointX[l])):
#                label.append(imgPointX[l][p])
#            for p in range(0, len(imgPointY[l])):
#                label.append(imgPointY[l][p])
#            for p in range(0, len(imgPointZ[l])):
#                label.append(imgPointZ[l][p])
            labels.append(label)
        return labels
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
        Dense(1024, activation='relu'),
        Dense(8, activation='linear')])
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
        
        cadTestImages = []
        cadTestPointOCoordinates = []
        cadTestPointXCoordinates = []
        cadTestPointYCoordinates = []
        cadTestPointZCoordinates = []
        cadTestNames = []
        imgTestImages = []
        imgTestPointOCoordinates = []
        imgTestPointXCoordinates = []
        imgTestPointYCoordinates = []
        imgTestPointZCoordinates = []
        imgTestNames = []
        
        numberOfTrainImages = int(round(len(cadImageNames) * proportionOfTestImages))
        numberOfTestImages = int(round(len(cadImageNames) - numberOfTrainImages))
        
        for x in range(0, len(cadImageNames)):
            for o in range(0, len(nameList)):
                if(cadImageNames[x] == nameList[o]):
                    if (x < numberOfTestImages):
                        cadTestPointOCoordinates.append(originCoordinates[o])
                        cadTestPointXCoordinates.append(pointXCoordinates[o])
                        cadTestPointYCoordinates.append(pointYCoordinates[o])
                        cadTestPointZCoordinates.append(pointZCoordinates[o])
                        cadTestImages.append(cadImages[x])
                        cadTestNames.append(cadImageNames[x])
                    else:
                        cadTrainPointOCoordinates.append(originCoordinates[o])
                        cadTrainPointXCoordinates.append(pointXCoordinates[o])
                        cadTrainPointYCoordinates.append(pointYCoordinates[o])
                        cadTrainPointZCoordinates.append(pointZCoordinates[o])
                        cadTrainImages.append(cadImages[x])
                        cadTrainNames.append(cadImageNames[x])
            for k in range(0, len(imgImageNames)):
                if(cadImageNames[x].replace("cube_cad_", "") == imgImageNames[k].replace("cube_img_", "")):
                    if (x < numberOfTestImages):
                        imgTestImages.append(imgImages[k])
                        imgTestNames.append(imgImageNames[k])
                    else:
                        imgTrainImages.append(imgImages[k])
                        imgTrainNames.append(imgImageNames[k])
                    for c in range(0, len(nameList)):
                        if (imgImageNames[k] == nameList[c]):
                            reader = DataReader.DataReader(cadFolder, imgFolder, metadataFolder)
                            if (x < numberOfTestImages):
                                imgTestPointOCoordinates.append(originCoordinates[c])
                                imgTestPointXCoordinates.append(pointXCoordinates[c])
                                imgTestPointYCoordinates.append(pointYCoordinates[c])
                                imgTestPointZCoordinates.append(pointZCoordinates[c])
                            else:
                                imgTrainPointOCoordinates.append(originCoordinates[c])
                                imgTrainPointXCoordinates.append(pointXCoordinates[c])
                                imgTrainPointYCoordinates.append(pointYCoordinates[c])
                                imgTrainPointZCoordinates.append(pointZCoordinates[c])
        trainImages = []
        for p in range (0, len(cadTrainNames)):        
            cadImage = np.array(cadTrainImages[p])
            imgImage = np.array(imgTrainImages[p])
            trainImages.append(np.concatenate((cadImage, imgImage), axis=2))
            if (p == 10):
                print("CAD Image")
                plt.imshow(cadImage)
#                print("IMG Image")
#                plt.imshow(imgImage)
                print("CAD name")
                print(cadTrainNames[p])
                print("CAD coordinates")
                print(cadTrainPointXCoordinates[p])
                print("IMG name")
                print(imgTrainNames[p])
                print("IMG Coordinates")
                print(imgTrainPointXCoordinates[p])
        testImages = []
        for l in range (0, len(cadTestNames)):        
            cadImage = np.array(cadTestImages[l])
            imgImage = np.array(imgTestImages[l])
            testImages.append(np.concatenate((cadImage, imgImage), axis=2))
            if (l == 10):
#                print("CAD Image")
#                plt.imshow(cadImage)
#                print("IMG Image")
#                plt.imshow(imgImage)
                print("CAD test name")
                print(cadTestNames[l])
                print("CAD test coordinates")
                print(cadTestPointXCoordinates[l])
                print("IMG test name")
                print(imgTestNames[l])
                print("IMG test Coordinates")
                print(imgTestPointXCoordinates[l])
        print("No. of train images")
        print(len(trainImages))
        print("No. of test images")
        print(len(testImages))
        return trainImages, reader.ConvertVectorListToArray(cadTrainPointOCoordinates), reader.ConvertVectorListToArray(cadTrainPointXCoordinates), reader.ConvertVectorListToArray(cadTrainPointYCoordinates), reader.ConvertVectorListToArray(cadTrainPointZCoordinates), cadTrainNames, reader.ConvertVectorListToArray(imgTrainPointOCoordinates), reader.ConvertVectorListToArray(imgTrainPointXCoordinates), reader.ConvertVectorListToArray(imgTrainPointYCoordinates), reader.ConvertVectorListToArray(imgTrainPointZCoordinates), imgTrainNames, testImages, reader.ConvertVectorListToArray(cadTestPointOCoordinates), reader.ConvertVectorListToArray(cadTestPointXCoordinates), reader.ConvertVectorListToArray(cadTestPointYCoordinates), reader.ConvertVectorListToArray(cadTestPointZCoordinates), cadTestNames, reader.ConvertVectorListToArray(imgTestPointOCoordinates), reader.ConvertVectorListToArray(imgTestPointXCoordinates), reader.ConvertVectorListToArray(imgTestPointYCoordinates), reader.ConvertVectorListToArray(imgTestPointZCoordinates), imgTestNames
    
    
vggNetwork = NetworkTrainer((64, 64, 8))
print("Loop")
trainImages, cadTrainPointOCoordinates, cadTrainPointXCoordinates, cadTrainPointYCoordinates, cadTrainPointZCoordinates, cadNames, imgTrainPointOCoordinates, imgTrainPointXCoordinates, imgTrainPointYCoordinates, imgTrainPointZCoordinates, imgImageNames, testImages, cadTestPointOCoordinates, cadTestPointXCoordinates, cadTestPointYCoordinates, cadTestPointZCoordinates, cadTestNames, imgTestPointOCoordinates, imgTestPointXCoordinates, imgTestPointYCoordinates, imgTestPointZCoordinates, imgTestNames = vggNetwork.prepareTrainTestImagesAndData("/home/blahoslav/Documents/BlenderDatasetPreparation/cad", "/home/blahoslav/Documents/BlenderDatasetPreparation/img", "/home/blahoslav/Documents/BlenderDatasetPreparation", 0.75)
y_train = (np.array(vggNetwork.prepareLabels(cadTrainPointOCoordinates, cadTrainPointXCoordinates, cadTrainPointYCoordinates, cadTrainPointZCoordinates, imgTrainPointOCoordinates, imgTrainPointXCoordinates, imgTrainPointYCoordinates, imgTrainPointZCoordinates)))/64
print(y_train)
X_train = trainImages
X_train = np.array([x for x in trainImages]) 
X_test = np.array([x for x in testImages]) 
y_test = (np.array(vggNetwork.prepareLabels(cadTestPointOCoordinates, cadTestPointXCoordinates, cadTestPointYCoordinates, cadTestPointZCoordinates, imgTestPointOCoordinates, imgTestPointXCoordinates, imgTestPointYCoordinates, imgTestPointZCoordinates)))/64
# model = vggNetwork.prepareVGG16Model()
# model.compile(loss=keras.losses.mean_absolute_error, optimizer='adam', metrics=["accuracy"]) 
# history = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, nb_epoch = 12)   
# model.save("experiment_6.h5")
# testImage = np.expand_dims(X_test[10], axis=0)
# print(model.predict(testImage))

# fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None, validation_freq=1)

# Preparing dataset for training
#picture1 = np.array(cadImages[5])
#picture2 = np.array(imgImages[5])
#combinedImages = np.concatenate((picture1, picture2), axis=2)
#plt.imshow(combinedImages)
#print(combinedImages)