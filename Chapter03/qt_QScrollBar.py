# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QScrollBar 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.label = QLabel("拖动滑动条去改变颜色")
        self.label.setFont(QFont("Arial", 16))
        hbox.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderval)
        hbox.addWidget(self.scrollbar1)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.setSingleStep(5)
        self.scrollbar2.setPageStep(50)
        self.scrollbar2.setValue(150)
        self.scrollbar2.setFocusPolicy(Qt.StrongFocus)
        self.scrollbar2.valueChanged.connect(self.sliderval)
        hbox.addWidget(self.scrollbar2)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.setSingleStep(5)
        self.scrollbar3.setPageStep(50)
        self.scrollbar3.setValue(100)
        self.scrollbar3.setFocusPolicy(Qt.TabFocus)
        self.scrollbar3.valueChanged.connect(self.sliderval)
        hbox.addWidget(self.scrollbar3)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QScrollBar 例子')
        self.setLayout(hbox)

    def sliderval(self):
        value_tup = (self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        _str = "拖动滑动条去改变颜色:\n左边不支持键盘，\n中间通过tab键or点击获取焦点，\n右边只能通过tab键获取焦点。\n当前选中(%d,%d,%d)"%value_tup
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(*value_tup, 255))
        self.label.setPalette(palette)
        self.label.setText(_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec())
