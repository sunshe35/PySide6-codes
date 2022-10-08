from dash import Dash, html, dcc, Input, Output
import plotly.express as px

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

class WorkThread(QThread):
    port = 8800

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        app = Dash(__name__)
        # assume you have a "long-form" data frame
        # see https://plotly.com/python/px-arguments/ for more options
        df = pd.DataFrame({
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })

        fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

        app.layout = html.Div(children=[
            html.H1(children='Hello Dash'),

            html.Div(children='''
                       Dash: A web application framework for your data.
                   '''),

            dcc.Graph(
                id='example-graph',
                figure=fig
            )
        ])
        app.run_server(debug=False, port=self.port)


class WorkThread2(QThread):
    port = 8801
    def __init__(self):
        super(WorkThread2, self).__init__()

    def run(self):
        external_stylesheets = [r'plotly_html//bWLwgP.css']
        app = Dash(__name__, external_stylesheets=external_stylesheets)
        self.app = app
        df = pd.read_csv(r'plotly_html/country_indicators.csv')
        app.layout = html.Div([
            html.Div([

                html.Div([
                    dcc.Dropdown(
                        df['Indicator Name'].unique(),
                        'Fertility rate, total (births per woman)',
                        id='crossfilter-xaxis-column',
                    ),
                    dcc.RadioItems(
                        ['Linear', 'Log'],
                        'Linear',
                        id='crossfilter-xaxis-type',
                        labelStyle={'display': 'inline-block', 'marginTop': '5px'}
                    )
                ],
                    style={'width': '49%', 'display': 'inline-block'}),

                html.Div([
                    dcc.Dropdown(
                        df['Indicator Name'].unique(),
                        'Life expectancy at birth, total (years)',
                        id='crossfilter-yaxis-column'
                    ),
                    dcc.RadioItems(
                        ['Linear', 'Log'],
                        'Linear',
                        id='crossfilter-yaxis-type',
                        labelStyle={'display': 'inline-block', 'marginTop': '5px'}
                    )
                ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
            ], style={
                'padding': '10px 5px'
            }),

            html.Div([
                dcc.Graph(
                    id='crossfilter-indicator-scatter',
                    hoverData={'points': [{'customdata': 'Japan'}]}
                )
            ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
            html.Div([
                dcc.Graph(id='x-time-series'),
                dcc.Graph(id='y-time-series'),
            ], style={'display': 'inline-block', 'width': '49%'}),

            html.Div(dcc.Slider(
                df['Year'].min(),
                df['Year'].max(),
                step=None,
                id='crossfilter-year--slider',
                value=df['Year'].max(),
                marks={str(year): str(year) for year in df['Year'].unique()}
            ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
        ])

        @app.callback(
            Output('crossfilter-indicator-scatter', 'figure'),
            Input('crossfilter-xaxis-column', 'value'),
            Input('crossfilter-yaxis-column', 'value'),
            Input('crossfilter-xaxis-type', 'value'),
            Input('crossfilter-yaxis-type', 'value'),
            Input('crossfilter-year--slider', 'value'))
        def update_graph(xaxis_column_name, yaxis_column_name,
                         xaxis_type, yaxis_type,
                         year_value):
            dff = df[df['Year'] == year_value]

            fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                             y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                             hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
                             )

            fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

            fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')

            fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

            fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

            return fig

        def create_time_series(dff, axis_type, title):
            fig = px.scatter(dff, x='Year', y='Value')

            fig.update_traces(mode='lines+markers')

            fig.update_xaxes(showgrid=False)

            fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

            fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                               xref='paper', yref='paper', showarrow=False, align='left',
                               text=title)

            fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

            return fig

        @app.callback(
            Output('x-time-series', 'figure'),
            Input('crossfilter-indicator-scatter', 'hoverData'),
            Input('crossfilter-xaxis-column', 'value'),
            Input('crossfilter-xaxis-type', 'value'))
        def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
            country_name = hoverData['points'][0]['customdata']
            dff = df[df['Country Name'] == country_name]
            dff = dff[dff['Indicator Name'] == xaxis_column_name]
            title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
            return create_time_series(dff, axis_type, title)

        @app.callback(
            Output('y-time-series', 'figure'),
            Input('crossfilter-indicator-scatter', 'hoverData'),
            Input('crossfilter-yaxis-column', 'value'),
            Input('crossfilter-yaxis-type', 'value'))
        def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
            dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
            dff = dff[dff['Indicator Name'] == yaxis_column_name]
            return create_time_series(dff, axis_type, yaxis_column_name)

        app.run_server(debug=False,port=self.port)



class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layoutH = QHBoxLayout()
        buttonReLoad1 = QPushButton('载入网页1')
        buttonReLoad2 = QPushButton('载入网页2')
        layoutH.addWidget(buttonReLoad1)
        layoutH.addWidget(buttonReLoad2)
        layoutH.addStretch(1)
        layout.addLayout(layoutH)
        buttonReLoad1.clicked.connect(self.onButtonReload1)
        buttonReLoad2.clicked.connect(self.onButtonReload2)

        self.qwebengine = QWebEngineView(self)
        layout.addWidget(self.qwebengine)


    def onButtonReload1(self):
        if hasattr(self, 'thread1'):
            self.qwebengine.load(QUrl(f'http://127.0.0.1:{self.thread1.port}/'))
            return
        self.thread1 = WorkThread()
        self.thread1.start()
        self.qwebengine.load(QUrl(f'http://127.0.0.1:{self.thread1.port}/'))

    def onButtonReload2(self):
        if hasattr(self, 'thread2'):
            self.qwebengine.load(QUrl(f'http://127.0.0.1:{self.thread2.port}/'))
            return
        self.thread2 = WorkThread2()
        self.thread2.start()
        self.qwebengine.load(QUrl(f'http://127.0.0.1:{self.thread2.port}/'))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    app.exec()
