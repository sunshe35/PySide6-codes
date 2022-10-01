# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QSpinBox 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300, 100)

        layout = QFormLayout()

        self.label = QLabel("current value:")
        # self.label.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.label)

        self.spinbox = QSpinBox()
        layout.addRow(QLabel('默认显示'), self.spinbox)
        self.spinbox.valueChanged.connect(lambda: self.on_valuechange(self.spinbox))

        label = QLabel("步长和范围：")
        self.spinbox_int = QSpinBox()
        self.spinbox_int.setRange(-20, 20)
        self.spinbox_int.setMinimum(-10)
        self.spinbox_int.setSingleStep(2)
        self.spinbox_int.setValue(0)
        layout.addRow(label, self.spinbox_int)
        self.spinbox_int.valueChanged.connect(lambda: self.on_valuechange(self.spinbox_int))

        label = QLabel("循环：")
        self.spinbox_wrap = QSpinBox()
        self.spinbox_wrap.setRange(-20, 20)
        self.spinbox_wrap.setSingleStep(5)
        self.spinbox_wrap.setWrapping(True)
        layout.addRow(label, self.spinbox_wrap)
        self.spinbox_wrap.valueChanged.connect(lambda: self.on_valuechange(self.spinbox_wrap))

        label = QLabel("前后缀")
        self.spinbox_price = QSpinBox()
        self.spinbox_price.setRange(0, 999)
        self.spinbox_price.setSingleStep(1)
        self.spinbox_price.setPrefix("¥")
        self.spinbox_price.setSuffix("/每个")
        self.spinbox_price.setValue(99)
        layout.addRow(label, self.spinbox_price)
        self.spinbox_price.valueChanged.connect(lambda: self.on_valuechange(self.spinbox_price))


        self.groupSeparatorSpinBox = QSpinBox()
        self.groupSeparatorSpinBox.setRange(-99999999, 99999999)
        self.groupSeparatorSpinBox.setValue(1000)
        self.groupSeparatorSpinBox.setGroupSeparatorShown(True)
        groupSeparatorChkBox = QCheckBox()
        groupSeparatorChkBox.setText("千分隔符：")
        groupSeparatorChkBox.setChecked(True)
        layout.addRow(groupSeparatorChkBox, self.groupSeparatorSpinBox)
        groupSeparatorChkBox.toggled.connect(self.groupSeparatorSpinBox.setGroupSeparatorShown)
        self.groupSeparatorSpinBox.valueChanged.connect(lambda: self.on_valuechange(self.groupSeparatorSpinBox))


        label = QLabel("特殊文本：")
        self.spinbox_zoom = QSpinBox()
        self.spinbox_zoom.setRange(0, 1000)
        self.spinbox_zoom.setSingleStep(10)
        self.spinbox_zoom.setSuffix("%")
        self.spinbox_zoom.setSpecialValueText("Automatic")
        self.spinbox_zoom.setValue(100)
        layout.addRow(label, self.spinbox_zoom)
        self.spinbox_zoom.valueChanged.connect(lambda: self.on_valuechange(self.spinbox_zoom))




        self.setLayout(layout)

    def on_valuechange(self, spinbox):
        self.label.setText("current value:" + str(spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec())
