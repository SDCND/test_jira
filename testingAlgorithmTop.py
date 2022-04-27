'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: top.py
 File Description: 
    This file will be running all of the functions to have a real time ball tracking
    system that will output in or out of bounds. 
'''
from itertools import count
from multiprocessing.connection import wait

import cv2
import math
import numpy as np

import algorithm1
import algorithm2
import algorithm3
import algorithm4

import ballDirection
import globalVariables

import struct
import socket

# VHDL
# import frameGrabber
# from frameGrabber import ImageFeedthrough
# from frameGrabber import ImageProcessing
# import struct
# import mmap

# import time

# Board doesn't have file yet 
# from inOutBounds import inBounds
""""
import io
import cv2
import remi.gui as gui
from remi import start, App

import logging
import numpy as np
import mmap
import struct
import sys, random
import ctypes
import copy
import os
"""
# import apriltag

# def realTimeTracker(frameLeftRGB,frameRightRGB,frameLeftGray,frameRightGray,minArea):
#     return inBounds

def main():
    # Testing Numbers
    imageFrameWidthDimensions = 2436 #4k
    videoMode = True
    colorFinderMaunal = False
    ballColor = "orange"

    # Create a background substarctor
    # Takes first frame as empty iamge, first frame will always be without the ball
    substractor = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    kernal = np.ones((5,5),np.uint8)
    
    if videoMode: # Video Mode

        path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
        path1 = 'testvideos/bounds/orangeBallMiddleBound2.mov'
        path2 = 'testvideos/bounds/orangeBallRightBound2.mov'
        path3 = 'testvideos/testDJM.mov'
        
        videoLeft = cv2.VideoCapture(path2) # Gets Video
        videoRight = cv2.VideoCapture(path2) # Gets Video
        
        # #connect to socket server. Unity Server
        # host = '68.180.86.216'  #change to your PC's IPv4 Address from ipcongif in CMD
        # port = 55001            #do not change port, it is hard coded into the unity server C# file
        # size = 1024
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((host,port))

        while True: # Video Mode
            success, frameLeft = videoLeft.read()
            success, frameRight = videoRight.read()
            
            grayFrameLeft = cv2.cvtColor(frameLeft,cv2.COLOR_BGR2GRAY)
            grayFrameRight = cv2.cvtColor(frameRight,cv2.COLOR_BGR2GRAY)

            # Algorithm 1 Testing
            # X,Y,Z = algorithm1.algorithm1(grayFrameLeft,grayFrameRight,globalVariables.minArea,kernal,substractor)
            # Algorithm 2 Testing
            X,Y,Z = algorithm2.algorithm2(grayFrameLeft,grayFrameRight,globalVariables.minArea,kernal,substractor)

            # Color Finder
            # Algorithm 3 Testing - Blob Detector
            # X,Y,Z = algorithm3.algorithm3(RGBFrameLeft,RGBFrameRight,'orange',globalVariables.minArea,customColor=False)
            # Algorithm 4 Testing - Contour Finder
            # X,Y,Z = algorithm4.algorithm4(RGBFrameLeft,RGBFrameRight,'orange',globalVariables.minArea,customColor=False)

            globalVariables.posListX.append(X)
            globalVariables.posListY.append(Y)
            
            # # Debugging
            # # Pack X, Y, Z values into a byte array
            # values = (0.0, 0.0, X, Y, Z, 0.0, 0.0, 0.0)
            # packer = struct.Struct('f f f f f f f f')
            # packed_data = packer.pack(*values)
            # s.send(packed_data) #send byte array to Unity server.
            
            print(X,Y,Z)
            grayFrameLeft = cv2.resize(grayFrameLeft,(0,0), None, 0.25,0.25)
            cv2.imshow("FrameLeft", grayFrameLeft)
            grayFrameRight = cv2.resize(grayFrameRight,(0,0), None, 0.25,0.25)
            cv2.imshow("FrameRight", grayFrameRight)
            cv2.waitKey(50)
    
    else: #Image Mode
        pathLeft = 'testImages/LabStereoImage/frameLeftRGB0.jpg'
        pathRight = 'testImages/LabStereoImage/frameRightRGB0.jpg'
        pathLeft2 = 'testImages/blueBall.jpg'
        pathRight2 = 'testImages/blueBall.jpg'
        pathLeft3 = 'testImages/StereoCamera/left3 (1).jpg'
        pathRight3 = 'testImages/StereoCamera/right3 (1).jpg'
        pathLeft4 = 'testImages/LabImages/left1.jpg'
        pathRight4 = 'testImages/LabImages/right1.jpg'
        pathLeft5 = 'testImages/LabImages/left5.jpg'
        pathRight5 = 'testImages/LabImages/right5.jpg'
        
        RGBFrameLeft = cv2.imread(pathLeft5)
        RGBFrameRight = cv2.imread(pathRight5)
        
        # Motion Detection Mode - Doesn't Work on one frame analysis
        grayFrameLeft = cv2.cvtColor(RGBFrameLeft,cv2.COLOR_BGR2GRAY)
        grayFrameRight = cv2.cvtColor(RGBFrameRight,cv2.COLOR_BGR2GRAY)
        
        # Check if iamges are showing right
        # if True:
        #     cv2.imshow("FrameLeft", frameLeft)
        #     cv2.imshow("FrameRight", frameRight)
        #     print(frameLeft)
        #     print("Space for shit")
        #     print(frameRight)
        #     cv2.waitKey(0)

        # frameLeftGray = cv2.imread(pathLeft2, cv2.IMREAD_GRAYSCALE)
        # frameRightGray = cv2.imread(pathRight2, cv2.IMREAD_GRAYSCALE)

        # Motion Detectin - Doesn't Work on one frame anaylsis
        # Algorithm 1 Testing
        # X,Y,Z = algorithm1.algorithm1(grayFrameLeft,grayFrameRight,globalVariables.minArea,kernal,substractor)
        # Algorithm 2 Testing
        # X,Y,Z = algorithm2.algorithm2(grayFrameLeft,grayFrameRight,globalVariables.minArea,kernal,substractor)
        
        # Color Finder
        # Algorithm 3 Testing - Blob Detector
        # X,Y,Z = algorithm3.algorithm3(RGBFrameLeft,RGBFrameRight,'orange',globalVariables.minArea,customColor=False)
        # Algorithm 4 Testing - Contour Finder
        # X,Y,Z = algorithm4.algorithm4(RGBFrameLeft,RGBFrameRight,'orange',globalVariables.minArea,customColor=False)

        globalVariables.posListX.append(X)
        globalVariables.posListY.append(Y)
        
        # Debugging
        print( "X Value: ", X, "\nY Value: ", Y,"\nZ Value: ",Z)
        cv2.imshow("FrameLeft", RGBFrameLeft)
        cv2.imshow("FrameRight", RGBFrameRight)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()