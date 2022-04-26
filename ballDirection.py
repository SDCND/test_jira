# Use OpenCV x,y coordinate system
# Top left is 0,0


def getPositions(positionList):
    if len(positionList) < 3:
        return print("Position List has less than Three positions")
    currentPoint = positionList[-1]
    previousPoint = positionList[-2]
    oldestPoint = positionList[-3]
    return currentPoint,previousPoint,oldestPoint

def ballState(positionListY, positionListX):
    currentPointY ,previousPointY ,oldestPointY = getPositions(positionListY)
    currentPointX ,previousPointX ,oldestPointX = getPositions(positionListX)
    
    ballLeftBound = ballLeftBound(currentPointX ,previousPointX ,oldestPointX)
    
    if ballFalling(currentPointY ,previousPointY ,oldestPointY):
        return ballLeftBound, True
    if ballRaising(currentPointY ,previousPointY ,oldestPointY):
        return ballLeftBound, True
    if ballBouncing(currentPointY ,previousPointY ,oldestPointY):
        return ballLeftBound, True
    else:
        return ballLeftBound

def ballBouncing(currentPoint,previousPoint,oldestPoint):
    ballBounce = False
    if previousPoint > currentPoint and previousPoint > oldestPoint:
        ballBounce = True
    return ballBounce

def ballPeaking(currentPoint,previousPoint,oldestPoint):
    ballPeak = False
    if previousPoint < currentPoint and previousPoint < oldestPoint:
        ballPeak = True
    return ballPeak

def ballFalling(currentPoint,previousPoint,oldestPoint):
    ballFalling = False
    if previousPoint < currentPoint and previousPoint > oldestPoint:
        ballFalling = True
    return ballFalling

def ballRaising(currentPoint,previousPoint,oldestPoint):
    ballRaising = False
    if previousPoint > currentPoint and previousPoint < oldestPoint:
        ballRaising = True
    return ballRaising

def ballLeftBound(currentPoint,previousPoint,oldestPoint):
    ballLeftBound = False
    if previousPoint > currentPoint and previousPoint < oldestPoint:
        ballLeftBound = True
    return ballLeftBound