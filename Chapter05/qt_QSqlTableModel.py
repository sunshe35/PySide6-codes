from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import sys
import os
os.chdir(os.path.dirname(__file__))

class QTableViewDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTableViewDemo, self).__init__(parent)
        self.setWindowTitle("QSqlTableModel案例")
        self.resize(500, 600)

        self.createTable()
        self.createWindow()
        self.onUpdate()

    def createWindow(self):

        # 排序：字段排序
        labelSort = QLabel('排序:')
        self.comboBoxSort = QComboBox()
        self.comboBoxSort.addItems(self.fieldList)
        self.comboBoxSort.setCurrentText(self.fieldList[0])
        layoutSort = QHBoxLayout()
        layoutSort.addWidget(labelSort)
        layoutSort.addWidget(self.comboBoxSort)
        self.comboBoxSort.currentIndexChanged.connect(lambda: self.onSort(self.sortType))

        # 排序：升序 or 降序
        buttonGroupSort = QButtonGroup(self)
        radioAsecend = QRadioButton("升序")
        radioAsecend.setChecked(True)
        buttonGroupSort.addButton(radioAsecend)
        radioDescend = QRadioButton("降序")
        buttonGroupSort.addButton(radioDescend)
        layoutSort.addWidget(radioAsecend)
        layoutSort.addWidget(radioDescend)
        buttonGroupSort.buttonClicked.connect(lambda button: self.onSort(button.text()))

        # 性别筛选按钮
        buttonGroupSex = QButtonGroup(self)
        layoutSexButton = QHBoxLayout()
        layoutSexButton.addWidget(QLabel('性别:'))
        radioAll = QRadioButton("All")
        radioAll.setChecked(True)
        buttonGroupSex.addButton(radioAll)
        layoutSexButton.addWidget(radioAll)
        radioMen = QRadioButton("男")
        buttonGroupSex.addButton(radioMen)
        layoutSexButton.addWidget(radioMen)
        radioWomen = QRadioButton("女")
        buttonGroupSex.addButton(radioWomen)
        layoutSexButton.addWidget(radioWomen)
        buttonGroupSex.buttonClicked.connect(self.onFilterSex)

        # 科目过滤
        labelSubject = QLabel('科目:')
        self.comboBoxSubject = QComboBox()
        self.comboBoxSubject.addItems(['All', '语文', '数学', '外语', '综合'])
        self.comboBoxSubject.setCurrentText('All')
        self.comboBoxSubject.currentTextChanged.connect(self.onSubjectChange)
        layoutSubject = QHBoxLayout()
        layoutSubject.addWidget(labelSubject)
        layoutSubject.addWidget(self.comboBoxSubject)

        # 第一排按钮管理
        layoutOne = QHBoxLayout()
        layoutOne.addLayout(layoutSort)
        layoutOne.addLayout(layoutSexButton)
        layoutOne.addLayout(layoutSubject)
        layoutOne.addStretch(1)

        # 增删按钮管理
        self.buttonAddRow = QPushButton('增加行')
        self.buttonInsertRow = QPushButton('插入行')
        self.buttonDeleteRow = QPushButton('删除行')
        self.buttonAddRow.clicked.connect(self.onAdd)
        self.buttonInsertRow.clicked.connect(self.onInsert)
        self.buttonDeleteRow.clicked.connect(self.onDelete)
        layoutEdit = QHBoxLayout()
        layoutEdit.addWidget(self.buttonAddRow)
        layoutEdit.addWidget(self.buttonInsertRow)
        layoutEdit.addWidget(self.buttonDeleteRow)

        layoutEdit.addStretch(1)
        # 明细标签
        self.labelCount = QLabel('共xxx行')
        self.labelCurrent = QLabel('row:,col:')
        layoutEdit.addWidget(self.labelCurrent)
        layoutEdit.addWidget(self.labelCount)
        selectModel = self.tableView.selectionModel()
        selectModel.currentChanged.connect(self.onCurrentChange)

        # 汇总管理
        layout = QVBoxLayout(self)
        layout.addLayout(layoutOne)
        layout.addWidget(self.tableView)
        layout.addLayout(layoutEdit)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    def createTable(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./db/database.db')
        if self.db.open() is not True:
            QMessageBox.critical(self, "警告", "数据连接失败，程序即将退出")
            exit()

        self.model = QSqlTableModel()
        self.model.setTable('student')
        self.model.setHeaderData(0, Qt.Horizontal, "编号")
        self.model.setHeaderData(1, Qt.Horizontal, "姓名")
        self.model.setHeaderData(2, Qt.Horizontal, "科目")
        self.model.setHeaderData(3, Qt.Horizontal, "性别")
        self.model.setHeaderData(4, Qt.Horizontal, "年纪")
        self.model.setHeaderData(5, Qt.Horizontal, "成绩")
        self.model.setHeaderData(6, Qt.Horizontal, "说明")
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        # 初始化数据表
        self.model.select()

        fileRecord = self.model.record()
        self.fieldList = []
        for i in range(fileRecord.count()):
            name = fileRecord.fieldName(i)
            self.fieldList.append(name)
        self.filterSex = ''  # 性别选择
        self.sortType = '升序'  # 升序 or 降序
        self.filterSubject = ''  # 科目选择

        self.tableView = QTableView()

        self.tableView.setModel(self.model)
        # self.selectModel = QItemSelectionModel()
        # self.tableView.setSelectionModel(self.selectModel)
        # 表格宽度的自适应调整
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def onAdd(self):
        self.tableView.scrollToBottom()
        rowCount = self.model.rowCount()
        self.model.insertRow(rowCount)

    def onInsert(self):
        index = self.tableView.currentIndex()
        row = index.row()
        self.model.insertRow(row)

    def onDelete(self):
        index = self.tableView.currentIndex()
        row = index.row()
        self.model.removeRow(row)

    def onCurrentChange(self, current: QModelIndex, previous: QModelIndex):
        self.labelCurrent.setText(f'row:{current.row()},col:{current.column()}')

    def onUpdate(self):
        if self.filterSex == '' and self.filterSubject == '':
            textFilter = ''
        elif self.filterSex != '' and self.filterSubject != '':
            textFilter = self.filterSex + ' and ' + self.filterSubject
        else:
            textFilter = self.filterSex + self.filterSubject
        self.model.setFilter(textFilter)

        if self.sortType == '升序':
            self.model.setSort(self.comboBoxSort.currentIndex(), Qt.AscendingOrder)
        else:
            self.model.setSort(self.comboBoxSort.currentIndex(), Qt.DescendingOrder)
        self.model.select()

        self.labelCount.setText(f'共 {self.model.rowCount()} 行')

    def onSort(self, sortType='升序'):
        self.sortType = sortType
        self.onUpdate()

    def onFilterSex(self, button: QRadioButton):
        text = button.text()
        if text != 'All':
            self.filterSex = f'sex="{button.text()}"'
        else:
            self.filterSex = ''
        self.onUpdate()

    def onSubjectChange(self, text):
        if text != 'All':
            self.filterSubject = f'subject="{text}"'
        else:
            self.filterSubject = ''
        self.onUpdate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTableViewDemo()
    demo.show()
    sys.exit(app.exec())
