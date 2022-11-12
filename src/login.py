from PyQt5 import QtCore, QtWidgets, uic

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        uic.loadUi('.\\gui\\login_form.ui', self)
        self.login_btn.clicked.connect(self.login)
        self.close_btn.clicked.connect(self.close)
        self.minimize_btn.clicked.connect(self.showMinimized)


    def login(self):
        self.switch_window.emit()