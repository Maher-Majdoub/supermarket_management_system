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