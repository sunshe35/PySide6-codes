# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QToolButton例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QToolButton,QMainWindow,QVBoxLayout,QHBoxLayout,QApplication,QWidget,QToolBar,QMenu,QLabel
import os
os.chdir(os.path.dirname(__file__))

class ToolButtonDemo(QMainWindow):

    def __init__(self, parent=None):
        super(ToolButtonDemo, self).__init__(parent)
        self.setWindowTitle("QToolButton例子")
        self.resize(800, 200)
        self.label_show = QLabel('这里会显示按钮按下信息',self)
        self.label_show.setGeometry(QRect(100, 100, 200, 30))

        # 在QWidget中显示工具按钮
        widget = QWidget(self)
        widget.setGeometry(QRect(40, 30, 500, 60))
        layout = QHBoxLayout()
        widget.setLayout(layout)


        # 文本工具按钮
        tool_button = QToolButton(self)
        tool_button.setText("工具按钮")
        layout.addWidget(tool_button)


        # 自动提升
        tool_button_AutoRaise = QToolButton(self)
        tool_button_AutoRaise.setText("工具按钮-AutoRise")
        tool_button_AutoRaise.setAutoRaise(True)
        layout.addWidget(tool_button_AutoRaise)

        # 图片工具按钮
        tool_button_pic = QToolButton(self)
        tool_button_pic.setText("工具按钮-图片")
        tool_button_pic.setIcon(QIcon("./images/python.png"))
        tool_button_pic.setIconSize(QSize(22,22))
        tool_button_pic.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        layout.addWidget(tool_button_pic)

        # 工具按钮+箭头
        tool_button_arrow = QToolButton(self)
        tool_button_arrow.setText("工具按钮-箭头")
        tool_button_arrow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tool_button_arrow.setArrowType(Qt.UpArrow)
        layout.addWidget(tool_button_arrow)

        # 菜单工具按钮
        tool_button_menu = QToolButton(self)
        tool_button_menu.setText("工具按钮-菜单")
        tool_button_menu.setAutoRaise(True)
        layout.addWidget(tool_button_menu)

        # 以下是为tool_button_menu添加menu信息。
        menu = QMenu(tool_button_menu)
        new_action = QAction("新建",menu)
        new_action.setData('NewAction')
        menu.addAction(new_action)
        open_action = QAction("打开",menu)
        open_action.setData('OpenAction')
        menu.addAction(open_action)
        menu.addSeparator()
        #    添加子菜单
        sub_menu = QMenu(menu)
        sub_menu.setTitle("子菜单")
        recent_action = QAction("最近打开",sub_menu)
        recent_action.setData('RecentAction')
        sub_menu.addAction(recent_action)
        menu.addMenu(sub_menu)
        tool_button_menu.setMenu(menu)
        tool_button_menu.setPopupMode(QToolButton.InstantPopup)

        # 工具按钮，嵌入到toolbar
        toobar = self.addToolBar("File")
        #   添加工具按钮1
        tool_button_bar1 = QToolButton(self)
        tool_button_bar1.setText("工具按钮-toobar1")
        toobar.addWidget(tool_button_bar1)
        #   添加工具按钮2
        tool_button_bar2 = QToolButton(self)
        tool_button_bar2.setText("工具按钮-toobar2")
        tool_button_bar2.setIcon(QIcon("./images/close.ico"))
        tool_button_arrow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toobar.addWidget(tool_button_bar2)
        #    添加其他QAction按钮
        new = QAction(QIcon("./images/new.png"), "new", self)
        toobar.addAction(new)
        open = QAction(QIcon("./images/open.png"), "open", self)
        toobar.addAction(open)


        # 槽函数
        tool_button.clicked.connect(lambda: self.button_click(tool_button))
        tool_button_AutoRaise.clicked.connect(lambda: self.button_click(tool_button_AutoRaise))
        tool_button_pic.clicked.connect(lambda: self.button_click(tool_button_pic))
        tool_button_arrow.clicked.connect(lambda: self.button_click(tool_button_arrow))
        tool_button_bar1.clicked.connect(lambda: self.button_click(tool_button_bar1))
        tool_button_bar2.clicked.connect(lambda: self.button_click(tool_button_bar2))
        tool_button_menu.triggered.connect(self.action_call)


    def button_click(self, button):
        self.label_show.setText('你按下了: '+button.text())

    def action_call(self, action):
        self.label_show.setText('触发了菜单action: '+action.data())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolButtonDemo()
    demo.show()
    sys.exit(app.exec())
