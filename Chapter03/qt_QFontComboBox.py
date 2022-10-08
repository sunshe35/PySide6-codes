# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QFontComboBox 例子
'''
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
os.chdir(os.path.dirname(__file__))

class FontComboBoxDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(FontComboBoxDemo, self).__init__(*args, **kwargs)
        self.setWindowTitle("QFontComboBox案例")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)
        self.text_show = QTextBrowser()

        layout.addWidget(self.text_show)

        toolbar = self.addToolBar('toolbar')

        # 设置字体，all
        font = QFontComboBox()
        font.currentFontChanged.connect(lambda font: self.text_show.setFont(font))
        toolbar.addWidget(font)

        # 设置字体,仅限中文
        font2 = QFontComboBox()
        font2.currentFontChanged.connect(lambda font: self.text_show.setFont(font))
        font2.setWritingSystem(QFontDatabase.SimplifiedChinese)
        toolbar.addWidget(font2)

        # 设置字体,等宽字体
        font3 = QFontComboBox()
        font3.currentFontChanged.connect(lambda font: self.text_show.setFont(font))
        font3.setFontFilters(QFontComboBox.MonospacedFonts)
        toolbar.addWidget(font3)

        # 设置字体大小
        font_size_list = [str(i) for i in range(5, 40, 2)]
        combobox = QComboBox(self, minimumWidth=60)
        combobox.addItems(font_size_list)
        combobox.setCurrentIndex(-1)
        combobox.activated.connect(lambda x: self.set_fontSize(int(font_size_list[x])))
        toolbar.addWidget(combobox)

        # 加粗按钮
        buttonBold = QToolButton()
        buttonBold.setShortcut('Ctrl+B')
        buttonBold.setCheckable(True)
        buttonBold.setIcon(QIcon("./images/Bold.png"))
        toolbar.addWidget(buttonBold)
        buttonBold.clicked.connect(lambda: self.setBold(buttonBold))

        # 倾斜按钮
        buttonItalic = QToolButton()
        buttonItalic.setShortcut('Ctrl+I')
        buttonItalic.setCheckable(True)
        buttonItalic.setIcon(QIcon("./images/Italic.png"))
        toolbar.addWidget(buttonItalic)
        buttonItalic.clicked.connect(lambda: self.setItalic(buttonItalic))

        self.text_show.setText('显示数据格式\n textEdit \n Python')

    def setBold(self, button):
        if button.isChecked():
            self.text_show.setFontWeight(QFont.Bold)
        else:
            self.text_show.setFontWeight(QFont.Normal)
        self.text_show.setText(self.text_show.toPlainText())

    def setItalic(self, button):
        if button.isChecked():
            self.text_show.setFontItalic(True)
        else:
            self.text_show.setFontItalic(False)
        self.text_show.setText(self.text_show.toPlainText())

    def set_fontSize(self, x):
        self.text_show.setFontPointSize(x)
        self.text_show.setText(self.text_show.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FontComboBoxDemo()
    w.show()
    sys.exit(app.exec())
