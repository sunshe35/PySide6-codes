# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QCheckBox 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import os
os.chdir(os.path.dirname(__file__))

class CheckBoxDemo(QWidget):

    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        self.textEdit.setMinimumWidth(400)


        layout_child = QHBoxLayout()
        self.checkBox1 = QCheckBox("&Checkbox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.button_click(self.checkBox1))
        layout_child.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("Checkbox2")
        self.checkBox2.setChecked(True)
        self.checkBox2.setIcon(QIcon(QPixmap("./images/python.png")))
        self.checkBox2.toggled.connect(lambda: self.button_click(self.checkBox2))
        layout_child.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("tristateBox")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda: self.button_click(self.checkBox3))
        layout_child.addWidget(self.checkBox3)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(layout_child)

        self.setLayout(layout)
        self.setWindowTitle("checkbox demo")

    def button_click(self, btn):
        chk1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ', chekState=' + str(
            self.checkBox1.checkState().name.decode('utf8')) + "\n"
        chk2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ', checkState=' + str(
            self.checkBox2.checkState().name.decode('utf8')) + "\n"
        chk3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ', checkState=' + str(
            self.checkBox3.checkState().name.decode('utf8')) + "\n"
        click = '你点击了' + btn.text()
        self.textEdit.setText(chk1Status + chk2Status + chk3Status+click)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkboxDemo = CheckBoxDemo()
    checkboxDemo.show()
    sys.exit(app.exec())
