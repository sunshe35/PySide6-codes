# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QSlider 例子
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class SliderDemo(QWidget):
    def __init__(self, parent=None):
        super(SliderDemo, self).__init__(parent)
        self.setWindowTitle("QSlider 例子")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("Hello Qt for Python")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # 水平滑块
        self.slider_horizon = QSlider(Qt.Horizontal)
        self.slider_horizon.setMinimum(10)
        self.slider_horizon.setMaximum(50)
        self.slider_horizon.setSingleStep(3)
        self.slider_horizon.setPageStep(10)
        self.slider_horizon.setValue(20)
        self.slider_horizon.setTickPosition(QSlider.TicksBelow)
        self.slider_horizon.setTickInterval(5)
        layout.addWidget(self.slider_horizon)

        # 垂直滑块
        self.slider_vertical = QSlider(Qt.Vertical)
        self.slider_vertical.setMinimum(5)
        self.slider_vertical.setMaximum(25)
        self.slider_vertical.setSingleStep(1)
        self.slider_vertical.setPageStep(5)
        self.slider_vertical.setValue(15)
        self.slider_vertical.setTickPosition(QSlider.TicksRight)
        self.slider_vertical.setTickInterval(5)
        self.slider_vertical.setMinimumHeight(100)
        layout.addWidget(self.slider_vertical)

        # 连接信号槽
        self.slider_horizon.valueChanged.connect(lambda :self.valuechange(self.slider_horizon))
        self.slider_vertical.valueChanged.connect(lambda :self.valuechange(self.slider_vertical))

        self.setLayout(layout)

    def valuechange(self,slider):
        size = slider.value()
        self.label.setText('选中大小：%d'%size)
        self.label.setFont(QFont("Arial", size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SliderDemo()
    demo.show()
    sys.exit(app.exec())
