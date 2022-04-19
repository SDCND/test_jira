'''
 Author: Alejandro(Steven)
 Date: April.13-2022
 File Name: ballPrediction.py
 File Description: 
    For this file the ball trejectory will be predicted using the last three x,y,z location
    of the ball centeroid coming from the ball tracking file(function)
    
    
 Technolgies Used: Python
 Library:Numpy
'''

import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

#Variables
# Position x,y,z dictionaries 
postionListX, postionListY, postionListZ = []
xList = [item for item in range(0,752)]
# Image Size W x H 752px x 480px
maxX, maxY, maxZ= None

# Polynomial Regression
# Equation: y = Ax^2 + Bx + C
if postionListX:
    # Step 0 Find the degree for polynomial regression line?
    
    # Step 1 Find Coefficients
    A,B,C = np.polyfit(postionListX, postionListY, 2) # Takes in two list, 2 degree only since one bump

for x in xList:
    y = int(A*x**2 + B*x + C)

# Prediction
a = A
b= B
c = C - y

x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
