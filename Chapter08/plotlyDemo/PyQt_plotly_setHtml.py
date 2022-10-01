# -*- coding: utf-8 -*- 


from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from pandas import DataFrame

import os
import plotly.offline as pyof
import plotly.graph_objs as go
from plotly import figure_factory as ff


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('setHtml无法渲染太大的内容')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()

        lagest_down = [-3.74, -3.736, -3.736, -5.969, -5.969]
        xticks = ['2017/01', '2017/02', '2017/03', '2017/04', '2017/05', ]

        trace1 = go.Bar(
            x=xticks,
            y=lagest_down,
            name='最大下跌'
        )

        data = [trace1]

        fig = go.Figure(data=data)
        merge_div = pyof.plot(fig, auto_open=False, output_type='div')
        message = '''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="UTF-8">
				<title></title>
			</head>
			<body>
              %s             
			</body>
		</html>
		''' % (merge_div)

        self.browser.setHtml(message)
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec())
