# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QDrag 例子

'''

import sys
from PySide6.QtWidgets import QPushButton, QWidget, QApplication
from PySide6.QtCore import Qt, QMimeData, QPoint,QByteArray
from PySide6.QtGui import QDrag
import PySide6

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        # print('b1 mouseMoveEvent 1')
        if e.buttons() != Qt.RightButton:
            return

        print('b1 mouseMoveEvent 1')
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        self.hotSpot = e.pos() - self.rect().topLeft()
        drag.setHotSpot(self.hotSpot)
        print('b1 mouseMoveEvent 2')
        dropAcion = drag.exec_(Qt.MoveAction)
        print('b1 mouseMoveEvent 3')
        print(dropAcion)


    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)

        if e.button() == Qt.LeftButton:
            print("请使用右键拖动")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.button = Button("鼠标用右键拖动", self)
        self.button.move(100, 65)

        self.button2 = QPushButton("鼠标用右键拖动2", self)
        self.button2.move(50, 35)

        self.setWindowTitle("拖拽应用案例1")
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, event):
        print('w dragEnterEvent')
        if event.mimeData().hasFormat("application/x-MyButton2"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.accept()

    def dropEvent(self, event:PySide6.QtGui.QDropEvent):
        print('w dropEnvent')
        if event.mimeData().hasFormat("application/x-MyButton2"):
            print('w dropEnvent b2 1')
            offset = self.offset
            self.child.move(event.position().toPoint() - offset)

            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
            print('w dropEnvent b2 2')
        else:
            print('w dropEnvent b1 1')
            position = event.pos()
            self.button.move(position-self.button.hotSpot)
            event.setDropAction(Qt.MoveAction)
            event.accept()
            print('w dropEnvent b1 2')
            # event.ignore()

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        print('w dragMoveEvent')
        if event.mimeData().hasFormat("application/x-MyButton2"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            # self.dragMoveEvent(event)
            event.accept()

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        print('w mousePressEvent')
        child = self.childAt(event.position().toPoint())

        if child is not self.button2:
            return
        print('w mousePressEvent b2 1')
        self.offset = QPoint(event.position().toPoint() - child.pos())
        self.child = child
        mimeData = QMimeData()
        mimeData.setData("application/x-MyButton2", QByteArray())

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        # drag.setPixmap(self.pixmap)
        drag.setHotSpot(event.position().toPoint() - child.pos())
        print('w mousePressEvent b2 2')
        moveAction = drag.exec_(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction)
        print('w mousePressEvent b2 3')
        print(moveAction)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()