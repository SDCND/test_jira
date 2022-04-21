'''
 Author: Alejandro(Steven)
 Date: April.20-2022
 File Name: ballAlgorithm2.py
 File Description: 
    Using motion detection an image with only the objects that moved will be show in the new image.
    With the use of findcontours the center of the ball will be used to ge the ball location in the image
'''

import cv2

# cap = cv2.VideoCapture(0)
path = 'videos/bounces/orangeBallBouncePingPongTable1.mov'
path1 = 'videos/bounds/orangeBallMiddleBound2.mov'
path2 = 'videos/bounds/orangeBallRightBound2.mov'
cap = cv2.VideoCapture(path)

# _, firstFrame = cap.read()
# firstFrameGray = cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)
# firstFrameGray = cv2.GaussianBlur(firstFrameGray,(5,5),0)
def MotionDetectionContours():

    substractor = cv2.createBackgroundSubtractorMOG2()

    while True:
        success, video = cap.read()
        
        videoGray = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
        
        imgMotionDetection = substractor.apply(videoGray)
        
        # _, mask = cv2.threshold(videoGray,100,255,cv2.THRESH_BINARY)
        # mask =  cv2.GaussianBlur(mask,(5,5),0)
        # mask = cv2.erode(mask, None, iterations=2)
        # mask = cv2.dilate(mask, None, iterations=2)
        # ImgMotionDetectionManual = cv2.absdiff(firstFrameGray,imgGray)

        videoGray = cv2.resize(videoGray, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
        cv2.imshow("Video Gray",videoGray)
        
        imgMotionDetection = cv2.resize(imgMotionDetection, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
        cv2.imshow("Motion Detection", imgMotionDetection)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    
    # Covernting Camera to Real World
    # Hard Code Numbers
        # cxLeft = 752 # width
        # cyLeft = 480 # height
        # b = 60; # baseline [mm]
        # f = 6; # focal length [mm]
        # pixelSize = .006; # pixel size [mm]
        # xLeft = float(xLeft)
        # yLeft = float(xLeft)
        # xRight = float(xRight)
        # yLeft = float(xLeft)
        # centerxLeft = float(xLeft/2)
        # centerxRight = float(xRight/2)
        # Z = (b * f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*pixelSize)
        # X = (Z * (xLeft-cxLeft)*pixelSize)/f
        # Y = (Z * (yLeft-cyLeft)*pixelSize)/f