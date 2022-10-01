# -*- coding: utf-8 -*- 
'''
    【简介】
    PySide6中 QTimer例子
 
  
'''

from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel, QCheckBox, \
    QMessageBox
from PySide6.QtCore import QTimer, QDateTime, Qt
import sys


class WinForm(QWidget):

    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("QTimer demo")
        self.listFile = QListWidget()
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        self.autoButon = QPushButton('延迟计时')
        layout = QGridLayout(self)

        # 初始化定时器
        self.timer = QTimer(self)
        self.timer2 = QTimer()
        self.timer2.setSingleShot(True)

        # showTime()方法
        self.timer.timeout.connect(self.showTime)

        self.checkBox = QCheckBox("单次计时")
        self.checkBox.stateChanged.connect(self.timer.setSingleShot)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        layout.addWidget(self.checkBox, 1, 2)
        layout.addWidget(self.autoButon, 2, 0, 1, 2)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.autoButon.clicked.connect(self.laterTimer)

        self.setLayout(layout)

    def showTime(self):
        # 获取系统现在的时间
        time = QDateTime.currentDateTime()
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 在标签上显示时间
        self.label.setText(timeDisplay)

    def startTimer(self):
        # 设置计时间隔并启动
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

    def laterTimer(self):
        self.label.setText("<font color=red size=12><b>延迟任务会在5秒后启动！</b></font>")
        self.timer2.singleShot(5000, lambda: QMessageBox.information(self, '延迟任务标题', '执行延迟任务'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec())
