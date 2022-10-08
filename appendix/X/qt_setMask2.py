# -*- coding: utf-8 -*-

"""
    【简介】
    不规则窗体的动画实现
    
    
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPixmap, QPainter, QCursor,QMouseEvent,QPaintEvent
from PySide6.QtCore import Qt, QTimer
import os
os.chdir(os.path.dirname(__file__))

class ShapeWidget(QWidget):
    def __init__(self, parent=None):
        super(ShapeWidget, self).__init__(parent)
        self.i = 1
        self.updatePix()
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1000毫秒
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    # 显示不规则 pic
    def updatePix(self):
        if self.i == 5:
            self.i = 1
        self.mypic = {1: './images/left.png', 2: "./images/up.png", 3: './images/right.png', 4: './images/down.png'}
        self.pix = QPixmap(self.mypic[self.i], "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None
        self.m_drag = False
        self.update()


    def mousePressEvent(self, event:QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPosition().toPoint() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event:QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPosition().toPoint() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event:QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event:QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, event:QMouseEvent):
        if event.button() == 1:
            self.i += 1
            self.updatePix()

    # 每1000毫秒修改paint
    def timeChange(self):
        self.i += 1
        self.updatePix()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShapeWidget()
    form.show()
    sys.exit(app.exec())
