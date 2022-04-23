import sys
from PyQt4 import QtGui

class Widget(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.answer1 = QtGui.QLabel()
        q1Edit = QtGui.QLineEdit()
        q1Edit.textChanged.connect(self.q1Changed)

        self.answer2 = QtGui.QLabel()
        q2Edit = QtGui.QLineEdit()
        q2Edit.textChanged.connect(self.q2Changed)

        grid = QtGui.QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(QtGui.QLabel('Question 1'), 1, 0)
        grid.addWidget(q1Edit, 1, 1)

        grid.addWidget(QtGui.QLabel('Question 2'), 2, 0)
        grid.addWidget(q2Edit, 2, 1)

        applyBtn = QtGui.QPushButton('Apply', self)
        applyBtn.clicked.connect(self.close)

        grid.addWidget(applyBtn,3,2)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)

    def q1Changed(self, text):
        self.answer1.setText(text)

    def q2Changed(self, text):
        self.answer2.setText(text)

    def returnAnswer1(self):
        return self.answer1.text()

    def returnAnswer2(self):
        return self.answer2.text()

    @staticmethod
    def getData(parent=None):
        dialog = Widget(parent)
        dialog.exec_()
        return [dialog.returnAnswer1(), dialog.returnAnswer2()]

def main():
    app = QtGui.QApplication([])
    window = Widget()
    data = window.getData()
    print(data[0])
    print(data[1])

if __name__ == '__main__':
    main()