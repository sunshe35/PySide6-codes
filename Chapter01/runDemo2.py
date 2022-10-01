# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QPushButton, QApplication, QWidget


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('启动方式2')
        button = QPushButton('Close', self)
        button.clicked.connect(self.close)


if __name__ == "__main__":

    app = QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)

    # 下面两行代码根据需要进行开启。
    # app.aboutToQuit.connect(app.deleteLater)
	# QApplication.setQuitOnLastWindowClosed(True)

    win = WinForm()
    win.show()
    app.exec()
