'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: findCustomColorHSCvalue.py
 File Description: 
    This is a file run to help find the perfect color match for the object being tracked
    it runs several windows showing you the original image, mask, and original image
    with the mask
'''
import cv2
import numpy as np


# Creates a window
cv2.namedWindow("TrackBars")
# Resizes the window created
cv2.resizeWindow("TrackBars",640,240)
# Creates taskbars in the windown

# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# mask Numbers applied
cv2.createTrackbar("Hue Min","TrackBars",13,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",109,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",208,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# {'hmin': 13, 'smin': 109, 'vmin': 208, 'hmax': 19, 'smax': 255, 'vmax': 255}

path = 'testImages/right5.jpg'
path1 = 'testImages/orange2.jpg' #'testImages/orangeBall.jpg'
path2 = 'testImages/whiteBall.jpg'
path3 = 'testImages/LabImages/left1.jpg'
path4 = 'testImages/LabImages/right1.jpg'
pathLeft5 = 'testImages/LabImages/left5.jpg'

while True:
    img = cv2.imread(pathLeft5)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    # Takes in imageSource, lowwer values array, upper values arrays
    mask = cv2.inRange(imgHSV,lower,upper)
    # Mask values: 27 57 33 118 80 255
    
    # Takes imgsource and mask display pixel value if pixel exists on both display
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    img = cv2.resize(img, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Original", img)
    imgHSV = cv2.resize(imgHSV, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("HSV Image", imgHSV)
    mask = cv2.resize(mask, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Mask Image", mask)
    imgResult = cv2.resize(imgResult, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Resulting Image",imgResult)

    cv2.waitKey(1)