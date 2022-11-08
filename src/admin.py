from .style_sheets import *
from PyQt5 import QtWidgets, uic

class Admin(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('.\\gui\\admin.ui', self)
        self.show() 
        self.containor.setCurrentWidget(self.stats_frame)
        self.stats_btn.clicked.connect(lambda : self.switch_btn_clicked(self.stats_frame, self.stats_lbl))
        self.products_btn.clicked.connect(lambda : self.switch_btn_clicked(self.products_frame, self.products_lbl))
        self.categories_btn.clicked.connect(lambda : self.switch_btn_clicked(self.categories_frame, self.categories_lbl))
        self.employees_btn.clicked.connect(lambda : self.switch_btn_clicked(self.employees_frame, self.employees_lbl))
        self.sellings_btn.clicked.connect(lambda : self.switch_btn_clicked(self.sellings_frame, self.sellings_lbl))
        self.bills_btn.clicked.connect(lambda : self.switch_btn_clicked(self.bills_frame, self.bills_lbl))

    def switch_btn_clicked(self, frame, lbl):
        self.containor.setCurrentWidget(frame)
        lbl.setProperty("enabled", "false")
        for i in range (self.options.count()):
            label = self.options.itemAt(i).widget()
            if label != lbl:
                label.setEnabled(True)
        self.setStyleSheet(admin_form_style_sheet)