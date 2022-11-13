from .style_sheets import *
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate, Qt
import time, datetime


class Admin(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
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
        self.logout_btn.clicked.connect(self.logout)


        #users frame
        self.users_clear_btn.clicked.connect(lambda: self.clear(self.users_frame))
        self.users_search_btn.clicked.connect(self.search_user)
        self.users_update_btn.clicked.connect(self.update_user)
        self.users_add_btn.clicked.connect(self.add_user)
        self.users_delete_btn.clicked.connect(self.delete_user)
        #initialization the table
        self.update_table()
        self.users_table.selectionModel().selectionChanged.connect(lambda: self.new_selection(self.users_table.currentRow()))

        #categories frame
        self.categories_clear_btn.clicked.connect(lambda: self.clear(self.categories_frame))
        self.categories_search_btn.clicked.connect(self.search_category)
    
    def logout(self):
        self.switch_window.emit()
        self.close()

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
        self.users_table.clearSelection()
        for children in frame.findChildren(QtWidgets.QWidget): 
            if children.statusTip() == 'del':
                children.setText('')
          
    def search_user(self):
        id = self.users_search_id.text()
        if id == '':
            self.update_table()
        table = self.users_table
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_id = %s", (id,))
        acc = cursor.fetchone()
        if acc != None:
            if acc[3] == 'admin':
                cursor.execute("SELECT * FROM admins WHERE account_id = %s", (id,))
                infos = cursor.fetchone()
            elif acc[3] == 'seller':
                cursor.execute("SELECT * FROM sellers WHERE account_id = %s", (id,))
                infos = cursor.fetchone()
            else:
                print('error')
        
            self.clear_table()
            table.insertRow(0)
            table.setItem(0 , 0, QTableWidgetItem(str(infos[0])))
            table.setItem(0 , 1, QTableWidgetItem(infos[1]))
            table.setItem(0 , 2, QTableWidgetItem(infos[2]))
            table.setItem(0 , 3, QTableWidgetItem(infos[3].strftime('%Y-%m-%d')))
            table.setItem(0 , 4, QTableWidgetItem(infos[4]))
            table.setItem(0 , 5, QTableWidgetItem(format(infos[5], ".15g")))
            table.setItem(0 , 6, QTableWidgetItem(infos[6]))
            table.setItem(0 , 7, QTableWidgetItem(infos[7]))
            table.setItem(0 , 8, QTableWidgetItem(acc[3]))
            table.setItem(0 , 9, QTableWidgetItem(acc[1]))
            table.setItem(0 , 10, QTableWidgetItem(acc[2]))
            table.selectRow(0)
        else:
            print('no acc')        
                
    def update_user(self):
        selected_row = self.users_table.currentRow()
        id = self.users_id.text()
        first_name = self.users_first_name.text()
        last_name = self.users_last_name.text()
        birth_date = datetime.datetime.strptime(self.users_birth_date.date().toString(Qt.ISODate), '%Y-%m-%d')
        phone_number = self.users_phone_number.text()
        adress = self.users_adress.toPlainText()
        salary = self.users_salary.text()
        gender = 'male' if self.users_male.isChecked() else 'female'
        user_name = self.users_user_name.text()
        password = self.users_password.text()
        role = self.users_role.currentText().lower()
        
        try:
            cursor = self.db.cursor()
            #getting the previous role
            cursor.execute('SELECT role FROM accounts WHERE account_id = %s', (id,))
            previous_role = cursor.fetchone()[0]
            
            #updating the acc
            update_acc = 'UPDATE accounts SET user_name = %s, password = %s, role = %s WHERE account_id = %s'        
            cursor.execute(update_acc,(user_name, password, role, id))

            #cheking if the role changed or not
            if previous_role == role:  #the role has not changed
                if role == 'admin':
                    update_admin = 'UPDATE admins SET first_name = %s, last_name = %s, birth_date = %s, phone_number = %s, salary = %s, gender = %s, adress = %s WHERE account_id = %s'
                    cursor.execute(update_admin, (first_name, last_name, birth_date, phone_number, salary, gender, adress, id))
                    self.db.commit()
                elif role == 'seller':
                    update_seller = 'UPDATE sellers SET first_name = %s, last_name = %s, birth_date = %s, phone_number = %s, salary = %s, gender = %s, adress = %s WHERE account_id = %s'
                    cursor.execute(update_seller, (first_name, last_name, birth_date, phone_number, salary, gender, adress, id))
                    self.db.commit()
            else: #the role has changed
                if role == 'admin' and previous_role == 'seller':
                    cursor.execute('DELETE FROM sellers WHERE (account_id = %s)', (id,))  #deleting the acc from the sellers table
                    cursor.execute('INSERT INTO admins VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id, first_name, last_name, birth_date, phone_number, salary, gender, adress))
                    self.db.commit()

                elif role == 'seller' and previous_role == 'admin':
                    cursor.execute('DELETE FROM admins WHERE (account_id = %s)', (id,))
                    cursor.execute('INSERT INTO sellers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id, first_name, last_name, birth_date, phone_number, salary, gender, adress))
                    self.db.commit()
            self.update_table()
            self.users_table.selectRow(selected_row)
        except:
            print("something went wrong")



    #add a users
    def add_user(self):
        #verify all inputs

        #id = self.users_id.text()
        first_name = self.users_first_name.text()
        last_name = self.users_last_name.text()
        birth_date = datetime.datetime.strptime(self.users_birth_date.date().toString(Qt.ISODate), '%Y-%m-%d')
        phone_number = self.users_phone_number.text()
        adress = self.users_adress.toPlainText()
        salary = self.users_salary.text()
        gender = 'male' if self.users_male.isChecked() else 'female'
        user_name = self.users_user_name.text()
        password = self.users_password.text()
        role = self.users_role.currentText().lower()


        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT MAX(account_id) FROM accounts')
            id = cursor.fetchone()[0]  + 1
            add_acc = 'INSERT INTO accounts VALUES (%s, %s, %s, %s)'        
            cursor.execute(add_acc,(id,user_name, password, role))
            

            if role == 'admin':
                add_admin = 'INSERT INTO admins VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(add_admin, (id, first_name, last_name, birth_date, phone_number, salary, gender, adress))
                self.db.commit()
            elif role == 'seller':
                add_seller = 'INSERT INTO sellers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(add_seller, (id, first_name, last_name, birth_date, phone_number, salary, gender, adress))
                self.db.commit()
            self.update_table()
        except Exception as e:
            print("something went wrong",e)


    def delete_user(self):
        #check if the acc is not this acc!

        if self.users_id.text().strip() == '':
            return

        id = self.users_id.text()
        if not(self.account_exist(id)): return
        
        cursor = self.db.cursor(prepared=True)
        cursor.execute("SELECT role FROM accounts WHERE (account_id = %s)", (id,))
        role = cursor.fetchone()[0]
        if role == 'admin':
            cursor.execute('DELETE FROM admins WHERE (account_id = %s)', (id,))
        elif role == 'seller':
            cursor.execute('DELETE FROM sellers WHERE (account_id = %s)', (id,))
        else:
            return
        cursor.execute('DELETE FROM accounts WHERE (account_id = %s)', (id,))
        self.db.commit()
        cursor = self.db.cursor()
        self.update_table()

    def search_category(self):
        cursor = self.db.cursor()
        category_id = self.category_id.text()
        cursor.execute('SELECT * FROM categories WHERE category_id = %s', (category_id,))
        print(cursor.fetchone()) #µµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµµ

    def clear_table(self):
        table = self.users_table
        table.clearSelection()
        while table.rowCount() >= 1:
            table.clearSelection()
            table.removeRow(table.rowCount()-1)

    def update_table(self):
        table = self.users_table
        self.clear_table()
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM admins JOIN accounts USING(account_id) UNION SELECT * FROM sellers JOIN accounts USING(account_id) ORDER BY account_id')
            results = cursor.fetchall()    
        except:
            print("error")
            return

        table = self.users_table
        while table.rowCount() >= 1:
            table.removeRow(table.rowCount()-1)
        for result in results:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition , 0, QTableWidgetItem(str(result[0])))
            table.setItem(rowPosition , 1, QTableWidgetItem(result[1]))
            table.setItem(rowPosition , 2, QTableWidgetItem(result[2]))
            table.setItem(rowPosition , 3, QTableWidgetItem(result[3].strftime('%Y-%m-%d')))
            table.setItem(rowPosition , 4, QTableWidgetItem(result[4]))
            table.setItem(rowPosition , 5, QTableWidgetItem(format(result[5], ".15g")))
            table.setItem(rowPosition , 6, QTableWidgetItem(result[6]))
            table.setItem(rowPosition , 7, QTableWidgetItem(result[7]))
            table.setItem(rowPosition , 8, QTableWidgetItem(result[10]))
            table.setItem(rowPosition , 9, QTableWidgetItem(result[8]))
            table.setItem(rowPosition , 10, QTableWidgetItem(result[9]))


    def new_selection(self, current_row):
        #display data from the selected row
        self.users_id.setText(self.users_table.item(current_row,0).text())
        self.users_first_name.setText(self.users_table.item(current_row,1).text()) 
        self.users_last_name.setText(self.users_table.item(current_row,2).text()) 
        self.users_birth_date.setDate(datetime.datetime.strptime(self.users_table.item(current_row,3).text(),'%Y-%m-%d').date())  #converting str object to date object
        self.users_phone_number.setText(self.users_table.item(current_row,4).text())
        self.users_salary.setText(self.users_table.item(current_row,5).text())
        self.users_male.setChecked(True) if self.users_table.item(current_row,6).text() == 'male' else self.users_female.setChecked(True)
        self.users_adress.setText(self.users_table.item(current_row,7).text())
        self.users_role.setCurrentText(self.users_table.item(current_row,8).text().lower().capitalize())
        self.users_user_name.setText(self.users_table.item(current_row,9).text().lower().capitalize())
        self.users_password.setText(self.users_table.item(current_row,10).text().lower().capitalize())


    def account_exist(self, id):
        return True