# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(809, 542)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(90, 100, 581, 361))
        self.groupBox.setStyleSheet(u"background-color:#d4c5c5;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-460, -10, 721, 381))
        self.label.setStyleSheet(u"background-color: #154c79;\n"
"/*padding: 10px;*/\n"
"border-radius:150%;")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 130, 121, 31))
        self.label_2.setStyleSheet(u"color: #fff;\n"
"font: mnonspace;\n"
"font-size: 18px;\n"
"background-color: #154c79;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 170, 171, 31))
        self.label_3.setStyleSheet(u"color: #fff;\n"
"font: bold;\n"
"font-size: 20px;\n"
"background-color: #154c79;")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 210, 151, 31))
        self.label_4.setStyleSheet(u"color: #fff;\n"
"font: mnonspace;\n"
"font-size: 18px;\n"
"background-color: #154c79;")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 60, 91, 41))
        self.label_5.setStyleSheet(u"color: #154c79;\n"
"font-size: 23px;\n"
"font : bold;")
        self.user_name = QLineEdit(self.groupBox)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setGeometry(QRect(310, 142, 211, 31))
        self.user_name.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #1c100b;\n"
"padding-bottom: 7px;\n"
"font-size: 18px;")
        self.passwd = QLineEdit(self.groupBox)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(310, 210, 211, 31))
        self.passwd.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #1c100b;\n"
"padding-bottom: 7px;\n"
"font-size: 18px;")
        self.passwd.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self.groupBox)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(310, 280, 211, 31))
        self.login_btn.setStyleSheet(u"QPushButton#login_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton#login_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton#login_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"")
        self.close_btn = QPushButton(self.groupBox)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(535, 4, 41, 31))
        self.close_btn.setStyleSheet(u"QPushButton#close_btn{\n"
"	border-style: none;\n"
"	color : #154c79;\n"
"	font: bold;\n"
"	font-size: 25px;	\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton#close_btn:pressed{\n"
"		padding-top: 5px;\n"
"}")
        self.minimize_btn = QPushButton(self.groupBox)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(494, 4, 41, 31))
        self.minimize_btn.setStyleSheet(u"QPushButton#minimize_btn{\n"
"	border-style: none;\n"
"	color : #154c79;\n"
"	font: bold;\n"
"	font-size:40px;	\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton#minimize_btn:pressed{\n"
"		padding-top: 5px;\n"
"}")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 340, 111, 21))
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: #fff;\n"
"font: mnonspace;\n"
"font-size: 1Zpx;\n"
"background-color: #154c79;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"WELCOME TO", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"SUPERMARKET", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"APPLICATION", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.user_name.setPlaceholderText(QCoreApplication.translate("Form", u"User Name", None))
        self.passwd.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"X", None))
        self.minimize_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u00a9 MEHER MAJDOUB", None))
    # retranslateUi

