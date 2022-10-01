# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QCalendarWidget 例子
   
  
'''

import sys
from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate


class CalendarExample(QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle('Calendar 例子')
        layout = QVBoxLayout()
        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.setCalendarPopup(True)


        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.setSelectedDate(QDate(2010, 1, 30))
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        # self.cal.setFirstDayOfWeek(Qt.Wednesday)
        self.cal.setFirstDayOfWeek(Qt.Wednesday)
        self.cal.move(20, 20)


        self.label = QLabel('此处会显示选择日期信息')


        self.cal.clicked.connect(lambda :self.showDate(self.cal))
        self.dateTimeEdit.dateChanged.connect(lambda x: self.cal.setSelectedDate(x))
        self.cal.clicked.connect(lambda x: self.dateTimeEdit.setDate(x))

        layout.addWidget(self.dateTimeEdit)
        layout.addWidget(self.cal)
        layout.addWidget(self.label)
        self.setLayout(layout)



    def showDate(self, cal):
        date = cal.selectedDate().toString("yyyy-MM-dd dddd")
        month = cal.monthShown()
        year = cal.yearShown()
        _str = '当前选择日期: %s;\n当前选择月份: %s;\n当前选择年份: %s;'%(date,month,year)
        self.label.setText(_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CalendarExample()
    demo.show()
    sys.exit(app.exec())
