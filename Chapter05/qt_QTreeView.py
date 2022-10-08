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
        self.setWindowTitle("QTreeView案例")
        self.resize(500, 600)
        self.text = QPlainTextEdit('用来显示QTreeView相关信息：')
        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)
        self.selectModel = QItemSelectionModel()
        self.treeView.setSelectionModel(self.selectModel)
        # 对照组
        self.treeView2 = QTreeView()
        self.treeView2.setModel(self.model)

        layout = QVBoxLayout(self)
        layout.addWidget(self.treeView)
        layout.addWidget(self.text)
        layout.addWidget(self.treeView2)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        self.initItem()

        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.treeView.setMouseTracking(True)

        # 信号与槽
        self.treeView.clicked.connect(self.onClicked)
        self.treeView.collapsed[QModelIndex].connect(lambda index :self.text.appendPlainText(f'{self.model.data(index)}: 触发了collapsed信号'))
        self.treeView.expanded[QModelIndex].connect(lambda index :self.text.appendPlainText(f'{self.model.data(index)}: expanded信号'))

    def initItem(self):
        # 设置列数
        self.model.setColumnCount(3)
        # 设置树形控件头部的标题
        self.model.setHorizontalHeaderLabels(['学科', '姓名', '分数'])


        # 设置根节点
        root = QStandardItem('学科')
        rootList = [root, QStandardItem('姓名'), QStandardItem('分数')]
        self.model.appendRow(rootList)

        # 设置图标
        root.setIcon(QIcon('./images/root.png'))

        # 设置根节点的背景颜色
        root.setBackground(QBrush(Qt.blue))
        rootList[1].setBackground(QBrush(Qt.yellow))
        rootList[2].setBackground(QBrush(Qt.red))

        # 一级节点
        for subject in ['语文', '数学', '外语', '综合']:
            itemSubject = QStandardItem(subject)
            root.appendRow([itemSubject, QStandardItem(), QStandardItem()])

            # 二级节点
            for name in ['张三', '李四', '王五', '赵六']:
                itemName = QStandardItem(name)
                itemName.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
                score = random.random() * 40 + 60
                itemScore = QStandardItem(str(score)[:5])
                if score >= 90:
                    itemScore.setBackground(QBrush(Qt.red))
                elif 80 <= score < 90:
                    itemScore.setBackground(QBrush(Qt.darkYellow))
                itemSubject.appendRow([QStandardItem(subject), itemName, itemScore])

        # 设置树形控件的列的宽度
        self.treeView.setColumnWidth(0, 150)

        # 节点全部展开
        self.treeView.expandAll()

        # 启用排序
        self.treeView.setSortingEnabled(True)

    def onClicked(self, index):
        text = self.model.data(index)
        self.text.appendPlainText(f'触发clicked信号，点击了："{text}"')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTreeViewDemo()
    demo.show()
    sys.exit(app.exec())
