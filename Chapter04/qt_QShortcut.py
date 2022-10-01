# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QShortcut和QKeySequence案例。
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class QShortcutDemo(QMainWindow):
    def __init__(self, parent=None):
        super(QShortcutDemo, self).__init__(parent)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)
        _label = QLabel('既可以触发菜单快捷键，也可以通过Ctrl+E触发自定义快捷键')
        self.label = QLabel('显示信息')
        layout.addWidget(_label)
        layout.addWidget(self.label)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        #  快捷键1
        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        # 快捷键2
        copy = QAction('Copy',self)
        copy.setShortcuts(QKeySequence.Copy)
        file.addAction(copy)

        # 快捷键3
        paste = QAction('Paste',self)
        # paste.setShortcuts(Qt.CTRL|Qt.Key_P)
        paste.setShortcut(QKeySequence(Qt.CTRL|Qt.Key_P))
        # paste.setShortcuts(QKeySequence(Qt.CTRL|Qt.Key_P))
        file.addAction(paste)

        quit = QAction("Quit", self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.action_trigger)

        # 自定义快捷键
        custom_shortcut = QShortcut(QKeySequence("Ctrl+E"), self)
        custom_shortcut.activated.connect(lambda :self.customShortcut(custom_shortcut))

        self.setWindowTitle("QShortcut 例子")
        self.resize(450, 200)

    def customShortcut(self,key):
        self.label.setText('触发自定义快捷键:%s'%key.keys())

    def action_trigger(self, q):
        self.label.setText('触发菜单：%s；快捷键:%s'%(q.text(),q.shortcuts()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QShortcutDemo()
    demo.show()
    sys.exit(app.exec())
