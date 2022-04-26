'''
 Author: Alejandro(Steven)
 File Name: ballPrediction.py
 File Description: 
    This file predict the movement of the ball. It takes in the position
    list for x and y and returns a prediction of x,y
'''
import numpy as np
import math

'''
Needs to get the region you are interested in to tell you the
prediction results
'''
def ballPrediction(positionListX,positionListY, bounds):
    degreeOfAccuracy = 10
    if positionListX:
        # Ball Prediction
        # Polynomial Regression y = Ax^2 + Bx + C
        # Find the Coefficients
        A, B, C = np.polyfit(positionListX, positionListY, 2)
 
    # Prediction - Look for the bound coordinates
    if len(positionListX) < degreeOfAccuracy:
        # X and Y can come from the court creation bounds
        # X values 330 to 430 
        # Y 590
        a = A                                                                       
        b = B
        c = C - 590
        # Still need to do the ball radius landing
        x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
        prediction = 330 < x < 430