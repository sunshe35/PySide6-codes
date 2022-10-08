from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

class QTreeWidgetDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle("QTreeWidget案例")
        self.resize(500, 600)
        self.text = QPlainTextEdit('用来显示QTreeWidget相关信息：')
        self.treeWidget = QTreeWidget()

        layout = QVBoxLayout(self)
        layout.addWidget(self.treeWidget)
        layout.addWidget(self.text)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        self.initItem()

        # selection
        # self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.treeWidget.setMouseTracking(True)

        # 信号与槽
        self.treeWidget.currentItemChanged[QTreeWidgetItem, QTreeWidgetItem].connect(self.onCurrentItemChanged)
        self.treeWidget.itemActivated[QTreeWidgetItem, int].connect(self.onItemActivated)
        self.treeWidget.itemClicked[QTreeWidgetItem, int].connect(self.onItemClicked)
        self.treeWidget.itemDoubleClicked[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemDoubleClicked信号：'))
        self.treeWidget.itemChanged[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemChanged信号：'))
        self.treeWidget.itemEntered[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemEntered信号：'))
        self.treeWidget.itemPressed[QTreeWidgetItem, int].connect(
            lambda item, column: self.text.appendPlainText(f'"{item.text(column)}"触发itemPressed信号：'))
        self.treeWidget.itemSelectionChanged.connect(lambda: self.text.appendPlainText(f'触发itemSelectionChanged信号：'))
        self.treeWidget.clicked.connect(self.onClicked)

    def initItem(self):
        # 设置列数
        self.treeWidget.setColumnCount(3)
        # 设置树形控件头部的标题
        self.treeWidget.setHeaderLabels(['学科', '姓名', '分数'])

        # 设置根节点
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, '学科')
        root.setText(1, '姓名')
        root.setText(2, '分数')
        root.setIcon(0, QIcon('./images/root.png'))

        # 设置根节点的背景颜色
        root.setBackground(0, QBrush(Qt.blue))
        root.setBackground(1, QBrush(Qt.yellow))
        root.setBackground(2, QBrush(Qt.red))

        # 设置树形控件的列的宽度
        self.treeWidget.setColumnWidth(0, 150)

        # 设置子节点1
        for subject in ['语文', '数学', '外语', '综合']:
            child1 = QTreeWidgetItem([subject, '', ''])
            root.addChild(child1)
            # 设置子节点2
            for name in ['张三', '李四', '王五', '赵六']:
                child2 = QTreeWidgetItem()
                child2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
                child2.setText(1, name)
                score = random.random() * 40 + 60
                child2.setText(2, str(score)[:5])
                if score >= 90:
                    child2.setBackground(2, QBrush(Qt.red))
                elif 80 <= score < 90:
                    child2.setBackground(2, QBrush(Qt.darkYellow))
                child1.addChild(child2)

        # 加载根节点的所有属性与子控件
        self.treeWidget.addTopLevelItem(root)

        # 节点全部展开
        self.treeWidget.expandAll()

        # 启用排序
        self.treeWidget.setSortingEnabled(True)

    def onClicked(self, index):
        item = self.treeWidget.currentItem()
        self.text.appendPlainText(f'触发clicked信号，点击了："{item.text(index.column())}"')


    def onCurrentItemChanged(self, current: QTreeWidgetItem, previous: QTreeWidgetItem):
        if previous == None:
            _str = f'触发currentItemChanged信号，当前项:"{current.text(0)}-{current.text(1)}-{current.text(2)}",之前项:None'
        else:
            _str = f'触发currentItemChanged信号，当前项:"{current.text(0)}-{current.text(1)}-{current.text(2)}",之前项:"{previous.text(0)}-{previous.text(1)}-{previous.text(2)}"'
        self.text.appendPlainText(_str)

    def onItemClicked(self, item: QTreeWidgetItem, column: int):
        self.text.appendPlainText(f'"{item.text(column)}"触发itemClicked信号：')
        return

    def onItemActivated(self, item: QTreeWidgetItem, column: int):
        self.text.appendPlainText(f'"{item.text(column)}"触发itemActivated信号：')
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTreeWidgetDemo()
    demo.show()
    sys.exit(app.exec())
