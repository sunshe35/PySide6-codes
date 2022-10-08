# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import math
import os
os.chdir(os.path.dirname(__file__))

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("QPainter示例")
        self.resize(400, 300)
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(['初始化','drawText', 'drawPoint', 'drawRect', 'drawChord','drawPolygon'])
        self.comboBox.textActivated.connect(self.onDraw)


    def paintEvent(self, event):
        self.paintInit(event)

    def paintInit(self,event):
        painter = QPainter(self)
        painter.setPen(QColor(Qt.red))
        painter.setFont(QFont('Arial', 20))
        painter.drawText(10, 50, "hello Python")
        painter.setPen(QColor(Qt.blue))
        painter.drawLine(10, 100, 100, 100)
        painter.drawRect(10, 150, 150, 100)
        painter.setPen(QColor(Qt.yellow))
        painter.drawEllipse(100, 50, 100, 50)
        painter.drawPixmap(220, 10, QPixmap("./images/python.png"))
        painter.fillRect(200, 175, 150, 100, QBrush(Qt.SolidPattern))

    def paintPoint(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            # 绘制正弦函数图形，它的周期是[-100, 100]
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)

    def paintText(self, event):
        painter = QPainter(self)
        # 设置画笔的颜色
        painter.setPen(QColor(168, 34, 3))
        # 设置字体
        painter.setFont(QFont('SimSun', 20))
        # 绘制文字
        painter.drawText(50, 60, '这里会显示文字234')

    def paintRect(self, event):
        painter = QPainter(self)
        rect = QRect(50, 60, 80, 60)
        painter.drawRect(rect)

    def paintChord(self, event):
        start_angle = 30 * 16
        arc_length = 120 * 16
        rect = QRect(50, 60, 80, 60)
        painter = QPainter(self)
        painter.drawChord(rect, start_angle, arc_length)

    def paintPolygon(self, event):
        points = QPolygon([
            QPoint(110, 180),
            QPoint(120, 110),
            QPoint(180, 130),
            QPoint(190, 170)
        ])
        painter = QPainter(self)
        painter.drawPolygon(points)

    def onDraw(self, text):
        if text == '初始化':
            self.paintEvent = self.paintInit
        if text == 'drawText':
            self.paintEvent = self.paintText
        elif text == 'drawPoint':
            self.paintEvent = self.paintPoint
        elif text == 'drawRect':
            self.paintEvent = self.paintRect
        elif text == 'drawChord':
            self.paintEvent = self.paintChord
        elif text == 'drawPolygon':
            self.paintEvent = self.paintPolygon
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec())
