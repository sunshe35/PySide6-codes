# -*- coding: utf-8 -*-
"""
She35 Editor
定义PyQt可以使用的MatplotlibWidget，PyQt可以通过这个类呈现matplotlib绘图结果。
"""
import sys
import random
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        # plt.rcParams['font.family'] = ['SimSun']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.fig.set_tight_layout(True)
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改

        # self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def start_static_plot(self, qt=None):
        if qt is not None:
            df = qt.posValDF.copy()
            ax1 = self.axes
            ax1.plot(df['val'], color='red', label='val', linewidth=2)
            ax1.legend(loc='upper left')
            ax2 = ax1.twinx()
            ax2.plot(df['valRate'], color='green', label='valRate', linewidth=0.5)
            ax2.legend(loc='upper right')
        else:
            # self.fig.suptitle('测试静态图')
            t = arange(0.0, 3.0, 0.01)
            s = sin(2 * pi * t)
            self.axes.plot(t, s)
            self.axes.set_ylabel('静态图：Y轴')
            self.axes.set_xlabel('静态图：X轴')
            self.axes.grid(True)

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''

    def start_day_plot(self, qx=None):
        if qx is not None:
            df = qx.posValDFBus.copy()
            ax1 = self.axes
            ax1.plot(df['val'], color='red', label='val', linewidth=2)
            ax1.legend(loc='upper left')
            ax2 = ax1.twinx()
            ax2.plot(df['valRate'], color='green', label='valRate', linewidth=0.5)
            ax2.legend(loc='upper right')
        else:
            # self.fig.suptitle('测试静态图')
            t = arange(0.0, 3.0, 0.01)
            s = sin(2 * pi * t)
            self.axes.plot(t, s)
            self.axes.set_ylabel('静态图：Y轴')
            self.axes.set_xlabel('静态图：X轴')
            self.axes.grid(True)

    '''启动绘制动态图'''

    def start_dynamic_plot(self):
        timer = QtCore.QTimer(self)
        # noinspection PyUnresolvedReferences
        timer.timeout.connect(self.update_figure)  # 每隔一段时间就会触发一次update_figure函数。
        timer.start(1000)  # 触发的时间间隔为1秒。

    '''动态图的绘图逻辑可以在这里修改'''

    def update_figure(self):
        self.fig.suptitle('测试动态图')
        # noinspection PyUnusedLocal
        _rnd = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], _rnd, 'r')
        self.axes.set_ylabel('动态图：Y轴')
        self.axes.set_xlabel('动态图：X轴')
        self.axes.grid(True)
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    # ui.mpl.start_static_plot()  # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
    ui.mpl.start_dynamic_plot()  # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
    ui.show()
    app.exec_()
