import cv2
import numpy as np

def empty(a):
    pass

path = 'testImages/right5.jpg'
path3 = 'testImages/LabImages/left1.jpg'
path4 = 'testImages/LabImages/right1.jpg'

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
cv2.createTrackbar("Hue Min","TrackBars",27,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",57,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",33,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",118,255,empty)
cv2.createTrackbar("Val Min","TrackBars",80,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path3)
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

    cv2.imshow("Original", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask Image", mask)
    cv2.imshow("Resulting Image",imgResult)

    cv2.waitKey(1)