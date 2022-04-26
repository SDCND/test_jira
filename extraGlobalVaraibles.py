

#*************** Hard Code Numbers From Intrinsic ***********
# Covernting Camera to Real World
imageWidth = 752 # cxLeft width
imageHeight = 480 # cyLeft height
b = 60; # baseline [mm]
f = 6; # focal length [mm]
pixelSize = .006; # pixel size [mm]

PingPongBallDiameter = 4 # cm (1.57in)
TenniseBallDiameter = 6.86 # cm (2.7in)
racquetballDiameter = 5.715 # cm (2.25in)
# soccerBallDiameter = 24.26 # cm (9.23in)
# basketballDiameter = 22 # cm (8.66in)
ballRadius = (PingPongBallDiameter)/2


xList = [item for item in range(0, imageFrameWidthDimensions)]
posListX, posListY, positions = [], [], []

if contours:
    if ballDirection.ballBouncing1(posListY) == True:
        posListX = posListX[len(posListX)-2:]
        posListY = posListY[len(posListY)-2:]
    if counter != 0:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])
    counter += 1
    pass

# Create the dot of the Center of the ball
for x in xList:
    y = int(A * x ** 2 + B * x + C)
    cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
    
# Draws the line and dot of the centroid of the ball
for imageFrame, (posX, posY) in enumerate(zip(posListX, posListY)):
    pos = (posX, posY)
    cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
    if imageFrame == 0:
        cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
    else:
        cv2.line(imgContours, pos, (posListX[imageFrame - 1], posListY[imageFrame - 1]), (0, 255, 0), 5)
