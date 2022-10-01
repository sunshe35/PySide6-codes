# -*- coding: utf-8 -*-

import pandas
import numpy
from qtpy.QtCore import Qt

from PySide6 import QtWidgets
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.DataTableView import DataTableWidget


# sys.excepthook = excepthook # 设置PyQt的异常钩子，在本例中基本没什么用

# 创建一个空的模型，该模型用于存储与处理数据
model = DataFrameModel()

# 创建一个应用用于显示表格
app = QtWidgets.QApplication([])
widget = DataTableWidget() # 创建一个空的表格，主要用来呈现数据
widget.resize(500, 300) # 调整Widget的大小
widget.show()
# 让表格绑定模型，也就是让表格呈现模型的内容
widget.setViewModel(model)

# 创建测试数据
data = {
    'A': [10, 11, 12],
    'B': [20, 21, 22],
    'C': ['Peter Pan', 'Cpt. Hook', 'Tinkerbell']
}
df = pandas.DataFrame(data)

# 下面两列用来测试委托是否成立
df['A'] = df['A'].astype(numpy.int8) # A列数据格式变成整型
df['B'] = df['B'].astype(numpy.float16) # B列数据格式变成浮点型

# 在模型中填入数据df
model.setDataFrame(df)

# 启动程序
app.exec()
