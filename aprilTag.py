import cv2
import numpy as np
import apriltag

def aprilTag():
    path = 'testvideos/bounces/orangeBallBouncePingPongTable1.mov'
    path1 = 'testvideos/bounds/orangeBallMiddleBound2.mov'
    path2 = 'testvideos/bounds/orangeBallRightBound2.mov'
    path3 = 'testvideos/L2R.mp4'
    path4 = 'testvideos/R2L.mp4'
    court = True
    cap = cv2.VideoCapture(path4)
    detector = apriltag.Detector()
    frameLeft, frameRight = cap
    tempImageLeft = np.ascontiguousarray(frameLeft[:,:,0:3], dtype=np.uint8)   # must make it contiguous for opencv processing to work
    tempImageRight = np.ascontiguousarray(frameRight[:,:,0:3], dtype=np.uint8)   # must make it contiguous for opencv processing to work

    grayImageLeft = frameLeft[:,:,3]
    grayImageRight = frameRight[:,:,3]

    # Define camera matrix for left camera.  This data is from Matlab but sometimes the upper right values
    # and middle right value are shown as the lower left and lower middle value in matlab.  Make sure to 
    # load in the matrix in this format.
    mtxLeft =  np.array([[1036.7336, 0,         312.6290],
                            [0,         1045.3576, 150.7533],
                            [0,         0,        1]])
    
    # Define distortion coefficients.  These are the radial distortion coeffs from matlab.
    dist = np.array([-0.4082, 0.5271, 0,0])

    # can do undistortion if you like as shown below
    tempImageLeft = cv2.undistort(tempImageLeft, mtxLeft, dist)
    grayImageLeft = cv2.undistort(grayImageLeft, mtxLeft, dist)
    
    # Start the detector for the aprilTag
    resultLeft = detector.detect(grayImageLeft)
    
    # Define camera matrix for right camera.  This data is from Matlab but sometimes the upper right values
    # and middle right value are shown as the lower left and lower middle value in matlab.  Make sure to 
    # load in the matrix in this format.
    mtxRight =  np.array([[1034.9096, 0,        302.7288],
                            [0,         1042.4151, 190.1091],
                            [0,         0,        1]])
    
    # Define distortion coefficients.  These are the radial distortion coeffs from matlab.
    dist = np.array([-0.3651, 0.2789, 0,0])

    # can do undistortion if you like as shown below
    tempImageRight = cv2.undistort(tempImageRight, mtxRight, dist)
    grayImageRight = cv2.undistort(grayImageRight, mtxRight, dist)
    
    # Start the detector for the aprilTag
    resultRight = detector.detect(grayImageRight)

    # define the various parameters that are for your camera.  the cxLeft, cyLeft, cxRight, cyRight
    # are just from the camera matrices above
    f = 6.23787; # focal length [mm]
    b = 62.3787 # baseline [mm]
    pixelSize = .006;  # [mm]
    cxLeft = 312.6290 # left camera principal pt
    cyLeft = 150.7533 # left camera principal pt
    cxRight = 302.7288 # right camera principal pt
    cyRight = 190.1091 # right camera principal pt
    tagSize = .1 # this is for a 10 cm x 10 cm tag
            
    # display blue bounding box around left image tag
    if not resultLeft:
        # no detections
        pass
    else:
        x1  = int(resultLeft[0].corners[0][0])
        y1  = int(resultLeft[0].corners[0][1])
        x2  = int(resultLeft[0].corners[1][0])
        y2  = int(resultLeft[0].corners[1][1])
        x3  = int(resultLeft[0].corners[2][0])
        y3  = int(resultLeft[0].corners[2][1])
        x4  = int(resultLeft[0].corners[3][0])
        y4  = int(resultLeft[0].corners[3][1])
        cXl = int(resultLeft[0].center[0])
        cYl = int(resultLeft[0].center[1])

        cv2.line(tempImageLeft,(x1,y1),(x2,y2),(255,255,0),1)
        cv2.line(tempImageLeft,(x2,y2),(x3,y3),(255,255,0),1)
        cv2.line(tempImageLeft,(x3,y3),(x4,y4),(255,255,0),1)
        cv2.line(tempImageLeft,(x4,y4),(x1,y1),(255,255,0),1)
        cv2.circle(tempImageLeft, (cXl, cYl), 2, (0, 0, 255), -1)

    # display blue bounding box around right image tag
    if not resultRight:
        # no detections
        pass
    else:
        x1  = int(resultRight[0].corners[0][0])
        y1  = int(resultRight[0].corners[0][1])
        x2  = int(resultRight[0].corners[1][0])
        y2  = int(resultRight[0].corners[1][1])
        x3  = int(resultRight[0].corners[2][0])
        y3  = int(resultRight[0].corners[2][1])
        x4  = int(resultRight[0].corners[3][0])
        y4  = int(resultRight[0].corners[3][1])
        cXr = int(resultRight[0].center[0])
        cYr = int(resultRight[0].center[1])

        cv2.line(tempImageRight,(x1,y1),(x2,y2),(255,255,0),1)
        cv2.line(tempImageRight,(x2,y2),(x3,y3),(255,255,0),1)
        cv2.line(tempImageRight,(x3,y3),(x4,y4),(255,255,0),1)
        cv2.line(tempImageRight,(x4,y4),(x1,y1),(255,255,0),1)
        cv2.circle(tempImageRight, (cXr, cYr), 2, (0, 0, 255), -1)

    ###########################################################################################
    # if both tags are found then do the below code.

    if resultLeft and resultRight:
        # determine the pose of the left & rightcamera relative to the april tag.
        leftpose = detector.detection_pose(resultLeft[0],(1036.7336, 1045.3576, 312.6290, 150.7533 ), tagSize, 1)
        rightPose = detector.detection_pose(resultRight[0],(1034.9096, 1042.4151, 302.7288, 190.1091 ), tagSize, 1)

        # print("left camera pose")
        # print(leftpose)
        # print("right camera pose")
        # print(rightPose)

        # determine x1,y1 and x2,y2 which are the center of the apriltag
        x1 = float(resultLeft[0].corners[0][0])
        y1 = float(resultLeft[0].corners[0][1])

        x2 = float(resultRight[0].corners[0][0])
        y2 = float(resultRight[0].corners[0][1])    

        # determine the X,Y,Z camera coordinate of the center of the tag.
        # the depth is determined with both cameras but the X and Y are determined with just the left camera. 
        Z = (b * f)/(abs((x1-cxLeft)-(x2-cxRight))*pixelSize);
        
        X = (Z * (x1-cxLeft)*pixelSize)/f;
        
        Y = (Z * (y1-cyLeft)*pixelSize)/f;
        
        # convert to m
        X = X/1000.0
        Y = Y/1000.0
        Z = Z/1000.0
        
        # since this vector will be multiplied by a 4x4 pose matrix a 1 must be appended to it
        camPt = np.array([X,Y,Z,1]).T
        
        # determine the position in the april tag coordinate system by performing a matrix multiplication 
        position = np.dot(np.linalg.inv(leftpose[0]),camPt)
        
        # convert to centimeters
        # positionCentimeters = position[0:3] * 100

        # pull out the rotation vector and translation vector from the pose matrix
        rotMat = leftpose[0][0:3,0:3]       # slice out the 3x3 rotation matrix from the 4x4 matrix
        rvec,_ = cv2.Rodrigues(rotMat)  # convert 3x3 rotation matrix to rotation vector
        tvec = leftpose[0][0:3,3]           # slice out the 3x1 translation vector

        rotMatRight = rightPose[0][0:3,0:3]       # slice out the 3x3 rotation matrix from the 4x4 matrix
        rvecRight,_ = cv2.Rodrigues(rotMatRight)  # convert 3x3 rotation matrix to rotation vector
        tvecRight = rightPose[0][0:3,3]           # slice out the 3x1 translation vector
        
        # plot court bounds based on user specification
        if (court == True):
            #Plot doubles rectangle for court
            points =  np.array([[-.4300 , -.1900 , 0],      #x1 , y1
                            [ .4200 , -.2032 , 0],          #x2 , y2
                            [ .4200 ,  .1900 , 0],          #x3 , y3
                            [-.4318 ,  .2032 , 0]])         #x4 , y4
        else:
            #Plot doubles rectangle for court
                points =  np.array([[-.4300, -.1400 , 0],      #x1 , y1
                            [.4200 , -.1524 , 0] ,          #x2 , y2
                            [.4200 , .1400  , 0],           #x3 , y3
                            [-.4300, .1524  , 0]])          #x4 , y4
        
        # convert april tag coordinate points to camera pixel points. 
        result = cv2.projectPoints(points, rvec, tvec, mtxLeft, None)
        rightResult = cv2.projectPoints(points, rvecRight, tvecRight, mtxRight, None)

        
        # just map the results to x's and y's. 
        Leftx1 = int(result[0][0][0][0])
        Lefty1 = int(result[0][0][0][1])
        Leftx2 = int(result[0][1][0][0])
        Lefty2 = int(result[0][1][0][1])
        Leftx3 = int(result[0][2][0][0])
        Lefty3 = int(result[0][2][0][1])
        Leftx4 = int(result[0][3][0][0])
        Lefty4 = int(result[0][3][0][1])

        Rightx1 = int(rightResult[0][0][0][0])
        Righty1 = int(rightResult[0][0][0][1])
        Rightx2 = int(rightResult[0][1][0][0])
        Righty2 = int(rightResult[0][1][0][1])
        Rightx3 = int(rightResult[0][2][0][0])
        Righty3 = int(rightResult[0][2][0][1])
        Rightx4 = int(rightResult[0][3][0][0])
        Righty4 = int(rightResult[0][3][0][1])
        
        # plot the line segments in camera pixel coordinates left camera
        cv2.line(tempImageLeft,(Leftx1,Lefty1),(Leftx2,Lefty2),(0,0,255),2) #red
        cv2.line(tempImageLeft,(Leftx2,Lefty2),(Leftx3,Lefty3),(255,255,0),2) #blue
        cv2.line(tempImageLeft,(Leftx3,Lefty3),(Leftx4,Lefty4),(0,255,0),2) #green
        cv2.line(tempImageLeft,(Leftx4,Lefty4),(Leftx1,Lefty1),(0,255,255),2) #yellow


        # plot the line segments in camera pixel coordinates right camera
        cv2.line(tempImageRight,(Rightx1,Righty1),(Rightx2,Righty2),(0,0,255),2) #red
        cv2.line(tempImageRight,(Rightx2,Righty2),(Rightx3,Righty3),(255,255,0),2) #blue
        cv2.line(tempImageRight,(Rightx3,Righty3),(Rightx4,Righty4),(0,255,0),2) #green
        cv2.line(tempImageRight,(Rightx4,Righty4),(Rightx1,Righty1),(0,255,255),2) #yellow

    #print "X: " + str(X) + " Y: " + str(Y) + " Z: " + str(Z)
    # tempImageLeft = cv2.undistort(tempImageLeft, mtxLeft, dist)
    # grayImageLeft = cv2.undistort(grayImageLeft, mtxLeft, dist)


    #tempImageLeft = cv2.drawKeypoints(tempImageLeft, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
