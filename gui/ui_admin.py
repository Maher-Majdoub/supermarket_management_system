# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFrame, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(1244, 796)
        Form.setAcceptDrops(False)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"QWidget#Form{\n"
"	background-color:#fff/*rgb(37, 150, 190)*/;\n"
"}\n"
"QLabel[statusTip = \"this\"]{\n"
"	color:black;\n"
"}\n"
"QHBoxLayout{\n"
"	background-color:black;\n"
"}\n"
"QFrame[statusTip = \"option\"]{\n"
"\n"
" }\n"
"\n"
"QFrame[statusTip = \"option\"][enabled = \"true\"]:hover{\n"
"	background-color: rgba(110, 110, 110,80);\n"
"	border-left: 6px solid #154c79;\n"
" }\n"
"QFrame[statusTip = \"option\"][enabled = \"false\"]{\n"
"	background-color: rgba(110, 110, 110, 80);\n"
"	border-left: 6px solid #154c79;\n"
" }\n"
"")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 201, 151))
        self.groupBox.setStyleSheet(u"border: none;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 91, 81))
        self.label.setPixmap(QPixmap(u":/icons/admin.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 121, 31))
        self.label_2.setStyleSheet(u"font-size: 15px;\n"
"font: bold;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 120, 71, 20))
        self.label_3.setStyleSheet(u"font-size : 20px;\n"
"font:bold;")
        self.containor = QStackedWidget(Form)
        self.containor.setObjectName(u"containor")
        self.containor.setGeometry(QRect(260, 20, 961, 751))
        self.containor.setStyleSheet(u"background-color:#fff;")
        self.stats_frame = QWidget()
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setAutoFillBackground(False)
        self.label_18 = QLabel(self.stats_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(270, 220, 181, 81))
        self.label_18.setStyleSheet(u"font-size: 50px;")
        self.containor.addWidget(self.stats_frame)
        self.products_frame = QWidget()
        self.products_frame.setObjectName(u"products_frame")
        self.tableWidget = QTableWidget(self.products_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(320, 40, 631, 701))
        self.tableWidget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tableWidget.setAcceptDrops(False)
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.label_19 = QLabel(self.products_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 290, 51, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_24 = QLabel(self.products_frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 350, 41, 31))
        self.label_24.setFont(font)
        self.label_25 = QLabel(self.products_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 420, 71, 31))
        self.label_25.setFont(font)
        self.label_26 = QLabel(self.products_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(20, 230, 51, 31))
        self.label_26.setFont(font)
        self.product_id = QLineEdit(self.products_frame)
        self.product_id.setObjectName(u"product_id")
        self.product_id.setGeometry(QRect(110, 220, 191, 41))
        self.product_id.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.product_name = QLineEdit(self.products_frame)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setGeometry(QRect(110, 280, 191, 41))
        self.product_name.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.product_price = QLineEdit(self.products_frame)
        self.product_price.setObjectName(u"product_price")
        self.product_price.setGeometry(QRect(110, 340, 191, 41))
        self.product_price.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.product_quantity = QLineEdit(self.products_frame)
        self.product_quantity.setObjectName(u"product_quantity")
        self.product_quantity.setGeometry(QRect(110, 410, 191, 41))
        self.product_quantity.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.add_btn = QPushButton(self.products_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(10, 640, 91, 41))
        self.add_btn.setStyleSheet(u"QPushButton#add_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#add_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#add_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.update_btn = QPushButton(self.products_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(110, 640, 91, 41))
        self.update_btn.setStyleSheet(u"QPushButton#update_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#update_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#update_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.delete_btn = QPushButton(self.products_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(210, 640, 91, 41))
        self.delete_btn.setStyleSheet(u"QPushButton#delete_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#delete_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#delete_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.product_category = QComboBox(self.products_frame)
        self.product_category.addItem("")
        self.product_category.addItem("")
        self.product_category.addItem("")
        self.product_category.addItem("")
        self.product_category.setObjectName(u"product_category")
        self.product_category.setGeometry(QRect(20, 480, 281, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_category.sizePolicy().hasHeightForWidth())
        self.product_category.setSizePolicy(sizePolicy)
        self.product_category.setFont(font)
        self.product_category.setTabletTracking(False)
        self.product_category.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #154c79;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"color :#154c79;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	border: 0px;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border-image: url(:/icons/down-arrow.png);\n"
"	\n"
"}")
        self.product_category.setInsertPolicy(QComboBox.InsertAtBottom)
        self.product_category.setIconSize(QSize(30, 30))
        self.clear_btn = QPushButton(self.products_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(230, 530, 71, 31))
        self.clear_btn.setStyleSheet(u"QPushButton#clear_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#clear_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#clear_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.label_16 = QLabel(self.products_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(90, 60, 141, 131))
        self.label_16.setPixmap(QPixmap(u":/icons/products_c.png"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.products_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(110, 20, 91, 31))
        self.label_17.setStyleSheet(u"color: #154c79;\n"
"font-size: 20px;\n"
"font: bold;\n"
"")
        self.products_search_btn = QPushButton(self.products_frame)
        self.products_search_btn.setObjectName(u"products_search_btn")
        self.products_search_btn.setGeometry(QRect(150, 530, 71, 31))
        self.products_search_btn.setStyleSheet(u"QPushButton#products_search_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#products_search_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#products_search_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.containor.addWidget(self.products_frame)
        self.categories_frame = QWidget()
        self.categories_frame.setObjectName(u"categories_frame")
        self.label_27 = QLabel(self.categories_frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(110, 20, 111, 31))
        self.label_27.setStyleSheet(u"color: #154c79;\n"
"font-size: 20px;\n"
"font: bold;\n"
"")
        self.label_20 = QLabel(self.categories_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 60, 141, 131))
        self.label_20.setPixmap(QPixmap(u":/icons/categories_c.png"))
        self.label_20.setScaledContents(True)
        self.categorie_name = QLineEdit(self.categories_frame)
        self.categorie_name.setObjectName(u"categorie_name")
        self.categorie_name.setGeometry(QRect(110, 330, 191, 41))
        self.categorie_name.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.categorie_id = QLineEdit(self.categories_frame)
        self.categorie_id.setObjectName(u"categorie_id")
        self.categorie_id.setGeometry(QRect(110, 270, 191, 41))
        self.categorie_id.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_28 = QLabel(self.categories_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 400, 91, 31))
        self.label_28.setFont(font)
        self.label_29 = QLabel(self.categories_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 340, 51, 31))
        self.label_29.setFont(font)
        self.label_30 = QLabel(self.categories_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 280, 51, 31))
        self.label_30.setFont(font)
        self.categorie_price = QLineEdit(self.categories_frame)
        self.categorie_price.setObjectName(u"categorie_price")
        self.categorie_price.setGeometry(QRect(110, 390, 191, 41))
        self.categorie_price.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.categories_clear_btn = QPushButton(self.categories_frame)
        self.categories_clear_btn.setObjectName(u"categories_clear_btn")
        self.categories_clear_btn.setGeometry(QRect(240, 460, 71, 31))
        self.categories_clear_btn.setStyleSheet(u"QPushButton#categories_clear_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_clear_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_clear_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.categories_add_btn = QPushButton(self.categories_frame)
        self.categories_add_btn.setObjectName(u"categories_add_btn")
        self.categories_add_btn.setGeometry(QRect(20, 570, 91, 41))
        self.categories_add_btn.setStyleSheet(u"QPushButton#categories_add_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_add_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_add_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.categories_update_btn = QPushButton(self.categories_frame)
        self.categories_update_btn.setObjectName(u"categories_update_btn")
        self.categories_update_btn.setGeometry(QRect(120, 570, 91, 41))
        self.categories_update_btn.setStyleSheet(u"QPushButton#categories_update_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_update_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_update_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.categories_delete_btn = QPushButton(self.categories_frame)
        self.categories_delete_btn.setObjectName(u"categories_delete_btn")
        self.categories_delete_btn.setGeometry(QRect(220, 570, 91, 41))
        self.categories_delete_btn.setStyleSheet(u"QPushButton#categories_delete_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_delete_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_delete_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.tableWidget_2 = QTableWidget(self.categories_frame)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QRect(320, 40, 631, 691))
        self.tableWidget_2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tableWidget_2.setAcceptDrops(False)
#if QT_CONFIG(statustip)
        self.tableWidget_2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tableWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_2.setAutoFillBackground(True)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.categories_search_btn = QPushButton(self.categories_frame)
        self.categories_search_btn.setObjectName(u"categories_search_btn")
        self.categories_search_btn.setGeometry(QRect(160, 460, 71, 31))
        self.categories_search_btn.setStyleSheet(u"QPushButton#categories_search_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_search_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#categories_search_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.containor.addWidget(self.categories_frame)
        self.employees_frame = QWidget()
        self.employees_frame.setObjectName(u"employees_frame")
        self.label_31 = QLabel(self.employees_frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(40, 240, 111, 31))
        self.label_31.setFont(font)
        self.categorie_id_2 = QLineEdit(self.employees_frame)
        self.categorie_id_2.setObjectName(u"categorie_id_2")
        self.categorie_id_2.setGeometry(QRect(160, 230, 241, 41))
        self.categorie_id_2.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_32 = QLabel(self.employees_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(40, 300, 91, 31))
        self.label_32.setFont(font)
        self.label_33 = QLabel(self.employees_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(40, 360, 91, 31))
        self.label_33.setFont(font)
        self.dateEdit = QDateEdit(self.employees_frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(160, 420, 241, 31))
        self.dateEdit.setAcceptDrops(False)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.categorie_id_3 = QLineEdit(self.employees_frame)
        self.categorie_id_3.setObjectName(u"categorie_id_3")
        self.categorie_id_3.setGeometry(QRect(160, 290, 241, 41))
        self.categorie_id_3.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.categorie_id_4 = QLineEdit(self.employees_frame)
        self.categorie_id_4.setObjectName(u"categorie_id_4")
        self.categorie_id_4.setGeometry(QRect(160, 350, 241, 41))
        self.categorie_id_4.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_34 = QLabel(self.employees_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(40, 420, 91, 31))
        self.label_34.setFont(font)
        self.label_35 = QLabel(self.employees_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(40, 580, 61, 31))
        self.label_35.setFont(font)
        self.radioButton = QRadioButton(self.employees_frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(160, 580, 61, 31))
        self.radioButton_2 = QRadioButton(self.employees_frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(250, 580, 71, 31))
        self.label_36 = QLabel(self.employees_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(630, 30, 211, 31))
        self.label_36.setStyleSheet(u"color: #154c79;\n"
"font-size: 20px;\n"
"font: bold;\n"
"")
        self.label_37 = QLabel(self.employees_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(560, 90, 91, 31))
        self.label_37.setFont(font)
        self.categorie_id_5 = QLineEdit(self.employees_frame)
        self.categorie_id_5.setObjectName(u"categorie_id_5")
        self.categorie_id_5.setGeometry(QRect(660, 80, 241, 41))
        self.categorie_id_5.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_38 = QLabel(self.employees_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(560, 160, 91, 31))
        self.label_38.setFont(font)
        self.categorie_id_6 = QLineEdit(self.employees_frame)
        self.categorie_id_6.setObjectName(u"categorie_id_6")
        self.categorie_id_6.setGeometry(QRect(660, 150, 241, 41))
        self.categorie_id_6.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_39 = QLabel(self.employees_frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(560, 230, 51, 31))
        self.label_39.setFont(font)
        self.comboBox = QComboBox(self.employees_frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(660, 230, 241, 21))
        self.label_40 = QLabel(self.employees_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(40, 470, 111, 31))
        self.label_40.setFont(font)
        self.categorie_id_7 = QLineEdit(self.employees_frame)
        self.categorie_id_7.setObjectName(u"categorie_id_7")
        self.categorie_id_7.setGeometry(QRect(160, 460, 241, 41))
        self.categorie_id_7.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_41 = QLabel(self.employees_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(40, 520, 81, 31))
        self.label_41.setFont(font)
        self.categorie_id_8 = QLineEdit(self.employees_frame)
        self.categorie_id_8.setObjectName(u"categorie_id_8")
        self.categorie_id_8.setGeometry(QRect(160, 520, 241, 41))
        self.categorie_id_8.setStyleSheet(u"border: none;\n"
"border-bottom: 3px solid #154c79;\n"
"color: #154c79;\n"
"font-size: 18px;")
        self.label_42 = QLabel(self.employees_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(40, 630, 61, 31))
        self.label_42.setFont(font)
        self.textEdit = QTextEdit(self.employees_frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(160, 630, 241, 71))
        self.label_21 = QLabel(self.employees_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(120, 80, 141, 131))
        self.label_21.setPixmap(QPixmap(u":/icons/employee_c.png"))
        self.label_21.setScaledContents(True)
        self.label_43 = QLabel(self.employees_frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(140, 30, 111, 31))
        self.label_43.setStyleSheet(u"color: #154c79;\n"
"font-size: 20px;\n"
"font: bold;\n"
"")
        self.tableView = QTableView(self.employees_frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(490, 350, 471, 401))
        self.Employees_add_btn = QPushButton(self.employees_frame)
        self.Employees_add_btn.setObjectName(u"Employees_add_btn")
        self.Employees_add_btn.setGeometry(QRect(580, 290, 91, 41))
        self.Employees_add_btn.setStyleSheet(u"QPushButton#Employees_add_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#Employees_add_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#Employees_add_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.employees_update_btn = QPushButton(self.employees_frame)
        self.employees_update_btn.setObjectName(u"employees_update_btn")
        self.employees_update_btn.setGeometry(QRect(690, 290, 91, 41))
        self.employees_update_btn.setStyleSheet(u"QPushButton#employees_update_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_update_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_update_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.employees_delete_btn = QPushButton(self.employees_frame)
        self.employees_delete_btn.setObjectName(u"employees_delete_btn")
        self.employees_delete_btn.setGeometry(QRect(800, 290, 91, 41))
        self.employees_delete_btn.setStyleSheet(u"QPushButton#employees_delete_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_delete_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_delete_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.employees_clear_btn = QPushButton(self.employees_frame)
        self.employees_clear_btn.setObjectName(u"employees_clear_btn")
        self.employees_clear_btn.setGeometry(QRect(330, 720, 71, 31))
        self.employees_clear_btn.setStyleSheet(u"QPushButton#employees_clear_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_clear_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_clear_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.employees_search_btn = QPushButton(self.employees_frame)
        self.employees_search_btn.setObjectName(u"employees_search_btn")
        self.employees_search_btn.setGeometry(QRect(240, 720, 71, 31))
        self.employees_search_btn.setStyleSheet(u"QPushButton#employees_search_btn{\n"
"	background-color : #154c79;\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_search_btn:hover{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 10px;\n"
"	font-size: 15px;\n"
"	font : bold;\n"
"}\n"
"QPushButton#employees_search_btn:pressed{\n"
"	background-color : rgba(0, 21, 76, 200);\n"
"	color: rgba(255 , 255, 255, 210);\n"
"	border-radius: 13px;\n"
"	font-size: 15px;\n"
"	padding-top: 2px;\n"
"	font : bold;\n"
"}")
        self.containor.addWidget(self.employees_frame)
        self.sellings_frame = QWidget()
        self.sellings_frame.setObjectName(u"sellings_frame")
        self.label_22 = QLabel(self.sellings_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(230, 290, 191, 81))
        self.label_22.setStyleSheet(u"font-size: 50px;")
        self.containor.addWidget(self.sellings_frame)
        self.bills_frame = QWidget()
        self.bills_frame.setObjectName(u"bills_frame")
        self.label_23 = QLabel(self.bills_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(340, 290, 181, 81))
        self.label_23.setStyleSheet(u"font-size: 50px;")
        self.containor.addWidget(self.bills_frame)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(240, 20, 31, 761))
        self.line.setStyleSheet(u"color: rgba(110,110,110,50)")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 180, 241, 511))
        self.options = QVBoxLayout(self.verticalLayoutWidget)
        self.options.setObjectName(u"options")
        self.options.setContentsMargins(0, 0, 0, 0)
        self.stats_lbl = QFrame(self.verticalLayoutWidget)
        self.stats_lbl.setObjectName(u"stats_lbl")
        self.stats_lbl.setEnabled(False)
        self.stats_lbl.setFrameShape(QFrame.StyledPanel)
        self.stats_lbl.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.stats_lbl)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 10, 71, 51))
        self.label_5.setBaseSize(QSize(50, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.stats_lbl)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 51, 51))
        self.label_4.setMaximumSize(QSize(51, 51))
        self.label_4.setBaseSize(QSize(30, 30))
        font2 = QFont()
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_4.setFont(font2)
        self.label_4.setPixmap(QPixmap(u":/icons/stats.png"))
        self.label_4.setScaledContents(True)
        self.stats_btn = QPushButton(self.stats_lbl)
        self.stats_btn.setObjectName(u"stats_btn")
        self.stats_btn.setGeometry(QRect(0, 0, 221, 81))
        self.stats_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.stats_lbl)

        self.products_lbl = QFrame(self.verticalLayoutWidget)
        self.products_lbl.setObjectName(u"products_lbl")
        self.products_lbl.setFrameShape(QFrame.StyledPanel)
        self.products_lbl.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.products_lbl)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 51, 51))
        self.label_7.setMaximumSize(QSize(51, 51))
        self.label_7.setBaseSize(QSize(30, 30))
        self.label_7.setFont(font2)
        self.label_7.setPixmap(QPixmap(u":/icons/products.png"))
        self.label_7.setScaledContents(True)
        self.label_6 = QLabel(self.products_lbl)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 10, 131, 51))
        self.label_6.setBaseSize(QSize(50, 20))
        self.label_6.setFont(font1)
        self.label_6.setToolTipDuration(-1)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"QLabel:pressed{\n"
"color:red;\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setIndent(1)
        self.products_btn = QPushButton(self.products_lbl)
        self.products_btn.setObjectName(u"products_btn")
        self.products_btn.setGeometry(QRect(0, 0, 221, 81))
        self.products_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.products_lbl)

        self.categories_lbl = QFrame(self.verticalLayoutWidget)
        self.categories_lbl.setObjectName(u"categories_lbl")
        self.categories_lbl.setEnabled(True)
        self.categories_lbl.setFrameShape(QFrame.StyledPanel)
        self.categories_lbl.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.categories_lbl)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 51, 51))
        self.label_8.setMaximumSize(QSize(51, 51))
        self.label_8.setBaseSize(QSize(30, 30))
        self.label_8.setFont(font2)
        self.label_8.setPixmap(QPixmap(u":/icons/categories.png"))
        self.label_8.setScaledContents(True)
        self.label_10 = QLabel(self.categories_lbl)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 10, 161, 51))
        self.label_10.setBaseSize(QSize(50, 20))
        self.label_10.setFont(font1)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.categories_btn = QPushButton(self.categories_lbl)
        self.categories_btn.setObjectName(u"categories_btn")
        self.categories_btn.setGeometry(QRect(0, 0, 221, 81))
        self.categories_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.categories_lbl)

        self.employees_lbl = QFrame(self.verticalLayoutWidget)
        self.employees_lbl.setObjectName(u"employees_lbl")
        self.employees_lbl.setFrameShape(QFrame.StyledPanel)
        self.employees_lbl.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.employees_lbl)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 10, 159, 51))
        self.label_9.setBaseSize(QSize(50, 20))
        self.label_9.setFont(font1)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.employees_lbl)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 51, 51))
        self.label_11.setMaximumSize(QSize(51, 51))
        self.label_11.setBaseSize(QSize(30, 30))
        self.label_11.setFont(font2)
        self.label_11.setPixmap(QPixmap(u":/icons/employee.png"))
        self.label_11.setScaledContents(True)
        self.employees_btn = QPushButton(self.employees_lbl)
        self.employees_btn.setObjectName(u"employees_btn")
        self.employees_btn.setGeometry(QRect(0, 0, 221, 81))
        self.employees_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.employees_lbl)

        self.sellings_lbl = QFrame(self.verticalLayoutWidget)
        self.sellings_lbl.setObjectName(u"sellings_lbl")
        self.sellings_lbl.setFrameShape(QFrame.StyledPanel)
        self.sellings_lbl.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.sellings_lbl)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 10, 51, 51))
        self.label_13.setMaximumSize(QSize(51, 51))
        self.label_13.setBaseSize(QSize(30, 30))
        self.label_13.setFont(font2)
        self.label_13.setPixmap(QPixmap(u":/icons/sellings.png"))
        self.label_13.setScaledContents(True)
        self.label_12 = QLabel(self.sellings_lbl)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 10, 141, 51))
        self.label_12.setBaseSize(QSize(50, 20))
        self.label_12.setFont(font1)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.sellings_btn = QPushButton(self.sellings_lbl)
        self.sellings_btn.setObjectName(u"sellings_btn")
        self.sellings_btn.setGeometry(QRect(0, 0, 221, 81))
        self.sellings_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.sellings_lbl)

        self.bills_lbl = QFrame(self.verticalLayoutWidget)
        self.bills_lbl.setObjectName(u"bills_lbl")
        self.bills_lbl.setEnabled(True)
        self.bills_lbl.setFrameShape(QFrame.StyledPanel)
        self.bills_lbl.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.bills_lbl)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 10, 51, 51))
        self.label_15.setMaximumSize(QSize(51, 51))
        self.label_15.setBaseSize(QSize(30, 30))
        self.label_15.setFont(font2)
        self.label_15.setPixmap(QPixmap(u":/icons/bill.png"))
        self.label_15.setScaledContents(True)
        self.label_14 = QLabel(self.bills_lbl)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 10, 151, 51))
        self.label_14.setBaseSize(QSize(50, 20))
        self.label_14.setFont(font1)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.bills_btn = QPushButton(self.bills_lbl)
        self.bills_btn.setObjectName(u"bills_btn")
        self.bills_btn.setGeometry(QRect(0, 0, 221, 81))
        self.bills_btn.setStyleSheet(u"\n"
"background-color: rgba(0,0,0,0);\n"
"")

        self.options.addWidget(self.bills_lbl)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        self.containor.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(statustip)
        Form.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Meher Majdoub", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ADMIN", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"STATS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Quantity", None));
        self.label_19.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Price", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"ID", None))
        self.product_id.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Id", None))
        self.product_name.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Name", None))
        self.product_price.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Price", None))
        self.product_quantity.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Quantity", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.product_category.setItemText(0, QCoreApplication.translate("Form", u"computer", None))
        self.product_category.setItemText(1, QCoreApplication.translate("Form", u"fish", None))
        self.product_category.setItemText(2, QCoreApplication.translate("Form", u"gold", None))
        self.product_category.setItemText(3, QCoreApplication.translate("Form", u"phone", None))

        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"Products", None))
        self.products_search_btn.setText(QCoreApplication.translate("Form", u"search", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Categories", None))
        self.label_20.setText("")
        self.categorie_name.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Name", None))
        self.categorie_id.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Id", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"ID", None))
        self.categorie_price.setPlaceholderText(QCoreApplication.translate("Form", u"Enter description", None))
        self.categories_clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.categories_add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.categories_update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.categories_delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Price", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Quantity", None));
        self.categories_search_btn.setText(QCoreApplication.translate("Form", u"search", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Employee ID", None))
        self.categorie_id_2.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Id", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.categorie_id_3.setPlaceholderText(QCoreApplication.translate("Form", u"Enter First Name", None))
        self.categorie_id_4.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Last Name", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Birth Date", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Gender", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Male", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Female", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Employee's Account", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"User Name", None))
        self.categorie_id_5.setPlaceholderText(QCoreApplication.translate("Form", u"Enter User Name", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Password", None))
        self.categorie_id_6.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Role", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Employee", None))

        self.label_40.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.categorie_id_7.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Phone Number", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Salary", None))
        self.categorie_id_8.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Salary", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"Adress", None))
        self.label_21.setText("")
        self.label_43.setText(QCoreApplication.translate("Form", u"Employees", None))
        self.Employees_add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.employees_update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.employees_delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.employees_clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.employees_search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"sellings", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"BILLS", None))
#if QT_CONFIG(statustip)
        self.stats_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Stats", None))
        self.label_4.setText("")
        self.stats_btn.setText("")
#if QT_CONFIG(statustip)
        self.products_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText("")
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("Form", u"Products", None))
        self.products_btn.setText("")
#if QT_CONFIG(statustip)
        self.categories_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText("")
#if QT_CONFIG(statustip)
        self.label_10.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("Form", u"Categories", None))
        self.categories_btn.setText("")
#if QT_CONFIG(statustip)
        self.employees_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Employees", None))
        self.label_11.setText("")
        self.employees_btn.setText("")
#if QT_CONFIG(statustip)
        self.sellings_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
        self.label_13.setText("")
#if QT_CONFIG(statustip)
        self.label_12.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
        self.label_12.setText(QCoreApplication.translate("Form", u"Sellings", None))
        self.sellings_btn.setText("")
#if QT_CONFIG(statustip)
        self.bills_lbl.setStatusTip(QCoreApplication.translate("Form", u"option", None))
#endif // QT_CONFIG(statustip)
        self.label_15.setText("")
#if QT_CONFIG(statustip)
        self.label_14.setStatusTip(QCoreApplication.translate("Form", u"this", None))
#endif // QT_CONFIG(statustip)
        self.label_14.setText(QCoreApplication.translate("Form", u"Billls", None))
        self.bills_btn.setText("")
    # retranslateUi

