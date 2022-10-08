# -*- coding: utf-8 -*-
"""
    【简介】
	 加载QSS文件
     
"""
import sys
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(477, 258)
        self.setWindowTitle("QssDemo")
        layout = QFormLayout()

        button1 = QPushButton('button1')
        button1.setToolTip('类型选择器，最一般的使用方式')
        layout.addRow('类型选择器',button1)

        buttonProperty = QPushButton('buttonProperty')
        buttonProperty.setProperty('name','btnProperty')
        buttonProperty.setToolTip('属性选择器，根据属性定位')
        layout.addRow('属性选择器',buttonProperty)

        buttonID = QPushButton('buttonID')
        # button1.setMaximumSize(64, 64)
        buttonID.setMinimumSize(64, 64)
        buttonID.setObjectName('btnID')
        buttonID.setToolTip('id选择器，点击会触发伪状态')
        layout.addRow('id选择器+伪状态',buttonID)

        comboBox = QComboBox()
        comboBox.addItems(['张三','李四','王五','赵六'])
        layout.addRow('子控件',comboBox)

        buttonOwn = QPushButton('控件自定义qss')
        buttonOwn.setStyleSheet('''* { 
            border: 2px solid #8f8f91;
            border-radius: 6px;
            background-color: gray;
            color: yellow }''')
        buttonOwn.setToolTip('子控件的Qss会覆盖父控件的设置')
        layout.addRow('控件自定义qss',buttonOwn)

        # 后代选择器
        glayout = QHBoxLayout()
        group = QGroupBox()
        group.setTitle('groupBox')
        group.setLayout(glayout)
        glayout.addWidget(QPushButton('button'))
        glayout.addWidget(QCheckBox('check'))
        checkBox2 = QCheckBox('check2')
        checkBox2.setObjectName('btnID')
        checkBox2.setMinimumSize(40,40)
        glayout.addWidget(checkBox2)
        layout.addRow('后代选择器',group)

        widget =  QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    styleFile = './style.qss'
    with open(styleFile, 'r') as f:
        qssStyle = f.read()
    win.setStyleSheet(qssStyle)
    win.show()

    sys.exit(app.exec())
