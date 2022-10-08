# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中QButton例子
    
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class CommandLinkButtonDemo(QDialog):
    def __init__(self, parent=None):
        super(CommandLinkButtonDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.label_show = QLabel('显示按钮信息')
        layout.addWidget(self.label_show)

        self.button1 = QCommandLinkButton("默认按钮")
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.button_click(self.button1))
        layout.addWidget(self.button1)

        self.button_descript = QCommandLinkButton("描述按钮",'描述信息')
        self.button_descript.clicked.connect(lambda: self.button_click(self.button_descript))
        layout.addWidget(self.button_descript)

        self.button_image = QCommandLinkButton('图片按钮')
        self.button_image.setCheckable(True)
        self.button_image.setDescription('设置自定义图片')
        self.button_image.setIcon(QIcon("./images/python.png"))
        self.button_image.clicked.connect(lambda: self.button_click(self.button_image))
        layout.addWidget(self.button_image)


        self.setWindowTitle("QCommandLinkButton demo")
        self.setLayout(layout)


    def button_click(self, button):
        if button.isChecked():
            self.label_show.setText('你按下了 ' + button.text() + "  isChecked=True")
        else:
            self.label_show.setText('你按下了 ' + button.text() + "  isChecked=False")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = CommandLinkButtonDemo()
    btnDemo.show()
    sys.exit(app.exec())
