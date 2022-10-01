# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 信号与槽 例子，说明参数传递的使用方法
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal,Slot,QMetaObject
from PySide6.QtGui import *
import time
from functools import partial

class SignalSlotDemo(QWidget):
    signal1 = Signal()
    signal2 = Signal(str)
    signal3 = Signal(str,int,list,dict)
    signal4 = Signal(str,int,list,dict)


    def __init__(self, *args, **kwargs):
        super(SignalSlotDemo, self).__init__(*args, **kwargs)
        self.setWindowTitle('信号与槽案例2-参数传递')
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel('用来显示信息', self)
        layout.addWidget(self.label)

        self.button1 = QPushButton("1-内置信号+默认参数", self)
        self.button1.setCheckable(True)
        layout.addWidget(self.button1)
        self.button1.clicked[bool].connect(self.button1Click)

        button2 = QPushButton("2-自定义信号+默认参数", self)
        button2.setCheckable(True)
        self.signal2[str].connect(self.button2Click)
        layout.addWidget(button2)
        button2.clicked.connect(lambda: self.signal2.emit('我是参数'))


        self.button3 = QPushButton("3-内置信号+自定义参数lambda", self)
        self.button3.setCheckable(True)
        layout.addWidget(self.button3)
        self.button3.clicked[bool].connect(lambda bool1:self.button3Click(bool1,button=self.button3,a=5,b='botton3'))

        self.button4 = QPushButton("4-内置信号+自定义参数partial", self)
        self.button4.setCheckable(True)
        layout.addWidget(self.button4)
        self.button4.clicked[bool].connect(partial(self.button4Click,*args,button=self.button4,a=7,b='button4'))

        self.button5 = QPushButton("5-自定义信号+自定义参数lambda", self)
        self.signal3[str,int,list,dict].connect(lambda a1,a2,a3,a4:self.button5Click(a1,a2,a3,a4,button=self.button5,a=7,b='button5'))
        layout.addWidget(self.button5)
        self.button5.clicked.connect(lambda: self.signal3.emit('参数1',2,[1,2,3,4],{'a':1,'b':2}))

        self.button6 = QPushButton("6-自定义信号+自定义参数partial", self)
        self.signal4[str,int,list,dict].connect(partial(self.button6Click,*args,button=self.button6,a=7,b='button6'))
        layout.addWidget(self.button6)
        self.button6.clicked.connect(lambda: self.signal4.emit('参数1',2,[1,2,3,4],{'a':1,'b':2}))

    def button1Click(self,bool1):
        if bool1 == True:
            self.label.setText("time:%s,触发了'1-内置信号+默认参数'，传递一个信号的默认参数:%s',表示该按钮被按下"%(time.strftime('%H:%M:%S'),bool1))
        else:
            self.label.setText("time:%s,触发了'1-内置信号+默认参数'，传递一个信号的默认参数:%s',表示该按钮没有被按下"%(time.strftime('%H:%M:%S'),bool1))



    def button2Click(self,_str):
        self.label.setText("time:%s,触发了'2-自定义信号+默认参数'，传递一个信号的默认参数:%s'"%(time.strftime('%H:%M:%S'),_str))


    def button3Click(self,bool1,button,a,b):
        if bool1 == True:
            _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递一个信号的默认参数:{bool1}',表示该按钮被按下。\n三个自定义参数button='{button}',a={a},b='{b}'"
        else:
            _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递一个信号的默认参数:{bool1}',表示该按钮没有被按下。\n三个自定义参数button='{button}',a={a},b='{b}'"
        self.label.setText(_str)


    def button4Click(self,bool1,button,a,b):
        if bool1 == True:
            _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递一个信号的默认参数:{bool1}',表示该按钮被按下。\n三个自定义参数button='{button}',a={a},b='{b}'"
        else:
            _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递一个信号的默认参数:{bool1}',表示该按钮没有被按下。\n三个自定义参数button='{button}',a={a},b='{b}'"
        self.label.setText(_str)

    def button5Click(self,*args,button,a,b):
        _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递信号的默认参数:{args}',\n三个自定义参数button='{button}',a={a},b='{b}'"
        # print(args,button,a,b)
        self.label.setText(_str)

    def button6Click(self,*args,button,a,b):
        _str = f"time:{time.strftime('%H:%M:%S')},触发了'{button.text()}'，传递信号的默认参数:{args}',\n三个自定义参数button='{button}',a={a},b='{b}'"
        # print(args,button,a,b)
        self.label.setText(_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SignalSlotDemo()
    demo.show()
    app.exec()
