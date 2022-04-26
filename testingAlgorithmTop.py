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
# import algorithm3
import algorithm4

import ballDirection
import globalVariables

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
    
    myColorFinder = c

    if videoMode: # Video Mode
        # Create a background substarctor
        # Takes first frame as empty iamge, first frame will always be without the ball
        substractor = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
        
        pathLeft = 'testvideos/testDJM.mov'
        pathRight = 'testvideos/testDJM.mov'
        path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
        path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
        videoLeftGray = cv2.VideoCapture(pathLeft) # Gets Video
        videoRightGray = cv2.VideoCapture(pathRight) # Gets Video
        
        while True:
            # Video Mode
            success, frameLeftGray = videoLeftGray.read()
            success, frameLeftGray = videoRightGray.read()

            # Algorithm 1 Testing
            # X,Y,Z = algorithm1.algorithm1(frameLeftGray,frameRightGray,minArea,substractor)
            #Algorithm 2 Testing
            X,Y,Z = algorithm2.algorithm2(frameLeftGray,frameRightGray,globalVariables.minArea,substractor)

            globalVariables.posListX.append(X)
            globalVariables.posListY.append(Y)
            
            # Debugging
            print(X,Y,Z)
            cv2.imshow("FrameLeft", frameLeftGray)
            cv2.imshow("FrameRight", frameRightGray)
            cv2.waitKey(0)
    
    else: #Image Mode
        pathLeft = "testImages/LabStereoImage/frameLeftRGB0"
        pathRight = "testImages/LabStereoImage/frameRightRGB0"
        pathLeft2 = 'testImages/left5.jpg'
        pathRight2 = 'testImages/right5.jpg'
        frameLeftGray = cv2.imread(pathLeft2, cv2.IMREAD_GRAYSCALE)
        frameRightGray = cv2.imread(pathRight2, cv2.IMREAD_GRAYSCALE)

        # Motion Detection        
        # Algorithm 1 Testing - Blob Detector
        # X,Y,Z = algorithm1.algorithm1(frameLeftGray,frameRightGray,globalVariables.minArea,substractor)
        # Algorithm 2 Testing - Contour Finder
        X,Y,Z = algorithm2.algorithm2(frameLeftGray,frameRightGray,globalVariables.minArea,substractor)

        # Color Finder
        # Algorithm 1 Testing - Blob Detector
        # X,Y,Z = algorithm3.algorithm3(frameLeftGray,frameRightGray,globalVariables.minArea,substractor)
        # # Algorithm 2 Testing - Contour Finder
        # X,Y,Z = algorithm4.algorithm4(frameLeftGray,frameRightGray,globalVariables.minArea,substractor)

        globalVariables.posListX.append(X)
        globalVariables.posListY.append(Y)
        
        # Debugging
        print(X,Y,Z)
        cv2.imshow("FrameLeft", frameLeftGray)
        cv2.imshow("FrameRight", frameRightGray)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()