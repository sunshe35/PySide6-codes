from PySide6.QtWidgets import *
import sys
from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg as
                                               FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np
import time
import matplotlib.pyplot as plt


class matplotlibDemo(QMainWindow):
    def __init__(self, parent=None):
        super(matplotlibDemo, self).__init__(parent)
        self.setWindowTitle("matplotlib for Qt案例")
        self.resize(950, 750)

        layoutButton = QHBoxLayout()
        buttonStatic = QPushButton('显示静态图')
        buttonDynamic = QPushButton('显示动态图')
        buttonStatic.clicked.connect(self.onButtonStatic)
        buttonDynamic.clicked.connect(self.onButtonDynamic)

        layoutButton.addWidget(buttonStatic)
        layoutButton.addWidget(buttonDynamic)
        layoutButton.addStretch(1)
        layout = QVBoxLayout()
        layout.addLayout(layoutButton)
        layout.addStretch(1)

        # 静态图+动态图
        self.static_canvas = FigureCanvas(Figure())
        # Ideally one would use self.addToolBar here, but it is slightly
        # incompatible between PyQt6 and other bindings, so we just add the
        # toolbar as a plain widget instead.
        layout.addWidget(NavigationToolbar(self.static_canvas, self))
        layout.addWidget(self.static_canvas)
        self.dynamic_canvas = FigureCanvas(Figure())
        layout.addWidget(NavigationToolbar(self.dynamic_canvas, self))
        layout.addWidget(self.dynamic_canvas)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        # 初始化一些绘图数据
        self.initPlot()

    def initPlot(self):
        # 配置matplotlib中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        # 绘制静态图，这里不需要触发self.static_canvas.draw()
        self._static_ax = self.static_canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self._static_ax.plot(t, np.tan(t), ".")

    def onButtonStatic(self):
        fig = self.static_canvas.figure
        fig.clear()
        fig.suptitle('静态图标题')
        axes = fig.subplots()
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        axes.plot(t, s)
        axes.set_ylabel('静态图：Y轴')
        axes.set_xlabel('静态图：X轴')
        axes.grid(True)  # 显示网格
        self.static_canvas.draw()

    def onButtonDynamic(self):
        if hasattr(self, 'timer'):
            return
        fig = self.dynamic_canvas.figure
        fig.suptitle('动态图标题')
        axes = fig.subplots()
        t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        self.line, = axes.plot(t, np.sin(t + time.time()))
        axes.set_ylabel('动态图：Y轴')
        axes.set_xlabel('动态图：X轴')
        axes.grid(True)  # 显示网格
        self.dynamic_canvas.draw()

        self.timer = self.dynamic_canvas.new_timer(50)
        self.timer.add_callback(self._update_canvas)
        self.timer.start()

    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self.line.set_data(t, np.sin(t + time.time()))
        self.line.figure.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = matplotlibDemo()
    demo.show()
    app.exec()
