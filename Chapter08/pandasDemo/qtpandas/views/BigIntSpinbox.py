# -*- coding: utf-8 -*-
"""Custom spinbox for very big integers (like numpy.int64 and uint64)

@author: Matthias Ludwig - Datalyze Solutions
"""

from qtpandas.compat import Qt, QtCore, QtGui
try:
    from PySide6 import QtWidgets
except:
    from PyQt6 import  QtWidgets

class BigIntSpinbox(QtWidgets.QAbstractSpinBox):
    """Custom spinbox for very big integers (like numpy.int64 and uint64)

    Attributes:

    """

    def __init__(self, parent=None):
        """the __init__ method.

        Args:
            parent (QObject): defaults to None. If parent is 0, the new widget becomes a window.
                If parent is another widget, this widget becomes a child window inside parent.
                The new widget is deleted when its parent is deleted.

        """
        super(BigIntSpinbox, self).__init__(parent)

        self._singleStep = 1
        self._minimum = -18446744073709551616
        self._maximum = 18446744073709551615

        rx = QtCore.QRegExp("[0-9]\\d{0,20}")
        validator = QtGui.QRegExpValidator(rx, self)

        self._lineEdit = QtGui.QLineEdit(self)
        self._lineEdit.setText('0')
        self._lineEdit.setValidator(validator)
        self.setLineEdit(self._lineEdit)

    def value(self):
        """getter function to _lineEdit.text. Returns 0 in case of exception."""
        try:
            return int(self._lineEdit.text())
        except:
            return 0

    def setValue(self, value):
        """setter function to _lineEdit.text.  Sets minimum/maximum as new value if value is out of bounds.

        Args:
            value (int/long): new value to set.

        Returns
            True if all went fine.
        """
        if value >= self.minimum() and value <= self.maximum():
            self._lineEdit.setText(str(value))
        elif value < self.minimum():
            self._lineEdit.setText(str(self.minimum()))
        elif value > self.maximum():
            self._lineEdit.setText(str(self.maximum()))
        return True

    def stepBy(self, steps):
        """steps value up/down by a single step. Single step is defined in singleStep().

        Args:
            steps (int): positiv int steps up, negativ steps down
        """
        self.setValue(self.value() + steps*self.singleStep())

    def stepEnabled(self):
        """Virtual function that determines whether stepping up and down is legal at any given time.

        Returns:
            ored combination of StepUpEnabled | StepDownEnabled
        """
        if self.value() > self.minimum() and self.value() < self.maximum():
            return self.StepUpEnabled | self.StepDownEnabled
        elif self.value() <= self.minimum():
            return self.StepUpEnabled
        elif self.value() >= self.maximum():
            return self.StepDownEnabled

    def singleStep(self):
        """getter to _singleStep. determines the value to add if stepBy() is done."""
        return self._singleStep

    def setSingleStep(self, singleStep):
        """setter to _singleStep. converts negativ values to positiv ones.

        Args:
            singleStep (int): new _singleStep value. converts negativ values to positiv ones.

        Raises:
            TypeError: If the given argument is not an integer.

        Returns:
            int or long: the absolute value of the given argument.
        """
        if not isinstance(singleStep, int):
            raise TypeError("Argument is not of type int")
        # don't use negative values
        self._singleStep = abs(singleStep)
        return self._singleStep

    def minimum(self):
        """getter to _minimum. lowest possible number"""
        return self._minimum

    def setMinimum(self, minimum):
        """setter to _minimum.

        Args:
            minimum (int or long): new _minimum value.

        Raises:
            TypeError: If the given argument is not an integer.
        """
        if not isinstance(minimum, int):
            raise TypeError("Argument is not of type int or long")
        self._minimum = minimum

    def maximum(self):
        """getter to _maximum. biggest possible number"""
        return self._maximum

    def setMaximum(self, maximum):
        """setter to _maximum.

        Args:
            maximum (int or long): new _maximum value
        """
        if not isinstance(maximum, int):
            raise TypeError("Argument is not of type int or long")
        self._maximum = maximum