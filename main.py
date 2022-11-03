"""
this is the main program
the project is not finished yet
"""

#imports
from PyQt5 import QtCore, QtGui, QtWidgets, uic 
import sys


class Ui(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show()

class LOGIN(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi('.\\gui\\login_form.ui', self)
        self.login_btn.clicked.connect(self.login)

    def login(self):
        self.switch_window.emit()



class Controller:
    def __init__(self):
        pass

        
    def show_login(self):

        self.login = LOGIN()
        self.login.switch_window.connect(self.show_admin_panel)
        self.login.show()


    def show_admin_panel(self):
        self.admin_panel = Ui()
        self.login.close()
        self.admin_panel.show()
        


    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())