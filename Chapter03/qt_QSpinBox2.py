# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QSpinBox 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class myQSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(myQSpinBox, self).__init__(parent)

    def valueFromText(self, text):
        regExp = QRegularExpression("(\\d+)(\\s*[xx]\\s*\\d+)?")
        match = regExp.match(text)
        if match.isValid():
            return match.captured(1).toInt()
        return 0

    def textFromValue(self, val):
        return ('%s x %s' % (val, val))


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

        self.spinbox = myQSpinBox()
        layout.addRow(QLabel('自定义显示：'), self.spinbox)
        self.spinbox.valueChanged.connect(lambda: self.on_valuechange(self.spinbox))


        self.setLayout(layout)

    def on_valuechange(self, spinbox):
        self.label.setText("current value:" + str(spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec())
