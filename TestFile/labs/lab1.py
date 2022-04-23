'''
 Author: Steven Varada Salazar
 Date: Wednesday Jan.26-2022
 File Name: lab1.py
 File Description: For this lab
                you will ask the user to provide the tennis ball centroid locations for both the left and right 
	            camera and you will compute and display the Z position of the ball
	The first step in finding a tennis ball in 3D space is to determine its Z position relative to your stereo camera
Equations Used:
  Disparity:   d = (abs((float(xLeft)-cxLeft)-(float(xRight)-cxRight))*ps) # disparity [mm]
  Depth Z axis:   Z = (b * f)/d # depth [mm]z
'''
from math import log10, floor

def main():
  xLeft =  input("Enter x left: ")
  xRight = input("Enter x right: ")
  b = 60; # baseline [mm]
  f = 6; # focal length [mm]
  ps = .006; # pixel size [mm]
  xNumPix = 752; # total number of pixels in x direction of the sensor [px]
  cxLeft = xNumPix/2; # left camera x center [px]
  cxRight = xNumPix/2; # right camera x center [px]
  d = (abs((float(xLeft)-cxLeft)-(float(xRight)-cxRight))*ps) # disparity [mm]
  Z = (b * f)/d # depth [mm]z
  print("Here is the result " + str(floor(Z)) + " mm")

if __name__ == '__main__':
    main()