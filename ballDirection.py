'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: ballDirection.py
 File Description: 
    This file is meant to help any other functions that need to find the ball
    direction status. 

    General Knowledge:
        Using OpenCV x,y coordinate system, where Top left of the image is 0,0
'''
import logging


"""
This function was created to give the user a overall status of the ball
direction. It returns an Array of booleans of the ball direction
Arrary Order: [ ballLeftBound, ballBouncing, ballPeaking, ballFailing, ballRaising ]
"""
def ballState(positionListY, positionListX):
    currentPointY ,previousPointY ,oldestPointY = getPositions(positionListY)
    currentPointX ,previousPointX ,oldestPointX = getPositions(positionListX)    

    ballLeftBound, ballBouncing, ballPeaking, ballFailing, ballRaising = False
    ballStatus = [ballLeftBound, ballBouncing, ballPeaking, ballFailing, ballRaising]

    # X-axis
    if previousPointX > currentPointX and previousPointX < oldestPointX:
        ballLeftBound = True
    else:
        logging.warning("Ball status is undeterminable, inconclusive X-axis ball movenment")
    # Y-axis
    if previousPointY > currentPointY and previousPointY > oldestPointY:
        ballBouncing = True
    elif previousPointY < currentPointY and previousPointY < oldestPointY:
        ballPeaking = True
    elif previousPointY < currentPointY and previousPointY > oldestPointY:
        ballFalling = True
    elif previousPointY < currentPointY and previousPointY > oldestPointY:
        ballFalling = True
    elif previousPointY > currentPointY and previousPointY < oldestPointY:
        ballRaising = True
    else:
        logging.warning("Ball status is undeterminable, inconclusive Y-axis ball movenment")
    return ballStatus

def getPositions(positionList):
    if len(positionList) < 3:
        return logging.warning("Position list given has less than 3 positions, not enough data")
    currentPoint = positionList[-1]
    previousPoint = positionList[-2]
    oldestPoint = positionList[-3]
    return currentPoint,previousPoint,oldestPoint

def ballBouncing(positionListY):
    ballBouncing = False
    currentPoint,previousPoint,oldestPoint = getPositions(positionListY)
    if previousPoint > currentPoint and previousPoint > oldestPoint:
        ballBouncing = True
    return ballBouncing

def ballPeaking(positionListY):
    ballPeaking = False
    currentPoint,previousPoint,oldestPoint = getPositions(positionListY)
    if previousPoint < currentPoint and previousPoint < oldestPoint:
        ballPeaking = True
    return ballPeaking

def ballFalling(positionListY):
    ballFalling = False
    currentPoint,previousPoint,oldestPoint = getPositions(positionListY)
    if previousPoint < currentPoint and previousPoint > oldestPoint:
        ballFalling = True
    return ballFalling

def ballRaising(positionListY):
    ballRaising = False
    currentPoint,previousPoint,oldestPoint = getPositions(positionListY)
    if previousPoint > currentPoint and previousPoint < oldestPoint:
        ballRaising = True
    return ballRaising

def ballLeftBound(positionListX):
    ballLeftBound = False
    currentPoint ,previousPoint ,oldestPoint = getPositions(positionListX)
    if previousPoint > currentPoint and previousPoint < oldestPoint:
        ballLeftBound = True
    return ballLeftBound

def ballBouncing1(positionList):
    ballBouncing = False
    if len(positionList) < 3:
        return logging.warning("Position list given has less than 3 positions, not enough data")
    currentPoint = positionList[-1]
    previousPoint = positionList[-2]
    oldestPoint = positionList[-3]
    if previousPoint > currentPoint and previousPoint > oldestPoint:
        ballBouncing = True
    return ballBouncing