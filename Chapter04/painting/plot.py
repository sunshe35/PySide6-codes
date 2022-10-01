#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
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

import math
import sys

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPoint, QRect, QTimer, Qt, Slot
from PySide6.QtGui import (QColor, QPainter, QPaintEvent, QPen, QPointList,
                           QTransform)


WIDTH = 680
HEIGHT = 480


class PlotWidget(QWidget):
    """Illustrates the use of opaque containers. QPointList
       wraps a C++ QList<QPoint> directly, removing the need to convert
       a Python list in each call to QPainter.drawPolyline()."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._timer = QTimer(self)
        self._timer.setInterval(20)
        self._timer.timeout.connect(self.shift)

        self._points = QPointList()
        self._x = 0
        self._delta_x = 0.05
        self._half_height = HEIGHT / 2
        self._factor = 0.8 * self._half_height

        for i in range(WIDTH):
            self._points.append(QPoint(i, self.next_point()))

        self.setFixedSize(WIDTH, HEIGHT)

        self._timer.start()

    def next_point(self):
        result = self._half_height - self._factor * math.sin(self._x)
        self._x += self._delta_x
        return result

    def shift(self):
        last_x = self._points[WIDTH - 1].x()
        self._points.pop_front()
        self._points.append(QPoint(last_x + 1, self.next_point()))
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        rect = QRect(QPoint(0, 0), self.size())
        painter.fillRect(rect, Qt.white)
        painter.translate(-self._points[0].x(), 0)
        painter.drawPolyline(self._points)
        painter.end()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = PlotWidget()
    w.show()
    sys.exit(app.exec())
