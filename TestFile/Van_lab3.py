#Vanessa Araiza
#Lab 3
from ctypes import alignment
import sys, math
from PyQt4 import QtCore, QtGui
import numpy as np
import cv2

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        # layout stuff
        calc = QtGui.QPushButton("X,Y,Z Distance")
        calc.clicked.connect(self.pushed)

        self.RFilePath = QtGui.QLineEdit()
        r1 = QtGui.QHBoxLayout()
        r1.addWidget(QtGui.QLabel("Enter Right Image Path:"))
        r1.addWidget(self.RFilePath)

        RBtn = QtGui.QPushButton("Sumbit Right Path")
        RBtn.clicked.connect(self.pushedR)

        self.LFilePath = QtGui.QLineEdit()
        r2 = QtGui.QHBoxLayout()
        r2.addWidget(QtGui.QLabel("Enter Left Image Path:"))
        r2.addWidget(self.LFilePath)

        LBtn = QtGui.QPushButton("Sumbit Left Path")
        LBtn.clicked.connect(self.pushedL)

        self.result = QtGui.QLabel(alignment=QtCore.Qt.AlignCenter)

        layout = QtGui.QFormLayout(self)
        layout.addRow(r1)
        layout.addRow(RBtn)
        layout.addRow(r2)
        layout.addRow(LBtn)
        layout.addRow(calc)
        layout.addRow(self.result)

        self.show()

    def pushedL(self):

        LimageFilePath = str(self.LFilePath.text())
        #imageFilePath = float(imageFilePath)
        Limage = cv2.imread(LimageFilePath,0)
        output = cv2.imread(LimageFilePath,1)
        blurred = cv2.GaussianBlur(Limage,(11,11),0)
        # Finds circles in a grayscale image using the Hough transform
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,param1=100,param2=50,minRadius=0,maxRadius=200)


    # cv2.HoughCircles function has a lot of parameters, so you can find more about it in documentation

    # or you can use cv2.HoughCircles? in jupyter nootebook to get that

# Check to see if there is any detection

        if circles is not None:

    # If there are some detections, convert radius and x,y(center) coordinates to integer

            circles = np.round(circles[0, :]).astype("int")
        for (self.xL, self.yL, self.rL) in circles:

        # Draw the circle in the output image

                cv2.circle(output, (self.xL, self.yL), self.rL, (0,255,0), 2)

        # Draw a rectangle(center) in the output image

                cv2.rectangle(output, (self.xL - 2, self.yL - 2), (self.xL + 2, self.yL + 2), (0,255,0), -1)

                print(self.xL)

                print(self.yL)

                print(self.rL)

 

        cv2.imshow("Circle Found Left Image",output)

        cv2.imwrite("LeftCircleDetection.jpg",output)

        cv2.waitKey()

    def pushedR(self):

        RimageFilePath = str(self.RFilePath.text())
        #imageFilePath = float(imageFilePath)
        image = cv2.imread(RimageFilePath,0)
        output = cv2.imread(RimageFilePath,1)
        blurred = cv2.GaussianBlur(image,(11,11),0)
        # Finds circles in a grayscale image using the Hough transform
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,param1=100,param2=50,minRadius=0,maxRadius=200)


    # cv2.HoughCircles function has a lot of parameters, so you can find more about it in documentation

    # or you can use cv2.HoughCircles? in jupyter nootebook to get that

# Check to see if there is any detection

        if circles is not None:

    # If there are some detections, convert radius and x,y(center) coordinates to integer

            circles = np.round(circles[0, :]).astype("int")
        for (self.xR, self.yR, self.rR) in circles:

        # Draw the circle in the output image

                cv2.circle(output, (self.xR, self.yR), self.rR, (0,255,0), 2)

        # Draw a rectangle(center) in the output image

                cv2.rectangle(output, (self.xR - 2, self.yR - 2), (self.xR + 2, self.yR + 2), (0,255,0), -1)

                print(self.xR)

                print(self.yR)

                print(self.rR)

 

        cv2.imshow("Circle Found Right Image",output)

        cv2.imwrite("RightCircleDetection.jpg",output)

        cv2.waitKey()

    def pushed(self):
        #self._list_widget.clear()
        #valRightX = float(self.RightX.text())
        #valRightY = float(self.RightY.text())
        #valLeftX = float(self.LeftX.text())
        #valLeftY = float(self.LeftY.text())
        self.b = 60
        self.f = 6
        self.ps = .006
        self.xNumPix = 752
        self.xLeft = 752/2
        self.yLeft = 480/2
        self.xRight = self.xNumPix/2
        #self.LX = float(self.LeftX.text())
        #self.LY = float(self.LeftY.text())
        #self.RX = float(self.RightX.text())
        #self.RY = float(self.RightY.text())
        self.z = (self.b*self.f)/(abs((self.xL-self.xLeft)-(self.xR-self.xRight))*self.ps)
        self.x = (self.z*(self.xL-self.xLeft)*self.ps)/self.f
        self.y = (self.z*(self.yL-self.yLeft)*self.ps)/self.f
        self.result.setText(str(self.x) + " mm, " + str(self.y) + " mm, " + str(self.z) + " mm, ")

def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()  







