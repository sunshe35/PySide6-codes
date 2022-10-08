import sys
from PySide6.QtWidgets import (QApplication, QWidget,QMainWindow
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout,QFrame,QLabel)
from PySide6.QtCore import QUrl
import urllib
import os
os.chdir(os.path.dirname(__file__))
class TextBrowser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("在这里添加你想要的数据，回车确认")
        self.lineEdit.returnPressed.connect(self.append_text)

        self.textBrowser = QTextBrowser()
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setSource(QUrl(r'.\support\textBrowser.html'))
        self.textBrowser.anchorClicked.connect(lambda url:self.statusBar().showMessage('你点击了url'+urllib.parse.unquote(url.url()),3000))
        self.textBrowser.historyChanged.connect(self.show_anchor)

        self.back_btn = QPushButton('Back')
        self.forward_btn = QPushButton('Forward')
        self.home_btn = QPushButton('Home')
        self.clear_btn = QPushButton('Clear')

        self.back_btn.pressed.connect(self.textBrowser.backward)
        self.forward_btn.pressed.connect(self.textBrowser.forward)
        self.clear_btn.pressed.connect(self.clear_text)
        self.home_btn.pressed.connect(self.textBrowser.home)

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.textBrowser)
        frame = QFrame()
        layout.addWidget(frame)

        self.text_show = QTextBrowser()
        self.text_show.setMaximumHeight(70)
        layout.addWidget(self.text_show)

        layout_frame = QHBoxLayout()
        layout_frame.addWidget(self.back_btn)
        layout_frame.addWidget(self.forward_btn)
        layout_frame.addWidget(self.home_btn)
        layout_frame.addWidget(self.clear_btn)
        frame.setLayout(layout_frame)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        self.setWindowTitle('QTextBrowser 案例')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.lineEdit.text()
        self.textBrowser.append(text)
        self.lineEdit.clear()

    def show_anchor(self):
        back = urllib.parse.unquote(self.textBrowser.historyUrl(-1).url())
        now = urllib.parse.unquote(self.textBrowser.historyUrl(0).url())
        forward = urllib.parse.unquote(self.textBrowser.historyUrl(1).url())
        _str = f'上一个url:{back},<br>当前url:{now},<br>下一个url:{forward}'
        self.text_show.setText(_str)

    def clear_text(self):
        self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextBrowser()
    sys.exit(app.exec())