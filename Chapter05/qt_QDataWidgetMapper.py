from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate
import sys
import os
os.chdir(os.path.dirname(__file__))

class DataWidgetMapperDemo(QMainWindow):

    def __init__(self, parent=None):
        super(DataWidgetMapperDemo, self).__init__(parent)
        self.setWindowTitle("QDataWidgetMapper案例")
        self.resize(550, 500)
        self.initModel()
        self.createWindow()

    def initModel(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("student2")
        self.sexIndex = self.model.fieldIndex('sex')
        self.subjectIndex = self.model.fieldIndex('subject')

        self.model.setRelation(self.sexIndex, QSqlRelation("sex", "id", "name"))
        self.model.setRelation(self.subjectIndex, QSqlRelation("subject", "id", "name"))
        self.model.setHeaderData(0, Qt.Horizontal, "编号")
        self.model.setHeaderData(1, Qt.Horizontal, "姓名")
        self.model.setHeaderData(2, Qt.Horizontal, "性别")
        self.model.setHeaderData(3, Qt.Horizontal, "科目")
        self.model.setHeaderData(4, Qt.Horizontal, "成绩")
        self.model.select()

    def createWindow(self):
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.delegate = QSqlRelationalDelegate(self.tableView)
        self.tableView.setItemDelegate(self.delegate)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.groupBox = QGroupBox()
        self.groupBox.setTitle('详细信息：')
        formLayout = QFormLayout(self.groupBox)

        self.idSpinBox = QSpinBox()
        self.idSpinBox.setMinimum(0)
        formLayout.addRow('编号',self.idSpinBox)

        self.nameEdite = QLineEdit()
        formLayout.addRow('姓名',self.nameEdite)
        self.sexComboBox = QComboBox()
        relationModelSex = self.model.relationModel(self.sexIndex)
        self.sexComboBox.setModel(relationModelSex)
        self.sexComboBox.setModelColumn(relationModelSex.fieldIndex("name"))
        formLayout.addRow('性别',self.sexComboBox)

        self.subjectComboBox = QComboBox()
        relationModelSubject = self.model.relationModel(self.subjectIndex)
        self.subjectComboBox.setModel(relationModelSubject)
        self.subjectComboBox.setModelColumn(relationModelSubject.fieldIndex("name"))
        formLayout.addRow('科目',self.subjectComboBox)
        self.scoreSpinBox = QSpinBox()
        self.scoreSpinBox.setMinimum(0)
        formLayout.addRow('成绩',self.scoreSpinBox)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(self.delegate)
        self.mapper.addMapping(self.idSpinBox, self.model.fieldIndex('id'))
        self.mapper.addMapping(self.nameEdite, self.model.fieldIndex('name'))
        self.mapper.addMapping(self.sexComboBox, self.sexIndex)
        self.mapper.addMapping(self.subjectComboBox, self.subjectIndex)
        self.mapper.addMapping(self.scoreSpinBox, self.model.fieldIndex('score'))
        self.mapper.toFirst()


        selectModel = self.tableView.selectionModel()
        selectModel.currentRowChanged.connect(self.mapper.setCurrentModelIndex)

        layout = QHBoxLayout()
        layout.addWidget(self.tableView)
        layout.addWidget(self.groupBox)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    if db.open() is not True:
        QMessageBox.critical(QWidget(), "警告", "数据连接失败，程序即将退出")
        exit()
    demo = DataWidgetMapperDemo()
    demo.show()
    sys.exit(app.exec())
