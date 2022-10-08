from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import os
import plotly.offline as pyof
import plotly.graph_objs as go
import pandas as pd
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
os.chdir(os.path.dirname(__file__))

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir

        self.qwebengine = QWebEngineView(self)
        layout = QHBoxLayout()
        layout.addWidget(self.qwebengine)
        self.setLayout(layout)
        self.qwebengine.load(QUrl.fromLocalFile(self.get_plotly_path_if_hs300_bais()))

    def get_plotly_path_if_hs300_bais(self, file_name='if_hs300_bais.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        df = pd.read_excel(r'plotly_html\if_index_bais.xlsx')

        '''绘制散点图'''
        line_main_price = go.Scatter(
            x=df.index,
            y=df['main_price'],
            name='main_price',
            connectgaps=True,  # 这个参数表示允许连接数据缺口
        )

        line_hs300_close = go.Scatter(
            x=df.index,
            y=df['hs300_close'],
            name='hs300_close',
            connectgaps=True,
        )
        data = [line_hs300_close, line_main_price]

        layout = dict(title='if_hs300_bais',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Price'),
                      )

        fig = go.Figure(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    app.exec()
