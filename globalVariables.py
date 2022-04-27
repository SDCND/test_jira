
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


# xList = [item for item in range(0, imageFrameWidthDimensions)]
posListX, posListY = [], []

minArea = 10

# Extra Useful Code

########### Prediction Reset ##########
# if contours:
#     if ballDirection.ballBouncing1(posListY) == True:
#         posListX = posListX[len(posListX)-2:]
#         posListY = posListY[len(posListY)-2:]
#     if counter != 0:
#         posListX.append(contours[0]['center'][0])
#         posListY.append(contours[0]['center'][1])
#     counter += 1
#     pass


######## Create the dot of the Center of the ball ##########
# for x in xList:
#     y = int(A * x ** 2 + B * x + C)
#     cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)
    
    
############### Draws the line and dot of the centroid of the ball #######
# for imageFrame, (posX, posY) in enumerate(zip(posListX, posListY)):
#     pos = (posX, posY)
#     cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
#     if imageFrame == 0:
#         cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
#     else:
#         cv2.line(imgContours, pos, (posListX[imageFrame - 1], posListY[imageFrame - 1]), (0, 255, 0), 5)
    
############### FrameLeft & FrameRight for loop together #########
    # for contourLeft,contourRight in zip(imgContoursLeft,imgContoursRight):
    #     areaLeft = cv2.contourArea(contourLeft)
    #     areaRight = cv2.contourArea(contourRight)
    #     if areaLeft and  areaRight > minArea:
    #         # Get Perimeter of closed contours
    #         peri = cv2.arcLength(contourLeft, True)
    #         peri = cv2.arcLength(contourRight, True)
    #         # It approximates a contour shape to another shape with less number of 
    #         # vertices depending upon the precision we specify
    #         approx = cv2.approxPolyDP(contourLeft, 0.02 * peri, True)
    #         approx = cv2.approxPolyDP(contourRight, 0.02 * peri, True)
            
    #         xLeft, yLeft, wLeft, hLeft = cv2.boundingRect(approx)
    #         cxLeft, cyLeft = xLeft + (wLeft // 2), yLeft + (hLeft // 2)
            
    #         xRight, yRight, wRight, hRight = cv2.boundingRect(approx)
    #         cxRight, cyRight = xRight + (wRight // 2), yRight + (hRight // 2)
            
    #         # Debugging Accuarcy Testing
    #         cv2.rectangle(frameLeft, (xLeft, yLeft), (xLeft + wLeft, yLeft + hLeft), (255,0,0), 2)
    #         cv2.circle(frameLeft, (xLeft + (wLeft // 2), yLeft + (hLeft // 2)), 5, (255,0,0), cv2.FILLED)
    #         cv2.rectangle(frameRight, (xRight, yRight), (xRight + wRight, yRight + hRight), (255,0,0), 2)
    #         cv2.circle(frameRight, (xRight + (wRight // 2), yRight + (hRight // 2)), 5, (255,0,0), cv2.FILLED)
