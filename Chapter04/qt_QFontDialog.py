# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QFontDialog 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.fontLabel = QLabel("Hello,我来显示字体效果")
        layout.addWidget(self.fontLabel)

        self.fontButton1 = QPushButton("设置QLabel字体")
        self.fontButton1.clicked.connect(self.set_label_font)
        layout.addWidget(self.fontButton1)

        self.fontButton2 = QPushButton("设置Qwidget字体")
        self.fontButton2.clicked.connect(lambda:self.setFont(QFontDialog.getFont(self.font(),self)[1]))
        layout.addWidget(self.fontButton2)

        self.setLayout(layout)
        self.setWindowTitle("Font Dialog 例子")
        # self.setFont(QFontDialog.getFont(self.font(),self)[1])

    def set_label_font(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = FontDialogDemo()
    demo.show()
    sys.exit(app.exec())
