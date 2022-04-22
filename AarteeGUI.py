import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
# from progress.bar import Bar
# from Tkinter import*
import os

  
class MyWidget(QtGui.QWidget):
  def __init__(self, parent = None):
    super(MyWidget, self).__init__(parent)
    test = True
    msg = self()
    # layout stuff
    
    cameraButton = QtGui.QPushButton('Set up Camera')
    vLayout = QtGui.QVBoxLayout()

    vLayout.addWidget(cameraButton)
    
    
    setCourt = QtGui.QPushButton('Set up Court')
    #vLayout = QtGui.QVBoxLayout()
    vLayout.addWidget(setCourt)

   
    detInOut = QtGui.QPushButton('Determine in or out')
    #vLayout = QtGui.QVBoxLayout()
    vLayout.addWidget(detInOut)

    
    outputData = QtGui.QPushButton('Output Data')
   # vLayout = QtGui.QVBoxLayout()
    vLayout.addWidget(outputData)
  
    
    imagePath = QtGui.QPushButton('Open Image Folder')
    #vLayout = QtGui.QVBoxLayout()
    vLayout.addWidget(imagePath)
    
    
    self.setLayout(vLayout)
    
    
    
    #slots
    cameraButton.clicked.connect(lambda: self.cameraOutput())
    setCourt.clicked.connect(lambda: self.courtOutput())
    detInOut.clicked.connect(lambda: self.ballInOutOutput())
    outputData.clicked.connect(lambda: self.open_new_dialog())
    self.dialog = secondWinow(self)
    imagePath.clicked.connect(lambda: self.imagePathOutput())
    
    
    
    
    self.col = QtGui.QColor(0, 0, 0)  
    self.square = QtGui.QFrame(self)
    self.square.setGeometry(150, 20, 100, 100)
    vLayout.addWidget(self.square)
    self.square.setStyleSheet("QWidget { background-color: %s }" %  
      self.col.name())
      
    val = 255
    #Ball in bound/out of bound 
    
    #
    #Ball Prediction Code
    #If 0 or 1
    #
    #--------------------------------------------------------
    #Add here
    test = 0
    if test == 0:
        self.col.setRed(val) 
    else:
        self.col.setBlue(val) 
        
    self.square.setStyleSheet("QFrame { background-color: %s }" %
        self.col.name())
    #------------------------------------------------------------
      


    self.square = QtGui.QFrame(self)
    #self.show_gif()
    self.show() 
  
  def setColor(self):
        
    source = self.sender()
    

    val = 255
    
    test = 0
    if test == 0:
        self.col.setRed(val)                             
    else:
        self.col.setBlue(val) 
        
    self.square.setStyleSheet("QFrame { background-color: %s }" %
        self.col.name()) 
        
            
  def open_new_dialog(self):
    self.dialog.show()
 
  def cameraOutput(self):
    print("Camera Button has been clicked!")
 
  def ballInOutOutput(self):
    self.about(self, "Ball In or Out Bound", "Ball is in play")
  
  def courtOutput(self):
    print("Set up Court Button has been clicked!")
    
  def imagePathOutput(self):
    newpath = r'C:\AprilTagImages' 
    if not os.path.exists(newpath):
      os.makedirs(newpath)
    
  
  

class secondWinow(QtGui.QWidget):
   def __init__(self, parent=None):
    super(secondWinow, self).__init__()
    vLayout = QtGui.QVBoxLayout()
    

    self.show();
    
   def calculateOuput(self):
   
    leftposx_to_str = float(self.leftposx.text())     
    rightposx_to_str  = float(self.rightposx.text())     
    leftposy_to_str  = float(self.leftposy.text())     
    rightposy_to_str  = float(self.rightposy.text()) 
    
    b = 60
    f = 6
    ps = .006
    yNumPix = 480
    cyLeft = yNumPix/2
    cyRight = yNumPix/2
    xNumPix = 752
    cxLeft = xNumPix/2
    cxRight = xNumPix/2
    
    d = (abs(((leftposx_to_str - cxLeft) - (rightposx_to_str - cxRight)))*ps)
    z = str((b * f)/d)
    x = str((z * (leftposx_to_str - cxLeft)*ps)/f)
    y = str((z*(leftposy_to_str - cyLeft) * ps)/f)
    
    zinMeters = str(z/1000)
    
    print ("z: " + zinMeters)
    print ("x: " + x)
    print ("y: " + y)
    

   
def main():
  app = QtGui.QApplication(sys.argv)
  main = MyWidget()
  main.show()
  sys.exit(app.exec_())
  
  # def open_new_dialog(self):
  #   self.nd = NewDialog(self)
  #   self.nd.show()

if __name__ == '__main__':
  main()  