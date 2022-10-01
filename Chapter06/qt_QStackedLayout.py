# -*- coding: utf-8 -*-


import sys
from PySide6.QtWidgets import *


class StackedLayoutDemo(QWidget):
    def __init__(self, parent=None):
        super(StackedLayoutDemo, self).__init__(parent)
        self.setWindowTitle("QStackedLayout布局管理例子")
        self.resize(400, 100)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加页面导航
        pageComboBox = QComboBox()
        pageComboBox.addItem("Page 1")
        pageComboBox.addItem("Page 2")
        pageComboBox.addItem("Page 3")
        layout.addWidget(pageComboBox)

        # 添加QStackedLayout
        stackedLayout = QStackedLayout()
        layout.addLayout(stackedLayout)

        # 添加页面1-3
        pageWidget1 = QWidget()
        layout1 = QHBoxLayout()
        pageWidget1.setLayout(layout1)
        stackedLayout.addWidget(pageWidget1)
        pageWidget2 = QWidget()
        layout2 = QVBoxLayout()
        pageWidget2.setLayout(layout2)
        stackedLayout.addWidget(pageWidget2)
        pageWidget3 = QWidget()
        layout3 = QFormLayout()
        pageWidget3.setLayout(layout3)
        stackedLayout.addWidget(pageWidget3)

        # 设置页面1-3
        for i in range(5):
            layout1.addWidget(QPushButton('button%d' % i))
            layout2.addWidget(QPushButton('button%d' % i))
            layout3.addRow('row%d' % i, QPushButton('button%d' % i))

        # 导航与页面链接
        pageComboBox.activated.connect(stackedLayout.setCurrentIndex)

        # 添加按钮切换导航页1-3
        buttonLayout = QHBoxLayout()
        layout.addLayout(buttonLayout)
        button1 = QPushButton('页面1')
        button2 = QPushButton('页面2')
        button3 = QPushButton('页面3')
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        button1.clicked.connect(lambda: stackedLayout.setCurrentIndex(0))
        button2.clicked.connect(lambda: stackedLayout.setCurrentWidget(pageWidget2))
        button3.clicked.connect(lambda: stackedLayout.setCurrentIndex(2))

        label = QLabel('显示信息')
        layout.addWidget(label)
        stackedLayout.currentChanged.connect(lambda x: label.setText('切换到页面%d' % (x + 1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StackedLayoutDemo()
    form.show()
    sys.exit(app.exec())
