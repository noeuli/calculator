# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('Message', self)
        self.btn1.clicked.connect(self.activateMessage) # link handler

        vbox = QVBoxLayout()    # create vertical layout
        vbox.addStretch(1)  # empty space
        vbox.addWidget(self.btn1)   # add button
        vbox.addStretch(1)  # empty space

        self.setLayout(vbox)    # (empty space - button - empty space) layout

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()
    
    def activateMessage(self):  # button click handler
        QMessageBox.information(self, "information", "Button clicked!")

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
