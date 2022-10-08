from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate
import sys
import os
os.chdir(os.path.dirname(__file__))

class SqlRelationalTableDemo(QMainWindow):

    def __init__(self, parent=None):
        super(SqlRelationalTableDemo, self).__init__(parent)
        self.setWindowTitle("QSqlRelationalTableModel案例")
        self.resize(550, 600)
        self.initModel()
        self.createWindow()

    def initModel(self):
        self.model = QSqlRelationalTableModel()
        self.model.setTable("student2")
        self.model.setRelation(2, QSqlRelation("sex", "id", "name"))
        self.model.setRelation(3, QSqlRelation("subject", "id", "name"))
        self.model.setHeaderData(0, Qt.Horizontal, "编号")

        self.model.setHeaderData(1, Qt.Horizontal, "姓名")
        self.model.setHeaderData(2, Qt.Horizontal, "性别")
        self.model.setHeaderData(3, Qt.Horizontal, "科目")
        self.model.setHeaderData(4, Qt.Horizontal, "成绩")
        self.model.select()

    def createWindow(self):
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(QSqlRelationalDelegate(self.tableView))
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableView2 = QTableView()
        self.tableView2.setModel(self.model)
        self.tableView2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableView3 = QTableView()
        model3 = QSqlRelationalTableModel()
        model3.setTable('student2')
        model3.select()
        self.tableView3.setModel(model3)
        self.tableView3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        layout.addSpacing(10)
        layout.addWidget(self.tableView2)
        layout.addSpacing(10)
        layout.addWidget(self.tableView3)
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
    demo = SqlRelationalTableDemo()
    demo.show()
    sys.exit(app.exec())
