"""PySide6 QWebEngineView Example"""

import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QLineEdit,
                               QMainWindow, QPushButton, QToolBar, QToolButton, QMessageBox)
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
os.chdir(os.path.dirname(__file__))

class WebEngineView(QWebEngineView):
    windowList = []  # 创建一个容器存储每个窗口，不然会崩溃，因为是createwindow函数里面的临时变量

    def createWindow(self, QWebEnginePage_WebWindowType):
        newWin = MainWindow()
        availableGeometry = mainWin.screen().availableGeometry()
        newWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
        newWin.show()
        self.windowList.append(newWin)
        return newWin.webEngineView


class MainWindow(QMainWindow):

    def __init__(self, homeUrl='http://www.baidu.com'):
        super().__init__()

        self.setWindowTitle('PySide6 QWebEngineView Example')
        self.inintToolBar(homeUrl)
        self.initWeb(homeUrl)

    def inintToolBar(self, homeUrl):
        self.toolBar = QToolBar()
        self.addToolBar(self.toolBar)
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('images/go-previous.png'))
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)
        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon('images/go-home.png'))
        self.homeButton.clicked.connect(lambda: self.webEngineView.load(homeUrl))
        self.toolBar.addWidget(self.homeButton)
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon('images/go-next.png'))
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)
        self.refreshButton = QPushButton()
        self.refreshButton.setIcon(QIcon('images/view-refresh.png'))
        self.refreshButton.clicked.connect(self.load)
        self.toolBar.addWidget(self.refreshButton)

        self.jsButton = QToolButton()
        self.jsButton.setText('runJS1')
        self.jsButton.clicked.connect(self.runJS1)
        self.toolBar.addWidget(self.jsButton)

        self.jsButton2 = QToolButton()
        self.jsButton2.setText('runJS2')
        self.jsButton2.clicked.connect(self.runJS2)
        self.toolBar.addWidget(self.jsButton2)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.addressLineEdit)

    def initWeb(self, homeUrl):
        self.webEngineView = WebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.addressLineEdit.setText(homeUrl)
        self.webEngineView.load(QUrl(homeUrl))
        self.webEngineView.titleChanged.connect(self.setWindowTitle)
        self.webEngineView.iconChanged.connect(self.setWindowIcon)
        self.webEngineView.urlChanged.connect(self.urlChanged)

        self.webEngineView.loadStarted.connect(lambda: self.statusBar().showMessage(f'触发loadStarted信号'))
        self.webEngineView.loadProgress.connect(lambda x: self.statusBar().showMessage(f'触发loadProgress信号,结果{x}'))
        self.webEngineView.loadFinished.connect(lambda x: self.statusBar().showMessage(f'触发loadFinished信号,结果{x}'))

    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def back(self):
        self.webEngineView.triggerPageAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())

    def runJS1(self):
        title = self.webEngineView.title()
        string = f'alert("当前标题是：{title}");'
        self.webEngineView.page().runJavaScript(string)

    def runJS2(self):
        string = '''
        function myFunction()
        {
            return document.title;
        }
        myFunction();
        '''

        def jsCallback(result):
            QMessageBox.information(self, "当前title", str(result))

        self.webEngineView.page().runJavaScript(string, 0, jsCallback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = mainWin.screen().availableGeometry()
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec())
