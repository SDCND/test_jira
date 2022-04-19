import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

cap = cv2.VideoCapture('videos/bounds/orangeBallRightBound2.mov')

# Create the Color finder object
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 0, 'smin': 109, 'vmin': 208, 'hmax': 19, 'smax': 255, 'vmax': 255}

posListX, posListY = [], []
xList = [item for item in range(0, 2436)]

while True:
    # Grabbing img
    success, img = cap.read() # Taking in the video from the video folder
    # img = cv2.imread("testImages/orangeBall.jpg")

    # Find the color Ball
    imgColor, mask  = myColorFinder.update(img,hsvVals)

    # Find Location of Ball
    imgContours, contours = cvzone.findContours(img, mask, minArea=200)

    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
    if posListX:
        # Polynomial Regression y = Ax^2 + Bx + C
        # Find the Coefficients
        A, B, C = np.polyfit(posListX, posListY, 2)
 
        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            if i == 0:
                cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
            else:
                cv2.line(imgContours, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 5)
 
        for x in xList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
 
        if len(posListX) < 10:
            # Prediction
            # X values 330 to 430  Y 590
            a = A
            b = B
            c = C - 590
 
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 330 < x < 430
    # Display
    img = cv2.resize(mask, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Image", img) # Makes the img appear on new window

    imgColor = cv2.resize(imgContours, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("ImageColor", imgColor) # Makes the img appear on new window
    
    imgContours = cv2.resize(imgContours, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("ImageColor", imgContours) # Makes the img appear on new window
    
    cv2.waitKey(50) #Change the FPS for user sight only