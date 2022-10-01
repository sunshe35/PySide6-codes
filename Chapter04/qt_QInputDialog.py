# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QInputDialog 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()
        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获得字符串")
        self.btn2.clicked.connect(self.getIext)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.btn4 = QPushButton("获得浮点数")
        self.btn4.clicked.connect(self.getDouble)
        self.le4 = QLineEdit()
        layout.addRow(self.btn4, self.le4)

        self.btn5 = QPushButton("获得多行字符串")
        self.btn5.clicked.connect(self.getMultiLine)
        self.le5 = QTextEdit()
        layout.addRow(self.btn5, self.le5)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog 例子")

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getIext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名:')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "输入数字", 10, minValue=-10, maxValue=120, step=10)
        if ok:
            self.le3.setText(str(num))

    def getDouble(self):
        num, ok = QInputDialog.getDouble(self, "double input dualog", "输入数字", 5, minValue=-1.00, maxValue=20.00,
                                         decimals=2, step=0.1)
        if ok:
            self.le4.setText(str(num))

    def getMultiLine(self):
        num, ok = QInputDialog.getMultiLineText(self, "MultiLineText input dualog", "输入多行字符串", '字符串1\n字符串2')
        if ok:
            self.le5.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputdialogDemo()
    demo.show()
    sys.exit(app.exec())
