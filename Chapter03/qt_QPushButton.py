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

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()
        self.label_show = QLabel('显示按钮信息')
        layout.addWidget(self.label_show)

        self.button1 = QPushButton("Button1")
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda: self.button_click(self.button1))
        layout.addWidget(self.button1)

        self.button_image = QPushButton('image')
        self.button_image.setCheckable(True)
        self.button_image.setIcon(QIcon(QPixmap("./images/python.png")))
        self.button_image.clicked.connect(lambda: self.button_click(self.button_image))
        layout.addWidget(self.button_image)

        self.button_disabled = QPushButton("Disabled")
        self.button_disabled.setEnabled(False)
        layout.addWidget(self.button_disabled)

        self.button_shortcut = QPushButton("&Shortcut_Key")
        self.button_shortcut.setDefault(True)
        self.button_shortcut.setCheckable(True)
        self.button_shortcut.clicked.connect(lambda: self.button_click(self.button_shortcut))
        layout.addWidget(self.button_shortcut)

        self.setWindowTitle("Button demo")
        self.setLayout(layout)


    def button_click(self, button):
        if button.isChecked():
            self.label_show.setText('你按下了' + button.text() + "  isChecked=True")
        else:
            self.label_show.setText('你按下了' + button.text() + "  isChecked=False")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec())
