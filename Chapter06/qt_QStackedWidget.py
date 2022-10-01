import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.setGeometry(400, 300, 300, 50)
        self.setWindowTitle('StackedWidget 例子')

        self.listWidget = QListWidget()
        self.listWidget.insertItem(0, '联系方式')
        self.listWidget.insertItem(1, '个人信息')
        self.listWidget.insertItem(2, '获奖情况')
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack1Init()
        self.stack2Init()
        self.stack3Init()
        self.stackWidget = QStackedWidget(self)
        self.stackWidget.addWidget(self.stack1)
        self.stackWidget.insertWidget(1,self.stack2)
        self.stackWidget.addWidget(self.stack3)

        pageComboBox = QComboBox()
        pageComboBox.addItem("Goto Page 0")
        pageComboBox.addItem("Goto Page 1")
        pageComboBox.addItem("Goto Page 2")
        # pageComboBox.activated.connect(self.stackWidget.setCurrentIndex)
        pageComboBox.activated.connect(self.listWidget.setCurrentRow)


        vlayout = QVBoxLayout(self)
        self.label = QLabel('用来显示信息')
        hlayout = QHBoxLayout(self)
        hlayout.addWidget(self.listWidget)
        hlayout.addWidget(self.stackWidget)
        vlayout.addWidget(pageComboBox)
        vlayout.addWidget(self.label)
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)
        self.listWidget.currentRowChanged.connect(self.stackWidget.setCurrentIndex)
        self.stackWidget.currentChanged.connect(self.stackChanged)


    def stack1Init(self):
        layout = QFormLayout()
        line1 = QLineEdit()
        line2 = QLineEdit()
        layout.addRow("姓名", line1)
        layout.addRow("电话", line2)
        self.stack1.setLayout(layout)
        line1.editingFinished.connect(lambda :self.label.setText(f'page0，更新了姓名：{line1.text()}'))
        line2.editingFinished.connect(lambda :self.label.setText(f'page0，更新了电话：{line2.text()}'))

    def stack2Init(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        radio1 = QRadioButton("男")
        radio2 = QRadioButton("女")
        sex.addWidget(radio1)
        sex.addWidget(radio2)
        layout.addRow(QLabel("性别"), sex)
        line = QLineEdit()
        layout.addRow("教育程度", line)
        self.stack2.setLayout(layout)
        radio1.clicked.connect(lambda:self.label.setText('page 1 更新了性别:男'))
        radio2.clicked.connect(lambda:self.label.setText('page 1 更新了性别:女'))
        line.editingFinished.connect(lambda :self.label.setText(f'page1，更新了教育程度：{line.text()}'))

    def stack3Init(self):
        layout = QHBoxLayout()
        check1 = QCheckBox('一等奖')
        check2 = QCheckBox('二等奖')
        check3 = QCheckBox('三等奖')
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        self.stack3.setLayout(layout)
        _dict = {0:False,2:True,1:True}
        check1.stateChanged.connect(lambda x:self.label.setText(f'page2，更新了“1等奖”获取情况：{_dict[x]}'))
        check2.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“2等奖”获取情况：{_dict[x]}'))
        check3.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“3等奖”获取情况：{_dict[x]}'))

    def stackChanged(self,index:int):
        text = self.listWidget.currentItem().text()
        self.label.setText(f'切换到页面{index},{text}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec())
