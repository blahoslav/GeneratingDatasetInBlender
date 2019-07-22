#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:44:32 2019

@author: blahoslav
"""
from PIL import Image
import glob
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
class DataReader:
    __ImageList = []
    __Images = []
    __MetadataNames = []
    __PointXCoordinates = []
    __PointYCoordinates = []
    __PointZCoordinates = []
    __OriginCoordinates = []
    def __init__(self, cadFolderAddress, imgFolderAddress, metadataFileAddress):
        self.cadFolderAddress = cadFolderAddress
        self.imgFolderAddress = imgFolderAddress
        self.MetadataFileAddress = metadataFileAddress
 
    def ReadImages(self):
        self.__cadImageList = []
        self.__cadImages = []
        self.__imgImageList = []
        self.__imgImages = []
        for imageName in glob.glob(self.cadFolderAddress + '/*.png'):
            self.__cadImageList.append(imageName.replace(self.cadFolderAddress + '/', ''))
            img = Image.open(imageName)
            width = 64
            height = 64
            img = img.resize((width, height), Image.ANTIALIAS) 
            self.__cadImages.append(img)
        for imageName in glob.glob(self.imgFolderAddress + '/*.png'):
            self.__imgImageList.append(imageName.replace(self.imgFolderAddress + '/', ''))
            img = Image.open(imageName)
            width = 64
            height = 64
            img = img.resize((width, height), Image.ANTIALIAS) 
            self.__imgImages.append(img)
        return self.__cadImageList, self.__cadImages, self.__imgImageList, self.__imgImages 
    
    def ReadMetadata(self):
        metadataFile = open(self.MetadataFileAddress + "/metadata", "r")
        self.__MetadataNames.clear()
        self.__OriginCoordinates.clear()
        self.__PointXCoordinates.clear()
        self.__PointYCoordinates.clear()
        self.__PointZCoordinates.clear()
        for line in metadataFile:
            line = line.replace("\n", "")
            if("name" in line):
                self.__MetadataNames.append(line.replace("name = ", ""))
            elif("x" in line):
                self.__PointXCoordinates.append(line.replace("x = ", ""))
            elif("y" in line):
                self.__PointYCoordinates.append(line.replace("y = ", ""))
            elif("z" in line):
                self.__PointZCoordinates.append(line.replace("z = ", ""))
            elif("o" in line):
                self.__OriginCoordinates.append(line.replace("o = ", ""))
        metadataFile.close()
        return self.__MetadataNames, self.__OriginCoordinates, self.__PointXCoordinates, self.__PointYCoordinates, self.__PointZCoordinates
    
    def ConvertVectorListToArray(self, vectorArray):
        arrayOfVectors = []
        for vector in vectorArray:
            vector = vector.replace("<Vector (", "")
            vector = vector.replace(")>","")
            vector = vector.split(",")
            vector = list(map(float, vector))
            vector = numpy.asarray(vector)
            arrayOfVectors.append(vector)
        return arrayOfVectors
        
reader = DataReader("/home/blahoslav/Documents/BlenderDatasetPreparation/cad", "/home/blahoslav/Documents/BlenderDatasetPreparation/img", "/home/blahoslav/Documents/BlenderDatasetPreparation")
cadImageNames, cadImages, imgImageNames, imgImages = reader.ReadImages()
#print(cadImages)
#plt.imshow(cadImages[10])
#imageContent = numpy.array(cadImages[10])
#print(imageContent)
#nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates = reader.ReadMetadata()
#reader.ConvertVectorListToArray(originCoordinates)