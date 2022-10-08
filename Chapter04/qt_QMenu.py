# -*- coding: utf-8 -*-

'''
    【简介】
	PySide6中 Qmenu 例子
   
  
'''

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
os.chdir(os.path.dirname(__file__))

class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.infoLabel = QLabel("<i>Choose a menu option, or right-click to invoke a context menu</i>")
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter)

        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(topFiller)
        layout.addWidget(self.infoLabel)
        layout.addWidget(bottomFiller)
        widget.setLayout(layout)

        self.createActions()
        self.createMenus()

        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Menus")
        self.setMinimumSize(160, 160)
        self.resize(480, 320)


    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec(event.globalPos())

    def newFile(self):
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def open(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")

    def save(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def print(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def bold(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def italic(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def leftAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def rightAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def justify(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def center(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def setLineSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def setParagraphSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def about(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                          "The <b>Menu</b> example shows how to create menu-bar menus and context menus.")

    def aboutQt(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")

    def createActions(self):
        self.newAct = QAction(QIcon("./images/new.png"), "&New")
        self.newAct.setShortcuts(QKeySequence.New)
        self.newAct.setStatusTip("Create a new file")
        self.newAct.triggered.connect(self.newFile)

        self.openAct = QAction(QIcon("./images/open.png"), "&Open...")
        self.openAct.setShortcuts(QKeySequence.Open)
        self.openAct.setStatusTip("Open an existing file")
        self.openAct.triggered.connect(self.open)

        self.saveAct = QAction(QIcon("./images/save.png"), "&Save")
        self.saveAct.setShortcuts(QKeySequence.Save)
        self.saveAct.setStatusTip("Save the document to disk")
        self.saveAct.triggered.connect(self.save)

        self.printAct = QAction("&Print...")
        self.printAct.setShortcuts(QKeySequence.Print)
        self.printAct.setStatusTip("Print the document")
        self.printAct.triggered.connect(self.print)

        self.exitAct = QAction("E&xit")
        self.exitAct.setShortcuts(QKeySequence.Quit)
        self.exitAct.setStatusTip("Exit the application")
        self.exitAct.triggered.connect(self.close)

        self.undoAct = QAction("&Undo")
        self.undoAct.setShortcuts(QKeySequence.Undo)
        self.undoAct.setStatusTip("Undo the last operation")
        self.undoAct.triggered.connect(self.undo)

        self.redoAct = QAction("&Redo")
        self.redoAct.setShortcuts(QKeySequence.Redo)
        self.redoAct.setStatusTip("Redo the last operation")
        self.redoAct.triggered.connect(self.redo)

        self.cutAct = QAction("Cu&t")
        self.cutAct.setShortcuts(QKeySequence.Cut)
        self.cutAct.setStatusTip("Cut the current selection's contents to the clipboard")
        self.cutAct.triggered.connect(self.cut)

        self.copyAct = QAction("&Copy")
        self.copyAct.setShortcuts(QKeySequence.Copy)
        self.copyAct.setStatusTip("Copy the current selection's contents to the clipboard")
        self.copyAct.triggered.connect(self.copy)

        self.pasteAct = QAction("&Paste")
        self.pasteAct.setShortcuts(QKeySequence.Paste)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into the current selection")
        self.pasteAct.triggered.connect(self.paste)

        self.boldAct = QAction("&Bold")
        self.boldAct.setCheckable(True)
        self.boldAct.setShortcut(QKeySequence.Bold)
        self.boldAct.setStatusTip("Make the text bold")
        self.boldAct.triggered.connect(self.bold)

        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QAction("&Italic")
        self.italicAct.setCheckable(True)
        self.italicAct.setShortcut(QKeySequence.Italic)
        self.italicAct.setStatusTip("Make the text italic")
        self.italicAct.triggered.connect(self.italic)

        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QAction("Set &Line Spacing...")
        self.setLineSpacingAct.setStatusTip("Change the gap between the lines of a paragraph")
        self.setLineSpacingAct.triggered.connect(self.setLineSpacing)

        self.setParagraphSpacingAct = QAction("Set &Paragraph Spacing...")
        self.setParagraphSpacingAct.setStatusTip("Change the gap between paragraphs")
        self.setParagraphSpacingAct.triggered.connect(self.setParagraphSpacing)

        self.aboutAct = QAction("&About")
        self.aboutAct.setStatusTip("Show the application's About box")
        self.aboutAct.triggered.connect(self.about)

        self.aboutQtAct = QAction("About &Qt")
        self.aboutQtAct.setStatusTip("Show the Qt library's About box")
        self.aboutQtAct.triggered.connect(QApplication.aboutQt)
        self.aboutQtAct.triggered.connect(self.aboutQt)

        self.leftAlignAct = QAction("&Left Align")
        self.leftAlignAct.setCheckable(True)
        self.leftAlignAct.setShortcut("Ctrl+L")
        self.leftAlignAct.setStatusTip("Left align the selected text")
        self.leftAlignAct.triggered.connect(self.leftAlign)

        self.rightAlignAct = QAction("&Right Align")
        self.rightAlignAct.setCheckable(True)
        self.rightAlignAct.setShortcut("Ctrl+R")
        self.rightAlignAct.setStatusTip("Right align the selected text")
        self.rightAlignAct.triggered.connect(self.rightAlign)

        self.justifyAct = QAction("&Justify")
        self.justifyAct.setCheckable(True)
        self.justifyAct.setShortcut("Ctrl+J")
        self.justifyAct.setStatusTip("Justify the selected text")
        self.justifyAct.triggered.connect(self.justify)

        self.centerAct = QAction("&Center")
        self.centerAct.setCheckable(True)
        self.centerAct.setShortcut("Ctrl+E")
        self.centerAct.setStatusTip("Center the selected text")
        self.centerAct.triggered.connect(self.center)

        alignmentGroup = QActionGroup(self)
        alignmentGroup.addAction(self.leftAlignAct)
        alignmentGroup.addAction(self.rightAlignAct)
        alignmentGroup.addAction(self.justifyAct)
        alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.newAct)

        fileMenu.addAction(self.openAct)

        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.printAct)

        fileMenu.addSeparator()

        fileMenu.addAction(self.exitAct)

        editMenu = self.menuBar().addMenu("&Edit")
        editMenu.addAction(self.undoAct)
        editMenu.addAction(self.redoAct)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAct)
        editMenu.addAction(self.copyAct)
        editMenu.addAction(self.pasteAct)
        editMenu.addSeparator()

        helpMenu = self.menuBar().addMenu("&Help")
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        formatMenu = editMenu.addMenu("&Format")
        formatMenu.addAction(self.boldAct)
        formatMenu.addAction(self.italicAct)
        formatMenu.addSeparator().setText("Alignment")
        formatMenu.addAction(self.leftAlignAct)
        formatMenu.addAction(self.rightAlignAct)
        formatMenu.addAction(self.justifyAct)
        formatMenu.addAction(self.centerAct)
        formatMenu.addSeparator()
        formatMenu.addAction(self.setLineSpacingAct)
        formatMenu.addAction(self.setParagraphSpacingAct)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MenuDemo()
    demo.show()
    sys.exit(app.exec())
