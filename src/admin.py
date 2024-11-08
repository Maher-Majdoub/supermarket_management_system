import time, datetime
from . import tools
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QDate, Qt
from .style_sheets import *


class Admin(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, db,id, name):
        self.db = db   #db = data_base
        self.name = name
        self.id = id
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show() 
        self.admin_name_lbl.setText(name)
        self.containor.setCurrentWidget(self.stats_frame)
        tm = time.localtime()
        self.expense_date.setDate(QDate(tm.tm_year, tm.tm_mon, tm.tm_mday))  #Current date set as default
        self.expense_search_date.setDate(QDate(tm.tm_year, tm.tm_mon, tm.tm_mday))
        self.products_btn.clicked.connect(lambda : self.switch_btn_clicked(self.products_frame, self.products_lbl))
        self.categories_btn.clicked.connect(lambda : self.switch_btn_clicked(self.categories_frame, self.categories_lbl))
        self.users_btn.clicked.connect(lambda : self.switch_btn_clicked(self.users_frame, self.users_lbl))
        self.incomes_btn.clicked.connect(lambda : self.switch_btn_clicked(self.incomes_frame, self.incomes_lbl))
        self.expenses_btn.clicked.connect(lambda : self.switch_btn_clicked(self.expenses_frame, self.expenses_lbl))
        self.logout_btn.clicked.connect(self.logout_btn_clicked)

        #users frame
        self.users_clear_btn.clicked.connect(lambda: self.clear(self.users_frame))
        self.users_search_btn.clicked.connect(self.search_user)
        self.users_update_btn.clicked.connect(self.update_user)
        self.users_add_btn.clicked.connect(self.add_user)
        self.users_delete_btn.clicked.connect(self.delete_user)
        #initialization the table
        self.update_users_table()
        self.users_table.selectionModel().selectionChanged.connect(lambda: self.new_selection(self.users_table.currentRow()))

        #categories frame
        self.update_categories_table()
        self.categories_clear_btn.clicked.connect(lambda: self.clear(self.categories_frame))
        self.categories_search_btn.clicked.connect(self.search_category)
        self.categories_add_btn.clicked.connect(self.add_category)
        self.categories_delete_btn.clicked.connect(self.delete_category)
        self.categories_update_btn.clicked.connect(self.update_category)
        self.categories_table.selectionModel().selectionChanged.connect(lambda: self.new_category_selection(self.categories_table.currentRow()))

        #products frame
        self.update_products_table()
        self.products_add_btn.clicked.connect(self.add_product)
        self.products_clear_btn.clicked.connect(lambda: self.clear(self.products_frame))
        self.products_update_btn.clicked.connect(self.update_product)
        self.products_delete_btn.clicked.connect(self.delete_product)
        self.products_search_btn.clicked.connect(self.search_product)
        self.products_table.selectionModel().selectionChanged.connect(lambda: self.new_product_selection(self.products_table.currentRow()))
        
        #incomes frame
        tm = time.localtime()
        self.incomes_date.setDate(datetime.datetime.now())
        self.incomes_date.dateTimeChanged.connect(self.update_incomes_table)
        self.incomes_table.selectionModel().selectionChanged.connect(lambda: self.new_income_selection(self.incomes_table.currentRow()))
        self.incomes_delete_btn.clicked.connect(self.delete_income)
        self.update_incomes_table()
        
        #expenses frame
        self.expense_add_btn.clicked.connect(self.add_expense)
        self.expense_update_btn.clicked.connect(self.update_expense)
        self.expense_delete_btn.clicked.connect(self.delete_expense)
        self.expense_search_date.dateTimeChanged.connect(self.search_expense)
        self.expense_clear_btn.clicked.connect(self.clear_expenses)
        self.expenses_table.selectionModel().selectionChanged.connect(lambda: self.new_expense_selection(self.expenses_table.currentRow()))
        self.search_expense()
        

    def logout_btn_clicked(self):
        if tools.throw_quetion('Logout', 'Are you sure want to Logout?') == 4194304 : return
        self.logout()
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
        id = self.users_search_id.text().strip()
        if id == '':
            self.update_users_table()
        if not tools.verify_integer(id, 'ID') : return
        table = self.users_table
        try:
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
                elif acc[3] == 'none':
                    tools.throw_error('Account Deleted')
                    return
                else:
                    tools.throw_error('Something went wrong')
                    return
            
                self.clear_table(table)
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
                tools.throw_error(f'There\'s not an account with ID = {id}')      
                self.users_search_id.setText('')  
                self.update_users_table()
        except:
            tools.throw_error('Something Went Wrong')
                
    def update_user(self):
        if not tools.verify_entries(self.users_frame): return
        id = self.users_id.text().strip()
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
        
        if tools.throw_quetion('Update User', f'Are you sure want to update this user?') == 4194304 : return
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
                    cursor.execute('DELETE FROM admins WHERE account_id = %s', (id,))
                    cursor.execute('INSERT INTO sellers VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id, first_name, last_name, birth_date, phone_number, salary, gender, adress))
                    self.db.commit()
            tools.throw_info('User Updated Successfully')
            self.update_users_table()
            self.clear(self.users_frame)
        except:
            tools.throw_error('Something Went Wrong')

    #add a user
    def add_user(self):
        if not tools.verify_entries(self.users_frame): return
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
        if tools.throw_quetion('Add New User', f'Are you sure want to add a new user with Role = *{role}*') == 4194304 : return
        
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM accounts WHERE user_name = %s OR password = %s', (user_name, password))
            r = cursor.fetchone()
            if r: 
                tools.throw_error('User Name or Password used in another account !')
                return
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
            self.update_users_table()
            tools.throw_info(f'{role.capitalize()} added Successfully')
        except:
            tools.throw_error('Something Went Wrong')

    def delete_user(self):
        id = self.users_id.text().strip()
        
        if self.users_id.text().strip() == '':
            tools.throw_error('Please select a user to delete it')
            return
        
        current_acc = False
        if id == str(self.id):
            if tools.throw_quetion('Delete User', f'Are you sure want to delete your account?') == 4194304 : return
            current_acc = True
        else:
            if tools.throw_quetion('Delete User', f'Are you sure want to delete this user?') == 4194304 : return
        
        try:
            cursor = self.db.cursor()
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
            tools.throw_info('Account Deleted Successfully')
            if current_acc: self.logout()
            self.update_users_table()
        except:
            tools.throw_error('Something Went Wrong')
     
    def clear_table(self, table):
        table.clearSelection()
        while table.rowCount() >= 1:
            table.clearSelection()
            table.removeRow(table.rowCount()-1)

    def update_users_table(self):
        table = self.users_table
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM admins JOIN accounts USING(account_id) UNION SELECT * FROM sellers JOIN accounts USING(account_id) ORDER BY account_id')
            results = cursor.fetchall()    
        except:
            tools.throw_error('Something Went Wrong')
            return
        
        self.clear_table(table)
        if results:
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
        
        
    def update_categories_table(self):
        table = self.categories_table
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM categories')
            results = cursor.fetchall()
            self.clear_table(table)
            for result in results:
                rowPosition = table.rowCount()
                table.insertRow(rowPosition)
                table.setItem(rowPosition , 0, QTableWidgetItem(str(result[0])))
                table.setItem(rowPosition , 1, QTableWidgetItem(result[1]))
                table.setItem(rowPosition , 2, QTableWidgetItem(result[2]))
        except:
            tools.throw_error('Something Went Wrong')

    def search_category(self):
        table = self.categories_table
        category_id = self.category_search_id.text().strip()
        cursor = self.db.cursor()
        if not tools.verify_id(category_id, 'Category ID'): 
            self.clear(self.categories_frame)
            self.update_categories_table()
            table.selectRow(0)
            return
        if category_id =='':
            self.update_categories_table()
        else:
            try:
                cursor = self.db.cursor()
                cursor.execute('SELECT * FROM categories WHERE (category_id = %s)', (category_id,))
                result = cursor.fetchone()
            except:
                tools.throw_error('Something Went Wrong')
                return
            if result:
                self.clear_table(table)
                table.insertRow(0)
                table.setItem(0 , 0, QTableWidgetItem(str(result[0])))
                table.setItem(0 , 1, QTableWidgetItem(result[1]))
                table.setItem(0 , 2, QTableWidgetItem(result[2]))
                table.selectRow(0)
            else:
                tools.throw_error(f'There\'s no category with ID = {category_id}')
                self.clear(self.categories_frame)
                self.update_categories_table()
                table.selectRow(0)

    def add_category(self):
        if not tools.verify_entries(self.categories_frame): return
        if tools.throw_quetion('Add Category', 'Are you sure want to add this category?') == 4194304 : return
        name = self.category_name.text().strip()
        desc = self.category_description.toPlainText().strip()
        desc = None if desc == '' else desc
        cursor = self.db.cursor() 
        try:
            # checking if there's a category that has the same name in the db
            cursor.execute('SELECT * FROM categories WHERE name = %s', (name,))  
            r = cursor.fetchone()
            if r:  #if there's a category
                tools.throw_error(f'There\'s a category named {name} already exists')     
                return
            

            #getting the id
            cursor.execute('SELECT MAX(category_id) FROM categories')
            r = cursor.fetchone()
            id = int(r[0]) + 1 if r[0] else 1
            # inserting the category
            cursor.execute('INSERT INTO categories VALUES (%s, %s, %s)', (id, name, desc))
            self.db.commit()
            self.update_categories_table()
            self.update_products_table()
            tools.throw_info('Category added Successfuly')
        except:
            tools.throw_error('Something Went Wrong')

    def new_category_selection(self, current_row):
        self.category_id.setText(self.categories_table.item(current_row,0).text())
        self.category_name.setText(self.categories_table.item(current_row,1).text()) 
        self.category_description.setText(self.categories_table.item(current_row,2).text()) 

    def delete_category(self):
        id = self.category_id.text().strip()
        if id == '': 
            tools.throw_error('Please select a category to Delete it')
            return
        if tools.throw_quetion('Delete Category', 'Are you sure want to delete this category') == 4194304 : return
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM products WHERE category_id = %s', (id,))
        r = cursor.fetchone()
        if r : 
            tools.throw_error('Cannot delete this category because there\'s products with this category.. Please Delete those products first')
            return
        try:
            cursor.execute('DELETE FROM categories WHERE category_id = %s', (id,))
            self.db.commit()
            self.update_categories_table()
            self.update_products_table()
            self.clear(self.categories_frame)
            tools.throw_info('Category deleted Successfuly')
        except:
            tools.throw_error('Something Went Wrong!')

    def update_category(self):
        id = self.category_id.text()
        if id == '': 
            tools.throw_error('Please select a category to update it')
            return
        if not tools.verify_entries(self.categories_frame): return
        name = self.category_name.text()
        desc = self.category_description.toPlainText()
        if tools.throw_quetion('Update Category', 'Are you sure want to update this category') == 4194304 : return
        try:
            cursor = self.db.cursor()
            cursor.execute('UPDATE categories SET name = %s, description = %s WHERE category_id = %s', (name, desc, id))
            self.db.commit()
            self.update_categories_table()
            self.update_products_table()
            self.clear(self.categories_frame)
            tools.throw_info('Category Updated Successfuly')
        except:
            tools.throw_error('Something Went Wrong')

    def update_products_table(self):
        try:
            table = self.products_table
            self.clear_table(table)
            cursor = self.db.cursor()
            cursor.execute('SELECT name FROM categories')
            categories = cursor.fetchall()
            self.product_category.clear()
            cat = [categories[i][0] for i in range(len(categories))]
            self.product_category.addItems(cat)
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            if products:
                for product in products:
                    rowPosition = table.rowCount()
                    cursor.execute('SELECT name FROM categories WHERE category_id = %s', (int(product[1]),))
                    cat = cursor.fetchone()
                    table.insertRow(rowPosition)
                    table.setItem(rowPosition , 0, QTableWidgetItem(str(product[0])))
                    table.setItem(rowPosition , 1, QTableWidgetItem(product[2]))
                    table.setItem(rowPosition , 2, QTableWidgetItem(cat[0]))
                    table.setItem(rowPosition , 3, QTableWidgetItem(format(product[3], ".15g")))
                    table.setItem(rowPosition , 4, QTableWidgetItem(str(product[4])))
        except:
            tools.throw_error('Something Went Wrong')

    def add_product(self):
        if not tools.verify_entries(self.products_frame):
            return
        if tools.throw_quetion('Add Product', 'Are you sure want to add this Product?') == 4194304 : return
        name = self.product_name.text()
        price = self.product_price.text()
        quantity = self.product_quantity.text()
        cat = self.product_category.currentText()
        try:
            cursor = self.db.cursor()
            # checking if there's a product that has the same name in the db
            cursor.execute('SELECT * FROM products WHERE name = %s', (name,))  
            r = cursor.fetchone()
            if r:  #if there's a category
                tools.throw_error(f'There\'s a product named {name} already exists')     
                return
            

            #getting the id
            cursor.execute('SELECT MAX(product_id) FROM products')
            r = cursor.fetchone()
            id = int(r[0]) + 1 if r[0] else 1
            cursor.execute('SELECT category_id FROM categories WHERE name LIKE (%s)', (cat,))
            cat_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO products VALUES (%s, %s, %s, %s, %s)', (id, cat_id, name, price, quantity))
            self.db.commit()
            self.clear(self.products_frame)
            tools.throw_info('Product Added Successfully')
            self.update_products_table()
        except:
            tools.throw_error('Something Went Wrong')
            
    def delete_product(self):
        id = self.product_id.text().strip()
        if id == '': 
            tools.throw_error('Please select a product to Delete it')
            return
        if tools.throw_quetion('Delete Product', 'Are you sure want to Delete this Product?') == 4194304 : return
        try:
            cursor = self.db.cursor()
            cursor.execute('DELETE FROM products WHERE (product_id = %s)', (id,))
            self.db.commit()
            tools.throw_info('Product Deleted Successfully')
            self.update_products_table()
            self.clear(self.products_frame)
        except:
            tools.throw_error('Something Went Wrong')
    
    def new_product_selection(self, current_row):
        self.product_id.setText(self.products_table.item(current_row,0).text())
        self.product_name.setText(self.products_table.item(current_row, 1).text())
        self.product_category.setCurrentText(self.products_table.item(current_row,2).text())
        self.product_price.setText(self.products_table.item(current_row, 3).text())
        self.product_quantity.setText(self.products_table.item(current_row, 4).text())

    def update_product(self):
        id = self.product_id.text().strip()
        if id == '': 
            tools.throw_error('Please select a product to update it')
            return
        if tools.throw_quetion('Update Product', 'Are you sure want to Update this Product?') == 4194304 : return
        if not tools.verify_entries(self.products_frame): return
        name = self.product_name.text().strip()
        price = self.product_price.text().strip()
        quantity = self.product_quantity.text().strip()
        cat = self.product_category.currentText().strip()
        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT category_id FROM categories WHERE name LIKE (%s)', (cat,))
            cat_id = cursor.fetchone()[0]
            cursor.execute('UPDATE products SET category_id = %s, name = %s, unit_price = %s, quantity = %s WHERE product_id = %s', (cat_id, name, price, quantity, id))
            self.db.commit()
            tools.throw_info('Product Updated Successfully')
            self.update_products_table()
            self.clear(self.products_frame)
            
        except:
            tools.throw_error('Something Went Wrong')

    def search_product(self):
        table = self.products_table
        product_id = self.product_search_id.text().strip()
        if product_id  =='':
            self.update_products_table()
            return
        if not tools.verify_integer(product_id, 'Product ID') : return
        else:
            try:
                cursor = self.db.cursor()
                cursor.execute('SELECT * FROM products WHERE (product_id = %s)', (product_id,))
                result = cursor.fetchone()
                if result:
                    cat_id = result[1]
                    cursor.execute('SELECT name FROM categories WHERE category_id = %s', (cat_id,))
                    cat = cursor.fetchone()[0]
                    self.clear_table(table)
                    table.insertRow(0)
                    table.setItem(0 , 0, QTableWidgetItem(str(result[0])))       
                    table.setItem(0 , 1, QTableWidgetItem(result[2]))
                    table.setItem(0 , 2, QTableWidgetItem(cat))     
                    table.setItem(0 , 3, QTableWidgetItem(format(result[3], ".15g")))
                    table.setItem(0 , 4, QTableWidgetItem(str(result[4])))
                else:
                    tools.throw_error(f'There\'s no product with ID = {product_id}')
            except:
                tools.throw_error('Something Went Wrong')

    def update_incomes_table(self):
        try:
            table = self.incomes_table
            date = datetime.datetime.strptime(self.incomes_date.date().toString(Qt.ISODate), '%Y-%m-%d')
            cursor = self.db.cursor()
            cursor.execute('SELECT sell_id, account_id, product_id, quantity, unit_price FROM sells WHERE date = %s', (date,))
            results = cursor.fetchall()
            if results:  #if result not None
                self.clear_table(table)
                for result in results:
                    rowPosition = table.rowCount()
                    table.insertRow(rowPosition)
                    table.setItem(rowPosition , 0, QTableWidgetItem(str(result[0])))
                    table.setItem(rowPosition , 1, QTableWidgetItem(str(result[1])))
                    table.setItem(rowPosition , 2, QTableWidgetItem(str(result[2])))
                    table.setItem(rowPosition , 3, QTableWidgetItem(str(result[3])))
                    table.setItem(rowPosition , 4, QTableWidgetItem(str(result[4])))
                    table.setItem(rowPosition , 5, QTableWidgetItem(str(result[3] * result[4])))
                table.selectRow(0)
                self.new_income_selection(0)
            else:
                self.clear_table(table)
            self.update_total_incomes()
        except:
            tools.throw_error('Something Went Wrong')
    
    def new_income_selection(self, current_row):
        table = self.incomes_table
        self.incomes_id.setText(table.item(current_row,0).text())
        self.incomes_seller_id.setText(table.item(current_row,1).text())
        self.incomes_product_id.setText(table.item(current_row,2).text())
        self.incomes_quantity.setText(table.item(current_row,3).text())
        self.incomes_unit_price.setText(table.item(current_row,4).text())
        self.incomes_total_income.setText(table.item(current_row,5).text())
        
    def delete_income(self):
        id = self.incomes_id.text().strip()
        if id == '':
            tools.throw_error('Please select an income to delete it')
            return
        if tools.throw_quetion('Delete income', 'Are you sure want to Delete this income?') == 4194304 : return
        try:
            cursor = self.db.cursor()
            cursor.execute('DELETE FROM sells WHERE sell_id = %s', (id,))
            self.db.commit()
            tools.throw_info('Income Deleted Successfully')
            self.update_incomes_table()
        except:
            tools.throw_error('Something Went Wrong')
                    
    def add_expense(self):
        if not tools.verify_entries(self.expenses_frame): return
        if tools.throw_quetion('Add expense', 'Are you sure want to add this expense?') == 4194304 : return    
        try:   
            cursor = self.db.cursor()
            cursor.execute('SELECT MAX(expense_id) FROM expenses')
            result = cursor.fetchone() 
            expense_id = int(result[0]) + 1 if result[0] else 1
            admin_id = self.id
            ammount = float(self.expense_ammount.text().strip())
            type_ = self.expense_type.currentText()
            date = datetime.datetime.strptime(self.expense_date.date().toString(Qt.ISODate), '%Y-%m-%d')
            desc = self.expense_description.toPlainText().strip()
            cursor.execute('INSERT INTO expenses VALUES (%s, %s, %s, %s, %s, %s)', (expense_id, admin_id, ammount, type_, date, desc if desc != '' else None))
            self.db.commit()
            tools.throw_info('Expense Added Successfully')
            self.search_expense()
        except:
            tools.throw_error('Something Went Wrong')
        
    def update_expense(self):
        if not tools.verify_entries(self.expenses_frame): return
        expense_id = self.expense_id.text()
        ammount = self.expense_ammount.text().strip()
        type_ = self.expense_type.currentText()
        date = datetime.datetime.strptime(self.expense_date.date().toString(Qt.ISODate), '%Y-%m-%d')
        date = datetime.datetime.strptime(self.expense_date.date().toString(Qt.ISODate), '%Y-%m-%d')
        desc = self.expense_description.toPlainText().strip()
        if tools.throw_quetion('Update expense', 'Are you sure want to update this expense?') == 4194304 : return  
        try:
            cursor = self.db.cursor()
            cursor.execute('UPDATE expenses SET ammount = %s, type = %s, date = %s, description = %s WHERE expense_id = %s', (ammount, type_, date, desc, expense_id))
            self.db.commit()
            tools.throw_info('Expense Updated Successfully')
            self.search_expense()
        except:
            tools.throw_error('Something Went Wrong')
        
    def delete_expense(self):
        expense_id = self.expense_id.text().strip()
        if expense_id == '':
            tools.throw_error('Please Select an expense to delete it')
            return
        
        if tools.throw_quetion('Delete expense', 'Are you sure want to delete this expense?') == 4194304 : return  
        try:
            cursor = self.db.cursor()
            cursor.execute('DELETE FROM expenses WHERE expense_id = %s', (expense_id,))
            self.db.commit()
            tools.throw_info('Expense Deleted Successfully')
            self.search_expense()
            
        except:
            tools.throw_error('Something Went Wrong')
        
    def search_expense(self):
        try:
            cursor = self.db.cursor()
            table = self.expenses_table
            date = self.expense_search_date.date().toPyDate()
            year = date.year
            month = date.month
            
            cursor.execute('SELECT * FROM expenses WHERE YEAR(date) = %s AND MONTH(date) = %s', (year, month))
            results = cursor.fetchall()
            if results:
                self.clear_table(table)
                for result in results:
                    rowPosition = table.rowCount()
                    table.insertRow(rowPosition)
                    table.setItem(rowPosition , 0, QTableWidgetItem(str(result[0])))
                    table.setItem(rowPosition , 1, QTableWidgetItem(str(result[1])))
                    table.setItem(rowPosition , 2, QTableWidgetItem(str(result[2])))
                    table.setItem(rowPosition , 3, QTableWidgetItem(str(result[3])))
                    table.setItem(rowPosition , 4, QTableWidgetItem(str(result[4])))
                    table.setItem(rowPosition , 5, QTableWidgetItem(str(result[5])))
                table.selectRow(0)
            else:
                self.clear_table(table)
                self.clear(self.expenses_frame)
            self.update_total_expenses()
        except:
            tools.throw_error('Something Went wrong')
                
    def new_expense_selection(self, current_row):
        table = self.expenses_table
        self.expense_id.setText(table.item(current_row, 0).text())
        self.expense_admin_id.setText(table.item(current_row, 1).text())
        self.expense_ammount.setText(table.item(current_row, 2).text())
        self.expense_type.setCurrentText(table.item(current_row, 3).text())
        self.expense_date.setDate(datetime.datetime.strptime(table.item(current_row, 4).text(),'%Y-%m-%d').date())
        self.expense_description.setText(table.item(current_row, 5).text())
        
    def clear_expenses(self):
        self.clear_table(self.expenses_table)
        self.clear(self.expenses_frame)
    
    def update_total_expenses(self):
        total = 0
        table = self.expenses_table
        for i in range(table.rowCount()):
            total += float(table.item(i, 2).text())
        
        self.total_expenses_lbl.setText(str(total) + '  $')
    
    def update_total_incomes(self):
        total = 0
        table = self.incomes_table
        for i in range(table.rowCount()):
            total += float(table.item(i, 5).text())
        
        self.total_incomes_lbl.setText(str(total) + '  $')

