import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DockWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockWidgetDemo, self).__init__(parent)
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("&File")
        file.addAction("&New")
        file.addAction("&Save")
        file.addAction("&Quit")
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setLayout(layout)
        self.setWindowTitle("QDockWidget例子")

        self.createDock1Window()
        self.createDock2Window()
        self.createDock3Window()
        self.createDock4Window()
        self.createDock5Window()

        file.triggered.connect(lambda x:self.textEdit.insertPlainText(f'\n点击了菜单：{x.text()}'))
        self.textEdit.clear()

    def createDockWidget(self, title='', n=1):
        dockWidget = QDockWidget(title, self)
        listWidget = QListWidget()
        listWidget.addItem(f"dock{n}-item1")
        listWidget.addItem(f"dock{n}-item2")
        listWidget.addItem(f"dock{n}-item3")
        listWidget.currentTextChanged.connect(lambda x: self.textEdit.insertPlainText(f'\n点击了{x}'))
        dockWidget.setWidget(listWidget)
        dockWidget.dockLocationChanged.connect(lambda x: self.textEdit.insertPlainText(f'\ndockLocationChanged信号：{x}'))
        dockWidget.featuresChanged.connect(lambda x: self.textEdit.insertPlainText(f'\nfeaturesChanged信号：{x}'))
        dockWidget.topLevelChanged.connect(lambda x: self.textEdit.insertPlainText(f'\ntopLevelChanged信号：{x}'))
        return dockWidget

    def createDock1Window(self):
        dockWidget1 = self.createDockWidget(title="Dockable1-默认", n=1)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget1)

    def createDock2Window(self):
        dockWidget2 = self.createDockWidget(title="Dockable2-限制停靠区域:右|下", n=2)
        dockWidget2.setAllowedAreas(Qt.RightDockWidgetArea | Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget2)

    def createDock3Window(self):
        dockWidget3 = self.createDockWidget(title="Dockable3-浮动", n=3)
        dockWidget3.setFloating(True)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget3)

    def createDock4Window(self):
        dockWidget4 = self.createDockWidget(title="Dockable4-关闭/移动/左侧栏", n=4)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget4)
        dockWidget4.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable|QDockWidget.DockWidgetVerticalTitleBar)

    def createDock5Window(self):
        dockWidget5 = self.createDockWidget(title="Dockable5-修改自定义标题", n=5)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget5)
        dockWidget5.setTitleBarWidget(QLabel('Dockable5-使用自定义标题',self))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockWidgetDemo()
    demo.show()
    sys.exit(app.exec())
