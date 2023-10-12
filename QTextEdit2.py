import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("QTextEdit2.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TextEdit_Practice2")
        self.Add.clicked.connect(self.addText)
        
        # 폰트 설정
        self.Clear.clicked.connect(self.clearText)
        self.FontUbuntu.clicked.connect(lambda: self.setFont("Ubuntu"))        
        self.FontNanumGothic.clicked.connect(lambda: self.setFont("NanumGothic"))

        self.Red.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.Green.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.Blue.clicked.connect(lambda: self.setTextColor(0, 0, 255))
        self.SetFontSize.clicked.connect(self.setTextSize)
        self.FontSize.returnPressed.connect(self.setTextSize)

        self.Input.clear()
        self.Output.clear()

        ### 폰트 크기 숫자만 입력되게 하는 방법
        ## 방법 1. 폰트 크기 입력창에 QIntValidator 적용
        self.FontSize.setValidator(QIntValidator())

        ## 방법 2. int 아닌 형 들어오면 실시간으로 지우기 
        # self.FontSize.textChanged.connect(self.checkDigit)

    def checkDigit(self):
        text = self.FontSize.text()
        if (text.isdigit() == False):
            self.FontSize.setText(text[:-1])

    def setTextSize(self):
        size = int(self.FontSize.text())
        self.Output.selectAll()
        self.Output.setFontPointSize(size)
        self.Output.moveCursor(QTextCursor.End)

    def setTextColor(self, r, g, b):
        color = QColor(r,g,b)
        self.Output.selectAll()
        self.Output.setTextColor(color)
        self.Output.moveCursor(QTextCursor.End)

    def addText(self):
        text = self.Input.toPlainText()
        self.Input.clear()
        self.Output.append(text)

    def clearText(self):
        self.Input.clear()
        self.Output.clear()


    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.Output.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
