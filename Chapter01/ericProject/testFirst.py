# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PySide6.QtCore import  Slot
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox


from Ui_testFirst import Ui_Form


class Form(QWidget, Ui_Form):
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
        # TODO: not implemented yet
        print('测试消息')
        QMessageBox.information(self, "标题", "测试消息")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    demo = Form()
    demo.show()
    sys.exit(app.exec())
