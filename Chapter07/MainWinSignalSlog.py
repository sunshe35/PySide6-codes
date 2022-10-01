# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinSignalSlog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 225)
        self.controlsGroup = QGroupBox(Form)
        self.controlsGroup.setObjectName(u"controlsGroup")
        self.controlsGroup.setGeometry(QRect(10, 20, 451, 151))
        self.layoutWidget = QWidget(self.controlsGroup)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 411, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.numberSpinBox = QSpinBox(self.layoutWidget)
        self.numberSpinBox.setObjectName(u"numberSpinBox")

        self.horizontalLayout.addWidget(self.numberSpinBox)

        self.styleCombo = QComboBox(self.layoutWidget)
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.setObjectName(u"styleCombo")

        self.horizontalLayout.addWidget(self.styleCombo)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.printButton = QPushButton(self.layoutWidget)
        self.printButton.setObjectName(u"printButton")

        self.horizontalLayout.addWidget(self.printButton)

        self.layoutWidget1 = QWidget(self.controlsGroup)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 100, 201, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.previewStatus = QCheckBox(self.layoutWidget1)
        self.previewStatus.setObjectName(u"previewStatus")

        self.horizontalLayout_2.addWidget(self.previewStatus)

        self.previewButton = QPushButton(self.layoutWidget1)
        self.previewButton.setObjectName(u"previewButton")

        self.horizontalLayout_2.addWidget(self.previewButton)

        self.resultGroup = QGroupBox(Form)
        self.resultGroup.setObjectName(u"resultGroup")
        self.resultGroup.setGeometry(QRect(470, 20, 231, 151))
        self.resultLabel = QLabel(self.resultGroup)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(20, 30, 191, 101))

        self.retranslateUi(Form)
        self.previewButton.clicked.connect(Form.emitPreviewSignal)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6253\u5370\u63a7\u4ef6", None))
        self.controlsGroup.setTitle(QCoreApplication.translate("Form", u"\u6253\u5370\u63a7\u5236", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6253\u5370\u4efd\u6570:", None))
        self.styleCombo.setItemText(0, QCoreApplication.translate("Form", u"A3", None))
        self.styleCombo.setItemText(1, QCoreApplication.translate("Form", u"A4", None))
        self.styleCombo.setItemText(2, QCoreApplication.translate("Form", u"A5", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"\u7eb8\u5f20\u7c7b\u578b:", None))
        self.printButton.setText(QCoreApplication.translate("Form", u"\u6253\u5370", None))
        self.previewStatus.setText(QCoreApplication.translate("Form", u"\u5168\u5c4f\u9884\u89c8", None))
        self.previewButton.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
        self.resultGroup.setTitle(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u7ed3\u679c", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

