# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layoutWin2.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_LayoutDemo(object):
    def setupUi(self, LayoutDemo):
        if not LayoutDemo.objectName():
            LayoutDemo.setObjectName(u"LayoutDemo")
        LayoutDemo.resize(565, 430)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(LayoutDemo.sizePolicy().hasHeightForWidth())
        LayoutDemo.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(LayoutDemo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 504, 94))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.doubleSpinBox_returns_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_min.setObjectName(u"doubleSpinBox_returns_min")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.doubleSpinBox_returns_min.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_returns_min.setSizePolicy(sizePolicy2)
        self.doubleSpinBox_returns_min.setMaximum(0.800000000000000)
        self.doubleSpinBox_returns_min.setSingleStep(0.010000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_returns_min, 1, 0, 1, 1)

        self.doubleSpinBox_returns_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_returns_max.setObjectName(u"doubleSpinBox_returns_max")

        self.gridLayout.addWidget(self.doubleSpinBox_returns_max, 1, 1, 1, 1)

        self.doubleSpinBox_maxdrawdown_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdown_min.setObjectName(u"doubleSpinBox_maxdrawdown_min")

        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_min, 2, 0, 1, 1)

        self.doubleSpinBox_maxdrawdown_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_maxdrawdown_max.setObjectName(u"doubleSpinBox_maxdrawdown_max")

        self.gridLayout.addWidget(self.doubleSpinBox_maxdrawdown_max, 2, 1, 1, 1)

        self.doubleSpinBox_sharp_min = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_min.setObjectName(u"doubleSpinBox_sharp_min")

        self.gridLayout.addWidget(self.doubleSpinBox_sharp_min, 3, 0, 1, 1)

        self.doubleSpinBox_sharp_max = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sharp_max.setObjectName(u"doubleSpinBox_sharp_max")

        self.gridLayout.addWidget(self.doubleSpinBox_sharp_max, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.pushButton)

        LayoutDemo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LayoutDemo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 565, 23))
        LayoutDemo.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LayoutDemo)
        self.statusbar.setObjectName(u"statusbar")
        LayoutDemo.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.doubleSpinBox_returns_min)
        self.label_4.setBuddy(self.doubleSpinBox_maxdrawdown_min)
        self.label_5.setBuddy(self.doubleSpinBox_sharp_min)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(LayoutDemo)

        QMetaObject.connectSlotsByName(LayoutDemo)
    # setupUi

    def retranslateUi(self, LayoutDemo):
        LayoutDemo.setWindowTitle(QCoreApplication.translate("LayoutDemo", u"MainWindow", None))
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("LayoutDemo", u"&\u6536\u76ca", None))
        self.label_4.setText(QCoreApplication.translate("LayoutDemo", u"&\u6700\u5927\u56de\u64a4", None))
        self.label_5.setText(QCoreApplication.translate("LayoutDemo", u"&sharp\u6bd4", None))
        self.label.setText(QCoreApplication.translate("LayoutDemo", u"\u6700\u5c0f\u503c", None))
        self.label_2.setText(QCoreApplication.translate("LayoutDemo", u"\u6700\u5927\u503c", None))
        self.pushButton.setText(QCoreApplication.translate("LayoutDemo", u"\u5f00\u59cb", None))
    # retranslateUi

