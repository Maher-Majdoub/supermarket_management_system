from .style_sheets import *
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
import time, datetime



class Seller(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self, db, name):
        self.db = db   #db = data_base
        self.name = name
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\seller.ui', self)
        self.show() 
        self.seller_name.setText(name)
        tm = time.localtime()
        self.date.setText(str(tm.tm_year)+ '-' + str(tm.tm_mon) + '-' + str(tm.tm_mday))
        self.load_categories()
        self.category.currentTextChanged.connect(self.update)

    def load_categories(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT name FROM categories')
        results = cursor.fetchall()
        categories = [result[0] for result in results]
        self.category.addItems(categories)

    def update(self):
        cat = self.category.currentText()
        cursor = self.db.cursor(buffered=True)
        cursor.execute('select category_id from categories where name = %s', (cat,))
        cat_id = cursor.fetchone()[0]
        cursor.execute('select name from products where category_id = %s', (cat_id,))
        results = cursor.fetchall()
        products = [result[0] for result in results]
        self.product.clear()
        self.product.addItems(products)
