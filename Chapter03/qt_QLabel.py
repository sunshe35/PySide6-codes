# -*- coding: utf-8 -*-


'''
    【简介】
    PySide6中Qlabel例子

'''

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette
import sys
import os
os.chdir(os.path.dirname(__file__))

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        # 显示普通标签
        label_normal = QLabel(self)
        label_normal.setText("这是一个普通标签,居中。")
        label_normal.setAlignment(Qt.AlignCenter)
        # label_normal.setAutoFillBackground(True)

        # 背景标签
        label_color = QLabel(self)
        label_color.setText("这是一个有红色背景白色字体标签，左对齐。")
        label_color.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        palette.setColor(QPalette.WindowText, Qt.white)
        label_color.setPalette(palette)
        label_color.setAlignment(Qt.AlignLeft)

        # html标签
        label_html = QLabel(self)
        label_html.setText("<a href='#'>这是一个html标签</a> <font color=red>hello <b>world</b> </font>")

        # 划过Qlabel绑定槽事件
        label_hover = QLabel(self)
        label_hover.setText("<a href='#'>鼠标划过该标签触发事件</a>")
        label_hover.linkHovered.connect(self.link_hovered)

        # 点击Qlabel绑定槽事件
        label_click = QLabel(self)
        label_click.setText("<a href='http://www.baidu.com'>点击可以打开百度</a>")
        label_click.linkActivated.connect(self.link_clicked)
        label_click.setOpenExternalLinks(True)

        # 显示图片
        label_pic = QLabel(self)
        label_pic.setAlignment(Qt.AlignCenter)
        label_pic.setToolTip('这是一个图片标签')
        label_pic.setPixmap(QPixmap("./images/cartoon1.ico"))


        # 添加布局管理
        vbox = QVBoxLayout()
        vbox.addWidget(label_normal)
        vbox.addStretch()
        vbox.addWidget(label_color)
        vbox.addStretch()
        vbox.addWidget(label_html)
        vbox.addStretch()
        vbox.addWidget(label_hover)
        vbox.addStretch()
        vbox.addWidget(label_click)
        vbox.addStretch()
        vbox.addWidget(label_pic)
        self.setLayout(vbox)

        self.setWindowTitle("QLabel 例子")


    def link_hovered(self):
        print("你的滑过了“鼠标划过该标签触发事件”。")


    def link_clicked(self):
        # 设置了setOpenExternalLinks(True)之后会自动屏蔽该信号。
        print("当鼠标点击“点击可以打开百度”标签时，触发事件。")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec())
