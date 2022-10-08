from PySide6.QtWidgets import *
import sys
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget
import os
os.chdir(os.path.dirname(__file__))
import pandas as pd

class qtpandasDemo(QMainWindow):

    def __init__(self, parent=None):
        super(qtpandasDemo, self).__init__(parent)
        self.setWindowTitle("qtpandas案例")
        self.resize(750, 500)
        layoutButton = QHBoxLayout()
        buttonInit = QPushButton('初始化数据')
        buttonSave = QPushButton('保存')
        layoutButton.addWidget(buttonInit)
        layoutButton.addWidget(buttonSave)
        layoutButton.addStretch(1)



        self.table = DataTableWidget()
        self.model = DataFrameModel()  # 设置新的模型
        self.table.setViewModel(self.model)

        self.df = pd.read_excel(r'./data/fund_data.xlsx')
        self.df_original = self.df.copy()  # 备份原始数据
        self.model.setDataFrame(self.df)

        buttonInit.clicked.connect(self.onButtonInit)
        buttonSave.clicked.connect(self.onButtonSave)

        layout = QVBoxLayout()
        layout.addLayout(layoutButton)
        layout.addWidget(self.table)
        widget=QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)


    def onButtonInit(self):
        """
        初始化pandas
        """
        self.model.setDataFrame(self.df_original)

    def onButtonSave(self):
        """
        保存数据
        """
        self.df.to_excel(r'./data/fund_data_new.xlsx')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = qtpandasDemo()
    demo.show()
    app.exec()


