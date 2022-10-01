# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinQrc.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QWidget)
import apprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(608, 479)
        self.fileOpenAction = QAction(MainWindow)
        self.fileOpenAction.setObjectName(u"fileOpenAction")
        icon = QIcon()
        icon.addFile(u":/pic/images/open.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileOpenAction.setIcon(icon)
        self.fileNewAction = QAction(MainWindow)
        self.fileNewAction.setObjectName(u"fileNewAction")
        icon1 = QIcon()
        icon1.addFile(u":/pic/images/new.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileNewAction.setIcon(icon1)
        self.fileCloseAction = QAction(MainWindow)
        self.fileCloseAction.setObjectName(u"fileCloseAction")
        icon2 = QIcon()
        icon2.addFile(u"images/close.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.fileCloseAction.setIcon(icon2)
        self.openCalc = QAction(MainWindow)
        self.openCalc.setObjectName(u"openCalc")
        icon3 = QIcon()
        icon3.addFile(u":/pic/images/calc.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.openCalc.setIcon(icon3)
        self.openNotepad = QAction(MainWindow)
        self.openNotepad.setObjectName(u"openNotepad")
        icon4 = QIcon()
        icon4.addFile(u"images/notepad.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.openNotepad.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 491, 321))
        self.label.setPixmap(QPixmap(u"images/python.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 608, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.fileNewAction)
        self.menu.addAction(self.fileCloseAction)
        self.toolBar.addAction(self.openCalc)
        self.toolBar.addAction(self.openNotepad)
        self.toolBar.addAction(self.fileOpenAction)
        self.toolBar.addAction(self.fileNewAction)
        self.toolBar.addAction(self.fileCloseAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileOpenAction.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.fileOpenAction.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.fileNewAction.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.fileNewAction.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+N", None))
#endif // QT_CONFIG(shortcut)
        self.fileCloseAction.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#if QT_CONFIG(shortcut)
        self.fileCloseAction.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.openCalc.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u5668", None))
#if QT_CONFIG(tooltip)
        self.openCalc.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8ba1\u7b97\u5668", None))
#endif // QT_CONFIG(tooltip)
        self.openNotepad.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4e8b\u672c", None))
#if QT_CONFIG(tooltip)
        self.openNotepad.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8bb0\u4e8b\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

