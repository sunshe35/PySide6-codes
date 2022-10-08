# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QToolBar 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class ToolBarDemo(QMainWindow):

    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle("toolbar 例子")
        self.resize(500, 300)
        self.label = QLabel('显示信息',self)
        self.label.setMinimumWidth(200)
        self.label.move(100,200)

        # 工具按钮组1,top1_1
        toolbar1 = self.addToolBar("toolbar1")
        new = QAction(QIcon("./images/new.png"), "new1", self)
        toolbar1.addAction(new)
        open = QAction(QIcon("./images/open.png"), "open1", self)
        open.setShortcut('Ctrl+O')
        toolbar1.addAction(open)
        save = QAction(QIcon("./images/save.png"), "save1", self)
        toolbar1.addAction(save)
        toolbar1.actionTriggered[QAction].connect(self.toolbar_pressed)


        # 工具按钮组2,top1_2
        toolbar2 = QToolBar('toolbar2')
        toolbar2.addAction(QAction(QIcon("./images/cartoon1.ico"), "cartoon2", self))
        toolbar2.addAction(QAction(QIcon("./images/printer.png"), "print2", self))
        toolbar2.addAction(QAction(QIcon("./images/python.png"), "python2", self))
        toolbar1.addSeparator()
        spinbox = QSpinBox()
        toolbar2.addWidget(spinbox)
        toolbar2.actionTriggered[QAction].connect(self.toolbar_pressed)
        spinbox.valueChanged.connect(lambda: self.label.setText("触发了:spinbox,当前值："+str(spinbox.value())))
        self.addToolBar(toolbar2)


        # 工具按钮组3,top2
        toolbar3 = self.addToolBar("toolbar3")
        toolbar3.addAction(QAction(QIcon("./images/new.png"), "new3", self))
        toolbar3.addAction(QAction(QIcon("./images/open.png"), "open3", self))
        toolbar3.addAction(QAction(QIcon("./images/save.png"), "save3", self))
        toolbar3.actionTriggered[QAction].connect(self.toolbar_pressed)
        self.insertToolBarBreak(toolbar3)

        # 工具按钮组4,left
        toolbar4 = QToolBar('toolbar4')
        #   添加工具按钮1
        tool_button_bar1 = QToolButton(self)
        tool_button_bar1.setText("工具按钮-toobar1")
        toolbar4.addWidget(tool_button_bar1)
        #   添加工具按钮2
        tool_button_bar2 = QToolButton(self)
        tool_button_bar2.setText("工具按钮-toobar2")
        tool_button_bar2.setIcon(QIcon("./images/close.ico"))
        toolbar4.addWidget(tool_button_bar2)
        toolbar4.addSeparator()
        #    添加其他QAction按钮
        new = QAction(QIcon("./images/new.png"), "new4", self)
        toolbar4.addAction(new)
        open = QAction(QIcon("./images/open.png"), "open4", self)
        toolbar4.addAction(open)
        toolbar4.actionTriggered[QAction].connect(self.toolbar_pressed)
        tool_button_bar1.clicked.connect(lambda :self.toolbar_pressed(tool_button_bar1))
        tool_button_bar2.clicked.connect(lambda :self.toolbar_pressed(tool_button_bar2))

        self.addToolBar(Qt.LeftToolBarArea, toolbar4)

        self.popup = self.createPopupMenu()


    def createPopupMenu(self):
        menu = QMenu(self)
        new = QAction("New", menu)
        new.setData('NewAction')
        new.setShortcut('Ctrl+N')
        menu.addAction(new)

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        menu.addAction(save)

        menu.triggered[QAction].connect(self.toolbar_pressed)
        return menu

    def toolbar_pressed(self, a):
        self.label.setText('触发了按钮:'+a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolBarDemo()
    demo.show()
    sys.exit(app.exec())
