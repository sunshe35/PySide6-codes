import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class TabDemo(QWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tabWidget = QTabWidget(self)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab1, "Page 0")
        self.tabWidget.insertTab(1,self.tab2, "Page 1")
        self.tabWidget.addTab(self.tab3, "Page 2")
        self.tab1Init()
        self.tab2Init()
        self.tab3Init()

        # 修改选项卡默认信息
        self.tabWidget.setTabShape(self.tabWidget.Triangular)
        self.tabWidget.setTabPosition(self.tabWidget.South)

        pageComboBox = QComboBox()
        pageComboBox.addItem("Goto Page 0")
        pageComboBox.addItem("Goto Page 1")
        pageComboBox.addItem("Goto Page 2")
        # 导航与页面链接
        pageComboBox.activated.connect(self.tabWidget.setCurrentIndex)

        vlayout =QVBoxLayout(self)
        self.label = QLabel('用来显示信息')
        vlayout.addWidget(pageComboBox)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.tabWidget)
        self.setLayout(vlayout)

        self.setWindowTitle("QTabWidget 例子")
        self.resize(400,200)

        self.tabWidget.currentChanged.connect(self.tabChanged)

    def tab1Init(self):
        layout = QFormLayout()
        line1 = QLineEdit()
        line2 = QLineEdit()
        layout.addRow("姓名", line1)
        layout.addRow("电话", line2)
        self.tab1.setLayout(layout)
        self.tabWidget.setTabText(0, "联系方式")
        line1.editingFinished.connect(lambda :self.label.setText(f'page0，更新了姓名：{line1.text()}'))
        line2.editingFinished.connect(lambda :self.label.setText(f'page0，更新了电话：{line2.text()}'))


    def tab2Init(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        radio1 = QRadioButton("男")
        radio2 = QRadioButton("女")
        sex.addWidget(radio1)
        sex.addWidget(radio2)
        layout.addRow(QLabel("性别"), sex)
        line = QLineEdit()
        layout.addRow("教育程度", line)
        self.tab2.setLayout(layout)
        self.tabWidget.setTabText(1, "个人信息")
        self.tabWidget.setTabToolTip(1,'更新：个人信息')
        self.tabWidget.setTabIcon(1,QIcon(r'images/cartoon1.ico'))
        self.tabWidget.tabBar().setTabTextColor(1, QColor(40,120,120))

        radio1.clicked.connect(lambda:self.label.setText('page 1 更新了性别:男'))
        radio2.clicked.connect(lambda:self.label.setText('page 1 更新了性别:女'))
        line.editingFinished.connect(lambda :self.label.setText(f'page1，更新了教育程度：{line.text()}'))

    def tab3Init(self):
        layout = QHBoxLayout()
        check1 = QCheckBox('一等奖')
        check2 = QCheckBox('二等奖')
        check3 = QCheckBox('三等奖')
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        self.tab3.setLayout(layout)
        self.tabWidget.setTabText(2, "获奖情况")
        self.tabWidget.setTabToolTip(2,'更新：获奖情况')
        self.tabWidget.setTabIcon(2,QIcon(r'images/bao13.png'))
        self.tabWidget.tabBar().setTabTextColor(2, 'red')

        _dict = {0:False,2:True,1:True}
        check1.stateChanged.connect(lambda x:self.label.setText(f'page2，更新了“1等奖”获取情况：{_dict[x]}'))
        check2.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“2等奖”获取情况：{_dict[x]}'))
        check3.stateChanged.connect(lambda x: self.label.setText(f'page2，更新了“3等奖”获取情况：{_dict[x]}'))

    def tabChanged(self, index:int):
        a = self.tabWidget.currentWidget()
        text = self.tabWidget.tabBar().tabText(index)
        self.label.setText(f'切换到页面{index},{text}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec())
