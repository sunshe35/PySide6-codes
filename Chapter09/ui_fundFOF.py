# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fundFOF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 535))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_parameter_tree = QWidget(self.scrollAreaWidgetContents)
        self.widget_parameter_tree.setObjectName(u"widget_parameter_tree")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_parameter_tree.sizePolicy().hasHeightForWidth())
        self.widget_parameter_tree.setSizePolicy(sizePolicy)
        self.widget_parameter_tree.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.widget_parameter_tree)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.QWebEngineView_ProductVsHs300 = QWebEngineView(self.scrollAreaWidgetContents)
        self.QWebEngineView_ProductVsHs300.setObjectName(u"QWebEngineView_ProductVsHs300")
        sizePolicy.setHeightForWidth(self.QWebEngineView_ProductVsHs300.sizePolicy().hasHeightForWidth())
        self.QWebEngineView_ProductVsHs300.setSizePolicy(sizePolicy)
        self.QWebEngineView_ProductVsHs300.setMinimumSize(QSize(0, 100))
        self.QWebEngineView_ProductVsHs300.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_3.addWidget(self.QWebEngineView_ProductVsHs300)

        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(200, 200))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.QWebEngineview_MonthReturn = QWebEngineView(self.tab)
        self.QWebEngineview_MonthReturn.setObjectName(u"QWebEngineview_MonthReturn")
        self.QWebEngineview_MonthReturn.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_2.addWidget(self.QWebEngineview_MonthReturn)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QWebEngineView_PeriodReturn = QWebEngineView(self.tab_2)
        self.QWebEngineView_PeriodReturn.setObjectName(u"QWebEngineView_PeriodReturn")
        self.QWebEngineView_PeriodReturn.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.horizontalLayout.addWidget(self.QWebEngineView_PeriodReturn)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.QWebEngineView_LagestBack = QWebEngineView(self.tab_3)
        self.QWebEngineView_LagestBack.setObjectName(u"QWebEngineView_LagestBack")
        self.QWebEngineView_LagestBack.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout.addWidget(self.QWebEngineView_LagestBack)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u91d1\u91cf\u5316\u6295\u7814\u7cfb\u7edfv0.11", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u6708\u5ea6\u6536\u76ca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u533a\u95f4\u6536\u76ca", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u56de\u64a4\u60c5\u51b5", None))
    # retranslateUi

