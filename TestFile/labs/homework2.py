'''
 Author: Steven Varada Salazar
 Date: Wednesday Feb.2-2022
 File Name: homework2.py
 File Description: For this lab take in two user input numbers and display
      of the two user input numbers
Technolgies Used:
    Python, PyQt'
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
    windowGUI.setWindowTitle("Homework 2 - Number sum")
    windowGUI.resize(500, 500)
    
    # Setting up grid
    grid = QtGui.QGridLayout()
    
    num1Label = QtGui.QLabel('First Number:', windowGUI)
    windowGUI.num1 = QtGui.QLabel('First Number', windowGUI)

    num2Label = QtGui.QLabel('Second Number:', windowGUI)
    windowGUI.num2 = QtGui.QLabel('Second Number', windowGUI)
    
    # Result prompts
    sumLabel = QtGui.QLabel('Sum Results: ', windowGUI)
    windowGUI.sumResults = QtGui.QLabel('Sum', windowGUI)
    resultButton = QtGui.QPushButton('Get Results', windowGUI)
    
    # Adding components to grid
    # Left Camera prompts
    grid.addWidget(num1Label, 1, 0)
    grid.addWidget(windowGUI.num1, 1, 1)
    
    grid.addWidget(num2Label, 3, 0)
    grid.addWidget(windowGUI.num2, 3, 1)

    grid.addWidget(sumLabel, 5, 0)
    grid.addWidget(windowGUI.sumResults, 5, 1)
    grid.addWidget(resultButton, 6, 0)
    
    windowGUI.setLayout(grid)
        
    # Function connecting to button
    resultButton.clicked.connect(windowGUI.GetResults)
    
    # Shows the GUI to user
    windowGUI.show()
  
  # Button Functions
  def GetResults(windowGUI, text):
    num1Input, _ = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "What is your first number?")
    num2Input, _ = QtGui.QInputDialog.getText(windowGUI,"Input Dialog Box", "What is your second number?")
    
    if num1Input:
      windowGUI.num1.setText(str(num1Input))
    if num2Input:
      windowGUI.num2.setText(str(num2Input))

    num1Input = float(num1Input)
    num2Input = float(num2Input)
    
    sumOutput = num1Input + num2Input
    windowGUI.sumResults.setText(str(sumOutput))
    
def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())
  print(x)

# Setups the environment to call main  
if __name__ == '__main__':
  main()