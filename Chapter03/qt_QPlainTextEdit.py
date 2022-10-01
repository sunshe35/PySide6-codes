from PySide6.QtWidgets import QApplication, QWidget, QTextEdit,QPlainTextEdit, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QPlainTextEdit 例子")
        self.resize(300, 270)
        self.textEdit = QPlainTextEdit()
        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        # 显示文本
        self.btn_plain = QPushButton("显示纯文本")
        self.btn_plain.clicked.connect(self.btn_plain_Clicked)
        layout.addWidget(self.btn_plain)

        self.setLayout(layout)

    def btn_plain_Clicked(self):
        font = QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setPlainText("Hello Qt for Python!\n单击按钮")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec())
