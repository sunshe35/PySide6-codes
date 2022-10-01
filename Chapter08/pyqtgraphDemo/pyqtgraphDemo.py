from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer
import sys
import numpy as np
import pyqtgraph as pg


class pyqtgraphDemo(QMainWindow):
    def __init__(self, parent=None):
        super(pyqtgraphDemo, self).__init__(parent)
        self.setWindowTitle("matplotlib for Qt案例")
        self.resize(950, 750)

        buttonGraph = QPushButton('pyqtgraph自己的布局')
        buttonLayout = QPushButton('使用layout布局')
        buttonGraph.clicked.connect(self.onButtonGraph)
        buttonLayout.clicked.connect(self.onButtonLayout)
        layoutButton = QHBoxLayout()
        layoutButton.addWidget(buttonGraph)
        layoutButton.addWidget(buttonLayout)
        layoutButton.addStretch(1)


        # 添加绘图
        pg.setConfigOption('background', '#E4E4E4')  # 设置背景为灰色
        pg.setConfigOption('foreground', 'd')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状
        # pg.setConfigOption('antialias',True) # 等价于上一句，所不同之处在于setconfigOptions可以传递多个参数进行多个设置，而setConfigOption一次只能接受一个参数进行一个设置。
        self.plot1 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        # p1 = self.plot1.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
        self.plot21 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.plot22 = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        layoutH2 = QHBoxLayout()
        layoutH2.addWidget(self.plot21)
        layoutH2.addWidget(self.plot22)

        layout = QVBoxLayout()
        layout.addLayout(layoutButton)
        layout.addWidget(self.plot1, stretch=2)
        layout.addLayout(layoutH2, stretch=1)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    def onButtonGraph(self):
        self.plot1.clear()
        p1 = self.plot1.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
        p2 = self.plot1.addPlot(title="Multiple curves")
        p2.plot(np.random.normal(size=100), pen=(255, 0, 0), name="Red curve")
        p2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        p2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")

        self.plot1.nextRow()

        p3 = self.plot1.addPlot(title="Drawing with points")
        p3.plot(np.random.normal(size=100), pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='w')

        p4 = self.plot1.addPlot(title="Parametric, grid enabled")
        x = np.cos(np.linspace(0, 2 * np.pi, 1000))
        y = np.sin(np.linspace(0, 4 * np.pi, 1000))
        p4.plot(x, y)
        p4.showGrid(x=True, y=True)

    def onButtonLayout(self):
        if hasattr(self,'p6'):
            return
        p5 = self.plot21.addPlot(title="Scatter plot, axis labels, log scale")
        x = np.random.normal(size=1000) * 1e-5
        y = x * 1000 + 0.005 * np.random.normal(size=1000)
        y -= y.min() - 1.0
        mask = x > 1e-15
        x = x[mask]
        y = y[mask]
        p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
        p5.setLabel('left', "Y Axis", units='A')
        p5.setLabel('bottom', "Y Axis", units='s')
        p5.setLogMode(x=True, y=False)

        self.p6 = self.plot22.addPlot(title="Updating plot")
        self.p6_curve = self.p6.plot(pen='y')
        self.p6_data = np.random.normal(size=(10, 1000))
        self.p6_ptr = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateP6)
        self.timer.start(50)

    def updateP6(self):
        self.p6_curve.setData(self.p6_data[self.p6_ptr % 10])
        if self.p6_ptr == 0:
            self.p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
        self.p6_ptr += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = pyqtgraphDemo()
    demo.show()
    app.exec()
