# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QLineEdit基本方法
  
'''

from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout,QPushButton,QLabel
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        flo = QFormLayout()

        # 正常文本框,对齐，tooltip
        lineEdit_normal = QLineEdit()
        lineEdit_normal.setText("122")
        lineEdit_normal.setAlignment(Qt.AlignCenter)
        lineEdit_normal.setToolTip('这是一个普通文本框')
        flo.addRow("普通文本框，居中", lineEdit_normal)

        # 显示颜色
        lineEdit_color = QLineEdit()
        lineEdit_color.setText("显示红色背景白色字体")
        lineEdit_color.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Base, Qt.red)
        palette.setColor(QPalette.Text, Qt.white)
        lineEdit_color.setPalette(palette)
        lineEdit_color.setAlignment(Qt.AlignLeft)
        flo.addRow("显示颜色，左对齐", lineEdit_color)

        # 占位提示符，限制长度
        lineEdit_maxLength = QLineEdit()
        lineEdit_maxLength.setMaxLength(5)
        # lineEdit_maxLength.setText("122")
        lineEdit_maxLength.setPlaceholderText("最多输入5个字符")
        flo.addRow("最大输入5个字符", lineEdit_maxLength)

        # 只读文本
        lineEdit_readOnly = QLineEdit()
        lineEdit_readOnly.setReadOnly(True)
        lineEdit_readOnly.setText("只读文本，不能编辑")
        flo.addRow("只读文本", lineEdit_readOnly)

        # 移动光标
        lineEdit_cursor = QLineEdit()
        self.lineEdit_cursor = lineEdit_cursor
        lineEdit_cursor.setText("点击左边按钮向右移动光标")
        self.lineEdit_cursor.setFocus()
        lineEdit_cursor.setCursorPosition(1)
        button = QPushButton("点我右移光标")
        button.clicked.connect(self.move_cursor)
        flo.addRow(button, lineEdit_cursor)

        # 编辑文本
        lineEdit_edit = QLineEdit()
        lineEdit_edit.setText("编辑文本")
        button2 = QPushButton("删除文本")
        button2.clicked.connect(lambda: lineEdit_edit.clear())
        flo.addRow(button2, lineEdit_edit)

        # 槽函数
        lineEdit_change = QLineEdit()
        lineEdit_change.setPlaceholderText("输入文本框会改变左侧标签")
        lineEdit_change.setFixedWidth(200)
        label = QLabel("槽函数应用")
        lineEdit_change.textChanged.connect(lambda: label.setText('更新标签：'+lineEdit_change.text()))
        flo.addRow(label, lineEdit_change)

        self.setLayout(flo)

    def move_cursor(self):
        # 移动光标
        self.lineEdit_cursor.cursorForward(True,2)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec())
