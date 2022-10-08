from PySide6.QtAxContainer import QAxWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QMainWindow
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt
import os
os.chdir(os.path.dirname(__file__))

class AxWidget(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        w = QWidget()
        self.setCentralWidget(w)
        layout = QVBoxLayout(self)
        w.setLayout(layout)
        self.resize(800, 600)
        self.setWindowTitle('QAxWidget案例')

        bar = self.menuBar()
        file = bar.addMenu("&File")
        file.addAction(QIcon('images/open.png'), "&Open")
        file.addAction("&Browser")
        file.addAction("&Exit")
        file.triggered[QAction].connect(self.fileAction)

        self.axWidget = QAxWidget(self)
        layout.addWidget(self.axWidget)


    def fileAction(self, q):
        if q.text() == "&Open":
            self.openFile()
        elif q.text() == "&Browser":
            self.browser()
        elif q.text() == '&Exit':
            QApplication.instance().quit()

    def browser(self):
        print('打开ie浏览器')
        # 设置ActiveX控件为IE Microsoft Web Browser
        # 设置ActiveX控件的id，最有效的方式就是使用UUID
        # 此处的{8856F961-340A-11D0-A96B-00C04FD705A2}就是Microsoft Web Browser控件的UUID
        self.axWidget.clear()
        self.axWidget.setControl("{8856f961-340a-11d0-a96b-00c04fd705a2}")
        self.axWidget.setObjectName("webWidget") # 设置控件的名称
        self.axWidget.setFocusPolicy(Qt.StrongFocus) # 设置控件接收键盘焦点的方式：鼠标单击、Tab键
        self.axWidget.setProperty("DisplayAlerts", False) # 不显示任何警告信息。
        self.axWidget.setProperty("DisplayScrollBars", True) # 显示滚动条
        self.axWidget.setProperty("Silent", True)

        # sUrl = "www.baidu.com"
        # self.axWidget.dynamicCall(f"Navigate({sUrl})")
        # self.axWidget.dynamicCall('GoHome()')
        # self.axWidget.dynamicCall("Navigate(const QString&)",'www.baidu.com')
        # self.axWidget.dynamicCall("Navigate(\"www.baidu.com\")")
        self.axWidget.dynamicCall("Navigate(www.baidu.com)")

    def openFile(self):

        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls);;word(*.docx *.doc);;pdf(*.pdf)')
        print('openFile', path)
        if not path:
            return
        if _.find('*.doc'):
            return self.openOffice(path, 'Word.Application')
        elif _.find('*.xls'):
            return self.openOffice(path, 'Excel.Application')
        elif _.find('*.pdf'):
            return self.openPdf(path)
        else:
            self.axWidget.clear()
            self.axWidget.dynamicCall('SetVisible (bool Visible)', 'false')  # 不显示窗体
            self.axWidget.setControl(path)


    def openOffice(self, path, app):
        self.axWidget.clear()
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, '错误', '没有安装  %s' % app)
        self.axWidget.dynamicCall('SetVisible (bool Visible)', 'false')  # 不显示窗体
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)

    def openPdf(self, path):
        self.axWidget.clear()
        if not self.axWidget.setControl('Adobe PDF Reader'):
            return QMessageBox.critical(self, '错误', '没有安装 Adobe PDF Reader')
        self.axWidget.dynamicCall('LoadFile(const QString&)', path)

    def closeEvent(self, event):
        self.axWidget.close()
        self.axWidget.clear()
        self.layout().removeWidget(self.axWidget)
        del self.axWidget
        super(AxWidget, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = AxWidget()
    w.show()
    sys.exit(app.exec())
