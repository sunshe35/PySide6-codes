import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MdiAreaDemo(QMainWindow):

    def __init__(self, parent=None):
        super(MdiAreaDemo, self).__init__(parent)
        self.count = 0
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.setWindowTitle("QMdiArea+QMdiSubWindow demo")

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("ShowSubList")
        file.addSeparator()
        file.addAction("cascade")
        file.addAction("Tiled")
        file.addSeparator()
        self.nextAct = QAction('Next')
        self.nextAct.setShortcuts(QKeySequence.New)
        self.nextAct.triggered.connect(self.mdi.activateNextSubWindow)
        file.addAction(self.nextAct)
        self.preAct = QAction('Pre')
        self.preAct.setShortcuts(QKeySequence(Qt.CTRL | Qt.Key_P))
        self.preAct.triggered.connect(self.mdi.activatePreviousSubWindow)
        file.addAction(self.preAct)
        file.triggered[QAction].connect(self.windowaction)
        file.addSeparator()
        order = file.addMenu('setOrder')
        order.addAction('create')
        order.addAction('stack')
        order.addAction('activateHistory')
        order.triggered[QAction].connect(self.orderAction)
        file.addSeparator()
        view = file.addMenu('setViewMode')
        view.addAction('subWindow')
        view.addAction('tabWindow')
        view.triggered[QAction].connect(self.viewAction)

        self.text = QPlainTextEdit()
        self.text.setWindowTitle('显示信息')
        self.text.resize(400, 600)
        self.text.move(100, 200)
        self.text.show()

        # 添加QWidget窗口
        widget = QWidget()
        textEdit = QTextEdit(widget)
        layout1 = QHBoxLayout()
        layout1.addWidget(textEdit)
        widget.setLayout(layout1)
        widget.setWindowTitle('QWidget窗口')
        widget.resize(300, 400)
        self.mdi.addSubWindow(widget)

        # 添加QWidget窗口2
        widget2 = QWidget()
        textEdit2 = QTextEdit()
        mdiWidget = self.mdi.addSubWindow(widget2)
        mdiWidget.setWidget(textEdit2)
        mdiWidget.setWindowTitle('QWidget窗口2')

        # 添加QWidget窗口3
        mdiWidget2 = self.mdi.addSubWindow(QTextEdit())
        mdiWidget2.setWindowTitle('QWidget窗口3')

        # 添加QMdiSubWindow窗口
        mdiSub = self.getMdiSubWindow(title='QMdiSubWindow窗口')
        self.mdi.addSubWindow(mdiSub)

        # 添加窗口-shaded
        mdiSub2 = self.getMdiSubWindow(title='shaded窗口')
        self.mdi.addSubWindow(mdiSub2)
        mdiSub2.showShaded()

        # 添加窗口-Option
        mdiSub3 = self.getMdiSubWindow(title='Option窗口')
        mdiSub3.setOption(mdiSub3.RubberBandMove, on=True)
        mdiSub3.setOption(mdiSub3.RubberBandResize, on=True)
        self.mdi.addSubWindow(mdiSub3)

        self.mdi.subWindowActivated.connect(lambda x: self.text.insertPlainText(f'\n触发subWindowActivated信号,title:{x.windowTitle() if x !=None else x}'))
        self.showInfo()


    def getMdiSubWindow(self, title=''):
        mdiSub = QMdiSubWindow()
        mdiSub.setWidget(QTextEdit())
        mdiSub.setWindowTitle(title)
        mdiSub.aboutToActivate.connect(lambda : self.text.insertPlainText(f'\n触发aboutToActivate信号,title:{title}'))
        mdiSub.windowStateChanged.connect(lambda old,new:self.text.insertPlainText(f'\n触发windowStateChanged信号,title:{title},old:{self.getState(old)},new:{self.getState(new)}'))
        return mdiSub

    def getState(self,status):
        if status ==  Qt.WindowState.WindowNoState:
            return 'WindowNoState'
        elif status ==  Qt.WindowState.WindowMinimized:
            return 'WindowMinimized'
        elif status ==  Qt.WindowState.WindowMaximized:
            return 'WindowMaximized'
        elif status ==  Qt.WindowState.WindowMaximized:
            return 'WindowMaximized'
        elif status ==  Qt.WindowState.WindowActive:
            return 'WindowActive'
        else:
            return 'None'



    def windowaction(self, q):
        if q.text() == "New":
            self.count = self.count + 1
            sub = self.getMdiSubWindow(title="NewWindow" + str(self.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()
        elif q.text() == 'ShowSubList':
            self.showInfo()

    def orderAction(self, q):
        if q.text() == 'create':
            self.mdi.setActivationOrder(self.mdi.CreationOrder)
        elif q.text() == 'stack':
            self.mdi.setActivationOrder(self.mdi.StackingOrder)
        elif q.text() == 'activateHistory':
            self.mdi.setActivationOrder(self.mdi.ActivationHistoryOrder)
        self.showInfo()

    def viewAction(self, q):
        if q.text() == 'subWindow':
            self.mdi.setViewMode(self.mdi.SubWindowView)
        elif q.text() == 'tabWindow':
            self.mdi.setViewMode(self.mdi.TabbedView)

    def showInfo(self):
        orderList = self.mdi.subWindowList(order=self.mdi.activationOrder())

        self.text.insertPlainText(f'\n当前排序方式：{self.mdi.activationOrder().name}，最新subWindowList:')

        count = 1
        for subWindow in orderList:
            title = subWindow.windowTitle()
            title = title.split('--')[1] if '--' in title else title
            subWindow.setWindowTitle(f'{count}--{title}')
            print(f'\nnum:{count},title:{subWindow.windowTitle()},shaded:{subWindow.isShaded()}')
            self.text.insertPlainText(f'\nnum:{count},title:{subWindow.windowTitle()},shaded:{subWindow.isShaded()}')
            count += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MdiAreaDemo()
    demo.show()
    sys.exit(app.exec())
