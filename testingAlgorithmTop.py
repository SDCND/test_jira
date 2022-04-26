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
from cv2 import imshow
import numpy as np
import algorithm1
import algorithm2
import ballDirection

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
    minArea = 1000
    posListX, posListY = [], []
    
    # Create a background substarctor
    substractor = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
    
    # Video Mode
    pathLeft = 'testvideos/testDJM.mov'
    pathRight = 'testvideos/testDJM.mov'
    
    path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
    path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'


    frameLeftGray = cv2.VideoCapture(pathLeft) # Gets Video
    frameRightGray = cv2.VideoCapture(pathRight) # Gets Video
    
    while True:
        # Video Mode
        # success, frameGray = cap.read()

        #Image Mode
        frameLeftGray = cv2.imread('testImages/left5.jpg', cv2.IMREAD_GRAYSCALE)
        frameRightGray = cv2.imread('testImages/right5.jpg', cv2.IMREAD_GRAYSCALE)

        # Algorithm 1 Testing
        # X,Y,Z = algorithm1.algorithm1(frameLeftGray,frameRightGray,minArea,substractor)
        #Algorithm 2 Testing
        X,Y,Z = algorithm2.algorithm2(frameLeftGray,frameRightGray,minArea,substractor)

        posListX.append(X)
        posListY.append(Y)
        
        print(X,Y,Z)
        cv2.imshow("FrameLeft", frameLeftGray)
        cv2.imshow("FrameRight", frameRightGray)
        cv2.waitKey(0)
        
        # Debugging Code
        # Draws the line and dot of the centroid of the ball
        # for imageFrame, (posX, posY) in enumerate(zip(posListX, posListY)):
        #     pos = (posX, posY)
        #     cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
        #     if imageFrame == 0:
        #         cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
        #     else:
        #         cv2.line(imgContours, pos, (posListX[imageFrame - 1], posListY[imageFrame - 1]), (0, 255, 0), 5)
        
        # # Create the dot of the Center of the ball
        # for x in xList:
        #     y = int(A * x ** 2 + B * x + C)
        #     cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)

        # Prediction Reset
        # if contours:
        #     if ballDirection.ballBouncing1(posListY) == True:
        #         posListX = posListX[len(posListX)-2:]
        #         posListY = posListY[len(posListY)-2:]
        #     if counter != 0:
        #         posListX.append(contours[0]['center'][0])
        #         posListY.append(contours[0]['center'][1])
        #     counter += 1
        # pass

if __name__ == "__main__":
    main()