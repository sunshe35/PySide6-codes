import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlog1 import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    def testSlot(self):
        print('这是一个自定义槽函数，你成功了')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
