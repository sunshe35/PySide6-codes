# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PySide6.QtCore import  Slot
from PySide6.QtWidgets import QDialog, QApplication, QMessageBox

from Ui_ericDemo import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @Slot(bool)
    def on_pushButton_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        print('测试消息')
        QMessageBox.information(self, "标题", "测试消息")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    demo = Dialog()
    demo.show()
    sys.exit(app.exec())
