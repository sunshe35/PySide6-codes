# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QProgressDialog(Bar) 例子
'''

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import *

import sys
import time


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog Demo")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.label = QLabel('显示进度条取消信息')
        layout.addWidget(self.label)

        button_modeless = QPushButton('显示无模式进度条，不会阻断其他窗口', self)
        button_modeless.clicked.connect(self.show_modeless)
        layout.addWidget(button_modeless)

        button_model = QPushButton('模式进度条，会阻断其他窗口', self)
        button_model.clicked.connect(self.show_modal)
        layout.addWidget(button_model)

        button_auto = QPushButton('不会自动关闭和重置的进度条', self)
        button_auto.clicked.connect(self.show_auto)
        layout.addWidget(button_auto)

        # 自定义进度条，
        button_custom = QPushButton('自定义QProgressDialog', self)
        button_custom.clicked.connect(self.show_custom)
        layout.addWidget(button_custom)

        # 水平滑块
        self.pd_slider = QProgressDialog("滑块进度条：点击滑块我会动", "Cancel", 10, 100, self)
        self.pd_slider.move(300, 400)
        self.pd_slider.canceled.connect(lambda: self.cancel(self.pd_slider))
        self.slider_horizon = QSlider(Qt.Horizontal)
        self.slider_horizon.setRange(10, 120)
        layout.addWidget(self.slider_horizon)
        self.slider_horizon.valueChanged.connect(lambda: self.valuechange(self.slider_horizon))
        bar = QProgressBar(self)  # QProgressBar
        bar.valueChanged.connect(lambda value: print('自定义Bar的Value值：', value))
        bar.setRange(1, 80)
        self.slider_horizon.valueChanged.connect(lambda value: bar.setValue(value))
        layout.addWidget(bar)
        # self.slider_horizon.valueChanged.connect(self.pd_slider.setValue)

        self.resize(300, 200)

    def show_modeless(self):
        pd_modeless = QProgressDialog("无模式进度条：可以操作父窗口", "Cancel", 0, 12)
        pd_modeless.move(300, 600)

        self.steps = 0

        def perform():
            pd_modeless.setValue(self.steps)
            self.label.setText(
                '当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(pd_modeless.value(), pd_modeless.maximum(),
                                                               pd_modeless.wasCanceled()))

            # // perform one percent of the operation
            self.steps += 1
            if self.steps > pd_modeless.maximum():
                self.timer.stop()

        self.timer = QTimer(self)
        self.timer.timeout.connect(perform)
        self.timer.start(1000)

        pd_modeless.canceled.connect(lambda: self.cancel(pd_modeless))
        pd_modeless.canceled.connect(self.timer.stop)

    def show_modal(self):
        max = 10
        pd_modal = QProgressDialog("模式进度条：不可以操作父窗口", "终止", 0, max, self)
        pd_modal.move(300, 600)
        pd_modal.setWindowModality(Qt.WindowModal)
        # pd_modal.setWindowModality(Qt.ApplicationModal)
        pd_modal.setMinimumDuration(1000)  # 一秒后出现对话框

        # 信号和槽要放在计时器后面，否则不会被执行
        pd_modal.canceled.connect(lambda: self.cancel(pd_modal))

        for i in range(max + 1):
            pd_modal.setValue(i)
            self.label.setText('当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(pd_modal.value(), pd_modal.maximum(),
                                                                              pd_modal.wasCanceled()))
            if pd_modal.value() >= pd_modal.maximum() or pd_modal.wasCanceled():
                break
            # print('you can do something  here')
            time.sleep(1)
            # pd_modal.setValue(max)

    def get_pd_auto(self):
        if not hasattr(self, 'pd_auto'):
            max = 5
            self.pd_auto = QProgressDialog("我不会自动关闭和重置，哈哈", "终止", 0, max, self)
            self.pd_auto.move(300, 600)
            self.pd_auto.setWindowModality(Qt.ApplicationModal)
            self.pd_auto.setMinimumDuration(1000)
            # self.pd_auto.setValue(0)

            self.pd_auto.setAutoClose(False)  # 取消满值自动关闭(默认情况下满值自动重置 )
            self.pd_auto.setAutoReset(False)  # 取消自动重置   (默认情况下满值自动重置 )

            self.pd_auto.canceled.connect(lambda: self.cancel(self.pd_auto))
        return self.pd_auto

    def show_auto(self):
        pd_auto = self.get_pd_auto()

        for i in range(1000):
            if pd_auto.value() >= pd_auto.maximum() or pd_auto.wasCanceled():
                self.label.setText('当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(pd_auto.value(), pd_auto.maximum(),
                                                                                  pd_auto.wasCanceled()))
                break
            pd_auto.setValue(pd_auto.value() + 1)
            self.label.setText('当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(pd_auto.value(), pd_auto.maximum(),
                                                                              pd_auto.wasCanceled()))
            # print('you can do something  here')
            time.sleep(1)
            # pd_auto.setValue(max)

    def show_custom(self):

        pd_custom = QProgressDialog(self)
        bar = QProgressBar()
        bar.setMaximum(9)
        bar.setMinimum(2)
        bar.valueChanged.connect(lambda value: print('自定义Bar的Value值：', value))
        pd_custom.setBar(bar)
        pd_custom.setLabel(QLabel('自定义进度条，使用自定义的QProgressBar'))
        pd_custom.setCancelButton(QPushButton('取消按钮'))

        pd_custom.move(300, 600)
        pd_custom.setWindowModality(Qt.WindowModal)
        # pd_custom.setWindowModality(Qt.ApplicationModal)
        pd_custom.setMinimumDuration(1000)  # 一秒后出现对话框

        # 信号和槽要放在计时器后面，否则不会被执行
        pd_custom.canceled.connect(lambda: self.cancel(pd_custom))

        for i in range(-1, bar.maximum() + 1):
            pd_custom.setValue(i)
            self.label.setText('当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(pd_custom.value(), pd_custom.maximum(),
                                                                              pd_custom.wasCanceled()))
            if pd_custom.value() >= pd_custom.maximum() or pd_custom.wasCanceled():
                break
            # print('you can do something  here')
            time.sleep(1)
            # pd_modal.setValue(max)

    def cancel(self, pg):
        self.statusBar().showMessage('你手动取消了进度条： “%s”' % pg.labelText(), 3000)

    def valuechange(self, slider):
        size = slider.value()
        self.pd_slider.setValue(size)
        self.label.setText(
            '当前进度条值: {}\n最大值: {}\n是否取消(重置)过进度条: {}'.format(self.pd_slider.value(), self.pd_slider.maximum(),
                                                           self.pd_slider.wasCanceled()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
