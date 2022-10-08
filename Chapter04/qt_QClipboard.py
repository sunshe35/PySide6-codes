# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QClipboard 例子
'''

import os
import sys
from PySide6.QtCore import QMimeData
from PySide6.QtWidgets import (QApplication,QWidget, QDialog, QGridLayout, QLabel, QPushButton, QTextEdit)
from PySide6.QtGui import QPixmap, QClipboard
from PySide6.QtGui import Qt
import os
os.chdir(os.path.dirname(__file__))

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        textCopyButton = QPushButton("&Copy Text")
        PasteButton = QPushButton("&Paste")
        htmlCopyButton = QPushButton("C&opy HTML")
        imageCopyButton = QPushButton("Co&py Image")
        self.textLabel = QLabel("Paste text")

        self.typeLabel = QLabel('type label')
        self.formatLabel = QLabel('format label: for valuechange')
        layout = QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)
        layout.addWidget(PasteButton, 1, 0, 1, 2)
        layout.addWidget(self.typeLabel, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 3)
        layout.addWidget(self.formatLabel, 3, 0, 1, 3)
        self.setLayout(layout)
        textCopyButton.clicked.connect(self.copyText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        imageCopyButton.clicked.connect(self.copyImage)

        PasteButton.clicked.connect(self.paste)

        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.updateClipboard)

        self.setWindowTitle("Clipboard 例子")

    def copyText(self):
        self.clipboard.setText("I've been clipped!")

    def copyImage(self):
        self.clipboard.setPixmap(QPixmap(os.path.join(
            os.path.dirname(__file__), "./images/python.png")))

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        self.clipboard.setMimeData(mimeData)

    def paste(self):
        mimeData = self.clipboard.mimeData()
        self.typeLabel.setText('')
        if mimeData.hasImage():
            self.textLabel.setPixmap(mimeData.imageData())
            self.typeLabel.setText(self.typeLabel.text() + '\n' + 'hasImage')
        elif mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())
            self.textLabel.setTextFormat(Qt.RichText)
            self.typeLabel.setText(self.typeLabel.text() + '\n' + 'hasHtml')
        elif mimeData.hasText():
            self.textLabel.setText(mimeData.text())
            self.textLabel.setTextFormat(Qt.PlainText)
            self.typeLabel.setText(self.typeLabel.text() + '\n' + 'hasText')
        else:
            self.textLabel.setText("Cannot display data")

    def updateClipboard(self):
        mimeData = self.clipboard.mimeData()

        formats = mimeData.formats()
        _str = ''

        for format in formats:
            data = mimeData.data(format)
            _str = _str + '\n' + format + '  :  ' + str(data.data()[:20])
        self.formatLabel.setText(_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    app.exec()
