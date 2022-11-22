from .style_sheets import *
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import time, datetime


class Seller(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, db, id,name):
        self.db = db   #db = data_base
        self.id = id
        self.name = name
        self.total = 0.0
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\seller.ui', self)
        self.seller_name.setText(name)
        self.show() 
        self.logout_btn.clicked.connect(self.logout)
        tm = time.localtime()
        self.date.setText(str(tm.tm_year)+ '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday))
        self.load_categories()
        self.refresh_category()
        self.category.currentTextChanged.connect(self.update)
        self.product.currentTextChanged.connect(self.product_changed)
        self.add_btn.clicked.connect(self.add_order)
        self.delete_btn.clicked.connect(self.delete_order)
        self.confirm_btn.clicked.connect(self.confirm_order)
        self.total_lbl.setText('{:.2f}    $'.format(self.total))
        self.category.currentTextChanged.connect(self.refresh_category)

    def load_categories(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT name FROM categories')
        results = cursor.fetchall()
        categories = [result[0] for result in results]
        self.category.addItems(categories)
        self.update()
        self.product_changed()

    def update(self):
        cat = self.category.currentText()
        cursor = self.db.cursor()
        cursor.execute('select category_id from categories where name = %s', (cat,))
        cat_id = cursor.fetchone()[0]
        cursor.execute('select name from products where category_id = %s', (cat_id,))
        results = cursor.fetchall()
        products = [result[0] for result in results]
        self.product.clear()
        self.product.addItems(products)

    def product_changed(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT unit_price, quantity FROM products WHERE name = %s', (self.product.currentText(),))

        result = cursor.fetchone()
        if result:
            self.unit_price.setText(str(result[0]))
            self.quantity.setMaximum(int(result[1]))
            self.quantity.setValue(1) if int(result[1]) != 0 else 0
    
    def add_order(self):
        category = self.category.currentText()
        product = self.product.currentText()
        unit_price = self.unit_price.text()
        quantity = self.quantity.value()
        if quantity == 0: return
        table = self.orders_table
        
        #cheking if the table contains this product
        for i in range(table.rowCount()):
            if category == table.item(i, 0).text() and product == table.item(i, 1).text():
                if quantity + int(table.item(i, 3).text()) > self.quantity.maximum():
                    quantity = self.quantity.maximum() - int(table.item(i, 3).text())
                table.setItem(i, 3, QTableWidgetItem(str( quantity + int( table.item(i, 3).text() ) ) ))
                self.total += float(table.item(i, 2).text()) * quantity
                self.total_lbl.setText('{:.2f}    $'.format(self.total))
                return
          
        #this will work if the table does not contains this product      
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QTableWidgetItem(category))
        table.setItem(row_position, 1, QTableWidgetItem(product))
        table.setItem(row_position, 2, QTableWidgetItem(unit_price))
        table.setItem(row_position, 3, QTableWidgetItem(str(quantity)))
        self.total += float(unit_price) * quantity
        self.total_lbl.setText('{:.2f}    $'.format(self.total))
        
    def refresh_category(self):
        table = self.products_table
        category = self.category.currentText()
        cursor = self.db.cursor()
        cursor.execute('SELECT category_id FROM categories WHERE name = %s', (category ,))
        result = cursor.fetchone()
        if result:
            cursor.execute('SELECT name, unit_price, quantity FROM products WHERE category_id = %s', (result[0],))
            products = cursor.fetchall()
            if products:
                self.clear(table)
                for product in products:
                    row_position = table.rowCount()
                    table.insertRow(row_position)
                    table.setItem(row_position, 0, QTableWidgetItem(product[0]))
                    table.setItem(row_position, 1, QTableWidgetItem(format(product[1], ".15g")))
                    table.setItem(row_position, 2, QTableWidgetItem(str(product[2])))
                    
    def clear(slef, table):
        table.clearSelection()
        while table.rowCount() >= 1:
            table.clearSelection()
            table.removeRow(table.rowCount()-1)
            
    def delete_order(self):
        table = self.orders_table
        if table.currentRow() != -1:
            unit_price = table.item(table.currentRow(), 2).text()
            quantity = table.item(table.currentRow(), 3).text()
            table.removeRow(table.currentRow())
            self.total -= float(unit_price) * int(quantity)
            self.total_lbl.setText('{:.2f}    $'.format(self.total))
            
    def confirm_order(self):
        cursor = self.db.cursor()
        table = self.orders_table
        date = datetime.date.today().strftime('%Y-%m-%d')
        for i in range(table.rowCount()):
            product = table.item(i, 1).text()
            unit_price = table.item(i, 2).text()
            quantity = table.item(i, 3).text()
            cursor.execute('SELECT product_id FROM products WHERE name = %s', (product,))
            product_id = cursor.fetchone()[0]
            cursor.execute('SELECT MAX(sell_id) FROM sells')
            result = cursor.fetchone()[0] 
            id = int(result) +1 if result else 1
            cursor.execute('INSERT INTO sells VALUES (%s, %s, %s, %s, %s, %s)', (id, self.id, product_id, unit_price, quantity, date))
            cursor.execute('SELECT quantity FROM products WHERE product_id = %s', (product_id,))
            previous_quantity = int(cursor.fetchone()[0])
            cursor.execute('UPDATE products SET quantity = %s - %s WHERE product_id = %s', (previous_quantity, quantity, product_id))
            self.db.commit()
        self.total = 0.0
        self.total_lbl.setText('{:.2f}    $'.format(self.total))    
        print('done ...')
        self.clear(table)
        self.refresh_category()
    
    def logout(self):
        self.switch_window.emit()
        self.close()
            
        
            