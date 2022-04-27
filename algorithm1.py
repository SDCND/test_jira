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
import motionDetection
import globalVariables

# Completed
# ******* Testing Requuired ************

def algorithm1(frameLeft,frameRight,minArea,substractor):
    # Motion Detection
    imgMotionDetectionLeft = motionDetection.motionDetection(frameLeft, substractor)
    imgMotionDetectionRight = motionDetection.motionDetection(frameRight, substractor)
    
    # Blob detector
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200

    #Filter by Area.
    params.filterByArea = True
    params.minArea = 2000
    params.maxArea = 14500

    #Filter by Color
    params.filterByColor = False

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = .7

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.1

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Set up the blob detector.
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs from the images
    keypointsLeft = detector.detect(imgMotionDetectionLeft)
    keypointsRight = detector.detect(imgMotionDetectionRight)

    #Finding the center of the Blob
    xLeft = keypointsLeft[0].pt[0]
    yLeft = keypointsLeft[0].pt[1]
    
    xRight = keypointsRight[0].pt[0]
    yRight = keypointsRight[0].pt[1]

    # Displaying
    blobs = cv2.drawKeypoints(frameLeft, keypointsLeft, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    blobs = cv2.drawKeypoints(frameRight, keypointsRight, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    xLeft = float(xLeft)
    yLeft = float(yLeft)
    xRight = float(xRight)
    yLeft = float(yRight)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = ((globalVariables.b * globalVariables.f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*globalVariables.pixelSize))/1000
    X = ((Z * (xLeft-globalVariables.imageWidth)*globalVariables.pixelSize)/globalVariables.f)/1000
    Y = ((Z * (yLeft-globalVariables.imageHeight)*globalVariables.pixelSize)/globalVariables.f)/1000
    
    # Display
    cv2.imshow("imgMotionDetectionLeft", imgMotionDetectionLeft)
    cv2.imshow("imgMotionDetectionRight", imgMotionDetectionRight)
    
    return X,Y,Z