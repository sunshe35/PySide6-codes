# -*- coding: utf-8 -*-


import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle('DateDialog')

        # 在布局中添加部件
        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        # 使用两个button(ok和cancel)分别连接accept()和reject()槽函数
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # 从对话框中获取当前日期和时间
    def dateTime(self):
        return self.datetime.dateTime()

    # 静态方法创建对话框并返回 (date, time, accepted)
    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        datetime = dialog.dateTime()
        return (datetime, result == QDialog.Accepted)


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('对话框关闭时返回值给主窗口例子')
        self.label = QLabel('用来显示数据')
        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('1、调用对话框')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('2、调用静态函数')
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.label)
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        datetime = dialog.dateTime()
        date = datetime.toString('yyyy-MM-dd')
        tim = datetime.time().toString()
        self.lineEdit.setText(datetime.toString('yyyy/MM/dd hh:mm:ss'))
        _str = f'日期对话框1返回值:\ndate={date};\ntime={tim};\nresult={result}'
        if result == QDialog.Accepted:
            _str += ',点击"确认"按钮'
        else:
            _str += ',点击"取消"按钮'
        self.label.setText(_str)
        dialog.destroy()

    def onButton2Click(self):
        datetime, result = DateDialog.getDateTime()
        date = datetime.toString('yyyy-MM-dd')
        tim = datetime.time().toString()
        self.lineEdit.setText(datetime.toString('yyyy/MM/dd hh:mm:ss'))
        _str = f'日期对话框2返回值:\ndate={date};\ntime={tim};\nresult={result}'
        if result == QDialog.Accepted:
            _str += ',点击"确认"按钮'
        else:
            _str += ',点击"取消"按钮'
        self.label.setText(_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec())
