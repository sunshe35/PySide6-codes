# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QDial 例子
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class dialDemo(QWidget):
    def __init__(self, parent=None):
        super(dialDemo, self).__init__(parent)
        self.setWindowTitle("QDial 例子")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("Hello Qt for Python")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # 普通qdial
        self.dial1 = QDial()
        self.dial1.setMinimum(10)
        self.dial1.setMaximum(50)
        self.dial1.setSingleStep(3)
        self.dial1.setPageStep(5)
        self.dial1.setValue(20)
        layout.addWidget(self.dial1)

        # 开启循环
        self.dial_wrap = QDial()
        self.dial_wrap.setMinimum(5)
        self.dial_wrap.setMaximum(25)
        self.dial_wrap.setSingleStep(1)
        self.dial_wrap.setPageStep(5)
        self.dial_wrap.setValue(15)
        self.dial_wrap.setWrapping(True)
        self.dial_wrap.setMinimumHeight(100)
        layout.addWidget(self.dial_wrap)

        # 连接信号槽
        self.dial1.valueChanged.connect(lambda :self.valuechange(self.dial1))
        self.dial_wrap.valueChanged.connect(lambda :self.valuechange(self.dial_wrap))

        self.setLayout(layout)

    def valuechange(self,dial):
        size = dial.value()
        self.label.setText('选中大小：%d'%size)
        self.label.setFont(QFont("Arial", size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWheelScrollLines(2)
    demo = dialDemo()
    demo.show()
    sys.exit(app.exec())
