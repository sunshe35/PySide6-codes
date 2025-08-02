# -*- coding: utf-8 -*-

import sys 	
from PySide6.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from MainWinMenuToolbar import Ui_MainWindow
from PySide6.QtCore import QCoreApplication
import os

class MainForm( QMainWindow , Ui_MainWindow):  
	def __init__(self):  
		super(MainForm,self).__init__()  
		self.setupUi(self) 
		# 菜单的点击事件，当点击关闭菜单时连接槽函数 close()     
		self.fileCloseAction.triggered.connect(self.close)  
		# 菜单的点击事件，当点击打开菜单时连接槽函数 openFile()     
		self.fileOpenAction.triggered.connect(self.openFile)

		# 打开计算器
		self.openCalc.triggered.connect(lambda :os.system('calc'))

		# 打开记事本
		self.openNotepad.triggered.connect(lambda :os.system('notepad'))



	def openFile(self):
		file,ok= QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)") 
		# 在状态栏显示文件地址  		
		self.statusbar.showMessage(file)                   
    
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec())
