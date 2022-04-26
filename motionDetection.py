'''
 Author: Alejandro(Steven)
 Date: April.13-2022
 File Name: motionDetection.py
 File Description: 
    Uses the filter backgroundSubtractorMOG2 to have a background image
    to compare to the current image to get a image with only the objects
    that have moved in the image
    
    This substractor must be defined before the while loop reading the
    video frames
    Create a background substarctor
    substractor = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
'''

import cv2
import numpy as np

def motionDetection(blackWhiteImage, substractor):
    # Creates a materix to help clean the image pixels
    kernal = np.ones((5,5),np.uint8)

    # Subsstract background
    imgMotionDetection = substractor.apply(blackWhiteImage)
    
    imgMorphology = cv2.morphologyEx(imgMotionDetection, cv2.MORPH_OPEN, kernal)

    return imgMorphology