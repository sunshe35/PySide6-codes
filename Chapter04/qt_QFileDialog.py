# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 QFileDialog 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel("此处显示文件信息")
        layout.addWidget(self.label)
        self.label2 = QLabel()
        layout.addWidget(self.label2)

        self.button_pic_filter1 = QPushButton("加载图片-过滤1(静态方法)")
        self.button_pic_filter1.clicked.connect(self.file_pic_filter1)
        layout.addWidget(self.button_pic_filter1)

        self.button_pic_filter2 = QPushButton("加载图片-过滤2(实例化方法)")
        self.button_pic_filter2.clicked.connect(self.file_pic_filter2)
        layout.addWidget(self.button_pic_filter2)

        self.button_pic_filter3 = QPushButton("加载图片-过滤3(实例化方法)")
        self.button_pic_filter3.clicked.connect(self.file_pic_filter3)
        layout.addWidget(self.button_pic_filter3)

        self.button_MultiFile1 = QPushButton("选择多个文件-过滤1(静态方法)")
        self.button_MultiFile1.clicked.connect(self.file_MultiFile1)
        layout.addWidget(self.button_MultiFile1)

        self.button_MultiFile2 = QPushButton("选择多个文件-过滤2(实例化方法)")
        self.button_MultiFile2.clicked.connect(self.file_MultiFile2)
        layout.addWidget(self.button_MultiFile2)

        self.button_file_mode = QPushButton("file_mode示例：选择文件夹")
        self.button_file_mode.clicked.connect(self.file_mode_show)
        layout.addWidget(self.button_file_mode)

        self.button_directory = QPushButton("选择文件夹(静态方法)")
        self.button_directory.clicked.connect(self.directory_show)
        layout.addWidget(self.button_directory)

        self.button_save = QPushButton("存储文件")
        self.button_save.clicked.connect(self.file_save)
        layout.addWidget(self.button_save)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog 例子")

    def file_pic_filter1(self):
        fname, _ = QFileDialog.getOpenFileName(self, caption='Open file1', dir=os.path.abspath('.') + '\\images',
                                               filter="Image files (*.jpg *.png);;Image files2(*.ico *.gif);;All files(*)")
        self.label.setPixmap(QPixmap(fname))
        self.label2.setText('你选择了:\n' + fname)

    def file_pic_filter2(self):
        file_dialog = QFileDialog(self, caption='Open file2', directory=os.path.abspath('.') + '\\images',
                                  filter="Image files (*.jpg *.png);;Image files2(*.ico *.gif);;All files(*)")

        if file_dialog.exec():
            file_path_list = file_dialog.selectedFiles()
            self.label.setPixmap(QPixmap(file_path_list[0]))
            self.label2.setText('你选择了:\n' + file_path_list[0])

    def file_pic_filter3(self):
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle('Open file3')
        file_dialog.setDirectory(os.path.abspath('.') + '\\images')
        file_dialog.setNameFilter("Image files (*.jpg *.png);;Image files2(*.ico *.gif);;All files(*)")

        if file_dialog.exec():
            file_path_list = file_dialog.selectedFiles()
            self.label.setPixmap(QPixmap(file_path_list[0]))
            self.label2.setText('你选择了:\n' + file_path_list[0])

    def file_MultiFile1(self):
        file_path_list, _ = QFileDialog.getOpenFileNames(self, caption='选择多个文件', dir=os.path.abspath('.'),
                                                         filter="All files(*);;Python files(*.py);;Image files (*.jpg *.png);;Image files2(*.ico *.gif)")
        self.label.setText('你选择了如下路径：\n' + ';\n'.join(file_path_list))
        self.label2.setText('')

    def file_MultiFile2(self):
        file_dialog = QFileDialog(self, caption='选择多个文件', directory=os.path.abspath('.'),
                                  filter="All files(*);;Python files(*.py);;Image files (*.jpg *.png);;Image files2(*.ico *.gif)")
        file_dialog.setFileMode(file_dialog.ExistingFiles)
        if file_dialog.exec():
            file_path_list = file_dialog.selectedFiles()
            self.label.setText('你选择了如下路径：\n' + ';\n'.join(file_path_list))
            self.label2.setText('')

    def file_mode_show(self):
        file_dialog = QFileDialog(self, caption='file_mode示例：选择文件夹', directory=os.path.abspath('.'))
        file_dialog.setFileMode(file_dialog.Directory)
        if file_dialog.exec():
            file_path_list = file_dialog.selectedFiles()
            self.label.setText('你选择了如下路径：\n' + ';\n'.join(file_path_list))
            self.label2.setText('')

    def directory_show(self):
        directory_path = QFileDialog.getExistingDirectory(caption='获取存储路径', dir=os.path.abspath('.'))
        self.label.setText('获取目录：\n' + directory_path)
        self.label2.setText('')

    def file_save(self):
        file_save_path, _ = QFileDialog.getSaveFileName(self, caption='获取存储路径', dir=os.path.abspath('.'),
                                                        filter="All files(*);;Python files(*.py);;Image files (*.jpg *.png);;Image files2(*.ico *.gif)")
        self.label.setText('存储路径如下：\n' + file_save_path)
        self.label2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec())
