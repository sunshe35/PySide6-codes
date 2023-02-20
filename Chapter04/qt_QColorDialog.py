# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QColorDialog 例子
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class ColorDlg(QDialog):

    def __init__(self, parent=None):
        super(ColorDlg, self).__init__(parent)
        self.setWindowTitle('QColorDialog案例')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.colorLabel = QLabel('显示颜色效果')
        layout.addWidget(self.colorLabel)

        colorButton = QPushButton("QColorDialog.get&Color()")
        colorButton.clicked.connect(self.setColor)
        layout.addWidget(colorButton)

        # 颜色选项
        self.colorDialogOptionsWidget = DialogOptionsWidget()
        self.colorDialogOptionsWidget.addCheckBox("使用Qt对话框(非系统)", QColorDialog.DontUseNativeDialog)
        self.colorDialogOptionsWidget.addCheckBox("显示透明度alpha", QColorDialog.ShowAlphaChannel)
        self.colorDialogOptionsWidget.addCheckBox("不显示buttons", QColorDialog.NoButtons)
        layout.addWidget(self.colorDialogOptionsWidget)

        # 自定义颜色设置
        layout.addSpacerItem(QSpacerItem(100, 20))
        self.label2 = QLabel('设置自定义颜色')
        layout.addWidget(self.label2)
        self.combobox = QComboBox(self, minimumWidth=100)
        item_list = ['#ffffff', '#ffff00', '#ff0751', '#52aeff']
        index_list = [2, 3, 4, 5]
        for i in range(len(item_list)):
            self.combobox.addItem(item_list[i], index_list[i])
        self.combobox.activated.connect(lambda: self.on_activate(self.combobox))
        layout.addWidget(self.combobox)

    def setColor(self):
        options = self.colorDialogOptionsWidget.value()
        if options:
            color = QColorDialog.getColor(Qt.green, self, "Select Color", options)
        else:
            color = QColorDialog.getColor(Qt.green, self, "Select Color")
        if color.isValid():
            self.colorLabel.setText(color.name())
            self.colorLabel.setPalette(QPalette(color))
            self.colorLabel.setAutoFillBackground(True)

    def on_activate(self, combobox):
        color = QColor(combobox.currentText())
        index = combobox.currentData()
        QColorDialog.setCustomColor(index, color)
        self.label2.setText('QColorDialog在位置{} 已经添加自定义颜色{}'.format(index, combobox.currentText()))
        self.label2.setPalette(QPalette(color))
        self.label2.setAutoFillBackground(True)


class DialogOptionsWidget(QWidget):

    def __init__(self, parent=None):
        super(DialogOptionsWidget, self).__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.checkBoxList = []

    def addCheckBox(self, text, value):
        checkBox = QCheckBox(text)
        self.layout.addWidget(checkBox)
        self.checkBoxList.append((checkBox, value))

    def value(self):
        result = 0
        for checkBox_tuple in self.checkBoxList:
            if checkBox_tuple[0].isChecked():
                result = result|checkBox_tuple[1]
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ColorDlg()
    form.show()
    app.exec()
