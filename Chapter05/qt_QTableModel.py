from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

SUBJECT, NAME, SCORE, DESCRIPTION = range(4)


class Student(object):

    def __init__(self, subject, name, score=0, description=""):
        self.subject = subject
        self.name = name
        self.score = score
        self.description = description

    def __hash__(self):
        return super(Student, self).__hash__()

    def __lt__(self, other):
        if self.name < other.name:
            return True
        if self.subject < other.subject:
            return True
        return id(self) < id(other)


    def __eq__(self, other):
        if self.name == other.name:
            return True
        if self.subject == other.subject:
            return True
        return id(self) == id(other)


class StudentTableModel(QAbstractTableModel):

    def __init__(self, filename=""):
        super(StudentTableModel, self).__init__()
        self.students = []

    def initData(self):
        for subject in ['语文', '数学', '外语', '综合']:
            for name in ['张三', '李四', '王五', '赵六']:
                score = random.random() * 40 + 60
                if score>=80:
                    _str = f'{name}的{subject}成绩是：优秀'
                else:
                    _str = f'{name}的{subject}成绩是：良好'
                student = Student(subject, name, score, _str)
                self.students.append(student)
        self.sortBySubject()

    def sortByName(self):

        self.students = sorted(self.students,key=lambda x:(x.name,x.subject))
        self.endResetModel()

    def sortBySubject(self):
        self.students = sorted(self.students, key=lambda x: (x.subject, x.name))
        self.endResetModel()

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.students)):
            return None
        student = self.students[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == SUBJECT:
                return student.subject
            elif column == NAME:
                return student.name
            elif column == DESCRIPTION:
                return student.description
            elif column == SCORE:
                return "{:.2f}".format(student.score)
        elif role == Qt.TextAlignmentRole:
            if column == SCORE:
                return int(Qt.AlignRight | Qt.AlignVCenter)
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        elif role == Qt.ForegroundRole and column == SCORE:
            if student.score < 80:
                return QColor(Qt.black)
            elif student.score < 90:
                return QColor(Qt.darkGreen)
            elif student.score < 100:
                return QColor(Qt.red)
        elif role == Qt.BackgroundRole:
            if student.subject in ("数学", "语文"):
                return QColor(250, 230, 250)
            elif student.subject in ("外语",):
                return QColor(250, 250, 230)
            elif student.subject in ("综合"):
                return QColor(230, 250, 250)
            else:
                return QColor(210, 230, 230)
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return int(Qt.AlignLeft | Qt.AlignVCenter)
            return int(Qt.AlignRight | Qt.AlignVCenter)
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            if section == SUBJECT:
                return "科目"
            elif section == NAME:
                return "姓名"
            elif section == SCORE:
                return "分数"
            elif section == DESCRIPTION:
                return "说明"
        return int(section + 1)

    def rowCount(self, index=QModelIndex()):
        return len(self.students)

    def columnCount(self, index=QModelIndex()):
        return 4

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.students) and role==Qt.EditRole:
            student = self.students[index.row()]
            column = index.column()
            if column == SUBJECT:
                student.subject = value
            elif column == NAME:
                student.name = value
            elif column == DESCRIPTION:
                student.description = value
            elif column == SCORE:
                try:
                    student.score = int(value)
                except:
                    print('输入错误，请输入数字')

            self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
            return True
        return False

    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.students.insert(position + row, Student("test", "test", 0,''))
        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.students = (self.students[:position] + self.students[position + rows:])
        self.endRemoveRows()
        return True


class QTableViewDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTableViewDemo, self).__init__(parent)
        self.setWindowTitle("QTableModel案例")
        self.resize(500, 600)
        self.tableView = QTableView()
        self.model = StudentTableModel()
        self.model.initData()

        self.tableView.setModel(self.model)
        self.selectModel = QItemSelectionModel()
        self.tableView.setSelectionModel(self.selectModel)
        self.tableView.horizontalHeader().setStretchLastSection(True)

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



        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

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
