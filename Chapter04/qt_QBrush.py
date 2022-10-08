# -*- coding: utf-8 -*-

"""
    【简介】
    绘图中QBrush 的例子 ,绘制不同样式的矩形。
    
    
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
os.chdir(os.path.dirname(__file__))

class BrushDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Linear Gradient", Qt.LinearGradientPattern)
        self.comboBox.addItem("Radial Gradient", Qt.RadialGradientPattern)
        self.comboBox.addItem("Conical Gradient", Qt.ConicalGradientPattern)
        self.comboBox.addItem("Texture", Qt.TexturePattern)
        self.comboBox.addItem("Solid", Qt.SolidPattern)
        self.comboBox.addItem("Horizontal", Qt.HorPattern)
        self.comboBox.addItem("Vertical", Qt.VerPattern)
        self.comboBox.addItem("Cross", Qt.CrossPattern)
        self.comboBox.addItem("Backward Diagonal", Qt.BDiagPattern)
        self.comboBox.addItem("Forward Diagonal", Qt.FDiagPattern)
        self.comboBox.addItem("Diagonal Cross", Qt.DiagCrossPattern)
        self.comboBox.addItem("Dense 1", Qt.Dense1Pattern)
        self.comboBox.addItem("Dense 2", Qt.Dense2Pattern)
        self.comboBox.addItem("Dense 3", Qt.Dense3Pattern)
        self.comboBox.addItem("Dense 4", Qt.Dense4Pattern)
        self.comboBox.addItem("Dense 5", Qt.Dense5Pattern)
        self.comboBox.addItem("Dense 6", Qt.Dense6Pattern)
        self.comboBox.addItem("Dense 7", Qt.Dense7Pattern)
        self.comboBox.addItem("None", Qt.NoBrush)

        label = QLabel("&Brush Style:", self)
        label.setBuddy(self.comboBox)
        self.comboBox.move(100, 0)

        self.comboBox.activated.connect(self.brush_changed)

        self.brush = QBrush()
        self.setGeometry(300, 300, 365, 280)
        self.setWindowTitle('QBrush案例')

    def paintEvent(self, event):

        rect = QRect(50, 60, 180, 160)
        painter = QPainter(self)
        painter.setBrush(self.brush)
        painter.drawRoundedRect(rect, 50, 40, Qt.RelativeSize)

    def set_brush(self, brush):
        self.brush = brush
        self.update()

    def brush_changed(self):
        style = Qt.BrushStyle(self.comboBox.itemData(self.comboBox.currentIndex(), Qt.UserRole))

        if style == Qt.LinearGradientPattern:
            linear_gradient = QLinearGradient(0, 0, 100, 100)
            linear_gradient.setColorAt(0.0, Qt.white)
            linear_gradient.setColorAt(0.2, Qt.green)
            linear_gradient.setColorAt(1.0, Qt.black)
            self.set_brush(QBrush(linear_gradient))
        elif style == Qt.RadialGradientPattern:
            radial_gradient = QRadialGradient(50, 50, 50, 70, 70)
            radial_gradient.setColorAt(0.0, Qt.white)
            radial_gradient.setColorAt(0.2, Qt.green)
            radial_gradient.setColorAt(1.0, Qt.black)
            self.set_brush(QBrush(radial_gradient))
        elif style == Qt.ConicalGradientPattern:
            conical_gradient = QConicalGradient(50, 50, 150)
            conical_gradient.setColorAt(0.0, Qt.white)
            conical_gradient.setColorAt(0.2, Qt.green)
            conical_gradient.setColorAt(1.0, Qt.black)
            self.set_brush(QBrush(conical_gradient))
        elif style == Qt.TexturePattern:
            self.set_brush(QBrush(QPixmap('images/open.png')))
        elif style == Qt.VerPattern:
            brush = QBrush(style)
            brush.setColor(Qt.red)
            self.set_brush(brush)
        else:
            self.set_brush(QBrush(Qt.green, style))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = BrushDemo()
    demo.show()
    sys.exit(app.exec())
