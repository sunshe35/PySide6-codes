# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中QRadio例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Radiodemo(QWidget):
    def __init__(self, parent=None):
        super(Radiodemo, self).__init__(parent)
        layout = QHBoxLayout(self)
        self.label = QLabel('显示按钮按下信息')
        self.label.setFixedWidth(120)
        layout.addWidget(self.label)

        # button1,button2未接管按钮
        self.button1 = QRadioButton("按钮1")
        self.button1.setChecked(True)
        self.button1.toggled.connect(lambda: self.button_select(self.button1))
        layout.addWidget(self.button1)

        self.button2 = QRadioButton("按钮2")
        self.button2.toggled.connect(lambda: self.button_select(self.button2))
        layout.addWidget(self.button2)
        
        # button3,button4 使用groupbox接管按钮
        group_box1 = QGroupBox('QGroupbox', self)
        layout_group_box = QVBoxLayout()
        self.button3 = QRadioButton("按钮3")
        self.button3.setChecked(True)
        self.button3.toggled.connect(lambda: self.button_select(self.button3))
        layout_group_box.addWidget(self.button3)

        self.button4 = QRadioButton("按钮4")
        self.button4.toggled.connect(lambda: self.button_select(self.button4))
        layout_group_box.addWidget(self.button4)
        group_box1.setLayout(layout_group_box)

        layout.addWidget(group_box1)

        # button5,button6 使用button_group接管按钮
        button_group = QButtonGroup(self)
        self.button5 = QRadioButton("按钮5")
        self.button5.setChecked(True)
        self.button5.toggled.connect(lambda: self.button_select(self.button5))
        button_group.addButton(self.button5)
        layout.addWidget(self.button5)

        self.button6 = QRadioButton("按钮6")
        self.button6.toggled.connect(lambda: self.button_select(self.button6))
        button_group.addButton(self.button6)
        layout.addWidget(self.button6)


        self.setLayout(layout)
        self.setWindowTitle("RadioButton demo")

    def button_select(self, button):
        if button.isChecked() == True:
            self.label.setText(button.text() + " is selected")
        else:
            self.label.setText(button.text() + " is deselected")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    radioDemo = Radiodemo()
    radioDemo.show()
    sys.exit(app.exec())
