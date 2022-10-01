import plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import copy
import os

pyof = py.offline


def plot_show(qt):
    '''
    RhQuant的基于plotly的绘图模块，
    :param qt: RhQuant类的实例化
    :return:
    '''
    dataList = copy.copy(qt.plotDataList)
    dataList.append(['', ''])  # 为了能够凑够24*2（原来23*2），
    dataList.append(['', ''])  # 为了能够凑够24*2（原来23*2），
    list0, list1, list2, list3 = [dataList[6 * i:6 * i + 6] for i in range(0, 4)]
    arr_result = np.concatenate([list0, list1, list2, list3], axis=1)
    df_table = pd.DataFrame(arr_result, columns=['回测内容', '回测结果'] * 4)

    figure = FF.create_table(df_table, index_title='Date')
    _df = qt.posValDF.copy()
    _df_b = qt.posValDFBus.copy()
    trace1 = go.Scatter(
        x=_df.index,
        y=_df['val'],
        name='val',
        xaxis='x2',
        yaxis='y2',
        legendgroup='one',
        # mode = 'lines',
        line=dict(
            color='#FF0000',
            width=3),
    )

    trace2 = go.Scatter(
        x=_df.index,
        y=_df['valRate'],
        xaxis='x2',
        yaxis='y3',
        name='valRate',
        legendgroup='one',
        line=dict(
            color='#00EE00',
            width=1)
    )

    trace3 = go.Scatter(
        x=_df_b.index,
        y=_df_b['val'] / _df_b['val'][0],
        # name='net_value',
        xaxis='x4',
        yaxis='y4',
        # mode = 'lines',
        line=dict(
            color='#FF0000',
            width=3),
        showlegend=False,
    )

    trace4 = go.Scatter(
        x=_df_b.index,
        y=_df_b['valRate'],
        xaxis='x4',
        yaxis='y5',
        # name='valRate',
        showlegend=False,
        line=dict(
            color='#00EE00',
            width=1)
    )

    # 把 trace 添加到 figure 中
    # figure['data'].extend(go.Data([trace1, trace2, trace3, trace4]))
    figure.add_traces((trace1, trace2, trace3, trace4))

    figure.layout.update(
        yaxis={'domain': [.81, 1]},
        yaxis2={'domain': [.45, .79],
                'anchor': 'x2',
                'title': '剩余资金'},
        yaxis3=dict(
            title='收益率',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y2',
            side='right'
        ),
        yaxis4={'domain': [0, .36],
                'anchor': 'x4',
                'title': '净值'},
        yaxis5=dict(
            title='收益率',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y4',
            side='right'
        ),
        # xaxis={"tickformat":'%Y/%m/%d'},
        xaxis2={'anchor': 'y2', "tickformat": '%Y/%m/%d'},
        xaxis4={'anchor': 'y4', "tickformat": '%Y/%m/%d'},
        margin={'t': 75, 'b': 30, 'l': 50, 'r': 50},
        title='回溯测试输出结果',
        height=1800,
        legend=dict(x=.9,
                    y=.8,
                    xanchor='auto',
                    yanchor='auto'),
        # plot_bgcolor='white',
        template='plotly_white',
    )
    # fig.update_xaxes(tickformat='%Y/%m/%d')

    # 画图!
    filePath = qt.pathSaveDirName + os.sep + qt.strategyName + '.html'
    pyof.plot(figure, filename=filePath, show_link=False)
