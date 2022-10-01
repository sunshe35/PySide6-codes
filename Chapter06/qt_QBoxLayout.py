# -*- coding: utf-8 -*-

"""
    【简介】
    QBoxLayout布局管理例子,同样可适用于QVBoxLayout和QHBoxLayout

"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class BoxLayoutDemo(QWidget):
    def __init__(self, parent=None):
        super(BoxLayoutDemo, self).__init__(parent)
        self.setWindowTitle("Q(H/V)BoxLayout布局管理例子")
        self.resize(800, 200)

        # 水平布局按照从左到右的顺序进行添加按钮部件。
        # layout = QBoxLayout(QBoxLayout.LeftToRight)
        # layout = QBoxLayout(QBoxLayout.RightToLeft)
        # layout = QVBoxLayout()
        layout = QHBoxLayout()

        # addWidget
        layout.addWidget(QPushButton(str(1)), stretch=1, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(QPushButton(str(2)), stretch=1)
        layout.addWidget(QPushButton(str(3)), alignment=Qt.AlignRight | Qt.AlignBottom)

        # addStretch
        layout.addStretch(2)
        layout.addWidget(QPushButton('addStretch1'), stretch=1, alignment=Qt.AlignTop)
        layout.addStretch(1)
        layout.addWidget(QPushButton('addStretch2'), stretch=2)

        # addSpacing
        layout.addSpacing(10)
        layout.addWidget(QPushButton('addSpacing'))

        # addLayout
        vlayout = QVBoxLayout()
        for i in range(3):
            vlayout.addWidget(QPushButton('addLayout%s' % (i + 1)))

        # 设置边距
        vlayout.setContentsMargins(10, 20, 40, 60)
        vlayout.setSpacing(10)

        layout.addLayout(vlayout)
        self.setLayout(layout)

        # 显示sizePolice和sizeHint信息-基于QWidget
        _str = ''
        for w in self.findChildren(QPushButton):
            # if hasattr(w,'text'):
            vPolicy = w.sizePolicy().verticalPolicy().name.decode('utf8')
            hPolicy = w.sizePolicy().horizontalPolicy().name.decode('utf8')
            sizeHint = w.sizeHint().toTuple()
            _str = _str + f'按钮：{w.text()}，sizeHint:{sizeHint}，sizePolicy:{vPolicy}/{hPolicy}' + '\n'
        self.label = QLabel()
        self.label.setText(_str)
        self.label.setWindowTitle('显示sizePolice和sizeHint信息-基于QWidget')
        self.label.show()

        # 显示stretch、sizePolice、sizeHint信息-基于Layout
        _str2 = ''
        for i in range(layout.count()):
            item = layout.itemAt(i)
            stretch = layout.stretch(i)
            if isinstance(item.widget(), QPushButton):
                w = item.widget()
                vPolicy = w.sizePolicy().verticalPolicy().name.decode('utf8')
                hPolicy = w.sizePolicy().horizontalPolicy().name.decode('utf8')
                sizeHint = item.sizeHint().toTuple()
                _str2 = _str2 + f'num:{i}，按钮:{w.text()}，stretch:{stretch}，sizeHint:{sizeHint}，sizePolicy:{vPolicy}/{hPolicy}' + '\n'
            elif isinstance(item, QSpacerItem):
                vPolicy = item.sizePolicy().verticalPolicy().name.decode('utf8')
                hPolicy = item.sizePolicy().horizontalPolicy().name.decode('utf8')
                sizeHint = item.sizeHint().toTuple()
                _str2 = _str2 + f'num:{i}，QSpacerItem，stretch:{stretch}，sizeHint:{sizeHint}，sizePolicy:{vPolicy}/{hPolicy}' + '\n'
            else:  # 处理嵌套Layout
                for j in range(vlayout.count()):
                    w = vlayout.itemAt(j).widget()
                    _str2 = _str2 + f'num:{i}-{j}，按钮:{w.text()}，stretch:{stretch}，sizeHint:{sizeHint}，sizePolicy:{vPolicy}/{hPolicy}' + '\n'
        self.label2 = QLabel()
        self.label2.setWindowTitle('显示stretch、sizePolice、sizeHint信息-基于Layout')
        self.label2.setText(_str2)
        self.label2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = BoxLayoutDemo()
    form.show()
    sys.exit(app.exec())
