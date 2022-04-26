"""
    Author: Alejandro(Steven)
    Date: April.20-2022
    File Name: inOUtBounds.py
    File Description: 
        Using only real world coordinates for the ball and court determine if the ball
        is in or out of bounds
"""

def inBounds(X,Z,boundCorners):
    # bound corners: BottomRight, BottomLeft, TopLeft, TopRight
    # ((x1,y1), (x2,y2), ,(x3,y3) , (x4,y4))
    
    bottomLeftCorner = boundCorners[1]
    TopRightCorner = boundCorners[3]
    
    if bottomLeftCorner[0] < X or TopRightCorner[0] > X:
        return True
    elif bottomLeftCorner[1] < Z or TopRightCorner[1] > Z:
        return True
    else:
        return False