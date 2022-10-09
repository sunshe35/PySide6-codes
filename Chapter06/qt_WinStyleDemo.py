# -*- coding: utf-8 -*-

'''
    【简介】
     界面风格例子
    
'''

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
os.chdir(os.path.dirname(__file__))

class WinStyleDemo(QMainWindow):
    def __init__(self, parent=None):
        super(WinStyleDemo, self).__init__(parent)
        self.setWindowTitle("界面风格例子")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.resize(300, 100)

        # Style
        self.styleLabel = QLabel("1、SetStyle:")
        self.styleComboBox = QComboBox()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.styleLabel)
        hlayout.addWidget(self.styleComboBox)
        layout.addLayout(hlayout)

        # 增加 styles 从 QStyleFactory
        self.styleComboBox.addItems(QStyleFactory.keys())
        # 选择当前界面风格
        index = self.styleComboBox.findText(QApplication.style().objectName(), Qt.MatchFixedString)
        # 设置当前界面风格
        self.styleComboBox.setCurrentIndex(index)
        # 通过comboBox选择界面分割
        self.styleComboBox.activated.connect(self.handleStyleChanged)

        # WinFlag
        self.flagLabel = QLabel("2、SetWindowsFlag")
        self.flagList = ["Widget", "Window", "Dialog", "Sheet", "Drawer", "Popup", "Tool", "ToolTip", "SplashScreen",
                         "SubWindow", "ForeignWindow", "CoverWindow"]
        self.flagComboBox = QComboBox()
        self.flagComboBox.addItems(self.flagList)
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.flagLabel)
        hlayout2.addWidget(self.flagComboBox)
        layout.addLayout(hlayout2)
        self.flagComboBox.activated.connect(self.winFlagChanged)

        # WinFlagHint
        self.checkLabel = QLabel('3、SetWinFlagHint')
        self.checkList = ["MSWindowsFixedSizeDialogHint", "FramelessWindowHint", "CustomizeWindowHint",
                          "WindowTitleHint", "WindowSystemMenuHint", "WindowMaximizeButtonHint",
                          "WindowMinimizeButtonHint", "WindowMinMaxButtonsHint", "WindowMaximizeButtonHint",
                          "WindowMinimizeButtonHint", "WindowCloseButtonHint", "WindowContextHelpButtonHint",
                          "WindowStaysOnTopHint", "WindowStaysOnBottomHint"]
        self.checkBoxList = []
        hlayoutCheck = QHBoxLayout()
        self.gridLayout = QGridLayout()
        hlayoutCheck.addWidget(self.checkLabel)
        hlayoutCheck.addLayout(self.gridLayout)
        i = j = 0
        for text in self.checkList:
            _widget = QCheckBox(text, self)
            self.checkBoxList.append(_widget)
            self.gridLayout.addWidget(_widget, i % 5, j)
            i += 1
            if i % 5 == 0:
                j += 1
        layout.addLayout(hlayoutCheck)

        self.buttonUpdateFalg = QPushButton('更新2+3')
        layout.addWidget(self.buttonUpdateFalg)
        self.buttonUpdateFalg.clicked.connect(self.updateWinFlag)

        # 背景颜色
        self.colorLabel = QLabel('4、设置背景色')
        layoutColor = QHBoxLayout()
        layoutColor.addWidget(self.colorLabel)
        self.buttonGroup = QButtonGroup()
        # self.colorButtonList = []
        for text in ['default', 'setStyleSheet', 'setPalette', 'paintEvent']:
            button = QRadioButton(text)
            self.buttonGroup.addButton(button)
            layoutColor.addWidget(button)
            # self.colorButtonList.append(button)
        self.buttonGroup.buttonClicked.connect(self.updateBackColor)

        layout.addLayout(layoutColor)

        # 透明度
        hlayout3 = QHBoxLayout()
        hlayout3.addWidget(QLabel('5、设置透明度'))
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(10, 99)
        self.slider.setSingleStep(5)
        self.slider.setValue(90)
        self.slider.valueChanged.connect(lambda x: self.setWindowOpacity(x / 100))
        hlayout3.addWidget(self.slider)
        layout.addLayout(hlayout3)

        self.setLayout(hlayout)

    def _paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.green)
        # 设置背景颜色，左半屏幕
        painter.drawRect(0, 0, self.width() / 2, self.height())
        # 设置背景图片，右半屏幕
        pixmap = QPixmap("./images/screen1.jpg")
        painter.drawPixmap(self.width() / 2, 0, self.width() / 2, self.height(), pixmap)

    # 改变界面风格
    def handleStyleChanged(self, a: int):
        style = self.styleComboBox.currentText()
        QApplication.setStyle(style)

    def winFlagChanged(self, a: int):
        flag = self.flagComboBox.currentText()
        self.setWindowFlag(getattr(Qt, flag))
        self.show()

    def updateWinFlag(self):
        _text = ''
        flagText = self.flagComboBox.currentText()
        _text += flagText
        flag = getattr(Qt, flagText)
        for checkButton in self.checkBoxList:
            if checkButton.isChecked():
                flag |= getattr(Qt, checkButton.text())
                _text += f'+{checkButton.text()}'
                self.setWindowFlags(flag)

        print('当前flag以及Hint为：', _text)
        self.show()

    def initBackColor(self):
        # 初始化背景设置
        self.setStyle(QMainWindow().style())
        self.setStyleSheet('')
        self.setPalette(QMainWindow().palette())
        self.paintEvent = QMainWindow().paintEvent
        self.update()
        self.show()

    def updateBackColor(self, button: QRadioButton):
        text = button.text()
        self.initBackColor()
        if text == 'setStyleSheet':
            self.setStyleSheet('color: green; background-color: yellow;')
            self.update()
        elif text == 'setPalette':
            # QPalette设置
            palette = QPalette()
            palette.setColor(QPalette.ButtonText, Qt.darkCyan)
            palette.setColor(QPalette.WindowText, Qt.red)
            self.setPalette(palette)
            self.update()
        elif text == 'paintEvent':
            self.paintEvent = self._paintEvent
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = WinStyleDemo()
    demo.show()
    sys.exit(app.exec())
