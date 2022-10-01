import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DialogButtonBox(QWidget):
    def __init__(self):
        super(DialogButtonBox, self).__init__()
        self.setWindowTitle("QDialogButtonBox 例子")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel('显示信息')
        layout.addWidget(self.label)

        buttonBox_dialog = self.create_buttonBox()
        button1 = QPushButton("1、嵌入对话框中")
        layout.addWidget(button1)
        button1.clicked.connect(lambda: self.show_dialog(buttonBox_dialog))

        layout.addWidget(QLabel('2、嵌入窗口中：'))
        layout.addWidget(self.create_buttonBox())

    def show_dialog(self, buttonBox):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog + QDialogButtonBox demo")
        layout = QVBoxLayout()
        layout.addWidget(QLabel('QDialogButtonBox嵌入到对话框中实例'))
        layout.addWidget(buttonBox)
        dialog.setLayout(layout)
        dialog.move(self.geometry().x(), self.geometry().y() + 180)
        # 绑定相应信号与槽，用于退出对话框
        buttonBox.accepted.connect(dialog.accept)
        buttonBox.rejected.connect(dialog.reject)
        buttonBox.setOrientation(Qt.Vertical)  # 垂直排列
        dialog.exec()

    def create_buttonBox(self):
        buttonBox = QDialogButtonBox()
        buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Reset | QDialogButtonBox.Help | QDialogButtonBox.Yes | QDialogButtonBox.No | QDialogButtonBox.Apply)
        # 自定义按钮
        buttonBox.addButton(QPushButton('MyOk-ApplyRole'), buttonBox.ApplyRole)
        buttonBox.addButton(QPushButton('MyOk-AcceptRole'), buttonBox.AcceptRole)
        buttonBox.addButton(QPushButton('MyNo-AcceptRole'), buttonBox.RejectRole)
        # 绑定信号与槽
        buttonBox.accepted.connect(lambda: self.label.setText(self.label.text() + '\n触发了accepted'))
        buttonBox.rejected.connect(lambda: self.label.setText(self.label.text() + '\n触发了rejected'))
        buttonBox.helpRequested.connect(lambda: self.label.setText(self.label.text() + '\n触发了helpRequested'))
        buttonBox.clicked.connect(lambda button: self.label.setText('点击了按钮：' + button.text()))
        return buttonBox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    demo = DialogButtonBox()
    demo.show()
    sys.exit(app.exec())
