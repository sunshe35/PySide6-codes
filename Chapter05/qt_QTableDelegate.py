from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import re
import sys
import datetime

from qt_QTableModel import StudentTableModel
import os
os.chdir(os.path.dirname(__file__))

SUBJECT, NAME, SCORE, DESCRIPTION = range(4)


class StudentTableDelegate(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(StudentTableDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == DESCRIPTION:
            text = index.model().data(index)
            if text[-2:] == '优秀':
                text = f'{text[:-2]}<font color=red><b>优秀</b></font>'
                index.model().setData(index, value=text)
            elif text[-2:] == '良好':
                text = f'{text[:-2]}<font color=green><b>良好</b></font>'
                index.model().setData(index, value=text)
            palette = QApplication.palette()
            document = QTextDocument()
            document.setDefaultFont(option.font)
            if option.state & QStyle.State_Selected:
                document.setHtml("<font color={}>{}</font>".format(
                    palette.highlightedText().color().name(), text))
            else:
                document.setHtml(text)
            color = (palette.highlight().color()
                     if option.state & QStyle.State_Selected
                     else QColor(index.model().data(index, Qt.BackgroundRole)))
            painter.save()
            painter.fillRect(option.rect, color)
            painter.translate(option.rect.x(), option.rect.y())
            document.drawContents(painter)
            painter.restore()
        else:
            QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        fm = option.fontMetrics
        if index.column() == SCORE:
            return QSize(fm.averageCharWidth(), fm.height())
        if index.column() == DESCRIPTION:
            text = index.model().data(index)
            document = QTextDocument()
            document.setDefaultFont(option.font)
            document.setHtml(text)
            return QSize(document.idealWidth() + 5, fm.height())
        return QStyledItemDelegate.sizeHint(self, option, index)

    def createEditor(self, parent, option, index):
        if index.column() == SCORE:
            spinbox = QSpinBox(parent)
            spinbox.setRange(0, 100)
            spinbox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            return spinbox
        elif index.column() in (NAME, SUBJECT):
            editor = QLineEdit(parent)
            # self.connect(editor, SIGNAL("returnPressed()"), self.commitAndCloseEditor)
            return editor
        elif index.column() == DESCRIPTION:
            editor = QTextEdit()
            # self.connect(editor, SIGNAL("returnPressed()"), self.commitAndCloseEditor)
            return editor
        else:
            return QStyledItemDelegate.createEditor(self, parent, option, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (QTextEdit, QLineEdit)):
            self.emit(SIGNAL("commitData(QWidget*)"), editor)
            self.emit(SIGNAL("closeEditor(QWidget*)"), editor)

    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.DisplayRole)
        if index.column() == SCORE:
            try:
                value = int(float(text) + 0.5)
            except:
                value = 0
            editor.setValue(value)
        elif index.column() in (NAME, SUBJECT):
            editor.setText(text)
        elif index.column() == DESCRIPTION:
            editor.setHtml(text)
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        if index.column() == SCORE:
            model.setData(index, editor.value())
        elif index.column() in (NAME, SUBJECT):
            model.setData(index, editor.text())
        elif index.column() == DESCRIPTION:
            model.setData(index, editor.toHtml())
        else:
            QStyledItemDelegate.setModelData(self, editor, model, index)


class DateColumnDelegate(QStyledItemDelegate):

    def __init__(self, minimum=QDate(),
                 maximum=QDate.currentDate(),
                 format="yyyy-MM-dd", parent=None):
        super(DateColumnDelegate, self).__init__(parent)
        self.minimum = minimum
        self.maximum = maximum
        self.format = format

    def createEditor(self, parent, option, index):
        dateedit = QDateEdit(parent)
        dateedit.setDateRange(self.minimum, self.maximum)
        dateedit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        dateedit.setDisplayFormat(self.format)
        dateedit.setCalendarPopup(True)
        return dateedit

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.DisplayRole)
        try:
            date = datetime.datetime.strptime(value, '%Y-%m-%d').date()
            editor.setDate(QDate(date.year, date.month, date.day))
        except:
            print(value, index)
            editor.setDate(QDate())

    def setModelData(self, editor, model, index):
        model.setData(index, editor.date().toString('yyyy-MM-dd'))


class IntegerColumnDelegate(QStyledItemDelegate):

    def __init__(self, minimum=0, maximum=100, parent=None):
        super(IntegerColumnDelegate, self).__init__(parent)
        self.minimum = minimum
        self.maximum = maximum

    def createEditor(self, parent, option, index):
        spinbox = QSpinBox(parent)
        spinbox.setRange(self.minimum, self.maximum)
        spinbox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        return spinbox

    def setEditorData(self, editor, index):
        value = int(index.model().data(index, Qt.DisplayRole))
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        editor.interpretText()
        model.setData(index, editor.value())




class QTableViewDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTableViewDemo, self).__init__(parent)
        self.setWindowTitle("QTableDelegate案例")
        self.resize(550, 600)

        # 方式1：基于自定义模型的自定义委托
        self.tableView = QTableView()
        self.model = StudentTableModel()
        self.delegate = StudentTableDelegate()
        self.model.initData()

        self.tableView.setModel(self.model)
        self.selectModel = QItemSelectionModel()
        self.tableView.setSelectionModel(self.selectModel)
        self.tableView.setItemDelegate(self.delegate)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        # 方式2：通用模型的通用委托
        self.tableView2 = QTableView()
        self.model2 = QStandardItemModel(5, 4)
        self.init_model2()
        self.tableView2.setModel(self.model2)
        self.delegate2 = IntegerColumnDelegate()
        self.tableView2.setItemDelegateForColumn(2, self.delegate2)
        self.tableView2.setItemDelegateForColumn(3, DateColumnDelegate())

        self.buttonAddRow = QPushButton('增加行')
        self.buttonInsertRow = QPushButton('插入行')
        self.buttonDeleteRow = QPushButton('删除行')
        self.buttonAddRow.clicked.connect(self.onAdd)
        self.buttonInsertRow.clicked.connect(self.onInsert)
        self.buttonDeleteRow.clicked.connect(self.onDelete)

        self.model.setData(self.model.index(3, 1), 'Python', role=Qt.EditRole)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableView)
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.buttonAddRow)
        layoutH.addWidget(self.buttonInsertRow)
        layoutH.addWidget(self.buttonDeleteRow)
        layout.addLayout(layoutH)
        layout.addWidget(self.tableView2)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

    def init_model2(self):
        for row in range(self.model2.rowCount()):
            for column in range(self.model2.columnCount()):
                if column == 2:
                    value = column + row
                elif column == 3:
                    date = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d') + datetime.timedelta(days=column * row)
                    value = datetime.datetime.strftime(date, '%Y-%m-%d')
                else:
                    value = "row %s, col %s" % (row, column)
                item = QStandardItem(str(value))
                self.model2.setItem(row, column, item)

    def onAdd(self):
        rowCount = self.model.rowCount()
        self.model.insertRow(rowCount)

    def onInsert(self):
        index = self.tableView.currentIndex()
        row = index.row()
        self.model.insertRow(row)

    def onDelete(self):
        index = self.tableView.currentIndex()
        row = index.row()
        self.model.removeRow(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = QTableViewDemo()
    demo.show()
    sys.exit(app.exec())
