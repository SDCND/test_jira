import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
path1 = 'testvideos/bounds/orangeBallMiddleBound2.mov'
path2 = 'testvideos/bounds/orangeBallRightBound2.mov'
cap = cv2.VideoCapture(path)

# _, firstFrame = cap.read()
# firstFrameGray = cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)
# firstFrameGray = cv2.GaussianBlur(firstFrameGray,(5,5),0)

substractor = cv2.createBackgroundSubtractorMOG2()

while True:
    success, video = cap.read()
    kernal = np.ones((5,5),np.uint8)
    
    videoGray = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    
    imgMotionDetection = substractor.apply(videoGray)
    
    imgMorphology = cv2.morphologyEx(imgMotionDetection, cv2.MORPH_OPEN, kernal)
    
    # Using several Filters instead
    # _, mask = cv2.threshold(videoGray,100,255,cv2.THRESH_BINARY)
    # mask =  cv2.GaussianBlur(mask,(5,5),0)
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    # ImgMotionDetectionManual = cv2.absdiff(firstFrameGray,imgGray)

    videoGray = cv2.resize(videoGray, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Video Gray",videoGray)
    
    imgMotionDetection = cv2.resize(imgMotionDetection, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Motion Detection", imgMotionDetection)
    
    imgMorphology = cv2.resize(imgMorphology, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Morphology", imgMorphology)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break