# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QComboBox 例子
'''
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from functools import partial
import os
os.chdir(os.path.dirname(__file__))


item_list = ["C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go", "Ruby", "Lua", "PHP"]

data_list = [1972, 1983, 1995, 1991, 1992, 2000, 2014, 2009, 1995, 1993, 1995]



class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox案例")

        layout = QFormLayout(self)

        self.label = QLabel('显示数据信息')
        layout.addWidget(self.label)
        icon = QIcon("./images/python.png")  # 显示图标

        # 增加单项，不带数据
        self.combobox_addOne = QComboBox(self, minimumWidth=200)
        for i in range(len(item_list)):
            self.combobox_addOne.addItem(icon, item_list[i])
        self.combobox_addOne.setCurrentIndex(-1)
        layout.addRow(QLabel("增加单项，不带数据"), self.combobox_addOne)

        # 增加单项，附带数据
        self.combobox_addData = QComboBox(self, minimumWidth=200)
        for i in range(len(item_list)):
            self.combobox_addData.addItem(icon, item_list[i], data_list[i])
        self.combobox_addData.setCurrentIndex(-1)
        layout.addRow(QLabel("增加单项，附带数据"), self.combobox_addData)

        #  增加多项，不带数据
        self.combobox_addMore = QComboBox(self, minimumWidth=200)
        layout.addRow(QLabel("增加多项，不带数据"), self.combobox_addMore)
        self.combobox_addMore.addItems(item_list)
        self.combobox_addMore.setCurrentIndex(-1)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 允许修改1
        self.combobox_edit = QComboBox(self, minimumWidth=200)
        self.combobox_edit.setEditable(True)
        for i in range(len(item_list)):
            self.combobox_edit.addItem(icon, item_list[i])
        self.combobox_edit.setInsertPolicy(self.combobox_edit.InsertAfterCurrent)
        self.combobox_edit.setCurrentIndex(-1)
        layout.addRow(QLabel("允许修改1:默认"), self.combobox_edit)

        # 允许修改2
        self.combobox_edit2 = QComboBox(self, minimumWidth=200)
        self.combobox_edit2.setEditable(True)
        self.combobox_edit2.addItems(['1', '2', '3'])
        #       整数验证器
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)
        self.combobox_edit2.setValidator(pIntValidator)
        layout.addRow(QLabel("允许修改2:验证器"), self.combobox_edit2)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 删除项目
        layout_child = QHBoxLayout()
        self.button1 = QPushButton('删除项目')
        self.button2 = QPushButton('删除显示')
        self.button3 = QPushButton('删除所有')
        self.combobox_del = QComboBox(minimumWidth=200)
        self.combobox_del.setEditable(True)
        self.combobox_del.addItems(item_list)
        layout_child.addWidget(self.button1)
        layout_child.addWidget(self.button2)
        layout_child.addWidget(self.button3)
        layout_child.addWidget(self.combobox_del)
        self.button1.clicked.connect(lambda: self.combobox_del.removeItem(self.combobox_del.currentIndex()))
        self.button2.clicked.connect(lambda: self.combobox_del.clearEditText())
        self.button3.clicked.connect(lambda: self.combobox_del.clear())
        layout.addRow(layout_child)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # 模型接管，不带数据
        self.combobox_model = QComboBox(self, minimumWidth=200)
        self.tablemodel = QStringListModel(item_list)
        self.combobox_model.setModel(self.tablemodel)
        self.combobox_model.setCurrentIndex(-1)
        layout.addRow(QLabel("模型接管，不带数据"), self.combobox_model)

        # 信号与槽
        self.combobox_addOne.activated.connect(lambda x: self.on_activate(x, self.combobox_addOne))
        self.combobox_addData.activated.connect(partial(self.on_activate, *args, combobox=self.combobox_addData))
        self.combobox_addMore.highlighted.connect(lambda x: self.on_activate(x, self.combobox_addMore))
        self.combobox_model.activated.connect(lambda x: self.on_activate(x, self.combobox_model))
        self.combobox_edit.activated.connect(lambda x: self.on_activate(x, self.combobox_edit))
        self.combobox_edit2.currentIndexChanged.connect(lambda x: self.on_activate(x, self.combobox_edit2))
        self.combobox_del.activated.connect(lambda x: self.on_activate(x, self.combobox_del))

    def on_activate(self, index, combobox=None):
        _str = ' 信号index: {};\n currentIndex: {};\n 信号index==currentIndex: {};\n count: {};\n currentText: {};\n currentData: {};\n itemData: {};\n itemText: {};\n'.format(
            index, combobox.currentIndex(), index == combobox.currentIndex(), combobox.count(), combobox.currentText(),
            combobox.currentData(), combobox.itemData(index),combobox.itemText(index))
        self.label.setText(_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())
