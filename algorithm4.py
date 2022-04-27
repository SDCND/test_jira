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

def algorithm4(frameLeft,frameRight,ballColor,minArea,customColor=False):
    # Color Finder 
    HSVImageLeft = cv2.cvtColor(frameLeft,cv2.COLOR_BGR2HSV)
    HSVImageRight = cv2.cvtColor(frameLeft,cv2.COLOR_BGR2HSV)

    myColorFinder = colorFinder.colorFinder(False)
    HSVImageRight, colorMaskLeft = myColorFinder.update(HSVImageLeft, ballColor)
    HSVImageRight, colorMaskRight = myColorFinder.update(HSVImageRight, ballColor)

    if True:
        cv2.imshow("Mask Left", colorMaskLeft)
        cv2.imshow("Mask Right", colorMaskRight)
        print(frameLeft)
        print("Space for shit")
        print(frameRight)
        cv2.waitKey(0)

    # Contour Finder
    # Find object external outline points
    imgContoursLeft, hierarchy = cv2.findContours(colorMaskLeft, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgContoursRight, hierarchy = cv2.findContours(colorMaskRight, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print(imgContoursLeft)
    print(imgContoursRight)
    
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

    print("NO Detection?")
    print(cxLeft, cyLeft , cxRight, cyRight)
    xLeft = float(cxLeft)
    yLeft = float(cyLeft)
    xRight = float(cxRight)
    yLeft = float(cyRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((globalVariables.b * globalVariables.f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*globalVariables.pixelSize))/10
    X = ((Z * (xLeft-globalVariables.imageWidth)*globalVariables.pixelSize)/globalVariables.f)/10
    Y = ((Z * (yLeft-globalVariables.imageHeight)*globalVariables.pixelSize)/globalVariables.f)/10

    # Display
    cv2.imshow("colorMaskLeft", colorMaskLeft)
    cv2.imshow("colorMaskRight", colorMaskRight)

    return X,Y,Z