#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:44:32 2019

@author: blahoslav
"""
from PIL import Image
import glob
class DataReader:
    __ImageList = []
    __Images = []
    __MetadataNames = []
    __PointXCoordinates = []
    __PointYCoordinates = []
    __PointZCoordinates = []
    __OriginCoordinates = []
    def __init__(self, imageFolderAddress, metadataFileAddress):
        self.ImageFolderAddress = imageFolderAddress
        self.MetadataFileAddress = metadataFileAddress
 
    def ReadImages(self):
        for imageName in glob.glob(self.ImageFolderAddress + '/*.png'):
            self.__ImageList.append(imageName.replace(self.ImageFolderAddress + '/', ''))
            self.__Images.append(Image.open(imageName))
        return self.__ImageList
    
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
            if("x" in line):
                self.__PointXCoordinates.append(line.replace("x = ", ""))
            if("y" in line):
                self.__PointYCoordinates.append(line.replace("y = ", ""))
            if("z" in line):
                self.__PointZCoordinates.append(line.replace("z = ", ""))
            if("o" in line):
                self.__OriginCoordinates.append(line.replace("o = ", ""))
        return self.__MetadataNames, self.__OriginCoordinates, self.__PointXCoordinates, self.__PointYCoordinates, self.__PointZCoordinates
    
reader = DataReader("/home/blahoslav/Documents/BlenderDatasetPreparation", "/home/blahoslav/Documents/BlenderDatasetPreparation")
imageNameList = reader.ReadImages()
nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates = reader.ReadMetadata()


        


        
