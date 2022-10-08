# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QStatusBar 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import time
import os
os.chdir(os.path.dirname(__file__))

class StatusDemo(QMainWindow):
    def __init__(self, parent=None):
        super(StatusDemo, self).__init__(parent)
        self.resize(300,200)

        bar = self.menuBar()
        file = bar.addMenu("File")
        new = QAction(QIcon("./images/new.png"), "new", self)
        new.setStatusTip('select menu: new')
        open_ = QAction(QIcon("./images/open.png"), "open", self)
        open_.setStatusTip('select menu: open')
        save = QAction(QIcon("./images/save.png"), "save", self)
        save.setStatusTip('select menu: save')
        file.addActions([new,open_,save])
        file.triggered[QAction].connect(self.processTrigger)
        self.init_statusBar()

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.label.setText(time.strftime("%Y-%m-%d %a %H:%M:%S")))
        self.timer.start(1000)

    def init_statusBar(self):
        self.status_bar = QStatusBar()
        self.status_bar2 = QStatusBar()
        self.status_bar2.setMinimumWidth(150)
        self.label = QLabel('显示永久信息：时间')
        self.button = QPushButton('清除时间')

        self.status_bar.addWidget(self.status_bar2)
        self.status_bar.addWidget(self.label)
        self.status_bar.addWidget(self.button)

        self.setWindowTitle("QStatusBar 例子")
        self.setStatusBar(self.status_bar)
        self.button.clicked.connect(lambda :self.status_bar.removeWidget(self.label))



    def processTrigger(self, q):
        self.status_bar2.showMessage('点击了menu: '+q.text(), 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StatusDemo()
    demo.show()
    sys.exit(app.exec())
