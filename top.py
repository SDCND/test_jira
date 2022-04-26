'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: top.py
 File Description: 
    This file will be running all of the functions to have a real time ball tracking
    system that will output in or out of bounds. 
'''

from itertools import count
import cv2
import math
from cv2 import imshow
import numpy as np
from algorithm1 import algorithm1

# VHDL
# import frameGrabber
from frameGrabber import ImageFeedthrough
from frameGrabber import ImageProcessing
import struct
import mmap

import time

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
    
    print("Before Initiailization")
    simulinkInitialize = True
    if  simulinkInitialize == True:
        print("init")
        f1 = open("/dev/mem", "r+b")
        simulinkMem = mmap.mmap( f1.fileno(), 1000, offset=0x81200000)
        simulinkMem.seek(0) 
        simulinkMem.write(struct.pack('l', 1))       # reset IP core
        simulinkMem.seek(8)                         
        simulinkMem.write(struct.pack('l', 752))     # image width
        simulinkMem.seek(12)                        
        simulinkMem.write(struct.pack('l', 480))     # image height
        simulinkMem.seek(16)                        
        simulinkMem.write(struct.pack('l', 0))       # zero horizontal porch
        simulinkMem.seek(20)                        
        simulinkMem.write(struct.pack('l', 0))       # zero vertical porch
        simulinkMem.seek(256) 
        simulinkMem.write(struct.pack('l', 255))  # coeff 1
        simulinkMem.write(struct.pack('l', 255))  # coeff 2
        simulinkMem.write(struct.pack('l', 255))  # coeff 3
        simulinkMem.seek(4) 
        simulinkMem.write(struct.pack('l', 1))       # enable IP core
    print("After Initiailization")
    
    # Clear Image
    global cameraFeedthrough
    cameraFeedthrough = ImageFeedthrough()
    # Clean Filtered Image
    global cameraProcessing
    cameraProcessing = ImageProcessing()
     
    # Have a boolean to change between RGB or GRay if desired
    frameLeftRGB,frameRightRGB = cameraFeedthrough.getStereoRGB()

    frameLeftGray,frameRightGray = cameraFeedthrough.getStereoGray()
    
    print("Before While")
    
    count = 0
    while count < 2:
        # Display Video Feed
        cv2.imwrite("frameLeftRGB%s.jpg" % count, frameLeftRGB)
        cv2.imwrite("frameRightRGB%s.jpg" % count, frameRightRGB)
        cv2.imwrite("frameLeftGray%s.jpg" % count, frameLeftGray)
        cv2.imwrite("frameRightGray%s.jpg" % count, frameRightGray)
        count += 1
        # X,Y,Z = algorithm1(frameLeftGray,frameRightGray,minArea)
        # posListX.append(X)
        # posListY.append(Y)
        # print(X,Y,Z)

if __name__ == "__main__":
    main()