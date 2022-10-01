# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中Qlabel例子
   按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
  
'''

from PySide6.QtWidgets import *
import sys


class QLabelDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Qlabel 例子')
        nameLb1 = QLabel('&Name', self)
        nameEd1 = QLineEdit(self)
        nameLb1.setBuddy(nameEd1)

        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit(self)
        nameLb2.setBuddy(nameEd2)

        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1, 0, 0)
        mainLayout.addWidget(nameEd1, 0, 1, 1, 2)

        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEd2, 1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    labelDemo = QLabelDemo()
    labelDemo.show()
    sys.exit(app.exec())
