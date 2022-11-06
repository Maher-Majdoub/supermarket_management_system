"""
this is the main program
the project is not finished yet
"""
#pyrcc5 icons.qrc -o icons.py


#imports
import sys
from gui.icons import icons
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
import sys
import mysql.connector


class Admin(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show()

class Login(QtWidgets.QWidget):
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
  
    def check_entries(x,y): return True

    def show_login(self):

        self.login = Login()
        self.login.switch_window.connect(self.show_user_panel)
        self.login.show()

    def show_user_panel(self):
        #getting informations from the user 
        user_name = self.login.user_name.text()
        password = self.login.passwd.text()

        user_name = user_name.strip()  #removing the white spaces
        password = password.strip()

        if not(self.check_entries):
            #tell the user to enter valid informations
            return

        #connecting to db
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'admin',
            database = 'supermarket_db'
        )
        #initialisate the cursor
        cursor = mydb.cursor()

        #geting the role of the user from the db
        get_role = "select role from accounts where user_name = %s and password = %s"
        cursor.execute(get_role, (user_name, password))

        try:
            role = cursor.fetchone()[0]
        except TypeError: #in case that theres no an acc 
            role = None


        if role == '\'admin\'':   
            self.admin_panel = Admin()
            self.login.close()
            self.admin_panel.show()
        elif role == '\'employee\'':
            print('hello')
        elif role == None:  #invalid user_name or password
            print('acc introuvable')
        else:
            print('invalid role')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())