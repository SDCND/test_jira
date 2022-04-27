'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: algorithm1.py
 File Description: 
    Uses motion detection to find object moving in the image then uses
    blobdection to find the ball in the image. Output real world X, Y, Z
'''
import cv2
import numpy as np
import math
import colorFinder
import globalVariables

def algorithm3(RGBFrameLeft,RGBFrameRight,ballColor,minArea,customColor=False):
    # Color Finder 
    myColorFinder = colorFinder.colorFinder(False)
    
    HSVImageLeft, colorMaskLeft = myColorFinder.update(RGBFrameLeft, ballColor)
    HSVImageRight, colorMaskRight = myColorFinder.update(RGBFrameRight, ballColor)

    # Blob detector
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    # params.minThreshold = 10
    # params.maxThreshold = 200

    #Filter by Area.
    params.filterByArea = True
    params.minArea = 10
    params.maxArea = 14500

    #Filter by Color
    params.filterByColor = False

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = .4

    # Filter by Convexity
    # params.filterByConvexity = True
    # params.minConvexity = 0.1

    # Filter by Inertia
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01

    imgBlurredLeft = cv2.GaussianBlur(colorMaskLeft,(7,7),0)
    imgBlurredRight = cv2.GaussianBlur(colorMaskRight,(7,7),0)
    
    # Set up the blob detector.
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs from the images
    keypointsLeft = detector.detect(colorMaskLeft)
    keypointsRight = detector.detect(colorMaskRight)
    
    print(keypointsLeft)
    print(keypointsRight)

    #Finding the center of the Blob
    xLeft = keypointsLeft[0].pt[0]
    yLeft = keypointsLeft[0].pt[1]
    
    xRight = keypointsRight[0].pt[0]
    yRight = keypointsRight[0].pt[1]

    # Displaying
    blobsLeft = cv2.drawKeypoints(RGBFrameLeft, keypointsLeft, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    blobsRight = cv2.drawKeypoints(RGBFrameRight, keypointsRight, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    xLeft = float(xLeft)
    yLeft = float(yLeft)
    xRight = float(xRight)
    yRight = float(yRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((globalVariables.b * globalVariables.f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*globalVariables.pixelSize))/10
    X = ((Z * (xLeft-globalVariables.imageWidth)*globalVariables.pixelSize)/globalVariables.f)/10
    Y = ((Z * (yLeft-globalVariables.imageHeight)*globalVariables.pixelSize)/globalVariables.f)/10
    
    return X,Y,Z