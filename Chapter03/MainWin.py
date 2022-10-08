# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中主窗口例子
'''

import sys
from PySide6.QtWidgets import QMainWindow, QApplication,QPushButton,QWidget,QHBoxLayout,QVBoxLayout
from PySide6.QtGui import QIcon,QGuiApplication
from PySide6 import QtCore
import os
os.chdir(os.path.dirname(__file__))

class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # 设置主窗体标签
        self.setWindowTitle("QMainWindow 例子")
        self.resize(800, 400)
        self.status = self.statusBar()


        # 添加布局管理器
        layout = QVBoxLayout()
        widget = QWidget(self)
        widget.setLayout(layout)
        widget.setGeometry(QtCore.QRect(200, 150, 200, 200))
        # self.setCentralWidget(widget)
        self.widget = widget

        # 关闭主窗口
        self.button1 = QPushButton('关闭主窗口')
        self.button1.clicked.connect(self.close)
        layout.addWidget(self.button1)

        # 主窗口居中显示
        self.button2 = QPushButton('主窗口居中')
        self.button2.clicked.connect(self.center)
        layout.addWidget(self.button2)

        # 显示图标
        self.button3 = QPushButton('显示图标')
        self.button3.clicked.connect(lambda :self.setWindowIcon(QIcon('./images/cartoon1.ico')))
        layout.addWidget(self.button3)

        # 显示状态栏
        self.button4 = QPushButton('显示状态栏')
        self.button4.clicked.connect(lambda: self.status.showMessage("这是状态栏提示，5秒钟后消失", 5000))
        layout.addWidget(self.button4)

        # 显示窗口坐标和大小
        self.button5 = QPushButton('显示窗口坐标及大小')
        self.button5.clicked.connect(self.show_geometry)
        layout.addWidget(self.button5)



    def center(self):
        screen = QGuiApplication.primaryScreen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def show_geometry(self):
        print('主窗口坐标信息，相对于屏幕')
        print('主窗口: x={}, y={}, width={}, height={}：'.format(self.x(),self.y(),self.width(),self.height()))
        print('主窗口geometry: x={}, y={}, width={}, height={}：'.format(self.geometry().x(),self.geometry().y(),self.geometry().width(),self.geometry().height()))
        print('主窗口frameGeometry: x={}, y={}, width={}, height={}：'.format(self.frameGeometry().x(),self.frameGeometry().y(),self.frameGeometry().width(),self.frameGeometry().height()))

        print('\n子窗口QWidget坐标信息，相对于主窗口：')
        print('子窗口self.widget: x={}, y={}, width={}, height={}：'.format(self.widget.x(),self.widget.y(),self.widget.width(),self.widget.height()))
        print('子窗口self.widget.geometry: x={}, y={}, width={}, height={}：'.format(self.widget.geometry().x(),self.widget.geometry().y(),self.widget.geometry().width(),self.widget.geometry().height()))
        print('子窗口self.widget.frameGeometry: x={}, y={}, width={}, height={}：'.format(self.widget.frameGeometry().x(),self.widget.frameGeometry().y(),self.widget.frameGeometry().width(),self.widget.frameGeometry().height()))



if __name__ == "__main__":
    app = QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    app.exec()

