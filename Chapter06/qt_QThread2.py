from PySide6.QtCore import Signal, QObject, QThread, Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QPushButton, QHBoxLayout
from PySide6.QtGui import QFont
import sys
import time


class Work(QObject):
    count = int(0)
    countSignal = Signal(int)

    def __init__(self):
        super(Work, self).__init__()

    def work(self):
        self.flag = True
        while self.flag:
            self.count += 1
            self.countSignal.emit(self.count)
            time.sleep(1)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('QThread demo')
        self.resize(515, 208)
        self.widget = QWidget()
        self.buttonStart = QPushButton('开始')
        self.buttonStop = QPushButton('结束')
        self.label = QLabel('0')
        self.label.setFont(QFont("Adobe Arabic", 28))
        self.label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.buttonStart)
        layout.addWidget(self.buttonStop)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStop.clicked.connect(self.onStop)

        self.thread = QThread()
        self.worker = Work()
        self.worker.countSignal.connect(self.flush)

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.work)
        self.thread.finished.connect(self.finished)

    def flush(self, count):
        self.label.setText(str(count))

    def onStart(self):
        self.statusBar().showMessage('button start.')
        self.buttonStart.setEnabled(False)
        self.thread.start()

    def onStop(self):
        self.statusBar().showMessage('button stop.')
        self.worker.flag = False
        self.thread.quit()

    def finished(self):
        self.statusBar().showMessage('多线程finish.')
        self.buttonStart.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec())
