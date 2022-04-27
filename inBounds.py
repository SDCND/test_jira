"""
    Author: Alejandro(Steven)
    Date: April.20-2022
    File Name: inOUtBounds.py
    File Description: 
        Using only real world coordinates for the ball and court determine if the ball
        is in or out of bounds
"""

# Ball real world coordinate are reltaive to the camera
# While the cour real world courts are relative to the april tag
# Needs Testing

def inBounds(X,Z,XCourtCenter,ZCourtCenter,boundCorners):
    # bound corners: BottomRight, BottomLeft, TopLeft, TopRight
    # ((x1,y1), (x2,y2), ,(x3,y3) , (x4,y4))

    Z = Z - ZCourtCenter
    X = X - XCourtCenter
    
    bottomLeftCorner = boundCorners[1]
    TopRightCorner = boundCorners[3]
    
    if bottomLeftCorner[0] < X or TopRightCorner[0] > X:
        return True
    elif bottomLeftCorner[1] < Z or TopRightCorner[1] > Z:
        return True
    else:
        return False
    
    
    #find how far the ball is from the court center
    bottomLeftCorner = courtCorners[0]
    bottomRightCorner = courtCorners[1]
    topRightCorner = courtCorners[2]
    topLeftCorner = courtCorners[3]
    
    Z = Z - ZCourtCenter
    X = X - XCourtCenter
    
    if X < 0 and Z < 0: 
        if X < bottomLeftCorner[0]:
            return False
        elif Z < bottomLeftCorner[1]:
            return False
    elif X > 0 and Z < 0:
        if X > bottomRightCorner[0]:
            return False
        elif Z < bottomRightCorner[1]:
            return False
    elif X > 0 and Z > 0:
        if X > topRightCorner[0]:
            return False
        elif Z > topRightCorner[1]:
            return False
    elif X < 0 and Z > 0:
        if X < topLeftCorner[0]:
            return False
        elif Z > topLeftCorner[1]:
            return False
    else:
        return True