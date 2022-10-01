# -*- coding: utf-8 -*-
"""
介绍布局管理的综合案例
"""

import sys
from PySide6.QtWidgets import *


class LayoutDemo(QDialog):
    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)

        self.NumGridRows = 3
        self.NumButtons = 4

        self.createMenu()
        self.createHorizontalGroupBox()
        self.createGridGroupBox()
        self.createFormGroupBox()

        # ! [1]
        bigEditor = QTextEdit()
        bigEditor.setPlainText("This widget takes up all the remaining space in the top-level layout.")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        # ! [1]

        # ! [2]
        mainLayout = QVBoxLayout()
        # ! [2] #! [3]
        mainLayout.setMenuBar(self.menuBar)
        # ! [3] #! [4]
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(bigEditor)
        mainLayout.addWidget(buttonBox)
        # ! [4] #! [5]
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Layouts")

    # ! [6]
    def createMenu(self):
        self.menuBar = QMenuBar()

        fileMenu = QMenu("&File", self)
        exitAction = fileMenu.addAction("E&xit")
        self.menuBar.addMenu(fileMenu)
        exitAction.triggered.connect(self.accept)


    # ! [6]

    # ! [7]
    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox("Horizontal layout")
        layout = QHBoxLayout()
        for i in range(0, self.NumButtons):
            button = QPushButton("Button %d" % (i + 1))
            layout.addWidget(button)
        self.horizontalGroupBox.setLayout(layout)

    # ! [7]

    # ! [8]
    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Grid layout")
        # ! [8]
        layout = QGridLayout()

        # ! [9]
        for i in range(0, self.NumGridRows):
            label = QLabel("Line %d:" % (i + 1))
            lineEdit = QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(lineEdit, i + 1, 1)

        # ! [9] #! [10]
        smallEditor = QTextEdit()
        smallEditor.setPlainText("This widget takes up about two thirds of the grid layout.")
        layout.addWidget(smallEditor, 0, 2, 4, 1)
        # ! [10]

        # ! [11]
        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)

    # ! [12]
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Line 1:"), QLineEdit())
        layout.addRow(QLabel("Line 2, long text:"), QComboBox())
        layout.addRow(QLabel("Line 3:"), QSpinBox())
        self.formGroupBox.setLayout(layout)
    # ! [12]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LayoutDemo()
    demo.show()
    sys.exit(app.exec())
