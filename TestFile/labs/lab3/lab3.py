'''
 Author: 
 Date: Monday Feb.14-2022
 File Name: lab3.py
 File Description: 
    For this lab a image is inputed into the GUI then outputs the X, Y, and Z of the object
    GUI:
    - Display left/right image, processed image with circle
    - Buttons to show final result and input the images
    - Showing where the object is and output the X, Y, and Z
Technolgies Used: Python
Library: PyQt, Numpy
Equations Used:
 Z axis: Z = (b * f)/(abs((x1-cxLeft)-(x2-cxRight))*pixelSize)
 X axis: X = (Z * (x1-cxLeft)*pixelSize)/f
 Y axis: Y = (Z * (y1-cyLeft)*pixelSize)/f
'''

import sys
import math
from PyQt4 import QtGui,QtCore
import numpy as np
import cv2

class myWidget(QtGui.QWidget):
  def __init__(self, parent=None):
    self.xl = 0
    self.yl = 0
    self.xr = 0
    self.yr = 0
    super(myWidget, self).__init__(parent)
    self.setWindowTitle("Lab 3") 
    self.gui_init()

  def gui_init(self):
    self.leftImage  = QtGui.QLineEdit()
    self.rightImage = QtGui.QLineEdit()

    self.xyz = QtGui.QLabel(alignment=QtCore.Qt.AlignCenter)

    row1 = QtGui.QHBoxLayout()
    row1.addWidget(QtGui.QLabel("  Left Image Path:"))
    row1.addWidget(self.leftImage)

    row2 = QtGui.QHBoxLayout()
    row2.addWidget(QtGui.QLabel("Right Image Path:"))
    row2.addWidget(self.rightImage)

    button = QtGui.QPushButton("Display X,Y,Z Distance")
    button.clicked.connect(self.onClick)

    layout = QtGui.QFormLayout(self)
    layout.addRow(row1)
    layout.addRow(row2)
    layout.addRow(button)
    layout.addRow(self.xyz)

  @QtCore.pyqtSlot()
  def onClick(self):
    # print('clicked')
    if self.leftImage.text():
      imageFilePath = str(self.leftImage.text())
      image = cv2.imread(imageFilePath,0)
      output = cv2.imread(imageFilePath,1)

      blurred = cv2.GaussianBlur(image,(11,11),0)

      # Finds circles in image using the Hough transform
      circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100, param1=100,param2=50,minRadius=0,maxRadius=200)

      # Check to see if there is any detection
      # If there are some detections, convert radius and x,y(center) coordinates to integer
      if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Draw the circle and mark center in the output image
        for (x, y, r) in circles:
          cv2.circle(output, (x, y), r, (0,255,0), 2)
          cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)
          
          self.xl = x
          self.yl = y
    
    if self.rightImage.text():
      imageFilePath = str(self.rightImage.text())
      image = cv2.imread(imageFilePath,0)
      output = cv2.imread(imageFilePath,1)

      blurred = cv2.GaussianBlur(image,(11,11),0)

      # Finds circles in image using the Hough transform
      circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100, param1=100,param2=50,minRadius=0,maxRadius=200)

      # Check to see if there is any detection
      # If there are some detections, convert radius and x,y(center) coordinates to integer
      if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Draw the circle and mark center in the output image
        for (x, y, r) in circles:
          cv2.circle(output, (x, y), r, (0,255,0), 2)
          cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)
          
          self.xr = x
          self.yr = y

      self.b = 60
      self.f = 6
      self.pixelSize = .006
      self.xLeft = 752/2
      self.yLeft = 480/2
      self.xNumPix = 752
      self.xRight = self.xNumPix/2
      self.z = math.trunc((self.b*self.f)/(abs((self.xl-self.xLeft)-(self.xr-self.xRight))*self.pixelSize))
      self.x = math.trunc((self.z * (self.xl-self.xLeft)*self.pixelSize)/self.f)
      self.y = math.trunc((self.z * (self.yl-self.yLeft)*self.pixelSize)/self.f)
 
      self.xyz.setText(str(self.x) + " mm, " + str(self.y) + " mm, " + str(self.z) + " mm")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = myWidget()
    w.show()
    sys.exit(app.exec_())