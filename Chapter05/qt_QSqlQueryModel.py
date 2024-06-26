# -*- coding: utf-8 -*- 

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
import os
os.chdir(os.path.dirname(__file__))

ID, NAME, SUBJECT, SEX, AGE, SCORE, DESCRIBE = range(7)


class SqlQueryModelDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("分页查询案例-只读")
        self.resize(750, 300)
        

        # 创建窗口
        self.createWindow()
        # 设置表格
        self.setTableView()

        # 信号槽连接
        self.firstButton.clicked.connect(self.onFirstButtonClick)
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.lastButton.clicked.connect(self.onLastButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)

        # 上下文菜单
        self.menu = self.generateMenu()
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableView.customContextMenuRequested.connect(self.showMenu)  ####右键菜单

    # 创建窗口
    def createWindow(self):
        # 操作布局
        operatorLayout = QHBoxLayout()
        self.prevButton = QPushButton("前一页")
        self.nextButton = QPushButton("后一页")
        self.firstButton = QPushButton("第一页")
        self.lastButton = QPushButton("最后一页")
        self.switchPageButton = QPushButton("Go")
        self.switchPageLineEdit = QLineEdit()
        self.switchPageLineEdit.setValidator(QIntValidator(self))
        self.switchPageLineEdit.setFixedWidth(40)

        switchPage = QLabel("转到第")
        page = QLabel("页")
        operatorLayout.addWidget(self.firstButton)
        operatorLayout.addWidget(self.prevButton)
        operatorLayout.addWidget(self.nextButton)
        operatorLayout.addWidget(self.lastButton)
        operatorLayout.addWidget(switchPage)
        operatorLayout.addWidget(self.switchPageLineEdit)
        operatorLayout.addWidget(page)
        operatorLayout.addWidget(self.switchPageButton)
        operatorLayout.addWidget(QSplitter())

        # 状态布局
        statusLayout = QHBoxLayout()
        self.totalPageLabel = QLabel()
        self.totalPageLabel.setFixedWidth(70)
        self.currentPageLabel = QLabel()
        self.currentPageLabel.setFixedWidth(70)

        self.totalRecordLabel = QLabel()
        self.totalRecordLabel.setFixedWidth(70)

        statusLayout.addWidget(self.totalPageLabel)
        statusLayout.addWidget(self.currentPageLabel)
        statusLayout.addWidget(QSplitter())
        statusLayout.addWidget(self.totalRecordLabel)

        # 设置表格属性
        self.tableView = QTableView()
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 创建界面
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tableView)
        mainLayout.addLayout(statusLayout)
        self.setLayout(mainLayout)
        
        

    # 设置表格
    def setTableView(self):

        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)

        # 设置当前页
        self.currentPage = 1
        # 每页显示记录数
        self.PageRecordCount = 10
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()
        # 得到总页数
        self.totalPage = int(self.totalRecrodCount / self.PageRecordCount + 0.5)

        # 设置总页数文本
        self.totalPageLabel.setText("总共%d页" % self.totalPage)
        # 设置总记录数
        self.totalRecordLabel.setText("共%d条" % self.totalRecrodCount)

        # 设置模型
        self.tableView.setModel(self.queryModel)

        # 显示首页数据
        self.recordQuery(0)
        # 刷新状态
        self.updateStatus()

        # 设置表头
        self.queryModel.setHeaderData(ID, Qt.Horizontal, "编号")
        self.queryModel.setHeaderData(NAME, Qt.Horizontal, "姓名")
        self.queryModel.setHeaderData(SUBJECT, Qt.Horizontal, "科目")
        self.queryModel.setHeaderData(SEX, Qt.Horizontal, "性别")
        self.queryModel.setHeaderData(AGE, Qt.Horizontal, "年纪")
        self.queryModel.setHeaderData(SCORE, Qt.Horizontal, "成绩")
        self.queryModel.setHeaderData(DESCRIBE, Qt.Horizontal, "说明")

        print('totalRecrodCount=' + str(self.totalRecrodCount))
        print('totalPage=' + str(self.totalPage))

    # 设置上下文菜单
    def generateMenu(self):
        menu = QMenu(self)
        # menu = QMenu(self.tableView)
        self.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # menu.setShortcutEnabled(True)
        menu.addAction(QIcon("images/up.png"), '第一页', self.onFirstButtonClick, QKeySequence(Qt.CTRL | Qt.Key_F))
        menu.addAction(QIcon("images/left.png"), '前一页', self.onPrevButtonClick, QKeySequence(Qt.CTRL | Qt.Key_P))
        menu.addAction(QIcon("images/right.png"), '后一页', self.onNextButtonClick, QKeySequence(Qt.CTRL | Qt.Key_N))
        menu.addAction(QIcon("images/down.png"), '最后一页', self.onLastButtonClick, QKeySequence(Qt.CTRL | Qt.Key_L))
        menu.addSeparator()
        menu.addAction('全选', lambda: self.tableView.selectAll(), QKeySequence(Qt.CTRL | Qt.Key_A))
        menu.addAction('选择行', lambda: self.tableView.selectRow(self.tableView.currentIndex().row()),
                       QKeySequence(Qt.CTRL | Qt.Key_R))
        menu.addAction('选择列', lambda: self.tableView.selectColumn(self.tableView.currentIndex().column()),
                       QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_R))
        for action in menu.actions():
            action.setShortcutContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
        return menu

    def showMenu(self, pos):
        self.menu.exec(QCursor.pos())  # 显示菜单

    # 得到记录数
    def getTotalRecordCount(self):
        self.queryModel.setQuery('select count(*) from student')
        rowCount = self.queryModel.record(0).value(0)
        print('rowCount=' + str(rowCount))
        return rowCount

    # 记录查询
    def recordQuery(self, limitIndex):
        szQuery = ("select * from student limit %d,%d" % (limitIndex, self.PageRecordCount))
        print('query sql=' + szQuery)
        self.queryModel.setQuery(szQuery)

    # 刷新状态
    def updateStatus(self):
        szCurrentText = "当前第%d页" % self.currentPage
        self.currentPageLabel.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.firstButton.setEnabled(False)
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(True)
            self.lastButton.setEnabled(True)
        elif self.currentPage >= self.totalPage - 1:
            self.firstButton.setEnabled(True)
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(False)
            self.lastButton.setEnabled(False)
        else:
            self.firstButton.setEnabled(True)
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(True)
            self.lastButton.setEnabled(True)

    # 第一页按钮按下
    def onFirstButtonClick(self):
        print('*** onFirstButtonClick ')
        self.recordQuery(0)
        self.currentPage = 1
        self.updateStatus()

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ')
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        print('*** onNextButtonClick ')
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 最后一页按钮按下
    def onLastButtonClick(self):
        print('*** onLastButtonClick ')
        limitIndex = (self.totalPage - 1) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage = self.totalPage
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.switchPageLineEdit.text()

        # 是否为空
        if szText == '':
            QMessageBox.information(self, "提示", "请输入跳转页面")
            return

        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount

        # 记录查询
        self.recordQuery(limitIndex)
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    # 打开数据库，该库由qt_createSql.py脚本创建。
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    if db.open() is not True:
        QMessageBox.critical(QWidget, 'open error', '数据库打开失败')
        exit()

    # 创建窗口
    demo = SqlQueryModelDemo()
    # 显示窗口
    demo.show()

    sys.exit(app.exec())
