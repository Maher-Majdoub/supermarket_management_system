"""
this is the main program
the project is not finished yet
"""

#imports
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi('.\\gui\\login_form.ui', self)
        self.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.close_btn.clicked.connect(window.close)
    window.minimize_btn.clicked.connect(window.showMinimized)
    app.exec_()