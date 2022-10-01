# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 信号与槽 例子
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal,Slot,QMetaObject,QThread, QDateTime
from PySide6.QtGui import *
import time



class SignalSlotDemo(QWidget):
    signal1 = Signal()
    signal2 = Signal(str)

    def __init__(self, *args, **kwargs):
        super(SignalSlotDemo, self).__init__(*args, **kwargs)
        self.setWindowTitle('信号与槽案例')
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.checkBox = QCheckBox('显示点击状态')
        layout.addWidget(self.checkBox)

        self.label = QLabel('用来显示信息', self)
        layout.addWidget(self.label)

        button1 = QPushButton("1-内置信号+内置槽", self)
        layout.addWidget(button1)
        button1.clicked.connect(self.checkBox.toggle)

        self.button2 = QPushButton("2-内置信号+自定义槽", self)
        layout.addWidget(self.button2)
        self.connect1 = self.button2.clicked.connect(self.button2Click)

        button3 = QPushButton("3-自定义信号+内置槽", self)
        self.signal1.connect(self.checkBox.toggle)
        layout.addWidget(button3)
        button3.clicked.connect(lambda: self.signal1.emit())

        button4 = QPushButton("4-自定义信号+自定义槽", self)
        self.signal2[str].connect(self.button4Click)
        layout.addWidget(button4)
        button4.clicked.connect(lambda: self.signal2.emit('我是参数'))

        button5 = QPushButton("5-断开连接'2-内置信号+自定义槽'", self)
        layout.addWidget(button5)
        button5.clicked.connect(self.button5Click)


        button6 = QPushButton("6-恢复连接'2-内置信号+自定义槽'", self)
        layout.addWidget(button6)
        button6.clicked.connect(self.button6Click)

        self.button7 = QPushButton("7-装饰器信号与槽", self)
        self.button7.setObjectName("button7Slot")
        layout.addWidget(self.button7)
        QMetaObject.connectSlotsByName(self)

        self.button8 = QPushButton("8-多线程信号与槽", self)
        layout.addWidget(self.button8)
        self.button8.clicked.connect(self.button8Click)



    def button2Click(self):
        self.checkBox.toggle()
        sender = self.sender()
        self.label.setText('time:%s,触发了 %s'% (time.strftime('%H:%M:%S'),sender.text()))

    def button4Click(self, _str):
        self.checkBox.toggle()
        self.label.setText('time:%s,触发了 4-内置信号+自定义槽,并传递了一个参数：“%s”' %(time.strftime('%H:%M:%S'),_str))

    def button5Click(self):
        try:
            self.button2.clicked.disconnect()
            # self.button2.disconnect(self.connect1)
            # self.button2.clicked.disconnect(self.button2Click)
            self.label.setText("time:%s,断开连接：'2-内置信号+自定义槽'" % time.strftime('%H:%M:%S'))
        except:
            self.label.setText("time:%s,'2-内置信号+自定义槽'已经断开连接，不用重复断开" % time.strftime('%H:%M:%S'))

    def button6Click(self):
        if self.isSignalConnect_(self.button2,'clicked()'):
            self.button2.clicked.disconnect(self.button2Click)
        # try:
        #     self.button2.clicked.disconnect(self.button2Click)
        # except:
        #     pass
        self.button2.clicked.connect(self.button2Click)
        self.label.setText("time:%s,重新连接了：'2-内置信号+自定义槽'"%time.strftime('%H:%M:%S'))



    @Slot()
    def on_button7Slot_clicked(self):
        self.checkBox.toggle()
        self.label.setText('time:%s,触发了 7-装饰器信号与槽' %time.strftime('%H:%M:%S'))


    def button8Click(self):
        self.checkBox.toggle()
        if hasattr(self,'backend'):
            self.label.setText(f"time:{time.strftime('%H:%M:%S')},已经开启线程，不用重复开启")
        else:
            # 创建线程
            self.backend = BackendThread()
            # 连接信号
            self.backend.update_date.connect(self.display_time)
            # 开始线程
            self.backend.start()

    def display_time(self,tim):
        self.button8.setText(f'8-多线程,time：{tim}')


    def isSignalConnect_(self, obj, name):
        """判断信号是否连接
        :param obj:        对象
        :param name:       信号名，如 clicked()
        """
        index = obj.metaObject().indexOfMethod(name)
        if index > -1:
            method = obj.metaObject().method(index)
            if method:
                return obj.isSignalConnected(method)
        return False


class BackendThread(QThread):
    # 通过类成员对象定义信号对象
    update_date = Signal(str)

    # 处理要做的业务逻辑
    def run(self):
        while True:
            self.update_date.emit(time.strftime('%H:%M:%S'))
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SignalSlotDemo()
    demo.show()
    app.exec()
