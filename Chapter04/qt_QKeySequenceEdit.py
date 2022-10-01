'''
QKeySequenceEdit的用法，QKeySequence用法请见qt_QShortcut文件。
'''
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class KeySequenceEdit(QMainWindow):
    def __init__(self, parent=None):
        super(KeySequenceEdit, self).__init__(parent)

        # 基本框架
        label1 = QLabel('菜单save快捷键绑定：')
        self.keyEdit1 = QKeySequenceEdit(self)
        label2 = QLabel('菜单copy快捷键绑定：')
        self.keyEdit2 = QKeySequenceEdit(self)
        layout1 = QHBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(self.keyEdit1)
        layout2 = QHBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(self.keyEdit2)
        self.label_show = QLabel('显示按键信息')
        self.text_show = QTextBrowser()
        self.text_show.setMaximumHeight(60)

        # 信号与槽绑定
        # self.keyEdit1.editingFinished.connect(lambda :print('输入完毕1'))
        # self.keyEdit2.editingFinished.connect(lambda :print('输入完毕2'))
        self.keyEdit1.keySequenceChanged.connect(lambda key:self.save.setShortcut(key))
        self.keyEdit2.keySequenceChanged.connect(lambda key:self.copy.setShortcut(key))
        self.keyEdit1.keySequenceChanged.connect(self.show_key)
        self.keyEdit2.keySequenceChanged.connect(self.show_key)

        # 菜单栏
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        self.save = QAction("Save", self)
        file.addAction(self.save)
        self.copy = QAction('Copy',self)
        file.addAction(self.copy)
        file.triggered[QAction].connect(lambda q:self.statusBar().showMessage('触发菜单：%s；快捷键:%s'%(q.text(),q.shortcuts()),3000))

        # 布局管理
        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addWidget(self.label_show)
        layout.addWidget(self.text_show)
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.resize(300,200)

    def show_key(self,key:QKeySequence):
        self.statusBar().showMessage('更新快捷键'+str(key),2000)
        key1 = self.keyEdit1.keySequence()
        key2 = self.keyEdit2.keySequence()
        _str = f'菜单栏快捷键更新成功；\nsave绑定：{key1}\ncopy绑定：{key2}'
        # self.label_show.setText(_str)
        self.text_show.setText(_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = KeySequenceEdit()
    demo.show()
    sys.exit(app.exec())

