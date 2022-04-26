'''
 Author: Alejandro(Steven)
 File Name: imageResize.py
 File Description: 
    Takes in an image and resizes the image based on the previous image
    ball centroid. This will be all done in pixel domain(x,y)
    
    **** Time is not provided hence the general image resize ****
    
'''
import ballDirection
 
def imageResizing(image, positionListY, positionListX, ballRadius,ballSpeed):
    # Cropps height x width
    # Origin 0,0 is top left of images in OpenCV
    currentPointY ,previousPointY ,oldestPointY = ballDirection.getPositions(positionListY)
    currentPointX ,previousPointX ,oldestPointX = ballDirection.getPositions(positionListX)
    
    # Falling and Going Left
    if ballDirection.ballFalling(currentPointY ,previousPointY ,oldestPointY) and ballDirection.ballLeftBound(currentPointX ,previousPointX ,oldestPointX):
        imageCropped = image[0:400,100:650]

    # Rasing and Going Left

    # Peaking and Going Left
    
    # Bouncing and Going Left    
    
    
    imgCropped = image[0:400,100:650]
    
    return imgCropped