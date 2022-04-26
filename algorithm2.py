'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: ballAlgorithm2.py
 File Description: 
    Using motion detection an image with only the objects that moved will be show in the new image.
    With the use of findcontours the center of the ball will be used to ge the ball location in the image
    Output the real world X,Y,& Z of the ball and if in or out of bound
'''

import cv2
import numpy as np
import math
import ballDirection
import motionDetection

def algorithm2(frameLeft,frameRight,minArea, substractor):

    imgMotionDetectionLeft = motionDetection(frameLeft, substractor)
    imgMotionDetectionRight = motionDetection(frameRight, substractor)

    # Find object external outline points
    imgContoursLeft, hierarchy = cv2.findContours(imgMotionDetectionLeft, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgContoursRight, hierarchy = cv2.findContours(imgMotionDetectionRight, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contourLeft,contourRight in enumerate(imgContoursLeft,imgContoursRight):
        areaLeft = cv2.contourArea(contourLeft)
        areaRight = cv2.contourArea(contourLeft)
        if areaLeft > minArea:
            # Perimeter determines if close or open object
            peri = cv2.arcLength(cnt, True)
            
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            
            x, y, w, h = cv2.boundingRect(approx)
            x,y = x + (w // 2), y + (h // 2)

    xLeft = keypointsLeft[0].pt[0]
    yLeft = keypointsLeft[0].pt[1]
    
    xRight = keypointsRight[0].pt[0]
    yRight = keypointsRight[0].pt[1]

    #*************** Hard Code Numbers From Intrinsic ***********
    #************ Gobal Variables*******
    #************ Temp*******
    imageWidth = 752 # cxLeft width
    imageHeight = 480 # cyLeft height
    b = 60; # baseline [mm]
    f = 6; # focal length [mm]
    pixelSize = .006; # pixel size [mm]

    xLeft = float(xLeft)
    yLeft = float(yLeft)
    xRight = float(xRight)
    yLeft = float(yRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = (b * f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*pixelSize)
    X = (Z * (xLeft-imageWidth)*pixelSize)/f
    Y = (Z * (yLeft-imageHeight)*pixelSize)/f
    
    return X,Y,Z