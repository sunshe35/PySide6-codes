# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QDialog 例子,扩展对话框
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class FindDialog(QDialog):

    def __init__(self, parent=None):
        super(FindDialog, self).__init__(parent)
        self.setWindowTitle("Extension")

        # topLeft: label+LineEdit
        label = QLabel("Find w&hat:")
        lineEdit = QLineEdit()
        label.setBuddy(lineEdit)
        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(lineEdit)

        # left: topLeft + QCheckBox * 2
        caseCheckBox = QCheckBox("Match &case")
        fromStartCheckBox = QCheckBox("Search from &start")
        fromStartCheckBox.setChecked(True)
        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(caseCheckBox)
        leftLayout.addWidget(fromStartCheckBox)

        # topRight: QPushButton * 2
        findButton = QPushButton("&Find")
        findButton.setDefault(True)
        moreButton = QPushButton("&More")
        moreButton.setCheckable(True)
        moreButton.setAutoDefault(False)
        buttonBox = QDialogButtonBox(Qt.Orientation.Vertical)
        buttonBox.addButton(findButton, QDialogButtonBox.ButtonRole.ActionRole)
        buttonBox.addButton(moreButton, QDialogButtonBox.ButtonRole.ActionRole)

        # hide QWidge
        extension = QWidget()
        extensionLayout = QVBoxLayout()
        extension.setLayout(extensionLayout)
        extension.hide()
        # hide QWidge: QCheckBox * 3
        wholeWordsCheckBox = QCheckBox("&Whole words")
        backwardCheckBox = QCheckBox("Search &backward")
        searchSelectionCheckBox = QCheckBox("Search se&lection")
        extensionLayout.setContentsMargins(QMargins())
        extensionLayout.addWidget(wholeWordsCheckBox)
        extensionLayout.addWidget(backwardCheckBox)
        extensionLayout.addWidget(searchSelectionCheckBox)

        # mainLayout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addWidget(buttonBox, 0, 1)
        mainLayout.addWidget(extension, 1, 0, 1, 2)
        mainLayout.setRowStretch(2, 1)
        self.setLayout(mainLayout)

        # signal & slot
        moreButton.toggled.connect(extension.setVisible)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = FindDialog()
    demo.show()
    sys.exit(app.exec())
