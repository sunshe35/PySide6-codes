from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

class QTreeViewDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTreeViewDemo, self).__init__(parent)
        self.setWindowTitle("QTreeView2案例")
        self.resize(600, 800)
        self.text = QPlainTextEdit('用来显示QTreeView2相关信息：')
        self.treeView = QTreeView()
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.selectModel = QItemSelectionModel()
        self.model.setRootPath(QDir.currentPath())
        self.treeView.setSelectionModel(self.selectModel)

        self.listView = QListView()
        self.tableView = QTableView()
        self.listView.setModel(self.model)
        self.tableView.setModel(self.model)

        layoutV = QVBoxLayout(self)
        layoutV.addWidget(self.listView)
        layoutV.addWidget(self.tableView)

        layout = QHBoxLayout(self)
        layout.addWidget(self.treeView)
        layout.addLayout(layoutV)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        # 信号与槽
        self.treeView.clicked.connect(self.onClicked)

    def onClicked(self, index):
        self.listView.setRootIndex(index)
        self.tableView.setRootIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTreeViewDemo()
    demo.show()
    sys.exit(app.exec())
