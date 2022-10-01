# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combination.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(913, 971)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_10 = QAction(MainWindow)
        self.action_10.setObjectName(u"action_10")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_Qt = QAction(MainWindow)
        self.action_Qt.setObjectName(u"action_Qt")
        self.action_PyQt = QAction(MainWindow)
        self.action_PyQt.setObjectName(u"action_PyQt")
        self.action_12 = QAction(MainWindow)
        self.action_12.setObjectName(u"action_12")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget_PGMS = QTabWidget(self.centralWidget)
        self.tabWidget_PGMS.setObjectName(u"tabWidget_PGMS")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(44)
        sizePolicy1.setHeightForWidth(self.tabWidget_PGMS.sizePolicy().hasHeightForWidth())
        self.tabWidget_PGMS.setSizePolicy(sizePolicy1)
        self.tabWidget_PGMS.setMinimumSize(QSize(800, 700))
        self.tabWidget_PGMS.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_PGMS.setAutoFillBackground(True)
        self.tabWidget_PGMS.setStyleSheet(u"")
        self.tabWidget_PGMS.setTabBarAutoHide(True)
        self.tab_Combination = QWidget()
        self.tab_Combination.setObjectName(u"tab_Combination")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_Combination)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea_3 = QScrollArea(self.tab_Combination)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 852, 958))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)

        self.doubleSpinBox_returns_min = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_returns_min.setObjectName(u"doubleSpinBox_returns_min")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_returns_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_returns_min.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_returns_min.setMaximum(0.300000000000000)
        self.doubleSpinBox_returns_min.setSingleStep(0.010000000000000)
        self.doubleSpinBox_returns_min.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_returns_min, 1, 0, 1, 1)

        self.doubleSpinBox_returns_max = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_returns_max.setObjectName(u"doubleSpinBox_returns_max")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_returns_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_returns_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_returns_max.setMinimum(0.000000000000000)
        self.doubleSpinBox_returns_max.setMaximum(10.000000000000000)
        self.doubleSpinBox_returns_max.setSingleStep(0.100000000000000)
        self.doubleSpinBox_returns_max.setValue(0.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_returns_max, 1, 1, 1, 1)

        self.doubleSpinBox_maxdrawdown_min = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_maxdrawdown_min.setObjectName(u"doubleSpinBox_maxdrawdown_min")
        self.doubleSpinBox_maxdrawdown_min.setMinimum(0.100000000000000)
        self.doubleSpinBox_maxdrawdown_min.setMaximum(1.000000000000000)
        self.doubleSpinBox_maxdrawdown_min.setSingleStep(0.010000000000000)
        self.doubleSpinBox_maxdrawdown_min.setValue(0.700000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 0, 1, 1)

        self.doubleSpinBox_maxdrawdown_max = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_maxdrawdown_max.setObjectName(u"doubleSpinBox_maxdrawdown_max")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_maxdrawdown_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_maxdrawdown_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_maxdrawdown_max.setMinimum(0.200000000000000)
        self.doubleSpinBox_maxdrawdown_max.setMaximum(1.000000000000000)
        self.doubleSpinBox_maxdrawdown_max.setSingleStep(0.010000000000000)
        self.doubleSpinBox_maxdrawdown_max.setValue(1.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_maxdrawdown_max, 2, 1, 1, 1)

        self.doubleSpinBox_sharp_min = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_sharp_min.setObjectName(u"doubleSpinBox_sharp_min")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_sharp_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_sharp_min.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_sharp_min.setMaximum(40.000000000000000)
        self.doubleSpinBox_sharp_min.setSingleStep(0.050000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_sharp_min, 3, 0, 1, 1)

        self.doubleSpinBox_sharp_max = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.doubleSpinBox_sharp_max.setObjectName(u"doubleSpinBox_sharp_max")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_sharp_max.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_sharp_max.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_sharp_max.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_sharp_max, 3, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_5)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_start_combination = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_start_combination.setObjectName(u"pushButton_start_combination")

        self.horizontalLayout_3.addWidget(self.pushButton_start_combination)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_stock = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_stock.setObjectName(u"checkBox_stock")

        self.horizontalLayout_7.addWidget(self.checkBox_stock)

        self.checkBox_compound = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_compound.setObjectName(u"checkBox_compound")

        self.horizontalLayout_7.addWidget(self.checkBox_compound)

        self.checkBox_future_manage = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_future_manage.setObjectName(u"checkBox_future_manage")

        self.horizontalLayout_7.addWidget(self.checkBox_future_manage)

        self.checkBox_event = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_event.setObjectName(u"checkBox_event")

        self.horizontalLayout_7.addWidget(self.checkBox_event)

        self.checkBox_bond = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_bond.setObjectName(u"checkBox_bond")

        self.horizontalLayout_7.addWidget(self.checkBox_bond)

        self.checkBox_macro = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_macro.setObjectName(u"checkBox_macro")

        self.horizontalLayout_7.addWidget(self.checkBox_macro)

        self.checkBox_combination_fund = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_combination_fund.setObjectName(u"checkBox_combination_fund")

        self.horizontalLayout_7.addWidget(self.checkBox_combination_fund)

        self.checkBox_relative_fund = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_relative_fund.setObjectName(u"checkBox_relative_fund")

        self.horizontalLayout_7.addWidget(self.checkBox_relative_fund)

        self.checkBox_others = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_others.setObjectName(u"checkBox_others")

        self.horizontalLayout_7.addWidget(self.checkBox_others)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.QWebEngineview_Combination_monte_markovitz = QWebEngineView(self.scrollAreaWidgetContents_3)
        self.QWebEngineview_Combination_monte_markovitz.setObjectName(u"QWebEngineview_Combination_monte_markovitz")
        self.QWebEngineview_Combination_monte_markovitz.setMinimumSize(QSize(0, 300))
        self.QWebEngineview_Combination_monte_markovitz.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_8.addWidget(self.QWebEngineview_Combination_monte_markovitz)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.QWebEngineview_Combination_Pie = QWebEngineView(self.scrollAreaWidgetContents_3)
        self.QWebEngineview_Combination_Pie.setObjectName(u"QWebEngineview_Combination_Pie")
        self.QWebEngineview_Combination_Pie.setMinimumSize(QSize(50, 200))
        self.QWebEngineview_Combination_Pie.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.horizontalLayout_5.addWidget(self.QWebEngineview_Combination_Pie)

        self.QWebEngineview_Combination_Table = QWebEngineView(self.scrollAreaWidgetContents_3)
        self.QWebEngineview_Combination_Table.setObjectName(u"QWebEngineview_Combination_Table")
        self.QWebEngineview_Combination_Table.setMinimumSize(QSize(0, 200))
        self.QWebEngineview_Combination_Table.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.horizontalLayout_5.addWidget(self.QWebEngineview_Combination_Table)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.QWebEngineview_Combination_Versus = QWebEngineView(self.scrollAreaWidgetContents_3)
        self.QWebEngineview_Combination_Versus.setObjectName(u"QWebEngineview_Combination_Versus")
        self.QWebEngineview_Combination_Versus.setEnabled(True)
        self.QWebEngineview_Combination_Versus.setMinimumSize(QSize(0, 300))
        self.QWebEngineview_Combination_Versus.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.verticalLayout_8.addWidget(self.QWebEngineview_Combination_Versus)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.QWebEngineview_Combination_monte_markovitz.raise_()
        self.QWebEngineview_Combination_Versus.raise_()

        self.horizontalLayout_6.addWidget(self.scrollArea_3)

        self.tabWidget_PGMS.addTab(self.tab_Combination, "")

        self.verticalLayout_5.addWidget(self.tabWidget_PGMS)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 913, 23))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        self.tabWidget_PGMS.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u91d1\u91cf\u5316\u6295\u7814\u7cfb\u7edfv0.11", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u9ecf\u8d34", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u54c8\u54c8", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_10.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.action_Qt.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8eQt", None))
        self.action_PyQt.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8ePyQt", None))
        self.action_12.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.label_7.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6536\u76ca", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u56de\u64a4", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sharp\u6bd4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u8303\u56f4", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u8303\u56f4", None))
        self.pushButton_start_combination.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.checkBox_stock.setText(QCoreApplication.translate("MainWindow", u"\u80a1\u7968\u7b56\u7565", None))
        self.checkBox_compound.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5408\u7b56\u7565", None))
        self.checkBox_future_manage.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u671f\u8d27", None))
        self.checkBox_event.setText(QCoreApplication.translate("MainWindow", u"\u4e8b\u4ef6\u9a71\u52a8", None))
        self.checkBox_bond.setText(QCoreApplication.translate("MainWindow", u"\u503a\u5238\u7b56\u7565", None))
        self.checkBox_macro.setText(QCoreApplication.translate("MainWindow", u"\u5b8f\u89c2\u7b56\u7565", None))
        self.checkBox_combination_fund.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u5408\u57fa\u91d1", None))
        self.checkBox_relative_fund.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u5bf9\u4ef7\u503c", None))
        self.checkBox_others.setText(QCoreApplication.translate("MainWindow", u"\u5176\u5b83\u7b56\u7565", None))
        self.tabWidget_PGMS.setTabText(self.tabWidget_PGMS.indexOf(self.tab_Combination), QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7ec4\u5408\u7ba1\u7406", None))
    # retranslateUi

