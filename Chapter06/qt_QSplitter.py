import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class SplitterExample(QWidget):
    def __init__(self):
        super(SplitterExample, self).__init__()
        self.setting = {}

        layout = QVBoxLayout(self)
        self.setWindowTitle('QSplitter布局管理例子')

        self.splitter1 = QSplitter()
        self.lineEdit = QLineEdit('lineEdit')
        self.splitter1.addWidget(self.lineEdit)
        self.splitter1.addWidget(QLabel('Label'))
        buttonShow = QPushButton('显/隐lineEdit')
        buttonShow.setCheckable(True)
        buttonShow.toggle()
        buttonShow.clicked.connect(lambda: self.buttonShowClick(buttonShow))
        self.splitter1.addWidget(buttonShow)
        layout.addWidget(self.splitter1)

        fram1 = QFrame()
        fram1.setFrameShape(QFrame.StyledPanel)
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(fram1)
        self.splitter2.addWidget(QTextEdit())
        self.splitter2.setSizes([50, 100])
        layout.addWidget(self.splitter2)

        self.splitter3 = QSplitter(Qt.Horizontal)
        self.splitter3.addWidget(QListView())
        self.splitter3.addWidget(QTreeView())
        self.splitter3.addWidget(QTextEdit())
        self.splitter3.setSizes([50, 100, 150])
        layout.addWidget(self.splitter3)

        buttonSave = QPushButton('SaveState')
        buttonSave.clicked.connect(self.saveSetting)
        buttonRestore = QPushButton('restoreState')
        buttonRestore.clicked.connect(self.restoreSetting)
        layout.addWidget(buttonSave)
        layout.addWidget(buttonRestore)

        self.setLayout(layout)

    def saveSetting(self):
        self.setting.update({"splitter1": self.splitter1.saveState()})
        self.setting.update({"splitter2": self.splitter2.saveState()})
        self.setting.update({"splitter3": self.splitter3.saveState()})

    def restoreSetting(self):
        self.splitter1.restoreState(self.setting["splitter1"])
        self.splitter2.restoreState(self.setting["splitter2"])
        self.splitter3.restoreState(self.setting["splitter3"])

    def buttonShowClick(self, button):
        if button.isChecked():
            self.lineEdit.show()
        else:
            self.lineEdit.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SplitterExample()
    demo.show()
    demo.saveSetting()
    sys.exit(app.exec())
