# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seller.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)
import icons_rc
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1232, 835)
        Form.setStyleSheet(u"QWiget{\n"
"	background-color: #fff;\n"
"}\n"
"QPushButton{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
" }\n"
"QPushButton:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
" }\n"
"QPushButton:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
" }\n"
"QLabel{\n"
"	color: #154c79;\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"}")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 30, 201, 151))
        self.groupBox.setStyleSheet(u"border: none;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 91, 81))
        self.label.setPixmap(QPixmap(u":/icons/seller.png"))
        self.label.setScaledContents(True)
        self.seller_name = QLabel(self.groupBox)
        self.seller_name.setObjectName(u"seller_name")
        self.seller_name.setGeometry(QRect(30, 90, 151, 31))
        self.seller_name.setStyleSheet(u"font-size: 15px;\n"
"font: bold;")
        self.seller_name.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 120, 81, 20))
        self.label_3.setStyleSheet(u"font-size : 20px;\n"
"font:bold;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 81, 31))
        self.category = QComboBox(Form)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(130, 200, 221, 31))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 260, 71, 31))
        self.product = QComboBox(Form)
        self.product.setObjectName(u"product")
        self.product.setGeometry(QRect(130, 260, 221, 31))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 320, 81, 31))
        self.unit_price = QLineEdit(Form)
        self.unit_price.setObjectName(u"unit_price")
        self.unit_price.setGeometry(QRect(130, 320, 221, 31))
        self.unit_price.setReadOnly(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 380, 81, 31))
        self.quantity = QSpinBox(Form)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setGeometry(QRect(130, 380, 221, 31))
        self.quantity.setMinimum(1)
        self.quantity.setMaximum(9999)
        self.quantity.setValue(1)
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(30, 420, 321, 41))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.add_btn.setFont(font)
        self.products_table = QTableWidget(Form)
        if (self.products_table.columnCount() < 3):
            self.products_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.products_table.setObjectName(u"products_table")
        self.products_table.setEnabled(True)
        self.products_table.setGeometry(QRect(30, 480, 321, 341))
        self.products_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.products_table.horizontalHeader().setMinimumSectionSize(56)
        self.products_table.horizontalHeader().setDefaultSectionSize(106)
        self.products_table.verticalHeader().setVisible(False)
        self.orders_table = QTableWidget(Form)
        if (self.orders_table.columnCount() < 4):
            self.orders_table.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.orders_table.setObjectName(u"orders_table")
        self.orders_table.setGeometry(QRect(370, 20, 651, 801))
        font1 = QFont()
        font1.setPointSize(7)
        self.orders_table.setFont(font1)
        self.orders_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.orders_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.orders_table.horizontalHeader().setDefaultSectionSize(162)
        self.orders_table.verticalHeader().setVisible(False)
        self.orders_table.verticalHeader().setDefaultSectionSize(40)
        self.confirm_btn = QPushButton(Form)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(1100, 590, 111, 41))
        self.confirm_btn.setFont(font)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1030, 60, 61, 31))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1060, 170, 141, 271))
        self.label_8.setFont(font)
        self.label_8.setPixmap(QPixmap(u":/icons/facture.png"))
        self.label_8.setScaledContents(True)
        self.date = QLabel(Form)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(1030, 470, 181, 41))
        self.date.setFont(font)
        self.date.setStyleSheet(u"background-color:  #154c79;\n"
"color : #fff;\n"
"font: bold;\n"
"font-size: 16px;")
        self.date.setTextFormat(Qt.RichText)
        self.date.setAlignment(Qt.AlignCenter)
        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(1030, 740, 101, 41))
        self.delete_btn.setFont(font)
        self.total_lbl = QLabel(Form)
        self.total_lbl.setObjectName(u"total_lbl")
        self.total_lbl.setGeometry(QRect(1080, 60, 141, 31))
        self.total_lbl.setAlignment(Qt.AlignCenter)
        self.logout_btn = QPushButton(Form)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(20, 20, 31, 41))
        self.logout_btn.setFont(font)
        self.logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_btn.setMouseTracking(False)
        self.logout_btn.setTabletTracking(False)
        self.logout_btn.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/icons/logout.png);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.seller_name.setText(QCoreApplication.translate("Form", u"seller name here", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"SELLER", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Category", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Product", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Unit price", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add To List", None))
        ___qtablewidgetitem = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"product", None));
        ___qtablewidgetitem1 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"unit price", None));
        ___qtablewidgetitem2 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"in stock", None));
        ___qtablewidgetitem3 = self.orders_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem4 = self.orders_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Product", None));
        ___qtablewidgetitem5 = self.orders_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Unit Price", None));
        ___qtablewidgetitem6 = self.orders_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Quantity", None));
        self.confirm_btn.setText(QCoreApplication.translate("Form", u"confirm", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.label_8.setText("")
        self.date.setText("")
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.total_lbl.setText("")
        self.logout_btn.setText("")
    # retranslateUi

