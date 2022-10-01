# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinSignalSlog1.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(452, 296)
        self.closeWinBtn = QPushButton(Form)
        self.closeWinBtn.setObjectName(u"closeWinBtn")
        self.closeWinBtn.setGeometry(QRect(150, 80, 121, 31))

        self.retranslateUi(Form)
        self.closeWinBtn.clicked.connect(Form.close)
        self.closeWinBtn.pressed.connect(Form.testSlot)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.closeWinBtn.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u7a97\u53e3", None))
    # retranslateUi

