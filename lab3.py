'''
 Author: Vanessa Ariza
 Date: Monday Feb.14-2022
 File Name: lab3.py
 File Description: 
    For this lab a image is inputed into the GUI then outputs the X, Y, and Z of the object
    GUI:
    - Display left/right image, processed image with circle
    - Buttons to show final result and input the images
    - Showing where the object is and output the X, Y, and Z
Technolgies Used: Python
Library: PyQt, Numpy
Equations Used:
 Z axis: Z = (b * f)/(abs((x1-cxLeft)-(x2-cxRight))*pixelSize)
 X axis: X = (Z * (x1-cxLeft)*pixelSize)/f
 Y axis: Y = (Z * (y1-cyLeft)*pixelSize)/f
'''
import sys
import numpy as np
import cv2

imageFilePath = raw_input('Enter Image Path: ')
image = cv2.imread(imageFilePath,0)
output = cv2.imread(imageFilePath,1)


blurred = cv2.GaussianBlur(image,(11,11),0)

# Finds circles in a grayscale image using the Hough transform
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,param1=100,param2=50,minRadius=0,maxRadius=200)


# cv2.HoughCircles function has a lot of parameters, so you can find more about it in documentation

# or you can use cv2.HoughCircles? in jupyter nootebook to get that

# Check to see if there is any detection

if circles is not None:

    # If there are some detections, convert radius and x,y(center) coordinates to integer

    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:

        # Draw the circle in the output image

        cv2.circle(output, (x, y), r, (0,255,0), 2)

        # Draw a rectangle(center) in the output image

        cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)

        print(x)

        print(y)

        print(r)

cv2.imshow("circles found",output)

cv2.imwrite("CirclesDetection.jpg",output)

cv2.waitKey()