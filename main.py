"""
this is the main program
the project is not finished yet
"""
#pyrcc5 icons.qrc -o icons.py


#imports
import sys
from src.admin import Admin
from src.login import Login
from gui.icons import icons
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
import mysql.connector

#connecting to db
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'supermarket'
)


class Controller:
    def check_entries(x,y): #verfying the inputs
        return True

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

        #initialisate the cursor
        cursor = mydb.cursor()

        #geting the role of the user from the db
        get_role = "SELECT account_id, role FROM accounts WHERE user_name = %s AND password = %s" 
        cursor.execute(get_role, (user_name, password))

        role = None
        try:
            info = cursor.fetchone()
            id = info[0]
            role = info[1]
        except TypeError: #in case that theres not an acc 
            pass


        if role == 'admin':
            cursor.execute("SELECT first_name, last_name FROM admins WHERE %s = account_id",(id,))      
            info = cursor.fetchone()                  
            name = info[0] + ' ' + info[1]
            self.admin_panel = Admin(mydb, name)            
            self.admin_panel.show()     
            self.login.close()
            self.admin_panel.switch_window.connect(self.show_login)



        elif role == 'seller':
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