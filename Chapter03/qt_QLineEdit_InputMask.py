# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QLineEdit的输入掩码例子
  
'''

from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit的输入掩码例子")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH_")
        pDateLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA#")

        flo.addRow("数字掩码", pIPLineEdit)
        flo.addRow("Mac掩码", pMACLineEdit)
        flo.addRow("日期掩码", pDateLineEdit)
        flo.addRow("许可证掩码", pLicenseLineEdit)

        pIPLineEdit.setToolTip("ip: 192.168.*")
        pMACLineEdit.setToolTip("mac: ac:be:ad:*")
        pDateLineEdit.setToolTip("date: 2020-01-01")
        pLicenseLineEdit.setToolTip("许可证: HDFG-ADDB-*")

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec())
