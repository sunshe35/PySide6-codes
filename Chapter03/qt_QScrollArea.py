# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QScrollArea 例子


'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
os.chdir(os.path.dirname(__file__))

class QScrollAreaWindow(QMainWindow):
    def __init__(self):
        super(QScrollAreaWindow, self).__init__()
        self.setWindowTitle('QScrollArea案例')

        w = QWidget()
        self.setCentralWidget(w)
        layout_main = QVBoxLayout()
        w.setLayout(layout_main)

        # 创建一个QLabel滚动条
        label_scroll = QLabel()
        label_scroll.setPixmap(QPixmap("./images/boy.png"))
        self.scroll1 = QScrollArea()
        self.scroll1.setWidget(label_scroll)
        layout_main.addWidget(self.scroll1)

        ## 获取QScrollArea的Widget
        widget = self.scroll1.widget()
        print(widget is label_scroll)

        ## 获取以及处理QScrollArea的QScrollBar
        self.scroll1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        hScrollBar = self.scroll1.horizontalScrollBar()
        vScrollBar = self.scroll1.verticalScrollBar()
        vScrollBar.setSingleStep(5)
        vScrollBar.setPageStep(50)
        vScrollBar.setValue(200)
        vScrollBar.setFocusPolicy(Qt.TabFocus)

        # 创建一个QWidget滚动条
        self.scrollWidget = QWidget()
        self.scrollWidget.setMinimumSize(500, 1000)
        self.scroll2 = QScrollArea()
        self.scroll2.setWidget(self.scrollWidget)
        layout_main.addWidget(self.scroll2)

        ## 对QWidget滚动条添加控件
        layout_widget = QVBoxLayout()
        self.scrollWidget.setLayout(layout_widget)
        label_pic = QLabel()
        label_pic.setPixmap(QPixmap("./images/boy.png"))
        layout_widget.addWidget(label_pic)
        label_pic2 = QLabel()
        label_pic2.setPixmap(QPixmap("./images/python.jpg"))
        layout_widget.addWidget(label_pic2)
        button = QPushButton('按鈕')
        button.clicked.connect(lambda: self.on_click(button))
        layout_widget.addWidget(button)

        self.statusBar().showMessage("底部信息栏")
        self.resize(400, 800)

    def on_click(self, button):
        self.statusBar().showMessage('你点击了%s' % button.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QScrollAreaWindow()
    demo.show()
    sys.exit(app.exec())
