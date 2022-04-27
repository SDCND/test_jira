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
import TestFile.motionDetection as motionDetection
import globalVariables

def algorithm2(grayFrameLeft,grayFrameRight,minArea,kernal,substractor):
    # Motion Detection    
    imgMotionDetectionLeft = motionDetection.motionDetection(grayFrameLeft, substractor)
    imgMotionDetectionRight = motionDetection.motionDetection(grayFrameRight, substractor)

    motionMaskLeft = cv2.morphologyEx(imgMotionDetectionLeft, cv2.MORPH_OPEN, kernal)
    motionMaskRight = cv2.morphologyEx(imgMotionDetectionRight, cv2.MORPH_OPEN, kernal)

    # Contour Finder
    # Find object external outline points
    imgContoursLeft, hierarchy = cv2.findContours(motionMaskLeft, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgContoursRight, hierarchy = cv2.findContours(motionMaskRight, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cxLeft = 0
    cyLeft = 0
    cxRight = 0
    cyRight = 0
    # Left contour iteration
    for contour in imgContoursLeft:
        areaLeft = cv2.contourArea(contour)
        if areaLeft > minArea:
            # Get Perimeter of closed contours
            peri = cv2.arcLength(contour, True)
            # It approximates a contour shape to another shape with less number of 
            # vertices depending upon the precision we specify
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cxLeft, cyLeft = x + (w // 2), y + (h // 2)
            cv2.rectangle(grayFrameLeft, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(grayFrameLeft, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

    # Right contour iteration
    for contour in imgContoursRight:
        areaRight = cv2.contourArea(contour)
        if areaRight > minArea:
            # Get Perimeter of closed contours
            peri = cv2.arcLength(contour, True)
            # It approximates a contour shape to another shape with less number of 
            # vertices depending upon the precision we specify
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cxRight, cyRight = x + (w // 2), y + (h // 2)
            cv2.rectangle(grayFrameRight, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(grayFrameRight, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

    #*************** Hard Code Numbers From Intrinsic ***********
    # Covernting Camera to Real World
    imageWidth = 752 # cxLeft width
    imageHeight = 480 # cyLeft height
    b = 60; # baseline [mm]
    f = 6; # focal length [mm]
    pixelSize = .006; # pixel size [mm]
    
    xLeft = float(cxLeft)
    yLeft = float(cyLeft)
    xRight = float(cxRight)
    yRight = float(cyRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((b * f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*pixelSize))/1000
    X = ((Z * (xLeft-imageWidth)*pixelSize)/f)/1000
    Y = ((Z * (yLeft-imageHeight)*pixelSize)/f)/1000

    # Display
    imgMotionDetectionLeft = cv2.resize(imgMotionDetectionLeft,(0,0), None, 0.25,0.25)
    cv2.imshow("imgMotionDetectionLeft", imgMotionDetectionLeft)
    imgMotionDetectionRight = cv2.resize(imgMotionDetectionRight,(0,0), None, 0.25,0.25)
    cv2.imshow("imgMotionDetectionRight", imgMotionDetectionRight)

    return X, Y, Z