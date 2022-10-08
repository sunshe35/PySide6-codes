from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
from PySide6.QtGui import QColor,QFont
import sys
import os
os.chdir(os.path.dirname(__file__))

class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300, 270)
        self.textEdit = QTextEdit()
        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)

        # 显示文本
        self.btn_plain = QPushButton("显示纯文本")
        self.btn_plain.clicked.connect(self.btn_plain_Clicked)
        layout.addWidget(self.btn_plain)

        # 显示html
        self.btn_html = QPushButton("显示HTML")
        self.btn_html.clicked.connect(self.btn_html_Clicked)
        layout.addWidget(self.btn_html)

        # 显示markdown
        self.btn_markdown = QPushButton("显示markdown")
        self.btn_markdown.clicked.connect(self.btn_markdown_Clicked)
        layout.addWidget(self.btn_markdown)


        self.setLayout(layout)

    def btn_plain_Clicked(self):
        self.textEdit.setFontItalic(True)
        self.textEdit.setFontWeight(QFont.ExtraBold)
        self.textEdit.setFontUnderline(True)
        self.textEdit.setFontFamily('宋体')
        self.textEdit.setFontPointSize(15)
        self.textEdit.setTextColor(QColor(200,75,75))
        # self.textEdit.setText('Hello Qt for Python!\n单击按钮')
        self.textEdit.setPlainText("Hello Qt for Python!\n单击按钮")


    def btn_html_Clicked(self):
        a = ''

        dirname = _path = os.path.dirname(__file__)
        with open(dirname+'\support\myhtml.html', 'r', encoding='utf8') as f:
            a = f.read()
        self.textEdit.setHtml(a)



    def btn_markdown_Clicked(self):
        a = ''
        dirname = _path = os.path.dirname(__file__)
        with open(dirname+'\support\myMarkDown.md', 'r', encoding='utf8') as f:
            a = f.read()
        self.textEdit.setMarkdown(a)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec())
