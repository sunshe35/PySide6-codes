import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtPrintSupport import QPrintDialog, QPrinter


class ImageViewer(QMainWindow):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('QPixmap和QImage应用')
        # 设置窗口大小
        self.resize(800, 600)

        # 打印
        self.printer = QPrinter()
        # 缩放因子
        self.scaleFactor = 0.0

        # 创建显示图片的窗口
        self.imgLabel = QLabel()
        self.imgLabel.setBackgroundRole(QPalette.Base)
        self.imgLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imgLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imgLabel)

        self.setCentralWidget(self.scrollArea)

        self.initMenuBar()

    def initMenuBar(self):
        menuBar = self.menuBar()

        # 文件菜单
        menuFile = menuBar.addMenu('文件(&F)')
        actionOpen = QAction('打开(&O)...', self, shortcut='Ctrl+O', triggered=self.onFileOpen)
        self.actionPrint = QAction('打印(&P)...', self, shortcut='Ctrl+P', enabled=False, triggered=self.onFilePrint)
        actionExit = QAction('退出(&X)', self, shortcut='Ctrl+Q', triggered=QApplication.instance().quit)
        menuFile.addAction(actionOpen)
        menuFile.addAction(self.actionPrint)
        menuFile.addSeparator()
        menuFile.addAction(actionExit)

        # 编辑菜单
        menuEdit = menuBar.addMenu('编辑(&E)')
        self.actionCopy = QAction('复制(&C)', self, shortcut='Ctrl+C', enabled=False, triggered=self.onCopy)
        self.actionPaste = QAction('黏贴(&V)', self, shortcut='Ctrl+V', triggered=self.onPaste)
        menuEdit.addAction(self.actionCopy)
        menuEdit.addAction(self.actionPaste)

        # 视图菜单
        menuView = menuBar.addMenu('视图(&V)')
        self.actionZoomIn = QAction('放大(25%)(&I)', self, shortcut='Ctrl++', enabled=False, triggered=self.onViewZoomIn)
        self.actionZoomOut = QAction('缩小(25%)(&O)', self, shortcut='Ctrl+-', enabled=False,
                                     triggered=self.onViewZoomOut)
        self.actionNormalSize = QAction('原始尺寸(&N)', self, shortcut='Ctrl+S', enabled=False,
                                        triggered=self.onViewNormalSize)
        self.actionFitToWindow = QAction('适应窗口(&F)', self, shortcut='Ctrl+F', enabled=False, checkable=True,
                                         triggered=self.onViewFitToWindow)
        menuView.addAction(self.actionZoomIn)
        menuView.addAction(self.actionZoomOut)
        menuView.addAction(self.actionNormalSize)
        menuView.addSeparator()
        menuView.addAction(self.actionFitToWindow)

    # 打开文件
    def onFileOpen(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开文件', QDir.currentPath())
        if filename:
            image = QImage(filename)
            if image.isNull():
                QMessageBox.information(self, '图像浏览器', '不能加载文件%s.' % filename)
                return

            self.imgLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.actionPrint.setEnabled(True)
            self.actionFitToWindow.setEnabled(True)
            self.actionCopy.setEnabled(True)
            self.updateActions()

            if not self.actionFitToWindow.isChecked():
                self.imgLabel.adjustSize()

    # 打印
    def onFilePrint(self):
        dlg = QPrintDialog(self.printer, self)
        if dlg.exec():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imgLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imgLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imgLabel.pixmap())

    # 复制
    def onCopy(self):
        QGuiApplication.clipboard().setPixmap(self.imgLabel.pixmap())

    # 黏贴
    def onPaste(self):
        newPic = QGuiApplication.clipboard().pixmap()
        if newPic.isNull():
            self.statusBar().showMessage("No image in clipboard")
        else:
            self.imgLabel.setPixmap(newPic)
            self.setWindowFilePath('')
            w = newPic.width()
            h = newPic.height()
            d = newPic.depth()
            message = f"Obtained image from clipboard, {w}x{h}, Depth: {d}"
            self.statusBar().showMessage(message)

    # 放大图像
    def onViewZoomIn(self):
        self.scaleIamge(1.25)

    # 缩小图像
    def onViewZoomOut(self):
        self.scaleIamge(0.8)

    def onViewNormalSize(self):
        self.imgLabel.adjustSize()
        self.scaleFactor = 1.0

    # 自适应屏幕
    def onViewFitToWindow(self):
        fitToWindow = self.actionFitToWindow.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.onViewNormalSize()

        self.updateActions()

    def updateActions(self):
        checked = not self.actionFitToWindow.isChecked()
        self.actionZoomIn.setEnabled(checked)
        self.actionZoomOut.setEnabled(checked)
        self.actionNormalSize.setEnabled(checked)

    def scaleIamge(self, factor):
        self.scaleFactor *= factor
        self.imgLabel.resize(self.scaleFactor * self.imgLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.actionZoomIn.setEnabled(self.scaleFactor < 4.0)
        self.actionZoomOut.setEnabled(self.scaleFactor > 0.25)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() + ((factor - 1) * scrollBar.pageStep() / 2)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())
