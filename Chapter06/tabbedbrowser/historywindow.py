#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
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

from PySide6.QtWidgets import QApplication, QTreeView

from PySide6.QtCore import Signal, QAbstractTableModel, QModelIndex, Qt, QUrl


class HistoryModel(QAbstractTableModel):

    def __init__(self, history, parent=None):
        super().__init__(parent)
        self._history = history

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Title' if section == 0 else 'Url'
        return None

    def rowCount(self, index=QModelIndex()):
        return self._history.count()

    def columnCount(self, index=QModelIndex()):
        return 2

    def item_at(self, model_index):
        return self._history.itemAt(model_index.row())

    def data(self, index, role=Qt.DisplayRole):
        item = self.item_at(index)
        column = index.column()
        if role == Qt.DisplayRole:
            return item.title() if column == 0 else item.url().toString()
        return None

    def refresh(self):
        self.beginResetModel()
        self.endResetModel()


class HistoryWindow(QTreeView):

    open_url = Signal(QUrl)

    def __init__(self, history, parent):
        super().__init__(parent)

        self._model = HistoryModel(history, self)
        self.setModel(self._model)
        self.activated.connect(self._activated)

        screen = QApplication.desktop().screenGeometry(parent)
        self.resize(screen.width() / 3, screen.height() / 3)
        self._adjustSize()

    def refresh(self):
        self._model.refresh()
        self._adjustSize()

    def _adjustSize(self):
        if (self._model.rowCount() > 0):
            self.resizeColumnToContents(0)

    def _activated(self, index):
        item = self._model.item_at(index)
        self.open_url.emit(item.url())
