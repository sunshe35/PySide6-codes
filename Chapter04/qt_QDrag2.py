# -*- coding: utf-8 -*-
'''
    【简介】
	PySide6中 QDrag 应用案例

'''
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import PySide6
import sys
import os
os.chdir(os.path.dirname(__file__))

class DragWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setAcceptDrops(True)

        self.icon1 = QLabel('icon1',self)
        self.icon1.setPixmap(QPixmap("./images/save.png"))
        self.icon1.move(10, 10)
        self.icon1.setAttribute(Qt.WA_DeleteOnClose)

        self.icon2 = QLabel('icon2',self)
        self.icon2.setPixmap(QPixmap("./images/new.png"))
        self.icon2.move(100, 10)
        self.icon2.setAttribute(Qt.WA_DeleteOnClose)

        self.icon3 = QLabel('icon3',self)
        self.icon3.setPixmap(QPixmap("./images/open.png"))
        self.icon3.move(10, 80)
        self.icon3.setAttribute(Qt.WA_DeleteOnClose)

    def dragEnterEvent(self, event: PySide6.QtGui.QDragEnterEvent) -> None:
        if event.mimeData().hasFormat("application/x-dnditemdata"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event: PySide6.QtGui.QDragMoveEvent) -> None:
        if event.mimeData().hasFormat("application/x-dnditemdata"):
            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        if event.mimeData().hasFormat("application/x-dnditemdata"):

            # 接收 QMimeData中的 QPixmap数据
            itemData = event.mimeData().data("application/x-dnditemdata")
            pixmap = self.QByteArray2QPixmap(itemData)
            # pixmap = event.mimeData().imageData()
            # pixmap = self.parent().pixmap

            # 接收父类中的 QPoint 数据
            offset = self.parent().offset

            # 新建icon
            newIcon = QLabel('哈哈',self)
            newIcon.setPixmap(pixmap)
            newIcon.move(event.position().toPoint() - offset)
            newIcon.show()
            newIcon.setAttribute(Qt.WA_DeleteOnClose)

            if event.source() == self:
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()
        else:
            event.ignore()

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:

        child = self.childAt(event.position().toPoint())
        if not child:
            return

        # 通过 QMimeData传递 QPixmap数据
        pixmap = child.pixmap()
        # self.parent().pixmap = pixmap
        itemData = self.QPixmap2QByteArray(pixmap)
        mimeData = QMimeData()
        mimeData.setData("application/x-dnditemdata", itemData)
        # mimeData.setImageData(pixmap)

        # 通过共同的父类传递 QPoint 数据
        offset = QPoint(event.position().toPoint() - child.pos())
        self.parent().offset = offset

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.position().toPoint() - child.pos())

        # 触发MoveAction行为会关闭原来的icon，否则不关闭。
        action = drag.exec(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction)
        print(action)
        if  action== Qt.MoveAction:
            child.close()
        else:
            child.show()
            # child.setPixmap(pixmap)

    def QPixmap2QByteArray(self, q_image: QImage) -> QByteArray:
        """
            Args:
                 q_image: 待转化为字节流的QImage。
            Returns:
                 q_image转化成的byte array。
        """
        # 获取一个空的字节数组
        byte_array = QByteArray()
        # 将字节数组绑定到输出流上
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        # 将数据使用png格式进行保存
        q_image.save(buffer, "png", quality=100)
        return byte_array

    def QByteArray2QPixmap(self, byte_array: QByteArray):
            """
            Args:
                byte_array: 字节流图像。
            Returns:
                byte_array对应的字节流数组。
            """
            # 设置字节流输入池。
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.ReadOnly)
            # 读取图片。
            reader = QImageReader(buffer)
            img = QPixmap(reader.read())

            return img





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    horizontalLayout = QHBoxLayout(mainWidget)
    horizontalLayout.addWidget(DragWidget())
    horizontalLayout.addWidget(DragWidget())
    mainWidget.setWindowTitle('实现窗体内的拖拽和窗体间的复制')
    mainWidget.show()
    sys.exit(app.exec())