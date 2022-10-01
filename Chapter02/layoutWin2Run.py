# -*- coding: utf-8 -*-

"""
Module implementing LayoutDemo.
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication
from  layoutWin2 import Ui_LayoutDemo


class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @Slot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max:', self.doubleSpinBox_sharp_max.text())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec())
