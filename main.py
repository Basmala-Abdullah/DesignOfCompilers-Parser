from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Sample2 import Ui_MainWindow
'''''
class MyWindow(QMainWindow):
    def _init_(self):
        super(MyWindow,self)._init_()
        self.initUI()

    def button_clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)

    def update(self):
        self.label.adjustSize()
'''''
class myMainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super(myMainwindow,self).__init__(parent)
        self.setupUi(self)
def window():
    app = QApplication(sys.argv)
    win = myMainwindow()
    win.show()
    sys.exit(app.exec_())

window()