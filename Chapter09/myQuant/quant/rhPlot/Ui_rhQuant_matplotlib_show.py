# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rhQuant_matplotlib_show.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from .rhMatplotlibWidget import MatplotlibWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 763, 572))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_show_dataPre = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_show_dataPre.setObjectName(u"pushButton_show_dataPre")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_show_dataPre.sizePolicy().hasHeightForWidth())
        self.pushButton_show_dataPre.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_show_dataPre)

        self.pushButton_show_trade_flow = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_show_trade_flow.setObjectName(u"pushButton_show_trade_flow")
        sizePolicy.setHeightForWidth(self.pushButton_show_trade_flow.sizePolicy().hasHeightForWidth())
        self.pushButton_show_trade_flow.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_show_trade_flow)

        self.pushButton_show_money_flow = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_show_money_flow.setObjectName(u"pushButton_show_money_flow")
        sizePolicy.setHeightForWidth(self.pushButton_show_money_flow.sizePolicy().hasHeightForWidth())
        self.pushButton_show_money_flow.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton_show_money_flow)

        self.pushButton_hide_output = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_hide_output.setObjectName(u"pushButton_hide_output")
        sizePolicy.setHeightForWidth(self.pushButton_hide_output.sizePolicy().hasHeightForWidth())
        self.pushButton_hide_output.setSizePolicy(sizePolicy)
        self.pushButton_hide_output.setCheckable(True)
        self.pushButton_hide_output.setChecked(True)

        self.horizontalLayout_2.addWidget(self.pushButton_hide_output)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 210))

        self.verticalLayout.addWidget(self.tableWidget)

        self.matplotlibwidget_static = MatplotlibWidget(self.scrollAreaWidgetContents)
        self.matplotlibwidget_static.setObjectName(u"matplotlibwidget_static")
        self.matplotlibwidget_static.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.matplotlibwidget_static)

        self.matplotlibwidget_day = MatplotlibWidget(self.scrollAreaWidgetContents)
        self.matplotlibwidget_day.setObjectName(u"matplotlibwidget_day")
        self.matplotlibwidget_day.setMinimumSize(QSize(0, 200))

        self.verticalLayout.addWidget(self.matplotlibwidget_day)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_hide_output.clicked["bool"].connect(self.tableWidget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_show_dataPre.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6570\u636e\u5904\u7406(\u968f\u673a)", None))
        self.pushButton_show_trade_flow.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u4ea4\u6613\u6d41\u6c34", None))
        self.pushButton_show_money_flow.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8d44\u91d1\u6d41\u6c34", None))
        self.pushButton_hide_output.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u8f93\u51fa\u7ed3\u679c", None))
    # retranslateUi

