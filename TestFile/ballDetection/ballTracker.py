'''
Author: Anthony P Chiusano III
File Name: ballTracker.py
File Description:
    Uses SimpleBlobDetector to detect circular blobs within an image to determine
    the center point (x,y) of a pingpong ball
'''

# imports
import cv2
import numpy as np
# from frameGrabber import ImageFeedthrough

# global camera
# camera = ImageFeedthrough()

# time.sleep(1)
# # frameLeft,frameRight = camera.getStereoRGB()
# cv2.imwrite("left.jpg", frameLeft)
# cv2.imwrite("right.jpg", frameRight)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200

#Filter by Area.

params.filterByArea = True
params.minArea = 2000
params.maxArea = 14500

#Filter by Color
params.filterByColor = False

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = .7

# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.1

# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

# Read image
img = cv2.imread('testImages/right5.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.VideoCapture('videos/bounds/orangeBallMiddleBound3.mov')

imgBlurred = cv2.GaussianBlur(img,(7,7),0)

# Set up the blob detector.
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs from the image.
keypoints = detector.detect(imgBlurred)

#Finding the center of the Blob
x = keypoints[0].pt[0]
y = keypoints[0].pt[1]

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS - This method draws detected blobs as red circles and ensures that the size of the circle corresponds to the size of the blob.
blobs = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#Test Images
cv2.imshow('Blurred',imgBlurred)

# Show keypoints
print(x)
print(y)
cv2.imshow('Blobs',blobs)
cv2.imshow('ImgBlurred', imgBlurred)
cv2.waitKey(0)