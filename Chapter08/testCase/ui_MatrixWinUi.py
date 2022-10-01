# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MatrixWinUi.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollBar, QSizePolicy, QSlider,
    QSpinBox, QTextEdit, QWidget)

class Ui_MatrixWin(object):
    def setupUi(self, MatrixWin):
        if not MatrixWin.objectName():
            MatrixWin.setObjectName(u"MatrixWin")
        MatrixWin.resize(742, 461)
        self.groupBox = QGroupBox(MatrixWin)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 210, 451, 191))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.speedButton1 = QRadioButton(self.groupBox)
        self.speedButtonGroup = QButtonGroup(MatrixWin)
        self.speedButtonGroup.setObjectName(u"speedButtonGroup")
        self.speedButtonGroup.addButton(self.speedButton1)
        self.speedButton1.setObjectName(u"speedButton1")

        self.gridLayout_2.addWidget(self.speedButton1, 0, 0, 1, 1)

        self.speedButton3 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton3)
        self.speedButton3.setObjectName(u"speedButton3")

        self.gridLayout_2.addWidget(self.speedButton3, 0, 2, 1, 1)

        self.speedButton4 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton4)
        self.speedButton4.setObjectName(u"speedButton4")

        self.gridLayout_2.addWidget(self.speedButton4, 1, 0, 1, 1)

        self.speedButton5 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton5)
        self.speedButton5.setObjectName(u"speedButton5")
        self.speedButton5.setChecked(True)

        self.gridLayout_2.addWidget(self.speedButton5, 1, 1, 1, 1)

        self.speedButton6 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton6)
        self.speedButton6.setObjectName(u"speedButton6")

        self.gridLayout_2.addWidget(self.speedButton6, 1, 2, 1, 1)

        self.speedButton9 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton9)
        self.speedButton9.setObjectName(u"speedButton9")

        self.gridLayout_2.addWidget(self.speedButton9, 3, 2, 1, 1)

        self.speedButton8 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton8)
        self.speedButton8.setObjectName(u"speedButton8")

        self.gridLayout_2.addWidget(self.speedButton8, 3, 1, 1, 1)

        self.speedButton7 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton7)
        self.speedButton7.setObjectName(u"speedButton7")

        self.gridLayout_2.addWidget(self.speedButton7, 3, 0, 1, 1)

        self.speedButton2 = QRadioButton(self.groupBox)
        self.speedButtonGroup.addButton(self.speedButton2)
        self.speedButton2.setObjectName(u"speedButton2")

        self.gridLayout_2.addWidget(self.speedButton2, 0, 1, 1, 1)

        self.resultGroup = QGroupBox(MatrixWin)
        self.resultGroup.setObjectName(u"resultGroup")
        self.resultGroup.setGeometry(QRect(470, 210, 261, 191))
        self.resultText = QTextEdit(self.resultGroup)
        self.resultText.setObjectName(u"resultText")
        self.resultText.setGeometry(QRect(10, 20, 241, 161))
        self.layoutWidget = QWidget(MatrixWin)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 420, 390, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.okBtn = QPushButton(self.layoutWidget)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)

        self.clearBtn = QPushButton(self.layoutWidget)
        self.clearBtn.setObjectName(u"clearBtn")

        self.horizontalLayout.addWidget(self.clearBtn)

        self.cancelBtn = QPushButton(self.layoutWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.groupBox_2 = QGroupBox(MatrixWin)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 721, 191))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 151, 21))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 151, 21))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 131, 21))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 151, 22))
        self.tequilaScrollBar = QScrollBar(self.groupBox_2)
        self.tequilaScrollBar.setObjectName(u"tequilaScrollBar")
        self.tequilaScrollBar.setEnabled(True)
        self.tequilaScrollBar.setGeometry(QRect(130, 30, 361, 21))
        self.tequilaScrollBar.setMaximum(11)
        self.tequilaScrollBar.setValue(8)
        self.tequilaScrollBar.setSliderPosition(8)
        self.tequilaScrollBar.setOrientation(Qt.Horizontal)
        self.tripleSecSpinBox = QSpinBox(self.groupBox_2)
        self.tripleSecSpinBox.setObjectName(u"tripleSecSpinBox")
        self.tripleSecSpinBox.setGeometry(QRect(130, 60, 250, 21))
        self.tripleSecSpinBox.setMaximum(11)
        self.tripleSecSpinBox.setValue(4)
        self.limeJuiceLineEdit = QLineEdit(self.groupBox_2)
        self.limeJuiceLineEdit.setObjectName(u"limeJuiceLineEdit")
        self.limeJuiceLineEdit.setGeometry(QRect(130, 90, 257, 21))
        self.iceHorizontalSlider = QSlider(self.groupBox_2)
        self.iceHorizontalSlider.setObjectName(u"iceHorizontalSlider")
        self.iceHorizontalSlider.setGeometry(QRect(130, 120, 250, 22))
        self.iceHorizontalSlider.setMinimum(0)
        self.iceHorizontalSlider.setMaximum(20)
        self.iceHorizontalSlider.setValue(12)
        self.iceHorizontalSlider.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(610, 30, 61, 21))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(610, 50, 61, 21))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(610, 80, 61, 21))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(610, 120, 61, 21))
        self.selScrollBarLbl = QLabel(self.groupBox_2)
        self.selScrollBarLbl.setObjectName(u"selScrollBarLbl")
        self.selScrollBarLbl.setGeometry(QRect(520, 30, 51, 21))
        self.selIceSliderLbl = QLabel(self.groupBox_2)
        self.selIceSliderLbl.setObjectName(u"selIceSliderLbl")
        self.selIceSliderLbl.setGeometry(QRect(520, 120, 51, 21))

        self.retranslateUi(MatrixWin)
        self.okBtn.clicked.connect(MatrixWin.uiAccept)
        self.cancelBtn.clicked.connect(MatrixWin.uiReject)
        self.clearBtn.clicked.connect(MatrixWin.uiClear)
        self.iceHorizontalSlider.valueChanged.connect(MatrixWin.uiIceSliderValueChanged)
        self.tequilaScrollBar.valueChanged.connect(MatrixWin.uiScrollBarValueChanged)

        QMetaObject.connectSlotsByName(MatrixWin)
    # setupUi

    def retranslateUi(self, MatrixWin):
        MatrixWin.setWindowTitle(QCoreApplication.translate("MatrixWin", u"\u739b\u683c\u4e3d\u7279\u9e21\u5c3e\u9152*\u8c03\u9152\u5668", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MatrixWin", u"Speed of the blender", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MatrixWin", u"9\u79cd\u6405\u62cc\u901f\u5ea6", None))
        self.speedButton1.setText(QCoreApplication.translate("MatrixWin", u"&Mix", None))
        self.speedButton3.setText(QCoreApplication.translate("MatrixWin", u"&Puree", None))
        self.speedButton4.setText(QCoreApplication.translate("MatrixWin", u"&Chop", None))
        self.speedButton5.setText(QCoreApplication.translate("MatrixWin", u"&Karate Chop", None))
        self.speedButton6.setText(QCoreApplication.translate("MatrixWin", u"&Beat", None))
        self.speedButton9.setText(QCoreApplication.translate("MatrixWin", u"&Vaporize", None))
        self.speedButton8.setText(QCoreApplication.translate("MatrixWin", u"&Liquefy", None))
        self.speedButton7.setText(QCoreApplication.translate("MatrixWin", u"&Smash", None))
        self.speedButton2.setText(QCoreApplication.translate("MatrixWin", u"&Whip", None))
        self.resultGroup.setTitle(QCoreApplication.translate("MatrixWin", u"\u64cd\u4f5c\u7ed3\u679c", None))
        self.okBtn.setText(QCoreApplication.translate("MatrixWin", u"OK", None))
        self.clearBtn.setText(QCoreApplication.translate("MatrixWin", u"Clear", None))
        self.cancelBtn.setText(QCoreApplication.translate("MatrixWin", u"Cancel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MatrixWin", u"\u539f\u6599", None))
        self.label.setText(QCoreApplication.translate("MatrixWin", u"\u9f99\u820c\u5170\u9152", None))
        self.label_2.setText(QCoreApplication.translate("MatrixWin", u"\u4e09\u91cd\u84b8\u998f\u9152", None))
        self.label_7.setText(QCoreApplication.translate("MatrixWin", u"\u67e0\u6aac\u6c41", None))
        self.label_4.setText(QCoreApplication.translate("MatrixWin", u"\u51b0\u5757", None))
#if QT_CONFIG(tooltip)
        self.tequilaScrollBar.setToolTip(QCoreApplication.translate("MatrixWin", u"Jiggers of tequila", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tripleSecSpinBox.setToolTip(QCoreApplication.translate("MatrixWin", u"Jiggers of triple sec", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.limeJuiceLineEdit.setToolTip(QCoreApplication.translate("MatrixWin", u"Jiggers of lime juice", None))
#endif // QT_CONFIG(tooltip)
        self.limeJuiceLineEdit.setText(QCoreApplication.translate("MatrixWin", u"12.0", None))
#if QT_CONFIG(tooltip)
        self.iceHorizontalSlider.setToolTip(QCoreApplication.translate("MatrixWin", u"Chunks of ice", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MatrixWin", u"\u5347", None))
        self.label_3.setText(QCoreApplication.translate("MatrixWin", u"\u5347", None))
        self.label_8.setText(QCoreApplication.translate("MatrixWin", u"\u5347", None))
        self.label_5.setText(QCoreApplication.translate("MatrixWin", u"\u4e2a", None))
        self.selScrollBarLbl.setText("")
        self.selIceSliderLbl.setText("")
    # retranslateUi

