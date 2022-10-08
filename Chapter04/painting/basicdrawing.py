
#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide6 port of the widgets/painting/basicdrawing example from Qt v5.x, originating from PyQt"""

from PySide6.QtCore import QPoint, QRect, QSize, Qt, qVersion
from PySide6.QtGui import (QBrush, QConicalGradient, QLinearGradient, QPainter,
        QPainterPath, QPalette, QPen, QPixmap, QPolygon, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QLabel, QSpinBox, QWidget)
import os
os.chdir(os.path.dirname(__file__))
# import basicdrawing_rc


class RenderArea(QWidget):
    points = QPolygon([
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    ])

    (Line, Points, Polyline, Polygon, Rect, RoundedRect, Ellipse,
     Arc, Chord, Pie, Path, Text, Pixmap) = range(13)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pen = QPen()
        self.brush = QBrush()
        self.pixmap = QPixmap()

        self.shape = RenderArea.Polygon
        self.antialiased = False
        self.transformed = False
        self.pixmap.load('images/qt-logo.png')

        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)

    def minimumSizeHint(self):
        return QSize(100, 100)

    def sizeHint(self):
        return QSize(400, 200)

    def set_shape(self, shape):
        self.shape = shape
        self.update()

    def set_pen(self, pen):
        self.pen = pen
        self.update()

    def set_brush(self, brush):
        self.brush = brush
        self.update()

    def set_antialiased(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def set_transformed(self, transformed):
        self.transformed = transformed
        self.update()

    def paintEvent(self, event):
        rect = QRect(10, 20, 80, 60)

        path = QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)

        start_angle = 30 * 16
        arc_length = 120 * 16

        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        if self.antialiased:
            painter.setRenderHint(QPainter.Antialiasing)

        for x in range(0, self.width(), 100):
            for y in range(0, self.height(), 100):
                painter.save()
                painter.translate(x, y)
                if self.transformed:
                    painter.translate(50, 50)
                    painter.rotate(60.0)
                    painter.scale(0.6, 0.9)
                    painter.translate(-50, -50)

                if self.shape == RenderArea.Line:
                    painter.drawLine(rect.bottomLeft(), rect.topRight())
                elif self.shape == RenderArea.Points:
                    painter.drawPoints(RenderArea.points)
                elif self.shape == RenderArea.Polyline:
                    painter.drawPolyline(RenderArea.points)
                elif self.shape == RenderArea.Polygon:
                    painter.drawPolygon(RenderArea.points)
                elif self.shape == RenderArea.Rect:
                    painter.drawRect(rect)
                elif self.shape == RenderArea.RoundedRect:
                    painter.drawRoundedRect(rect, 25, 25, Qt.RelativeSize)
                elif self.shape == RenderArea.Ellipse:
                    painter.drawEllipse(rect)
                elif self.shape == RenderArea.Arc:
                    painter.drawArc(rect, start_angle, arc_length)
                elif self.shape == RenderArea.Chord:
                    painter.drawChord(rect, start_angle, arc_length)
                elif self.shape == RenderArea.Pie:
                    painter.drawPie(rect, start_angle, arc_length)
                elif self.shape == RenderArea.Path:
                    painter.drawPath(path)
                elif self.shape == RenderArea.Text:
                    qv = qVersion()
                    painter.drawText(rect, Qt.AlignCenter,
                                     f"PySide 6\nQt {qv}")
                elif self.shape == RenderArea.Pixmap:
                    painter.drawPixmap(10, 10, self.pixmap)

                painter.restore()

        painter.setPen(self.palette().dark().color())
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))


id_role = Qt.UserRole


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._render_area = RenderArea()

        self._shape_combo_box = QComboBox()
        self._shape_combo_box.addItem("Polygon", RenderArea.Polygon)
        self._shape_combo_box.addItem("Rectangle", RenderArea.Rect)
        self._shape_combo_box.addItem("Rounded Rectangle", RenderArea.RoundedRect)
        self._shape_combo_box.addItem("Ellipse", RenderArea.Ellipse)
        self._shape_combo_box.addItem("Pie", RenderArea.Pie)
        self._shape_combo_box.addItem("Chord", RenderArea.Chord)
        self._shape_combo_box.addItem("Path", RenderArea.Path)
        self._shape_combo_box.addItem("Line", RenderArea.Line)
        self._shape_combo_box.addItem("Polyline", RenderArea.Polyline)
        self._shape_combo_box.addItem("Arc", RenderArea.Arc)
        self._shape_combo_box.addItem("Points", RenderArea.Points)
        self._shape_combo_box.addItem("Text", RenderArea.Text)
        self._shape_combo_box.addItem("Pixmap", RenderArea.Pixmap)

        shape_label = QLabel("&Shape:")
        shape_label.setBuddy(self._shape_combo_box)

        self._pen_width_spin_box = QSpinBox()
        self._pen_width_spin_box.setRange(0, 20)
        self._pen_width_spin_box.setSpecialValueText("0 (cosmetic pen)")

        pen_width_label = QLabel("Pen &Width:")
        pen_width_label.setBuddy(self._pen_width_spin_box)

        self._pen_style_combo_box = QComboBox()
        self._pen_style_combo_box.addItem("Solid", Qt.SolidLine)
        self._pen_style_combo_box.addItem("Dash", Qt.DashLine)
        self._pen_style_combo_box.addItem("Dot", Qt.DotLine)
        self._pen_style_combo_box.addItem("Dash Dot", Qt.DashDotLine)
        self._pen_style_combo_box.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        self._pen_style_combo_box.addItem("None", Qt.NoPen)

        pen_style_label = QLabel("&Pen Style:")
        pen_style_label.setBuddy(self._pen_style_combo_box)

        self._pen_cap_combo_box = QComboBox()
        self._pen_cap_combo_box.addItem("Flat", Qt.FlatCap)
        self._pen_cap_combo_box.addItem("Square", Qt.SquareCap)
        self._pen_cap_combo_box.addItem("Round", Qt.RoundCap)

        pen_cap_label = QLabel("Pen &Cap:")
        pen_cap_label.setBuddy(self._pen_cap_combo_box)

        self._pen_join_combo_box = QComboBox()
        self._pen_join_combo_box.addItem("Miter", Qt.MiterJoin)
        self._pen_join_combo_box.addItem("Bevel", Qt.BevelJoin)
        self._pen_join_combo_box.addItem("Round", Qt.RoundJoin)

        pen_join_label = QLabel("Pen &Join:")
        pen_join_label.setBuddy(self._pen_join_combo_box)

        self._brush_style_combo_box = QComboBox()
        self._brush_style_combo_box.addItem("Linear Gradient",
                Qt.LinearGradientPattern)
        self._brush_style_combo_box.addItem("Radial Gradient",
                Qt.RadialGradientPattern)
        self._brush_style_combo_box.addItem("Conical Gradient",
                Qt.ConicalGradientPattern)
        self._brush_style_combo_box.addItem("Texture", Qt.TexturePattern)
        self._brush_style_combo_box.addItem("Solid", Qt.SolidPattern)
        self._brush_style_combo_box.addItem("Horizontal", Qt.HorPattern)
        self._brush_style_combo_box.addItem("Vertical", Qt.VerPattern)
        self._brush_style_combo_box.addItem("Cross", Qt.CrossPattern)
        self._brush_style_combo_box.addItem("Backward Diagonal", Qt.BDiagPattern)
        self._brush_style_combo_box.addItem("Forward Diagonal", Qt.FDiagPattern)
        self._brush_style_combo_box.addItem("Diagonal Cross", Qt.DiagCrossPattern)
        self._brush_style_combo_box.addItem("Dense 1", Qt.Dense1Pattern)
        self._brush_style_combo_box.addItem("Dense 2", Qt.Dense2Pattern)
        self._brush_style_combo_box.addItem("Dense 3", Qt.Dense3Pattern)
        self._brush_style_combo_box.addItem("Dense 4", Qt.Dense4Pattern)
        self._brush_style_combo_box.addItem("Dense 5", Qt.Dense5Pattern)
        self._brush_style_combo_box.addItem("Dense 6", Qt.Dense6Pattern)
        self._brush_style_combo_box.addItem("Dense 7", Qt.Dense7Pattern)
        self._brush_style_combo_box.addItem("None", Qt.NoBrush)

        brush_style_label = QLabel("&Brush Style:")
        brush_style_label.setBuddy(self._brush_style_combo_box)

        other_options_label = QLabel("Other Options:")
        self._antialiasing_check_box = QCheckBox("&Antialiasing")
        self._transformations_check_box = QCheckBox("&Transformations")

        self._shape_combo_box.activated.connect(self.shape_changed)
        self._pen_width_spin_box.valueChanged.connect(self.pen_changed)
        self._pen_style_combo_box.activated.connect(self.pen_changed)
        self._pen_cap_combo_box.activated.connect(self.pen_changed)
        self._pen_join_combo_box.activated.connect(self.pen_changed)
        self._brush_style_combo_box.activated.connect(self.brush_changed)
        self._antialiasing_check_box.toggled.connect(self._render_area.set_antialiased)
        self._transformations_check_box.toggled.connect(self._render_area.set_transformed)

        main_layout = QGridLayout()
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(3, 1)
        main_layout.addWidget(self._render_area, 0, 0, 1, 4)
        main_layout.setRowMinimumHeight(1, 6)
        main_layout.addWidget(shape_label, 2, 1, Qt.AlignRight)
        main_layout.addWidget(self._shape_combo_box, 2, 2)
        main_layout.addWidget(pen_width_label, 3, 1, Qt.AlignRight)
        main_layout.addWidget(self._pen_width_spin_box, 3, 2)
        main_layout.addWidget(pen_style_label, 4, 1, Qt.AlignRight)
        main_layout.addWidget(self._pen_style_combo_box, 4, 2)
        main_layout.addWidget(pen_cap_label, 5, 1, Qt.AlignRight)
        main_layout.addWidget(self._pen_cap_combo_box, 5, 2)
        main_layout.addWidget(pen_join_label, 6, 1, Qt.AlignRight)
        main_layout.addWidget(self._pen_join_combo_box, 6, 2)
        main_layout.addWidget(brush_style_label, 7, 1, Qt.AlignRight)
        main_layout.addWidget(self._brush_style_combo_box, 7, 2)
        main_layout.setRowMinimumHeight(8, 6)
        main_layout.addWidget(other_options_label, 9, 1, Qt.AlignRight)
        main_layout.addWidget(self._antialiasing_check_box, 9, 2)
        main_layout.addWidget(self._transformations_check_box, 10, 2)
        self.setLayout(main_layout)

        self.shape_changed()
        self.pen_changed()
        self.brush_changed()
        self._antialiasing_check_box.setChecked(True)

        self.setWindowTitle("Basic Drawing")

    def shape_changed(self):
        shape = self._shape_combo_box.itemData(self._shape_combo_box.currentIndex(),
                id_role)
        self._render_area.set_shape(shape)

    def pen_changed(self):
        width = self._pen_width_spin_box.value()
        style = Qt.PenStyle(self._pen_style_combo_box.itemData(
                self._pen_style_combo_box.currentIndex(), id_role))
        cap = Qt.PenCapStyle(self._pen_cap_combo_box.itemData(
                self._pen_cap_combo_box.currentIndex(), id_role))
        join = Qt.PenJoinStyle(self._pen_join_combo_box.itemData(
                self._pen_join_combo_box.currentIndex(), id_role))

        self._render_area.set_pen(QPen(Qt.blue, width, style, cap, join))

    def brush_changed(self):
        style = Qt.BrushStyle(self._brush_style_combo_box.itemData(
                self._brush_style_combo_box.currentIndex(), id_role))

        if style == Qt.LinearGradientPattern:
            linear_gradient = QLinearGradient(0, 0, 100, 100)
            linear_gradient.setColorAt(0.0, Qt.white)
            linear_gradient.setColorAt(0.2, Qt.green)
            linear_gradient.setColorAt(1.0, Qt.black)
            self._render_area.set_brush(QBrush(linear_gradient))
        elif style == Qt.RadialGradientPattern:
            radial_gradient = QRadialGradient(50, 50, 50, 70, 70)
            radial_gradient.setColorAt(0.0, Qt.white)
            radial_gradient.setColorAt(0.2, Qt.green)
            radial_gradient.setColorAt(1.0, Qt.black)
            self._render_area.set_brush(QBrush(radial_gradient))
        elif style == Qt.ConicalGradientPattern:
            conical_gradient = QConicalGradient(50, 50, 150)
            conical_gradient.setColorAt(0.0, Qt.white)
            conical_gradient.setColorAt(0.2, Qt.green)
            conical_gradient.setColorAt(1.0, Qt.black)
            self._render_area.set_brush(QBrush(conical_gradient))
        elif style == Qt.TexturePattern:
            self._render_area.set_brush(QBrush(QPixmap('images/brick.png')))
        else:
            self._render_area.set_brush(QBrush(Qt.green, style))


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
