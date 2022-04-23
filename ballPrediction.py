'''
 Author: Alejandro(Steven)
 Date: April.13-2022
 File Name: ballPrediction.py
 File Description: 
    For this file the ball trejectory will be predicted using the last three x,y,z location
    of the ball centeroid coming from the ball tracking file(function)
'''
import cv2
import numpy as np
import math
from findContours import findContours
from colorFinder import ColorFinder

path = 'videos/bounces/orangeBallBouncePingPongTable1.mov'
path1 = 'videos/bounds/orangeBallMiddleBound2.mov'
path2 = 'videos/bounds/orangeBallRightBound2.mov'
cap = cv2.VideoCapture(path2)

# Create the Color finder object
myColorFinder = ColorFinder.ColorFinder(False)

HSVOragneValue = {'hmin': 0, 'smin': 109, 'vmin': 208, 'hmax': 19, 'smax': 255, 'vmax': 255}
hsvVals = {'hmin': 0, 'smin': 109, 'vmin': 208, 'hmax': 19, 'smax': 255, 'vmax': 255}

imageFrameWidthDimensions = 2436 #4k
posListX, posListY = [], []
xList = [item for item in range(0, imageFrameWidthDimensions)]

while True:
    # Grabbing img
    success, img = cap.read()
    # img = cv2.imread("testImages/orangeBall.jpg")

    # Create the mask for the color of object
    imgColor, mask  = myColorFinder.update(img,hsvVals)

    # Mask to help get rid of noise
    # mask = cv2.erode(mask1,(5,5),iterations=3)
    # mask = cv2.dilate(mask,(5,5),iterations=3)

    # Find object external outline points
    imgContours, contours = findContours.findContours(img, mask, minArea=200)

    # Add the x and y centers of the ball in the two array list
    
    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
    
    if posListX:
        # Ball Prediction
        # Polynomial Regression y = Ax^2 + Bx + C
        # Find the Coefficients
        A, B, C = np.polyfit(posListX, posListY, 2)
 
        for imageFrame, (posX, posY) in enumerate(zip(posListX, posListY)):
    
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            if imageFrame == 0:
                cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
            else:
                cv2.line(imgContours, pos, (posListX[imageFrame - 1], posListY[imageFrame - 1]), (0, 255, 0), 5)
        
        # Create the dot of the cetner of the ball
        for x in xList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
 
        # Prediction
        if len(posListX) < 10:
            # X values 330 to 430  Y 590
            a = A                                                                       
            b = B
            c = C - 590
            # Still need to do the ball radius landing
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 330 < x < 430
 
    # Display
    img = cv2.resize(mask, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Image", img) # Makes the img appear on new window

    imgColor = cv2.resize(imgContours, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("ImageColor", imgColor) # Makes the img appear on new window

    cv2.waitKey(50) #Change the FPS for user sight only