
import logging
log = logging.getLogger(__name__)


try:
    import sip
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)
    sip.setapi('QDate', 2)
    sip.setapi('QDateTime', 2)
    sip.setapi('QTextStream', 2)
    sip.setapi('QTime', 2)
    sip.setapi('QUrl', 2)
except ValueError as e:
    log.error(e)
except ImportError as e:
    log.error(e)

try:
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    from PyQt6.QtWidgets import *
except:
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *

try:
    from PyQt6 import QtCore as QtCore_
    from PyQt6 import QtGui as QtGui2
    from PyQt6 import QtWidgets as QtGui_
    from PyQt6.QtCore import pyqtSlot as Slot, pyqtSignal as Signal
except ImportError as e:
    from PySide6 import QtCore as QtCore_
    from PySide6 import QtGui as QtGui2
    from PySide6 import QtWidgets as QtGui_
    from PySide6.QtCore import Slot, Signal


QtCore = QtCore_
QtGui = QtGui_
Qt = QtCore_.Qt


