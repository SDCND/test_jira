'''
 Author: Steven Varada Salazar
 Date: Wednesday Feb.2-2022
 File Name: lab2.py
 File Description: For this lab
                Creates a PyQt GUI enter tennies centroid [x,y] locations for both the left and right camera. That
                computes and displays the X, Y, and Z positon of the ball
            Method use pixels, that will then be used to copmute the distance of the ball
            in meters
Technolgies Used:
    Python, PyQt'
Equations Used:
 Z axis: Z = (b * f)/(abs((x1-cxLeft)-(x2-cxRight))*pixelSize)
 X axis: X = (Z * (x1-cxLeft)*pixelSize)/f
 Y axis: Y = (Z * (y1-cyLeft)*pixelSize)/f
'''
# Getting system operating system
import sys
# Obtains the PyQt4 from lib, taking in QtCore & QtGui
from PyQt4 import QtCore, QtGui

x = 5

class MyWidget(QtGui.QWidget):
  
  def __init__(windowGUI):
    # Use super to inherit MyWidget init
    super(MyWidget, windowGUI).__init__() 
    
    windowGUI.globalVar = 5
    
    # Window Sizing and titling
    windowGUI.setWindowTitle("Lab 2 - PyQt GUI")
    windowGUI.resize(500, 500)
    
    # Setting up grid
    grid = QtGui.QGridLayout()
    
    # GUI components - button dot fucntions, .move(x-axis,y-axis), .resize()
    # Left Camera prompts
    leftCameraLabel = QtGui.QLabel('Left Camera Values', windowGUI)
    windowGUI.xLeftCamVal = QtGui.QLabel('Left Camera x value', windowGUI)
    windowGUI.yLeftCamVal = QtGui.QLabel('Left Camera x value', windowGUI)

    # Right Camera prompts
    rightCameraLabel = QtGui.QLabel('Right Camera Values', windowGUI)
    windowGUI.xRightCamVal = QtGui.QLabel('Right Camera x value', windowGUI)
    windowGUI.yRightCamVal = QtGui.QLabel('Right Camera y value', windowGUI)
  
    # Result prompts
    resultButton = QtGui.QPushButton('Get Results', windowGUI)
    windowGUI.xresult = QtGui.QLabel('X-axis results: ', windowGUI)
    windowGUI.yresult = QtGui.QLabel('Y-axis results: ', windowGUI)
    windowGUI.zresult = QtGui.QLabel('Z-axis results: ', windowGUI)

    # Adding components to grid
    # Left Camera prompts
    grid.addWidget(leftCameraLabel, 1, 0)
    grid.addWidget(windowGUI.xLeftCamVal, 2, 0)
    grid.addWidget(windowGUI.yLeftCamVal, 2, 1)
    # Right Camera prompts
    grid.addWidget(rightCameraLabel, 4, 0)
    grid.addWidget(windowGUI.xRightCamVal, 5, 0)
    grid.addWidget(windowGUI.yRightCamVal, 5, 1)
    # Results Camera prompts
    grid.addWidget(resultButton, 6, 0)
    grid.addWidget(windowGUI.xresult, 7, 0)
    grid.addWidget(windowGUI.yresult, 7, 1)
    grid.addWidget(windowGUI.zresult, 7, 2)
    
    windowGUI.setLayout(grid)
        
    # Function connecting to button
    resultButton.clicked.connect(windowGUI.GetResults)
    
    # Shows the GUI to user
    windowGUI.show()
  
  # Button Functions
  def GetResults(windowGUI, text):
    xLeft,leftX = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "Enter tennise ball left x-axis value: ")
    yLeft,leftY = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "Enter tennise ball left y-axis value: ")
    xRight,rightX = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "Enter tennise ball right x-axis value: ")
    yRight,rightY = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "Enter tennise ball right y-axis value: ")
  
    if leftX:
      windowGUI.xLeftCamVal.setText(str(xLeft))
    if leftY:
      windowGUI.yLeftCamVal.setText(str(yLeft))
    if rightX:
      windowGUI.xRightCamVal.setText(str(xRight))
    if rightY:
      windowGUI.yRightCamVal.setText(str(yRight))

    # Hard Code Numbers
    cxLeft = 752 # width
    cyLeft = 480 # height
    b = 60; # baseline [mm]
    f = 6; # focal length [mm]
    pixelSize = .006; # pixel size [mm]
    xLeft = float(xLeft)
    yLeft = float(xLeft)
    xRight = float(xRight)
    yLeft = float(xLeft)
    centerxLeft = float(xLeft/2)
    centerxRight = float(xRight/2)
    Z = (b * f)/(abs((xLeft-centerxLeft)-(xRight-centerxRight))*pixelSize)
    X = (Z * (xLeft-cxLeft)*pixelSize)/f
    Y = (Z * (yLeft-cyLeft)*pixelSize)/f

    windowGUI.xresult.setText(str(Z))
    windowGUI.yresult.setText(str(X))
    windowGUI.zresult.setText(str(Y))    
  '''
  # Pop up windown to prevent accidental closing of the application
  def closeEvent(windowGUI, event):
    reply = QtGui.QMessageBox.question(windowGUI, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)

    if reply == QtGui.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
  '''
  
def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())
  print(x)

# Setups the environment to call main  
if __name__ == '__main__':
  main()