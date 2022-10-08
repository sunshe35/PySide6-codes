from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import os
os.chdir(os.path.dirname(__file__))

class QTableWidgetDemo(QMainWindow):
    addCount = 0
    insertCount = 0

    def __init__(self, parent=None):
        super(QTableWidgetDemo, self).__init__(parent)
        self.setWindowTitle("QTableWidget案例")
        self.resize(500, 600)
        self.text = QPlainTextEdit('用来显示QTableWidget相关信息：')
        self.tableWidget = QTableWidget(5, 4)


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
        self.buttonSelectAll.clicked.connect(lambda: self.tableWidget.selectAll())
        # self.buttonSelectAll.clicked.connect(self.onSelectAll)
        self.buttonSelectRow.clicked.connect(lambda: self.tableWidget.selectRow(self.tableWidget.currentRow()))
        self.buttonSelectColumn.clicked.connect(lambda: self.tableWidget.selectColumn(self.tableWidget.currentColumn()))
        self.buttonSelectOutput.clicked.connect(self.onButtonSelectOutput)
        # self.buttonSelectColumn.clicked.connect(self.onCheckNone)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableWidget)
        # layout.addWidget(self.tableWidget2)
        layout.addLayout(layoutH)
        layout.addLayout(layoutH2)
        layout.addLayout(layoutH3)
        layout.addWidget(self.text)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        self.initItem()




        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)

        # 行列标题
        rowCount = self.tableWidget.rowCount()
        columnCount = self.tableWidget.columnCount()
        self.tableWidget.setHorizontalHeaderLabels([f'col{i}' for i in range(columnCount)])
        self.tableWidget.setVerticalHeaderLabels([f'row{i}' for i in range(rowCount)])
        cusHeaderItem = QTableWidgetItem("cusHeader")
        cusHeaderItem.setIcon(QIcon("images/android.png"))
        cusHeaderItem.setTextAlignment(Qt.AlignVCenter)
        cusHeaderItem.setForeground(QBrush(QColor(255, 0, 0)))
        self.tableWidget.setHorizontalHeaderItem(2,cusHeaderItem)

        # 自定义控件
        model = self.tableWidget.model()
        self.tableWidget.setIndexWidget(model.index(4,3),QLineEdit('自定义控件-'*3))
        self.tableWidget.setIndexWidget(model.index(4,2),QSpinBox())
        self.tableWidget.setCellWidget(4,1,QPushButton("cellWidget"))



        # 调整行列宽高
        header = self.tableWidget.horizontalHeader()
        # # header.setStretchLastSection(True)
        # # header.setSectionResizeMode(QHeaderView.Stretch)
        # header.setSectionResizeMode(QHeaderView.Interactive)
        # header.resizeSection(3,120)
        # header.moveSection(0,2)
        # # self.tableView.resizeColumnsToContents()

        # header.setStretchLastSection(True)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        # headerH = self.tableWidget.horizontalHeader()

        # 排序单元格
        # self.tableWidget.sortItems(1,order=Qt.DescendingOrder)

        # 合并单元格
        self.tableWidget.setSpan(1, 0, 1, 2)
        item = QTableWidgetItem('合并单元格')
        item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(1,0,item)



        # 显示坐标
        buttonShowPosition = QToolButton(self)
        buttonShowPosition.setText('显示当前位置')
        self.toolbar.addWidget(buttonShowPosition)
        buttonShowPosition.clicked.connect(self.onButtonShowPosition)


        # 上下文菜单
        self.menu = self.generateMenu()
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableWidget.customContextMenuRequested.connect(self.showMenu)  ####右键菜单

        # 信号与槽
        self.tableWidget.currentItemChanged[QTableWidgetItem, QTableWidgetItem].connect(self.onCurrentItemChanged)
        self.tableWidget.itemActivated[QTableWidgetItem].connect(self.onItemActivated)
        self.tableWidget.itemClicked[QTableWidgetItem].connect(self.onItemClicked)
        self.tableWidget.itemDoubleClicked[QTableWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemDoubleClicked信号：'))
        self.tableWidget.itemChanged[QTableWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemChanged信号：'))
        self.tableWidget.itemEntered[QTableWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemEntered信号：'))
        self.tableWidget.itemPressed[QTableWidgetItem].connect(
            lambda item: self.text.appendPlainText(f'"{item.text()}"触发itemPressed信号：'))
        self.tableWidget.itemSelectionChanged.connect(lambda: self.text.appendPlainText(f'触发itemSelectionChanged信号：'))
        self.tableWidget.cellActivated[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellActivated'))
        self.tableWidget.cellChanged[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellChanged'))
        self.tableWidget.cellClicked[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellClicked'))
        self.tableWidget.cellDoubleClicked[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellDoubleClicked'))
        self.tableWidget.cellEntered[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellEntered'))
        self.tableWidget.cellPressed[int,int].connect(lambda row,column:self.onCellSignal(row,column,'cellPressed'))
        self.tableWidget.currentCellChanged[int,int,int,int].connect(lambda currentRow,currentColumn,previousRow,previousColumn:self.text.appendPlainText(f'row:{currentRow},column:{currentColumn},触发信号:currentCellChanged,preRow:{previousRow},preColumn:{columnCount}'))

    def initItem(self):
        # flag+check
        item = QTableWidgetItem('flag+check1')
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled|Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.tableWidget.setItem(2,0,item)
        item = QTableWidgetItem('flag+check2')
        item.setFlags(Qt.NoItemFlags)
        item.setCheckState(Qt.Unchecked)
        self.tableWidget.setItem(2,1,item)
        # setText
        item = QTableWidgetItem()
        item.setText('右对齐+check')
        item.setTextAlignment(Qt.AlignRight)
        item.setCheckState(Qt.Checked)
        self.tableWidget.setItem(3, 0, item)
        # setIcon
        item = QTableWidgetItem(f'setIcon')
        item.setIcon(QIcon('images/music.png'))
        item.setWhatsThis('whatsThis提示1')
        self.tableWidget.setItem(3, 1, item)
        # setFont、setFore(Back)ground
        item = QTableWidgetItem(f'setFont、setFore(Back)ground')
        item.setFont(QFont('宋体'))
        item.setForeground(QBrush(QColor(255, 0, 0)))
        item.setBackground(QBrush(QColor(0, 255, 0)))
        self.tableWidget.setItem(3, 2, item)
        # setToolTip,StatusTip,WhatsThis
        item = QTableWidgetItem(f'提示帮助')
        item.setToolTip('toolTip提示')
        item.setStatusTip('statusTip提示')
        item.setWhatsThis('whatsThis提示2')
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setItem(3, 3, item)
        # 开启statusbar
        statusBar = self.statusBar()
        statusBar.show()

        # 开启whatsThis功能
        whatsThis = QWhatsThis(self)
        self.toolbar = self.addToolBar('help')
        #    方式1：QAction
        self.actionHelp = whatsThis.createAction(self)
        self.actionHelp.setText('显示whatsThis-help')
        # self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))
        # self.actionHelp.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_H))
        self.toolbar.addAction(self.actionHelp)
        #   方式2：工具按钮
        tool_button = QToolButton(self)
        tool_button.setToolTip("显示whatsThis2-help")
        tool_button.setIcon(QIcon("images/help.jpg"))
        self.toolbar.addWidget(tool_button)
        tool_button.clicked.connect(lambda: whatsThis.enterWhatsThisMode())

        # 初始化表格
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is None:
                    _item = QTableWidgetItem(f'row:{row},col:{col}')
                    self.tableWidget.setItem(row, col, _item)


    def generateMenu(self):
        menu = QMenu(self)
        menu.addAction('增加行', lambda: self.onAdd('row'), QKeySequence(Qt.CTRL | Qt.Key_N))
        menu.addAction('插入行', lambda: self.onInsert('row'), QKeySequence(Qt.CTRL | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除行', lambda: self.onDelete('row'), QKeySequence(Qt.CTRL | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('增加列', lambda: self.onAdd('column'), QKeySequence(Qt.CTRL|Qt.SHIFT | Qt.Key_N))
        menu.addAction('插入列', lambda: self.onInsert('column'), QKeySequence(Qt.CTRL|Qt.SHIFT | Qt.Key_I))
        menu.addAction(QIcon("images/close.png"), '删除列', lambda: self.onDelete('column'), QKeySequence(Qt.CTRL|Qt.SHIFT | Qt.Key_D))
        menu.addSeparator()
        menu.addAction('全选', lambda: self.tableWidget.selectAll(), QKeySequence(Qt.CTRL | Qt.Key_A))
        menu.addAction('选择行', lambda: self.tableWidget.selectRow(self.tableWidget.currentRow()), QKeySequence(Qt.CTRL | Qt.Key_R))
        menu.addAction('选择列', lambda: self.tableWidget.selectColumn(self.tableWidget.currentColumn()), QKeySequence(Qt.CTRL |Qt.SHIFT| Qt.Key_R))
        menu.addAction('输出选择', self.onButtonSelectOutput)
        menu.addSeparator()
        menu.addAction(self.actionHelp)
        menu.addAction('显示当前位置',lambda :self.onButtonShowPosition())
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
        indexList = self.tableWidget.selectedIndexes()
        itemList = self.tableWidget.selectedItems()
        _row =indexList[0].row()
        text = ''
        for index,item in zip(indexList,itemList):
            row = index.row()
            if _row == row:
                text = text  +item.text()+ '  '
            else:
                text =text + '\n'+ item.text()+ '  '
                _row=row
        self.text.appendPlainText(text)


    def onCurrentItemChanged(self, current: QTableWidgetItem, previous: QTableWidgetItem):
        if previous == None:
            _str = f'触发currentItemChanged信号，当前项:"{current.text()}",之前项:None'
        elif current == None:
            _str = f'触发currentItemChanged信号，当前项:None,之前项:"{previous.text()}"'
        else:
            _str = f'触发currentItemChanged信号，当前项:"{current.text()}",之前项:"{previous.text()}"'
        self.text.appendPlainText(_str)

    def onItemClicked(self, item: QTableWidgetItem):
        self.tableWidget.currentRow()

        _str1 = f'当前点击:"{item.text()}"'

        if item.checkState() == Qt.Unchecked:
            item.setCheckState(Qt.Checked)
            _str2 = f'"{item.text()}"被选中'
        else:
            item.setCheckState(Qt.Unchecked)
            _str2 = f'"{item.text()}"被取消选中'

        self.text.appendPlainText(f'"{item.text()}"触发itemClicked信号：')
        self.text.appendPlainText(_str1)
        self.text.appendPlainText(_str2)
        return

    def onItemActivated(self, item: QTableWidgetItem):
        self.text.appendPlainText(f'"{item.text()}"触发itemActivated信号：')
        return

    def onCellSignal(self,row,column,type):
        _str = f'row:{row},column:{column},触发信号:{type}'
        self.text.appendPlainText(_str)

    def onAdd(self, type='row'):
        if type == 'row':
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            self.text.appendPlainText(f'row:{rowCount},新增一行')
        elif type == 'column':
            columnCount = self.tableWidget.columnCount()
            self.tableWidget.insertColumn(columnCount)
            self.text.appendPlainText(f'column:{columnCount},新增一列')

    def onInsert(self, type='row'):
        if type == 'row':
            row = self.tableWidget.currentRow()
            self.tableWidget.insertRow(row)
            self.text.appendPlainText(f'row:{row},插入一行')
        elif type == 'column':
            column = self.tableWidget.currentColumn()
            self.tableWidget.insertColumn(column)
            self.text.appendPlainText(f'column:{column},新增一列')

    def onDelete(self, type='row'):
        if type == 'row':
            row = self.tableWidget.currentRow()
            self.tableWidget.removeRow(row)
            self.text.appendPlainText(f'row:{row},被删除')
        elif type == 'column':
            column = self.tableWidget.currentColumn()
            self.tableWidget.removeColumn(column)
            self.text.appendPlainText(f'column:{column},被删除')

    def onCheckAll(self):
        self.text.appendPlainText('点击了“全选”')
        count = self.tableWidget.count()
        for i in range(count):
            item = self.tableWidget.item(i)
            item.setCheckState(Qt.Checked)

    def onCheckInverse(self):
        self.text.appendPlainText('点击了“反选”')
        count = self.tableWidget.count()
        for i in range(count):
            item = self.tableWidget.item(i)
            if item.checkState() == Qt.Unchecked:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

    def onCheckNone(self):
        self.text.appendPlainText('点击了“全不选”')
        count = self.tableWidget.count()
        for i in range(count):
            item = self.tableWidget.item(i)
            item.setCheckState(Qt.Unchecked)

    def onButtonShowPosition(self):
        row = self.tableWidget.currentRow()
        rowPositon = self.tableWidget.rowViewportPosition(row)
        rowAt = self.tableWidget.rowAt(rowPositon)
        column = self.tableWidget.currentColumn()
        columnPositon = self.tableWidget.columnViewportPosition(column)
        columnAt = self.tableWidget.columnAt(columnPositon)
        _str = f'当前row:{row},rowPosition:{rowPositon},rowAt:{rowAt}'+ \
            f'\n当前column:{column},columnPosition:{columnPositon},columnAt:{columnAt}'
        self.text.appendPlainText(_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTableWidgetDemo()
    demo.show()
    sys.exit(app.exec())
