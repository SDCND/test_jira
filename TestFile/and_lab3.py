# Andrew Quist
# pyqt 2 number sum function

import sys
import os
import cv2
import numpy as np
import PyQt4.QtGui as QtWidgets
from PyQt4 import QtCore
from PyQt4 import QtGui

class TestListView(QtGui.QListWidget):
    def __init__(self, type, parent=None):
        super(TestListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.ignore()

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.view = TestListView(self)
        self.connect(self.view, QtCore.SIGNAL("dropped"), self.pictureDropped)
        self.setCentralWidget(self.view)
        #filePath = str(QtGui.QFileDialog.getOpenFileName(None, "Enter Filename.",".jpg","(*.jpg)"))
        #img = cv2.imread(filePath)
        #cv2.imshow('img', img)
        #small_img = cv2.resize(img,(640,480))

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                print(url)
                #img = cv2.imread(url)
                #cv2.imshow('img', img)
                #small_img = cv2.resize(img,(640,480))
                icon = QtGui.QIcon(url)
                pixmap = icon.pixmap(72, 72)                
                icon = QtGui.QIcon(pixmap)
                item = QtGui.QListWidgetItem(url, self.view)
                item.setIcon(icon)
                item.setStatusTip(url)
                self.calc(url)
                
                
    def calc(self, path):
        #imageFilePath = float(imageFilePath)
        #image = cv2.imread(imageFilePath,0)
        imageFilePath = str(path)
        image = cv2.imread(imageFilePath,0)
        output = cv2.imread(imageFilePath,1)
        blurred = cv2.GaussianBlur(image,(11,11),0)
        # Finds circles in a grayscale image using the Hough transform
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,param1=100,param2=50,minRadius=0,maxRadius=200)

        if circles is not None:

    # If there are some detections, convert radius and x,y(center) coordinates to integer

            circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:

        # Draw the circle in the output image

                cv2.circle(output, (x, y), r, (0,255,0), 2)

        # Draw a rectangle(center) in the output image

                cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)

                print(x)

                print(y)

                print(r)
                
        cv2.imshow("circles found",output)

        cv2.imwrite("CirclesDetection.jpg",output)

        cv2.waitKey()

def main():
  app = QtGui.QApplication(sys.argv)
  form = MainForm()
  form.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()  