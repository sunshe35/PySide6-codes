# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

try: # 为了模块引用
    from .Ui_rhQuant_matplotlib_show import Ui_MainWindow
except: # 为了直接运行
    from Ui_rhQuant_matplotlib_show import Ui_MainWindow

import pickle
import numpy as np
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    RhQuant 基于 PyQt 的的绘图类，.
    """

    def __init__(self, qt=None, parent=None):
        """
        类的初始化
        :param qt: RhQuant的子类实例化
        :param parent:
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.matplotlibwidget_day.setMinimumHeight(650)
        self.matplotlibwidget_static.setMinimumHeight(650)
        if qt is not None:
            self.qt = qt
            # self.matplotlibwidget_dynamic.setVisible(False)
            # self.matplotlibwidget_static.setVisible(False)
            self.show_plot(self.qt)
            self.matplotlibwidget_static.mpl.start_static_plot(self.qt)
            self.matplotlibwidget_day.mpl.start_day_plot(self.qt)
        else:
            self.show_plot()
            self.matplotlibwidget_static.mpl.start_static_plot()
            self.matplotlibwidget_day.mpl.start_day_plot()

    def show_plot(self, qt=None):

        if qt is not None:
            list_result = qt.plotDataList
            pickle_file = open('plotDataList.pkl', 'wb')  # 以 wb 方式写入
            pickle.dump(list_result, pickle_file)  # 向pickle_file中写入plotDataList
            pickle_file.close()
        else:
            pickle_file = open('plotDataList.pkl', 'rb')  # 以 rb 方式读取
            list_result = pickle.load(pickle_file)  # 读取以pickle方式写入的文件pickle_file
            pickle_file.close()
        list_result.append(['', ''])  # 为了能够凑够24*2（原来22*2），
        list_result.append(['', ''])  # 为了能够凑够24*2（原来22*2），
        len_index = 6
        len_col = 8
        list0, list1, list2, list3 = [list_result[6 * i:6 * i + 6] for i in range(0, 4)]
        arr_result = np.concatenate([list0, list1, list2, list3], axis=1)
        self.tableWidget.setRowCount(len_index)
        self.tableWidget.setColumnCount(len_col)
        self.tableWidget.setHorizontalHeaderLabels(['回测内容', '回测结果'] * 4)
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len_index + 1)])
        # self.setMinimumHeight(200)
        # self.tableWidget.setMinimumWidth(40)

        for index in range(len_index):
            for col in range(len_col):
                self.tableWidget.setItem(index, col, QTableWidgetItem(arr_result[index, col]))
        self.tableWidget.resizeColumnsToContents()

    @Slot()
    def on_pushButton_show_dataPre_clicked(self):
        """
        打开数据预处理文件
        """
        if hasattr(self, 'qt'):
            if hasattr(self.qt, 'path_dataPre'):
                os.system(np.random.choice(self.qt.path_dataPre))

    @Slot()
    def on_pushButton_show_money_flow_clicked(self):
        """
        打开资金流文件
        """
        if hasattr(self, 'qt'):
            os.system(self.qt.pathPosValDF)
        print(5)

    @Slot()
    def on_pushButton_show_trade_flow_clicked(self):
        """
        打开交易流水文件
        """
        if hasattr(self, 'qt'):
            os.system(self.qt.pathTradeFlow)
        print(4)


def plot_show(qt=None):
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow(qt)
    ui.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    plot_show()
