import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import readerMain

readTime = 250

class Main(QWidget):
    def __init__(self, list):
        super().__init__()

        self.list = list
        self.counter = 0
        self.len_list = len(self.list)

        self.setWindowTitle(" ")
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: black;')
        self.wordLabel.setAlignment(Qt.AlignCenter)
        self.wordLabel.setGeometry(20, 20, 1000, 500)
        self.setMinimumSize(1000, 500)

        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(round(60000/readTime))

    def onTimeout(self):
        if self.counter >= self.len_list:
            loop = QEventLoop()
            QTimer.singleShot(3000, loop.quit)
            loop.exec_()
            self.close()

        self.wordLabel.setText(str(self.list[self.counter]))
        self.counter += 1

filename = input("Image: ")
list = readerMain(filename)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    app.setFont(QFontDatabase().font("Monospace", "Regular", 14))
    w = Main(list)
    w.show()
    sys.exit(app.exec())