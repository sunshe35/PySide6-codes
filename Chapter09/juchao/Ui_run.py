# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(249, 20))

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_search = QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName(u"pushButton_search")

        self.horizontalLayout_2.addWidget(self.pushButton_search)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_setting_advanced = QPushButton(self.centralwidget)
        self.pushButton_setting_advanced.setObjectName(u"pushButton_setting_advanced")
        self.pushButton_setting_advanced.setCheckable(True)
        self.pushButton_setting_advanced.setChecked(True)
        self.pushButton_setting_advanced.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_setting_advanced)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.frame_advanced = QFrame(self.centralwidget)
        self.frame_advanced.setObjectName(u"frame_advanced")
        self.frame_advanced.setFrameShape(QFrame.StyledPanel)
        self.frame_advanced.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_advanced)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_unlimite_time_flag = QCheckBox(self.frame_advanced)
        self.checkBox_unlimite_time_flag.setObjectName(u"checkBox_unlimite_time_flag")
        self.checkBox_unlimite_time_flag.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_unlimite_time_flag)

        self.label = QLabel(self.frame_advanced)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.dateEdit = QDateEdit(self.frame_advanced)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMaximumSize(QSize(400, 16777215))
        self.dateEdit.setDateTime(QDateTime(QDate(2002, 10, 10), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2002, 10, 10))

        self.horizontalLayout.addWidget(self.dateEdit)

        self.label_2 = QLabel(self.frame_advanced)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.frame_advanced)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_sort_flag = QCheckBox(self.frame_advanced)
        self.checkBox_sort_flag.setObjectName(u"checkBox_sort_flag")
        self.checkBox_sort_flag.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_sort_flag)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.frame_advanced)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_type = QComboBox(self.frame_advanced)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.comboBox_type)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(self.frame_advanced)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.comboBox_name = QComboBox(self.frame_advanced)
        self.comboBox_name.addItem("")
        self.comboBox_name.addItem("")
        self.comboBox_name.addItem("")
        self.comboBox_name.setObjectName(u"comboBox_name")
        sizePolicy1.setHeightForWidth(self.comboBox_name.sizePolicy().hasHeightForWidth())
        self.comboBox_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.comboBox_name)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_show_path = QLabel(self.frame_advanced)
        self.label_show_path.setObjectName(u"label_show_path")
        self.label_show_path.setLayoutDirection(Qt.LeftToRight)
        self.label_show_path.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_show_path)

        self.pushButton_change_save_path = QPushButton(self.frame_advanced)
        self.pushButton_change_save_path.setObjectName(u"pushButton_change_save_path")
        sizePolicy1.setHeightForWidth(self.pushButton_change_save_path.sizePolicy().hasHeightForWidth())
        self.pushButton_change_save_path.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.pushButton_change_save_path)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_filter_title = QLineEdit(self.frame_advanced)
        self.lineEdit_filter_title.setObjectName(u"lineEdit_filter_title")

        self.gridLayout.addWidget(self.lineEdit_filter_title, 0, 1, 1, 1)

        self.checkBox_filter_title = QCheckBox(self.frame_advanced)
        self.checkBox_filter_title.setObjectName(u"checkBox_filter_title")

        self.gridLayout.addWidget(self.checkBox_filter_title, 0, 0, 1, 1)

        self.lineEdit_filter_content = QLineEdit(self.frame_advanced)
        self.lineEdit_filter_content.setObjectName(u"lineEdit_filter_content")

        self.gridLayout.addWidget(self.lineEdit_filter_content, 1, 1, 1, 1)

        self.checkBox_filter_content = QCheckBox(self.frame_advanced)
        self.checkBox_filter_content.setObjectName(u"checkBox_filter_content")

        self.gridLayout.addWidget(self.checkBox_filter_content, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.frame_advanced)

        self.tabWidget_title = QTabWidget(self.centralwidget)
        self.tabWidget_title.setObjectName(u"tabWidget_title")
        self.tab_title = QWidget()
        self.tab_title.setObjectName(u"tab_title")
        self.verticalLayout_2 = QVBoxLayout(self.tab_title)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_title = QTableWidget(self.tab_title)
        self.tableWidget_title.setObjectName(u"tableWidget_title")

        self.verticalLayout_2.addWidget(self.tableWidget_title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_title_up = QPushButton(self.tab_title)
        self.pushButton_title_up.setObjectName(u"pushButton_title_up")
        self.pushButton_title_up.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_title_up)

        self.label_page_info_title = QLabel(self.tab_title)
        self.label_page_info_title.setObjectName(u"label_page_info_title")
        self.label_page_info_title.setMaximumSize(QSize(50, 16777215))
        self.label_page_info_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_page_info_title)

        self.pushButton_title_down = QPushButton(self.tab_title)
        self.pushButton_title_down.setObjectName(u"pushButton_title_down")
        self.pushButton_title_down.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_title_down)

        self.lineEdit_title_page = QLineEdit(self.tab_title)
        self.lineEdit_title_page.setObjectName(u"lineEdit_title_page")
        self.lineEdit_title_page.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_title_page)

        self.pushButton_title_jump_to = QPushButton(self.tab_title)
        self.pushButton_title_jump_to.setObjectName(u"pushButton_title_jump_to")
        self.pushButton_title_jump_to.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_title_jump_to)

        self.checkBox_select_title = QCheckBox(self.tab_title)
        self.checkBox_select_title.setObjectName(u"checkBox_select_title")
        sizePolicy1.setHeightForWidth(self.checkBox_select_title.sizePolicy().hasHeightForWidth())
        self.checkBox_select_title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.checkBox_select_title)

        self.pushButton_download_select_title = QPushButton(self.tab_title)
        self.pushButton_download_select_title.setObjectName(u"pushButton_download_select_title")
        sizePolicy1.setHeightForWidth(self.pushButton_download_select_title.sizePolicy().hasHeightForWidth())
        self.pushButton_download_select_title.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.pushButton_download_select_title)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget_title.addTab(self.tab_title, "")
        self.tab_content = QWidget()
        self.tab_content.setObjectName(u"tab_content")
        self.verticalLayout = QVBoxLayout(self.tab_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_content = QTableWidget(self.tab_content)
        self.tableWidget_content.setObjectName(u"tableWidget_content")

        self.verticalLayout.addWidget(self.tableWidget_content)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_content_up = QPushButton(self.tab_content)
        self.pushButton_content_up.setObjectName(u"pushButton_content_up")
        self.pushButton_content_up.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_content_up)

        self.label_page_info_content = QLabel(self.tab_content)
        self.label_page_info_content.setObjectName(u"label_page_info_content")
        self.label_page_info_content.setMaximumSize(QSize(50, 16777215))
        self.label_page_info_content.setLayoutDirection(Qt.LeftToRight)
        self.label_page_info_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_page_info_content)

        self.pushButton_content_down = QPushButton(self.tab_content)
        self.pushButton_content_down.setObjectName(u"pushButton_content_down")
        self.pushButton_content_down.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_content_down)

        self.lineEdit_content_page = QLineEdit(self.tab_content)
        self.lineEdit_content_page.setObjectName(u"lineEdit_content_page")
        self.lineEdit_content_page.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_content_page)

        self.pushButton_content_jump_to = QPushButton(self.tab_content)
        self.pushButton_content_jump_to.setObjectName(u"pushButton_content_jump_to")
        self.pushButton_content_jump_to.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_content_jump_to)

        self.checkBox_select_content = QCheckBox(self.tab_content)
        self.checkBox_select_content.setObjectName(u"checkBox_select_content")
        sizePolicy1.setHeightForWidth(self.checkBox_select_content.sizePolicy().hasHeightForWidth())
        self.checkBox_select_content.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.checkBox_select_content)

        self.pushButton_download_select_content = QPushButton(self.tab_content)
        self.pushButton_download_select_content.setObjectName(u"pushButton_download_select_content")
        sizePolicy1.setHeightForWidth(self.pushButton_download_select_content.sizePolicy().hasHeightForWidth())
        self.pushButton_download_select_content.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.pushButton_download_select_content)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.tabWidget_title.addTab(self.tab_content, "")

        self.verticalLayout_4.addWidget(self.tabWidget_title)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_setting_advanced.setDefault(False)
        self.tabWidget_title.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5238\u5546\u62a5\u544a\u83b7\u53d6\u7cfb\u7edf", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.pushButton_setting_advanced.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7", None))
        self.checkBox_unlimite_time_flag.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u9650\u65f6\u95f4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.checkBox_sort_flag.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u9650\u6392\u5e8f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f\u7c7b\u578b\uff1a", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u964d\u5e8f", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5347\u5e8f", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f\u540d\u79f0\uff1a", None))
        self.comboBox_name.setItemText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u5173\u5ea6", None))
        self.comboBox_name.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None))
        self.comboBox_name.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4ee3\u7801", None))

        self.label_show_path.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6765\u663e\u793a\u8def\u5f84", None))
        self.pushButton_change_save_path.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filter_title.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u7528\u6765\u8fc7\u6ee4\u6807\u9898\u641c\u7d22\u548c\u5185\u5bb9\u641c\u7d22</span>\uff0c\u53ea\u9488\u5bf9\u8fd4\u56de\u7684\u6807\u9898\u8fdb\u884c\u8fc7\u6ee4\uff0c\u8bed\u6cd5\u793a\u4f8b\uff1a</p><p><span style=\" color:#ff0000;\">\u4e2d\u56fd&amp;\u4e2d\u8f66&amp;(\u5e74\u5ea6|\u5b63\u5ea6)</span></p><p>\u8868\u793a\u4ec5\u663e\u793a\u6807\u9898\u4e2d\u542b\u6709\u4e2d\u56fd\uff0c\u4e2d\u8f66\uff0c\u5e74\u5ea6or\u5b63\u5ea6\u5173\u952e<span style=\" font-weight:600;\">(\u5e74\u5ea6\u3001\u5b63\u5ea6\u4e8c\u9009\u4e00)</span>\u8bcd\u7684\u7ed3\u679c\u3002</p><p>\u8be5\u8fc7\u6ee4\u89c4\u5219\u540c\u6837\u9002\u7528\u4e8e\u4e0b\u8f7d\u3002</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_filter_title.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_filter_title.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4\u6807\u9898", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_filter_content.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u53ea\u7528\u6765\u8fc7\u6ee4\u5185\u5bb9\u641c\u7d22</span>\uff0c\u53ea\u9488\u5bf9\u8fd4\u56de\u7684\u6587\u7ae0\u5185\u5bb9\u8fdb\u884c\u8fc7\u6ee4<span style=\" font-weight:600;\">\uff08\u82e5\u6ca1\u6709\u6587\u7ae0\u5185\u5bb9\u8fd4\u56de\uff0c\u5219\u4e0d\u8fdb\u884c\u8fc7\u6ee4\uff09</span>\uff0c\u8bed\u6cd5\u793a\u4f8b\uff1a</p><p><span style=\" color:#ff0000;\">\u4e2d\u56fd&amp;\u4e2d\u8f66&amp;(\u5e74\u5ea6|\u5b63\u5ea6)</span></p><p>\u8868\u793a\u4ec5\u663e\u793a\u6807\u9898\u4e2d\u542b\u6709\u4e2d\u56fd\uff0c\u4e2d\u8f66\uff0c\u5e74\u5ea6or\u5b63\u5ea6<span style=\" font-weight:600;\">(\u5e74\u5ea6\u3001\u5b63\u5ea6\u4e8c\u9009\u4e00)</span>\u5173\u952e\u8bcd\u7684\u7ed3\u679c\u3002</p><p>\u8be5\u8fc7\u6ee4\u89c4\u5219\u540c\u6837\u9002\u7528\u4e8e\u4e0b\u8f7d\u3002</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_filter_content.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4\u6587\u7ae0", None))
        self.pushButton_title_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.label_page_info_title.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.pushButton_title_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_title_jump_to.setText(QCoreApplication.translate("MainWindow", u"\u9875\u9762\u8df3\u8f6c", None))
        self.checkBox_select_title.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5f53\u9875", None))
        self.pushButton_download_select_title.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6240\u9009", None))
        self.tabWidget_title.setTabText(self.tabWidget_title.indexOf(self.tab_title), QCoreApplication.translate("MainWindow", u"\u6807\u9898\u641c\u7d22", None))
        self.pushButton_content_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.label_page_info_content.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.pushButton_content_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_content_jump_to.setText(QCoreApplication.translate("MainWindow", u"\u9875\u9762\u8df3\u8f6c", None))
        self.checkBox_select_content.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5f53\u9875", None))
        self.pushButton_download_select_content.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6240\u9009", None))
        self.tabWidget_title.setTabText(self.tabWidget_title.indexOf(self.tab_content), QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u641c\u7d22", None))
    # retranslateUi

