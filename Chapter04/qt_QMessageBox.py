# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QMessage 例子
   
  
'''
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class WinForm(QMainWindow):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("QMessage 例子")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel('显示消息框信息')
        layout.addWidget(self.label)

        button1 = QPushButton()
        button1.setText("普通消息框")
        layout.addWidget(button1)
        button1.clicked.connect(self.showMessageBox1)

        button2 = QPushButton()
        button2.setText("自定义消息框")
        layout.addWidget(button2)
        button2.clicked.connect(self.showMessageBox2)

        button3 = QPushButton()
        button3.setText("信号与槽")
        layout.addWidget(button3)
        button3.clicked.connect(self.showMessageBox3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def showMessageBox1(self):
        reply = QMessageBox.information(self, "标题", "对话框消息正文",
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok | QMessageBox.Apply,
                                        QMessageBox.Yes)
        self.label.setText('返回%s' % reply)

    def showMessageBox2(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('自定义消息框-标题')
        msgBox.setText("自定义消息框-内容")
        msgBox.setInformativeText("自定义消息框-informationText")
        msgBox.setDetailedText("显示详细文本信息，用来显示更多的文本信息")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setIcon(QMessageBox.Information)

        # 自定义按钮
        button1 = QPushButton('MyOk')
        msgBox.addButton(button1, QMessageBox.ApplyRole)

        reply = msgBox.exec()
        self.label.setText('返回:%s' % reply)
        if msgBox.clickedButton() == button1:
            self.label.setText(self.label.text() + ' 你点击了自定义按钮:' + button1.text())


    def showMessageBox3(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('信号与槽-Title')
        msgBox.setText("点击相应按钮，会触发对应信号")
        msgBox.setStandardButtons(QMessageBox.Ok |QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel| QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setIcon(QMessageBox.Information)

        # 自定义按钮
        button1 = QPushButton('MyOk-ApplyRole')
        msgBox.addButton(button1 , QMessageBox.ApplyRole)
        button2 = QPushButton('MyOk-AcceptRole')
        msgBox.addButton(button2, QMessageBox.AcceptRole)

        # 信号与槽
        msgBox.accepted.connect(lambda: self.statusBar().showMessage('触发了accepted信号',1000))
        msgBox.rejected.connect(lambda: self.statusBar().showMessage('触发了rejected信号',1000))

        reply = msgBox.exec()
        self.label.setText('返回:%s' % reply)
        if msgBox.clickedButton() in [button1,button2]:
            self.label.setText(self.label.text() + ' 你点击了自定义按钮:' + msgBox.clickedButton().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WinForm()
    demo.show()
    sys.exit(app.exec())
