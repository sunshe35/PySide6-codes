# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import pandas as pd
import numpy as np

from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
from combination import Ui_MainWindow
from Plotly_Qt import Plotly_Qt


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.plotly_PySide6 = Plotly_Qt()


    def check_check_box(self):
        strategy_list = []
        for each_checkBox in [self.checkBox_bond,self.checkBox_combination_fund,self.checkBox_compound,self.checkBox_event,self.checkBox_future_manage,self.checkBox_macro,self.checkBox_relative_fund,self.checkBox_others,self.checkBox_others]:
            if each_checkBox.isChecked():
                strategy_list.append(each_checkBox.text())
        return strategy_list


    @Slot()
    def on_pushButton_start_combination_clicked(self):
        """
        产品组合分析
        """

        strategy_list = self.check_check_box()
        if  len(strategy_list) > 3:
            print('最多选择3个策略')
            QMessageBox.information(self, "注意", "最多选择3个策略")
            return None

        if  len(strategy_list) == 0:
            print('最少选择1个策略')
            QMessageBox.information(self, "注意", "最少选择1个策略")
            return None

        self.QWebEngineview_Combination_monte_markovitz.setMinimumHeight(800)
        self.QWebEngineview_Combination_Pie.setMinimumHeight(400)
        self.QWebEngineview_Combination_Table.setMinimumHeight(400)
        self.QWebEngineview_Combination_Versus.setMinimumHeight(700)

        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:', self.doubleSpinBox_sharp_max.text())

        '''假设已经获取产品组合和权重'''
        df = pd.read_excel(r'data\组合.xlsx',index_col=[0])
        w = [0.4, 0.2, 0.4]
        df['组合'] = (df * w).sum(axis=1)


        df_hs300 = pd.read_excel(r'data\组合.xlsx',index_col=[0], sheet_name='Sheet2')
        # df_hs300.rename_axis(lambda x:pd.to_datetime(x),inplace=True)
        df_hs300.rename(lambda x:pd.to_datetime(x),inplace=True)

        self.QWebEngineview_Combination_monte_markovitz.load(
            QUrl.fromLocalFile(self.plotly_PySide6.get_plotly_path_monte_markovitz(monte_count=600)))
        self.QWebEngineview_Combination_Pie.load(
            QUrl.fromLocalFile(self.plotly_PySide6.get_plotly_path_combination_pie(df=df, w=w)))
        self.QWebEngineview_Combination_Versus.load(
            QUrl.fromLocalFile(self.plotly_PySide6.get_plotly_path_combination_versus(df=df,df_base=df_hs300, w=w)))
        self.QWebEngineview_Combination_Table.load(
            QUrl.fromLocalFile(self.plotly_PySide6.get_plotly_path_combination_table(df=df, w=w)))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    sys.exit(app.exec())
