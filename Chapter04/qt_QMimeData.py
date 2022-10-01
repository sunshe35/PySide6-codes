# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QMimeData 例子，结合QDrag举例说明。


'''
import sys
from PySide6.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication, QLabel, QVBoxLayout)
from PySide6.QtCore import QByteArray,QMimeData



class ButtonQMime(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class ButtonMyQMime(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
        self.mime = QMimeData()
        qb = QByteArray(bytes('abcd1234', encoding='utf8'))
        self.mime.setData('my_mimetype',qb)

    def dragEnterEvent(self, e):
        if self.mime.hasFormat('my_mimetype'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText('自定义format结果为：'+self.mime.data('my_mimetype').data().decode('utf8'))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        layout =QVBoxLayout()
        self.setLayout(layout)
        # layout.addWidget(QLabel(''))
        self.label = QLabel('拖拽到窗口显示拖拽format信息',self)
        layout.addWidget(self.label)

        edit = QLineEdit("我可以被拖拽，你可以用我拖拽，也可以拖拽文件到窗口", self)
        edit.setMinimumWidth(350)
        edit.setDragEnabled(True)
        layout.addWidget(edit)

        button = ButtonQMime('拖拽到此按钮，修改按钮text',self)
        layout.addWidget(button)

        button2 = ButtonMyQMime("拖拽到此按钮，显示自定义format", self)
        layout.addWidget(button2)

        self.setWindowTitle("QMimeData案例：通过拖拽传输数据")
        self.setGeometry(300, 300, 300, 150)
        self.show()


    def dragEnterEvent(self, e):
        _str = ''
        mime = e.mimeData()

        # 识别拖拽的文件
        if mime.hasUrls():
            path_list = e.mimeData().urls()
            _str = '\n'.join(a.path() for a in path_list)
            _str = '拖拽的文件路径为：\n' + _str + '\n\n'

        # 识别拖拽的文字
        if mime.hasText():
            _str = _str + '拖拽的文字内容为：\n' + mime.text() + '\n\n'

        format_list = mime.formats()
        self.label.setText(_str + '拖拽的formats为：\n'+'\n'.join(format_list))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())