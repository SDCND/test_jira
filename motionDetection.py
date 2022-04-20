import cv2
from cv2 import threshold

# cap = cv2.VideoCapture(0)
path = 'videos/bounces/orangeBallBouncePingPongTable1.mov'
path1 = 'videos/bounds/orangeBallMiddleBound2.mov'
path2 = 'videos/bounds/orangeBallRightBound2.mov'
cap = cv2.VideoCapture(path)

# _, firstFrame = cap.read()
# firstFrameGray = cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)
# firstFrameGray = cv2.GaussianBlur(firstFrameGray,(5,5),0)

substractor = cv2.createBackgroundSubtractorMOG2()

while True:
    success, video = cap.read()
    
    videoGray = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    
    vidMotionDetection = substractor.apply(videoGray)
    
    _, thresholdMask = cv2.threshold(videoGray,100,255,cv2.THRESH_BINARY)
    # imgDiff = cv2.absdiff(firstFrameGray,imgGray)
    
    # imgDiff =  cv2.GaussianBlur(imgDiff,(5,5),0)
    
    # _, imgDiff = cv2.threshold(imgDiff, 25,255, cv2.THRESH_BINARY)

    videoGray = cv2.resize(videoGray, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    vidMotionDetection = cv2.resize(vidMotionDetection, (0,0), None, 0.25,0.25) # Resized the img to fourth its size

    video = cv2.resize(video, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Video",video)
    videoGray = cv2.resize(videoGray, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Video Gray",videoGray)
    thresholdMask = cv2.resize(thresholdMask, (0,0), None, 0.25,0.25) # Resized the img to fourth its size
    cv2.imshow("Threshhold Mask",thresholdMask)
    cv2.imshow("Motion Detection", vidMotionDetection)
    # cv2.imshow("Video Diff",imgDiff)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break