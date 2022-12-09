"""
this is the main program
the project is not finished yet
"""
#pyrcc5 icons.qrc -o icons.py


#imports
import sys
from src import tools
from src.admin import Admin
from src.seller import Seller
from src.login import Login
from gui.icons import icons
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import mysql.connector


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
            cursor.execute("SELECT account_id, first_name, last_name FROM admins WHERE account_id = %s",(id,))      
            info = cursor.fetchone()     
            id = info[0]             
            name = info[1] + ' ' + info[2]
            self.admin_panel = Admin(mydb, id, name)            
            self.admin_panel.show()     
            self.login.close()
            self.admin_panel.switch_window.connect(self.show_login)

        elif role == 'seller':
            cursor.execute("SELECT first_name, last_name FROM sellers WHERE %s = account_id",(id,))      
            info = cursor.fetchone()                  
            name = info[0] + ' ' + info[1]
            self.seller_panel = Seller(mydb,id, name)            
            self.seller_panel.show()     
            self.login.close()
            self.seller_panel.switch_window.connect(self.show_login)
        else:
            tools.throw_error('Invalid User Name or Password')
 
def connect_to_db():
    #connecting to db
    try:
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'maher',
            password = '*Zyw2Z(x28LJ)6Kq',
            database = 'mydb'
        )
        return mydb
    except:
        app = QtWidgets.QApplication(sys.argv)
        tools.throw_error('Error Establishing a Database Connection')
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    mydb = connect_to_db()
    if mydb:  
        app = QtWidgets.QApplication(sys.argv)
        controller = Controller()
        controller.show_login()
        sys.exit(app.exec_())