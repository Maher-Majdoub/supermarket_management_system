from .style_sheets import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
import time


class Admin(QtWidgets.QWidget):
    def __init__(self, db, name):
        self.db = db   #db = data_base
        self.name = name
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show() 
        self.admin_name_lbl.setText(name)
        self.containor.setCurrentWidget(self.stats_frame)
        tm = time.localtime()
        self.expense_date.setDate(QDate(tm.tm_year, tm.tm_mon, tm.tm_mday))  #Current date set as default
        self.stats_btn.clicked.connect(lambda : self.switch_btn_clicked(self.stats_frame, self.stats_lbl))
        self.products_btn.clicked.connect(lambda : self.switch_btn_clicked(self.products_frame, self.products_lbl))
        self.categories_btn.clicked.connect(lambda : self.switch_btn_clicked(self.categories_frame, self.categories_lbl))
        self.users_btn.clicked.connect(lambda : self.switch_btn_clicked(self.users_frame, self.users_lbl))
        self.incomes_btn.clicked.connect(lambda : self.switch_btn_clicked(self.incomes_frame, self.incomes_lbl))
        self.expenses_btn.clicked.connect(lambda : self.switch_btn_clicked(self.expenses_frame, self.expenses_lbl))


        #users frame
        self.users_clear_btn.clicked.connect(lambda: self.clear(self.users_frame))
        self.users_search_btn.clicked.connect(self.search)
        self.users_update_btn.clicked.connect(self.update)
        self.users_add_btn.clicked.connect(self.add)
        self.users_delete_btn.clicked.connect(self.delete)
        #initialization the table
        self.initialize_table()


    #change the current frame when a switch btn clicked
    def switch_btn_clicked(self, frame, lbl):
        self.containor.setCurrentWidget(frame)
        lbl.setProperty("enabled", "false")
        for i in range (self.options.count()):
            label = self.options.itemAt(i).widget()
            if label != lbl:
                label.setEnabled(True)
        self.setStyleSheet(admin_form_style_sheet)

    #clear all lines edits in the frame
    def clear(self, frame):
        for children in frame.findChildren(QtWidgets.QWidget): 
            if children.statusTip() == 'del':
                children.setText('')

    def search(self):
        pass

    def update(self):
        self.initialize_table()

    #add a users
    def add(self):
        #verify all inputs

        id = self.users_id.text()
        first_name = self.users_first_name.text()
        last_name = self.users_last_name.text()
        birth_date = self.users_birth_date
        phone_number = self.users_phone_number.text()
        adress = self.users_adress.toPlainText()
        salary = self.users_salary.text()
        user_name = self.users_user_name.text()
        password = self.users_password.text()
        role = self.users_role.currentText().lower()


        try:
            cursor = self.db.cursor()
            add_acc = 'INSERT INTO accounts VALUES (%s, %s, %s, %s)'        
            cursor.execute(add_acc,(id, user_name, password, role))
            if role == 'admin':
                add_admin = 'INSERT INTO admins VALUES (%s, %s, %s, "2003-01-01", %s, %s, %s, %s)'
                cursor.execute(add_admin, (id, first_name, last_name, phone_number, salary, 'male', adress))
                self.db.commit()
            elif role == 'seller':
                add_admin = 'INSERT INTO sellers VALUES (%s, %s, %s, "2003-01-01", %s, %s, %s, %s)'
                cursor.execute(add_admin, (id, first_name, last_name, phone_number, salary, 'male', adress))
                self.db.commit()
        except:
            print("something went wrong")


    def delete(self):
        pass

    
    def initialize_table(self):
        table = self.users_table
        while table.rowCount() >= 1:
            table.removeRow(table.rowCount()-1)

        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM admins JOIN accounts USING(account_id) UNION SELECT * FROM sellers JOIN accounts USING(account_id)')
            results = cursor.fetchall()

            
        except:
            return
        table = self.users_table
        while table.rowCount() >= 1:
            table.removeRow(table.rowCount()-1)
        for result in results:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition , 0, QTableWidgetItem(result[0]))
            table.setItem(rowPosition , 1, QTableWidgetItem(result[1]+ ' ' + result[2]))
            table.setItem(rowPosition , 2, QTableWidgetItem(result[3].strftime('%Y-%m-%d')))
            table.setItem(rowPosition , 3, QTableWidgetItem(result[4]))
            table.setItem(rowPosition , 4, QTableWidgetItem(format(result[5], ".15g")))
            table.setItem(rowPosition , 5, QTableWidgetItem(result[6]))
            table.setItem(rowPosition , 6, QTableWidgetItem(result[7]))
            table.setItem(rowPosition , 7, QTableWidgetItem(result[10]))
