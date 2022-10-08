import pyqtgraph
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys
import os
os.chdir(os.path.dirname(__file__))

class QTableViewDemo(QMainWindow):
    addCount = 0
    insertCount = 0

    def __init__(self, parent=None):
        super(QTableViewDemo, self).__init__(parent)
        self.setWindowTitle("QTableView案例")
        self.resize(600, 800)
        self.text = QPlainTextEdit('用来显示QTableView相关信息：')
        self.tableView = QTableView()
        self.model = QStandardItemModel(5, 4)
        self.tableView.setModel(self.model)
        self.selectModel = QItemSelectionModel()
        self.tableView.setSelectionModel(self.selectModel)
        # 设置行列标题
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])
        for i in range(4):
            item = QStandardItem(f'行{i + 1}')
            self.model.setVerticalHeaderItem(i, item)

        # 对照组
        self.tableView2 = QTableView()
        self.tableView2.setModel(self.model)

        # 增删行
        self.buttonDeleteRow = QPushButton('删除行')
        self.buttonAddRow = QPushButton('增加行')
        self.buttonInsertRow = QPushButton('插入行')
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.buttonAddRow)
        layoutH.addWidget(self.buttonInsertRow)
        layoutH.addWidget(self.buttonDeleteRow)
        self.buttonAddRow.clicked.connect(lambda: self.onAdd('row'))
        self.buttonInsertRow.clicked.connect(lambda: self.onInsert('row'))
        self.buttonDeleteRow.clicked.connect(lambda: self.onDelete('row'))
        # 增删列
        self.buttonDeleteColumn = QPushButton('删除列')
        self.buttonAddColumn = QPushButton('增加列')
        self.buttonInsertColumn = QPushButton('插入列')
        layoutH2 = QHBoxLayout()
        layoutH2.addWidget(self.buttonAddColumn)
        layoutH2.addWidget(self.buttonInsertColumn)
        layoutH2.addWidget(self.buttonDeleteColumn)
        self.buttonAddColumn.clicked.connect(lambda: self.onAdd('column'))
        self.buttonInsertColumn.clicked.connect(lambda: self.onInsert('column'))
        self.buttonDeleteColumn.clicked.connect(lambda: self.onDelete('column'))

        # 选择
        self.buttonSelectAll = QPushButton('全选')
        self.buttonSelectRow = QPushButton('选择行')
        self.buttonSelectColumn = QPushButton('选择列')
        self.buttonSelectOutput = QPushButton('输出选择')
        layoutH3 = QHBoxLayout()
        layoutH3.addWidget(self.buttonSelectAll)
        layoutH3.addWidget(self.buttonSelectRow)
        layoutH3.addWidget(self.buttonSelectColumn)
        layoutH3.addWidget(self.buttonSelectOutput)
        self.buttonSelectAll.clicked.connect(lambda: self.tableView.selectAll())
        self.buttonSelectRow.clicked.connect(lambda: self.tableView.selectRow(self.tableView.currentIndex().row()))
        self.buttonSelectColumn.clicked.connect(
            lambda: self.tableView.selectColumn(self.tableView.currentIndex().column()))
        self.buttonSelectOutput.clicked.connect(self.onButtonSelectOutput)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)
        # layout.addWidget(self.tableView2)
        layout.addLayout(layoutH)
        layout.addLayout(layoutH2)
        layout.addLayout(layoutH3)
        layout.addWidget(self.text)
        layout.addWidget(self.tableView2)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        self.initItem()

        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)

        # 行列标题
        rowCount = self.model.rowCount()
        columnCount = self.model.columnCount()
        self.model.setHorizontalHeaderLabels([f'col{i}' for i in range(columnCount)])
        self.model.setVerticalHeaderLabels([f'row{i}' for i in range(rowCount)])
        cusHeaderItem = QStandardItem("cusHeader")
        cusHeaderItem.setIcon(QIcon("images/android.png"))
        cusHeaderItem.setTextAlignment(Qt.AlignVCenter)
        cusHeaderItem.setForeground(QColor(255, 0, 0))
        self.model.setHorizontalHeaderItem(2, cusHeaderItem)

        # 自定义控件
        self.tableView.setIndexWidget(self.model.index(4, 3), QLineEdit('自定义控件-' * 3))
        self.tableView.setIndexWidget(self.model.index(4, 2), QSpinBox())

        # 调整行列宽高
        header = self.tableView.horizontalHeader()
        # # header.setStretchLastSection(True)
        # # header.setSectionResizeMode(QHeaderView.Stretch)
        # header.setSectionResizeMode(QHeaderView.Interactive)
        # header.resizeSection(3,120)
        # header.moveSection(0,2)

        # header.setStretchLastSection(True)
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()

        # 排序单元格
        # self.model.sort(1,order=Qt.DescendingOrder)

        # 合并单元格
        self.tableView.setSpan(1, 0, 1, 2)
        item = QStandardItem('合并单元格')
        item.setTextAlignment(Qt.AlignCenter)
        self.model.setItem(1, 0, item)

        # 显示坐标
        buttonShowPosition = QToolButton(self)
        buttonShowPosition.setText('显示当前位置')
        self.toolbar.addWidget(buttonShowPosition)
        buttonShowPosition.clicked.connect(self.onButtonShowPosition)

        # 上下文菜单
        self.menu = self.generateMenu()
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableView.customContextMenuRequested.connect(self.showMenu)  ####右键菜单

    def initItem(self):

        # 初始化数据
        for row in range(self.model.rowCount()):
            for column in range(self.model.columnCount()):
                value = "row %s, column %s" % (row, column)
                item = QStandardItem(value)
                item.setData(QColor(155, 14, 0), role=Qt.ForegroundRole)
                item.setData(value + '-toolTip', role=Qt.ToolTipRole)
                item.setData(value + '-statusTip', role=Qt.StatusTipRole)
                item.setData(QIcon("images/open.png"), role=Qt.DecorationRole)
                self.model.setItem(row, column, item)

        # flag+check
        item = QStandardItem('flag+check1')
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.model.setItem(2, 0, item)
        item = QStandardItem('flag+check2')
        item.setFlags(Qt.NoItemFlags)
        item.setCheckState(Qt.Unchecked)
        self.model.setItem(2, 1, item)
        # setText
        item = QStandardItem()
        item.setText('右对齐+check')
        item.setTextAlignment(Qt.AlignRight)
        item.setCheckState(Qt.Checked)
        self.model.setItem(3, 0, item)
        # setIcon
        item = QStandardItem(f'setIcon')
        item.setIcon(QIcon('images/music.png'))
        item.setWhatsThis('whatsThis提示1')
        self.model.setItem(3, 1, item)
        # setFont、setFore(Back)ground
        item = QStandardItem(f'setFont、setFore(Back)ground')
        item.setFont(QFont('宋体'))
        item.setForeground(QBrush(QColor(255, 0, 0)))
        item.setBackground(QBrush(QColor(0, 255, 0)))
        self.model.setItem(3, 2, item)
        # setToolTip,StatusTip,WhatsThis
        item = QStandardItem(f'提示帮助')
        item.setToolTip('toolTip提示')
        item.setStatusTip('statusTip提示')
        item.setWhatsThis('whatsThis提示2')
        self.model.setItem(3, 3, item)

        # 开启statusbar
        statusBar = self.statusBar()
        statusBar.show()
        self.tableView.setMouseTracking(True)

        # 开启whatsThis功能
        whatsThis = QWhatsThis(self)
        self.toolbar = self.addToolBar('help')
        #    方式1：QAction
        self.actionHelp = whatsThis.createAction(self)
        self.actionHelp.setText('显示whatsThis-help')
        self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))
        self.toolbar.addAction(self.actionHelp)
        #   方式2：工具按钮
        tool_button = QToolButton(self)
        tool_button.setToolTip("显示whatsThis2-help")
        tool_button.setIcon(QIcon("images/help.jpg"))
        self.toolbar.addWidget(tool_button)
        tool_button.clicked.connect(lambda: whatsThis.enterWhatsThisMode())

        self.model.setData(self.model.index(4, 0), QColor(215, 214, 220), role=Qt.BackgroundRole)

    def generateMenu(self):
        menu = QMenu(self)
        menu.addAction('增加行', lambda: self.onAdd('row'), QKeySequence(Qt.CTRL | Qt.Key_N))
        menu.addAction('插入行', lambda: self.onInsert('row'), QKeySequence(Qt.CTRL | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除行', lambda: self.onDelete('row'), QKeySequence(Qt.CTRL | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('增加列', lambda: self.onAdd('column'), QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_N))
        menu.addAction('插入列', lambda: self.onInsert('column'), QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除列', lambda: self.onDelete('column'),
                       QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('全选', lambda: self.tableView.selectAll(), QKeySequence(Qt.CTRL | Qt.Key_A))
        menu.addAction('选择行', lambda: self.tableView.selectRow(self.tableView.currentIndex().row()),
                       QKeySequence(Qt.CTRL | Qt.Key_R))
        menu.addAction('选择列', lambda: self.tableView.selectColumn(self.tableView.currentIndex().column()),
                       QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_R))
        menu.addAction('输出选择', self.onButtonSelectOutput)
        menu.addSeparator()
        menu.addAction(self.actionHelp)
        menu.addAction('显示当前位置', lambda: self.onButtonShowPosition())
        return menu

    def showMenu(self, pos):
        self.menu.exec(QCursor.pos())  # 显示菜单

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction('选项1')
        menu.addAction('选项2')
        menu.addAction('选项3')
        menu.exec(event.globalPos())

    def onButtonSelectOutput(self):

        indexList = self.tableView.selectedIndexes()
        _row = indexList[0].row()
        text = ''
        for index in indexList:
            row = index.row()
            column = index.column()
            item = self.model.item(row, column)
            if _row == row:
                text = text + item.text() + '  '
            else:
                text = text + '\n' + item.text() + '  '
                _row = row
        self.text.appendPlainText(text)

    def onAdd(self, type='row'):
        if type == 'row':
            rowCount = self.model.rowCount()
            self.model.insertRow(rowCount)
            # self.tableView.insertRow(rowCount)
            self.text.appendPlainText(f'row:{rowCount},新增一行')
        elif type == 'column':
            columnCount = self.model.columnCount()
            self.model.insertColumn(columnCount)
            self.text.appendPlainText(f'column:{columnCount},新增一列')

    def onInsert(self, type='row'):
        index = self.tableView.currentIndex()
        if type == 'row':
            row = index.row()
            self.model.insertRow(row)
            self.text.appendPlainText(f'row:{row},插入一行')
        elif type == 'column':
            column = index.column()
            self.model.insertColumn(column)
            self.text.appendPlainText(f'column:{column},新增一列')

    def onDelete(self, type='row'):
        index = self.tableView.currentIndex()
        if type == 'row':
            row = index.row()
            self.model.removeRow(row)
            self.text.appendPlainText(f'row:{row},被删除')
        elif type == 'column':
            column = index.column()
            self.model.removeColumn(column)
            self.text.appendPlainText(f'column:{column},被删除')

    def onButtonShowPosition(self):
        index = self.tableView.currentIndex()
        row = index.row()
        rowPositon = self.tableView.rowViewportPosition(row)
        rowAt = self.tableView.rowAt(rowPositon)
        column = index.column()
        columnPositon = self.tableView.columnViewportPosition(column)
        columnAt = self.tableView.columnAt(columnPositon)
        _str = f'当前row:{row},rowPosition:{rowPositon},rowAt:{rowAt}' + \
               f'\n当前column:{column},columnPosition:{columnPositon},columnAt:{columnAt}'
        self.text.appendPlainText(_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTableViewDemo()
    demo.show()
    sys.exit(app.exec())
