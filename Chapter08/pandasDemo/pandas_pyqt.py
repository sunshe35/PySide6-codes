# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication

from Ui_pandas_pyqt import Ui_MainWindow

from qtpandas.models.DataFrameModel import DataFrameModel
import pandas as pd

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
        
        '''初始化pandasqt'''
        widget = self.pandastablewidget
        widget.resize(600, 500) # 如果对部件尺寸大小不满意可以在这里设置
        
        
        self.model = DataFrameModel() # 设置新的模型
        widget.setViewModel(self.model)
    
        self.df = pd.read_excel(r'./data/fund_data.xlsx')
        self.df_original = self.df.copy() # 备份原始数据
        self.model.setDataFrame(self.df)


    
    @Slot()
    def on_pushButton_clicked(self):
        """
        初始化pandas
        """
        self.model.setDataFrame(self.df_original)
    
    @Slot()
    def on_pushButton_2_clicked(self):
        """
        保存数据
        """
        self.df.to_excel(r'./data/fund_data_new.xlsx')
       

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
