import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class ToolBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(ToolBoxDemo, self).__init__(parent)
        self.toolBox = QToolBox(self)
        self.tool1 = QWidget()
        self.tool2 = QWidget()
        self.tool3 = QWidget()
        self.toolBox.addItem(self.tool1, "Page 0")
        self.toolBox.insertItem(1, self.tool2, "Page 1")
        self.toolBox.addItem(self.tool3, "Page 2")
        self.tool1Init()
        self.tool2Init()
        self.tool3Init()

        pageComboBox = QComboBox()
        pageComboBox.addItem("Goto Page 0")
        pageComboBox.addItem("Goto Page 1")
        pageComboBox.addItem("Goto Page 2")
        # 导航与页面链接
        pageComboBox.activated.connect(self.toolBox.setCurrentIndex)

        vlayout =QVBoxLayout(self)
        self.label = QLabel('用来显示信息')
        vlayout.addWidget(pageComboBox)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.toolBox)
        self.setLayout(vlayout)

        self.setWindowTitle("QToolBox 例子")
        self.resize(400,200)

        self.toolBox.currentChanged.connect(self.tabChanged)

    def tool1Init(self):
        layout = QFormLayout()
        line1 = QLineEdit()
        line2 = QLineEdit()
        layout.addRow("姓名", line1)
        layout.addRow("电话", line2)
        self.tool1.setLayout(layout)
        self.toolBox.setItemText(0, "联系方式")
        self.toolBox.setItemToolTip(0, '更新：联系方式')
        self.toolBox.setItemIcon(0, QIcon(r'images/android.png'))
        line1.editingFinished.connect(lambda :self.label.setText(f'page0，更新了姓名：{line1.text()}'))
        line2.editingFinished.connect(lambda :self.label.setText(f'page0，更新了电话：{line2.text()}'))


    def tool2Init(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        radio1 = QRadioButton("男")
        radio2 = QRadioButton("女")
        sex.addWidget(radio1)
        sex.addWidget(radio2)
        layout.addRow(QLabel("性别"), sex)
        line = QLineEdit()
        layout.addRow("教育程度", line)
        self.tool2.setLayout(layout)
        self.toolBox.setItemText(1, "个人信息")
        self.toolBox.setItemToolTip(1, '更新：个人信息')
        self.toolBox.setItemIcon(1, QIcon(r'images/cartoon1.ico'))

        radio1.clicked.connect(lambda:self.label.setText('page 1 更新了性别:男'))
        radio2.clicked.connect(lambda:self.label.setText('page 1 更新了性别:女'))
        line.editingFinished.connect(lambda :self.label.setText(f'page1，更新了教育程度：{line.text()}'))

    def tool3Init(self):
        layout = QHBoxLayout()
        check1 = QCheckBox('一等奖')
        check2 = QCheckBox('二等奖')
        check3 = QCheckBox('三等奖')
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        self.tool3.setLayout(layout)
        self.toolBox.setItemText(2, "获奖情况")
        self.toolBox.setItemToolTip(2, '更新：获奖情况')
        self.toolBox.setItemIcon(2, QIcon(r'images/bao13.png'))

        _dict = {0:False,2:True,1:True}
        check1.stateChanged.connect(lambda x:self.label.setText(f'page2，更新了“1等奖”获取情况：{_dict[x]}'))
        check2.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“2等奖”获取情况：{_dict[x]}'))
        check3.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“3等奖”获取情况：{_dict[x]}'))

    def tabChanged(self, index:int):
        a = self.toolBox.currentWidget()
        text = self.toolBox.itemText(index)
        self.label.setText(f'切换到页面{index},{text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ToolBoxDemo()
    demo.show()
    sys.exit(app.exec())
