import sys
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class LCDNumberDemo(QWidget):
    def __init__(self, parent=None):
        super(LCDNumberDemo, self).__init__(parent)
        layout = QFormLayout()
        self.setLayout(layout)

        # 标准lcd
        self.lcd = QLCDNumber(self)
        self.lcd.display(time.strftime('%Y/%m-%d', time.localtime()))
        layout.addRow('标准lcd：', self.lcd)

        # 修改可显示数字长度
        self.lcd_count = QLCDNumber(self)
        self.lcd_count.setDigitCount(10)
        self.lcd_count.display(time.strftime('%Y/%m-%d', time.localtime()))
        layout.addRow('修改显示长度：', self.lcd_count)

        # 修改可显示类型
        self.lcd_style = QLCDNumber(self)
        self.lcd_style.setDigitCount(8)
        self.lcd_style.setSegmentStyle(self.lcd_style.Flat)
        layout.addRow('修改显示类型：', self.lcd_style)

        # 修改可显示模式
        self.lcd_mode = QLCDNumber(self)
        self.lcd_mode.setMode(QLCDNumber.Mode.Bin)
        self.lcd_mode.setDigitCount(8)
        self.lcd_mode.display(18)
        layout.addRow('18以2进制形式显示：', self.lcd_mode)

        # 定时器
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle("QLCDNumber demo")
        self.resize(150, 60)

    def showTime(self):
        text = time.strftime('%H:%M:%S', time.localtime())
        self.lcd_style.display(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LCDNumberDemo()
    window.show()
    sys.exit(app.exec())
