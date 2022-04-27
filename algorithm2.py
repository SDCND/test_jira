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

def algorithm2(frameLeft,frameRight,minArea,substractor):
    # cornerAmount goes in function args
    # :param cornerAmount: Filters based on the corner points e.g. 4 = Rectangle or square
    
    # Motion Detection
    imgMotionDetectionLeft = motionDetection.motionDetection(frameLeft, substractor)
    imgMotionDetectionRight = motionDetection.motionDetection(frameRight, substractor)

    # Contour Finder
    # Find object external outline points
    imgContoursLeft, hierarchy = cv2.findContours(imgMotionDetectionLeft, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgContoursRight, hierarchy = cv2.findContours(imgMotionDetectionRight, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

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
            cv2.rectangle(frameLeft, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(frameLeft, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

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
            cv2.rectangle(frameRight, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(frameRight, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

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
    yLeft = float(cyRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((b * f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*pixelSize))/1000
    X = ((Z * (xLeft-imageWidth)*pixelSize)/f)/1000
    Y = ((Z * (yLeft-imageHeight)*pixelSize)/f)/1000

    # Display
    cv2.imshow("imgMotionDetectionLeft", imgMotionDetectionLeft)
    cv2.imshow("imgMotionDetectionRight", imgMotionDetectionRight)

    return X, Y, Z