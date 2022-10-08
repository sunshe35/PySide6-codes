# -*- coding: utf-8 -*-

"""
    【简介】
    自动化测试用例


"""

import unittest
import HTMLTestRunner
import time
from MatrixWinTest import MatrixWinTest
from PySide6.QtWidgets import QApplication
import sys
import os
os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(now)
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(MatrixWinTest))


    htmlFile = ".\\" + now + "HTMLtemplate.html"
    print('htmlFile=' + htmlFile)
    fp = open(htmlFile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"Qt for Python测试报告",
        description=u"用例测试情况")
    runner.run(testunit)
    app.exec()
    fp.close()

