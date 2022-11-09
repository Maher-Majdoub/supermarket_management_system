from .style_sheets import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
import time

class Admin(QtWidgets.QWidget):
    def __init__(self, db):
        self.db = db   #db = data_base
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show() 
        self.containor.setCurrentWidget(self.stats_frame)
        tm = time.localtime()
        self.expense_date.setDate(QDate(tm.tm_year, tm.tm_mon, tm.tm_mday))  #Current date set as default
        self.stats_btn.clicked.connect(lambda : self.switch_btn_clicked(self.stats_frame, self.stats_lbl))
        self.products_btn.clicked.connect(lambda : self.switch_btn_clicked(self.products_frame, self.products_lbl))
        self.categories_btn.clicked.connect(lambda : self.switch_btn_clicked(self.categories_frame, self.categories_lbl))
        self.users_btn.clicked.connect(lambda : self.switch_btn_clicked(self.users_frame, self.users_lbl))
        self.sellings_btn.clicked.connect(lambda : self.switch_btn_clicked(self.sellings_frame, self.sellings_lbl))
        self.expenses_btn.clicked.connect(lambda : self.switch_btn_clicked(self.expenses_frame, self.expenses_lbl))

        #users frame
        self.users_clear_btn.clicked.connect(lambda: self.clear(self.users_frame))
        self.users_search_btn.clicked.connect(self.search)
        self.users_update_btn.clicked.connect(self.update)
        self.users_add_btn.clicked.connect(self.add)
        self.users_delete_btn.clicked.connect(self.delete)


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
        pass

    #add a users
    def add(self):
        #verify all inputs

        id = self.users_id
        first_name = self.users_first_name.text()
        last_name = self.users_last_name.text()
        birth_date = self.users_birth_date
        phone_number = self.users_phone_number.text()
        adress = self.users_adress.toPlainText()
        salary = self.users_salary.text()
        role = self.users_role.currentText().lower()

        if role == 'admin':
            cursor = self.db.cursor()
            add_acc = 'INSERT INTO accounts VALUES (12,"fln","fln","admin")'
            add_admin = 'INSERT INTO admins (acount_id, first_name, last_name, birth_date, phone_number, adress) VALUES (12, "dfsqdfs", "sdfsdf", "1998-01-01", "324134", "qdsf")'
            try:
                cursor.execute(add_acc)
                cursor.execute(add_admin)
                self.db.commit()
            except:
                print("something went wrong!")


    def delete(self):
        pass