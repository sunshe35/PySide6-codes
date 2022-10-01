# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 DateTimeEdit 例子


'''

import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate, QDateTime, QTime


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDateTimeEdit例子')
        self.resize(300, 90)
        vlayout = QVBoxLayout()
        self.label = QLabel('显示日期选择信息')
        vlayout.addWidget(self.label)

        # QDateTimeEdit示例
        dateTimeLabel = QLabel('QDateTimeEdit示例:')
        dateTimeEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        dateTimeEdit01 = QDateTimeEdit(QDate.currentDate(), self)
        dateTimeEdit01.setDate(QDate(2030, 12, 31))
        dateTimeEdit02 = QDateTimeEdit(QTime.currentTime(), self)
        vlayout.addWidget(dateTimeLabel)
        vlayout.addWidget(dateTimeEdit)
        vlayout.addWidget(dateTimeEdit01)
        vlayout.addWidget(dateTimeEdit02)

        # QDateEdit 示例
        dateEdit = QDateEdit(QDate.currentDate())
        dateEdit.setDateRange(QDate(2015, 1, 1), QDate(2030, 12, 31))
        dateLabel = QLabel('QDateEdit示例:')
        vlayout.addWidget(dateLabel)
        vlayout.addWidget(dateEdit)

        # QTimeEdit 示例
        timeEdit = QTimeEdit(QTime.currentTime())
        timeEdit.setTimeRange(QTime(9, 0, 0, 0), QTime(16, 30, 0, 0))
        timeLabel = QLabel('QTimeEdit示例:')
        vlayout.addWidget(timeLabel)
        vlayout.addWidget(timeEdit)

        # 设置日期和时间格式
        meetingEdit = QDateTimeEdit(QDateTime.currentDateTime())
        formatLabel = QLabel("选择日期和时间格式:")
        formatComboBox = QComboBox()
        formatComboBox.addItems(
            ["yyyy-MM-dd hh:mm:ss (zzz 'ms')", "hh:mm:ss MM/dd/yyyy", "hh:mm:ss dd/MM/yyyy", "北京时间: hh:mm:ss",
             "hh:mm ap"])
        formatComboBox.textActivated.connect(
            lambda: self.setFormatString(formatComboBox.currentText(), meetingEdit))
        vlayout.addWidget(formatLabel)
        vlayout.addWidget(meetingEdit)
        vlayout.addWidget(formatComboBox)

        # 弹出日历小部件
        dateTimeEdit_cal = QDateTimeEdit(QDateTime.currentDateTime(), self)
        dateTimeEdit_cal.setCalendarPopup(True)
        vlayout.addWidget(QLabel('弹出日历小部件'))
        vlayout.addWidget(dateTimeEdit_cal)

        # 信号与槽
        dateTimeEdit.dateTimeChanged.connect(lambda: self.showDate(dateTimeEdit))
        dateTimeEdit01.dateTimeChanged.connect(lambda: self.showDate(dateTimeEdit01))
        dateTimeEdit02.dateTimeChanged.connect(lambda: self.showDate(dateTimeEdit02))
        dateEdit.dateTimeChanged.connect(lambda: self.showDate(dateEdit))
        timeEdit.dateTimeChanged.connect(lambda: self.showDate(timeEdit))
        meetingEdit.dateTimeChanged.connect(lambda: self.showDate(meetingEdit))
        dateTimeEdit_cal.dateTimeChanged.connect(lambda: self.showDate(dateTimeEdit_cal))

        self.setLayout(vlayout)

    def showDate(self, dateEdit):
        # 当前日期时间
        dateTime = dateEdit.dateTime().toString()
        date = dateEdit.date().toString('yyyy-MM-dd')
        time = dateEdit.time().toString()
        # 最大最小日期时间
        maxDateTime = dateEdit.maximumDateTime().toString('yyyy-MM-dd hh:mm:ss')
        minDateTime = dateEdit.minimumDateTime().toString(Qt.ISODate)

        # 最大最小日期
        maxDate = dateEdit.maximumDate().toString(Qt.ISODate)
        minDate = dateEdit.minimumDate().toString()

        # 最大最小时间
        maxTime = dateEdit.maximumTime().toString()
        minTime = dateEdit.minimumTime().toString()

        _str = '当前日期时间：{}\n当前日期：{}\n当前时间：{}\n最大日期时间：{}\n最小日期时间：{}\n最大日期：{}\n最小日期：{}\n最大时间：{}\n最小时间：{}\n'.format(
            dateTime, date, time, maxDateTime, minDateTime, maxDate, minDate, maxTime, minTime)
        self.label.setText(_str)

    def setFormatString(self, formatString, meetingEdit):
        meetingEdit.setDisplayFormat(formatString)

        if meetingEdit.displayedSections() & QDateTimeEdit.DateSections_Mask:
            meetingEdit.setDateRange(QDate(2004, 11, 1), QDate(2005, 11, 30))
        else:
            meetingEdit.setTimeRange(QTime(0, 7, 20, 0), QTime(21, 0, 0, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DateTimeEditDemo()
    demo.show()
    sys.exit(app.exec())
