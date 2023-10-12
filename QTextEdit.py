import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("QTextEdit.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextEdit_Practice")
        self.Add.clicked.connect(self.addText)
        self.Input.returnPressed.connect(self.addText)
        self.Clear.clicked.connect(self.clearText)
        
    def addText(self):
        text = self.Input.text()
        self.Output.append(text)
        self.Input.clear()

    def clearText(self):
        self.Input.clear()
        self.Output.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
