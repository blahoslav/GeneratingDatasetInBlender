ay#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:01:22 2019

@author: blahoslav
"""
class FileWriter:
    __MetadataNames = []
    __PointXCoordinates = []
    __PointYCoordinates = []
    __PointZCoordinates = []
    __OriginCoordinates = []
    def __init__(self, destinationFolderAddress):
        self.DestinationFolderAddress = destinationFolderAddress
        
    def WriteMetadataIntoFile(self, nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates):
        file = open(self.DestinationFolderAddress + "/metadata", "w")
        self.__MetadataNames = nameList
        self.__OriginCoordinates = originCoordinates
        self.__PointXCoordinates = pointXCoordinates
        self.__PointYCoordinates = pointYCoordinates
        self.__PointZCoordinates = pointZCoordinates
        print(self.__OriginCoordinates)
        for x in range(len(self.__MetadataNames)):
            file.write("name = " + self.__MetadataNames[x] + "\n")
            file.write("o = " + str(self.__OriginCoordinates[x]) + "\n")
            file.write("x = " + self.__PointXCoordinates[x] + "\n")
            file.write("y = " + self.__PointYCoordinates[x] + "\n")
            file.write("z = " + self.__PointZCoordinates[x] + "\n")
        file.close()

#writer = FileWriter("/home/blahoslav/Documents/BlenderDatasetPreparation")
#nameList = ["c1", "c2"]
#originCoordinates = ["(1, 1, 1)", "(2, 2, 2)"]
#pointXCoordinates = ["(1, 0, 0)", "(2, 0, 0)"]
#pointYCoordinates = ["(0, 1, 0)", "(0, 2, 0)"]
#pointZCoordinates = ["(0, 0, 1)", "(0, 0, 2)"]
#writer.WriteMetadataIntoFile(nameList, originCoordinates, pointXCoordinates, pointYCoordinates, pointZCoordinates)
        
        
        
#f = open("demofile3.txt", "w")
#f.write("Woops! I have deleted the content!")
#f.close()
