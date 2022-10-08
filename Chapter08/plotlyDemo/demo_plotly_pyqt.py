# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
os.chdir(os.path.dirname(__file__))

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.qwebengine = QWebEngineView(self)
        self.qwebengine.setGeometry(QRect(50, 20, 1200, 600))
        self.qwebengine.load(QUrl.fromLocalFile('\plotly_html\if_hs300_bais.html'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Window()
    screen.showMaximized()
    sys.exit(app.exec())
