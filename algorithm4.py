'''
 Author: Alejandro(Steven)
 Date: April.26-2022
 File Name: ballAlgorithm2.py
 File Description: 
    Using colorfinder to get a image color mask with the use of findcontours the center of the
    ball will be used to ge the ball location in the image. 
    Output the real world X,Y,& Z of the ball and if in or out of bound
'''

import cv2
import numpy as np
import math
import colorFinder
import globalVariables

def algorithm4(RGBFrameLeft,RGBFrameRight,ballColor,minArea,customColor=False):
    # Color Finder 
    myColorFinder = colorFinder.colorFinder(False)
    
    HSVImageLeft, colorMaskLeft = myColorFinder.update(RGBFrameLeft, ballColor)
    HSVImageRight, colorMaskRight = myColorFinder.update(RGBFrameRight, ballColor)

    imgBlurredLeft = cv2.GaussianBlur(colorMaskLeft,(7,7),0)
    imgBlurredRight = cv2.GaussianBlur(colorMaskRight,(7,7),0)

    # Contour Finder
    # Find object external outline points
    imgContoursLeft, hierarchy = cv2.findContours(imgBlurredLeft, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgContoursRight, hierarchy = cv2.findContours(imgBlurredRight, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
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
            cv2.rectangle(RGBFrameLeft, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(RGBFrameLeft, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

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
            cv2.rectangle(RGBFrameRight, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.circle(RGBFrameRight, (x + (w // 2), y + (h // 2)), 5, (255,0,0), cv2.FILLED)

    xLeft = float(cxLeft)
    yLeft = float(cyLeft)
    xRight = float(cxRight)
    yRight = float(cyRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((globalVariables.b * globalVariables.f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*globalVariables.pixelSize))/1000
    X = ((Z * (xLeft-globalVariables.imageWidth)*globalVariables.pixelSize)/globalVariables.f)/1000
    Y = ((Z * (yLeft-globalVariables.imageHeight)*globalVariables.pixelSize)/globalVariables.f)/1000

    return X,Y,Z