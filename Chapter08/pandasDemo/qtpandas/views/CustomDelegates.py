# -*- coding: utf-8 -*-


from qtpandas.compat import Qt, QtCore, QtGui, Signal, Slot
try:
    from PySide6 import QtWidgets
except:
    from PyQt6 import  QtWidgets

import numpy
from qtpandas.views.BigIntSpinbox import BigIntSpinbox
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.models.SupportedDtypes import SupportedDtypes

def createDelegate(dtype, column, view):
    try:
        model = view.model()
    except AttributeError:
        raise

    if model is None:
        raise ValueError('no model set for the current view')

    if not isinstance(model, DataFrameModel):
        raise TypeError('model is not of type DataFrameModel')

    if dtype in model._intDtypes:
        intInfo = numpy.iinfo(dtype)
        delegate = BigIntSpinboxDelegate(intInfo.min, intInfo.max, parent=view)
    elif dtype in model._floatDtypes:
        floatInfo = numpy.finfo(dtype)
        delegate = CustomDoubleSpinboxDelegate(floatInfo.min, floatInfo.max, decimals=model._float_precisions[str(dtype)], parent=view)
    elif dtype == object:
        delegate = TextDelegate(parent=view)
    else:
        delegate = None

    # get old delegate
    oldDelegate = view.itemDelegateForColumn(column)
    if oldDelegate is not None:
        del oldDelegate
    # update the view
    view.setItemDelegateForColumn(column, delegate)
    return delegate

class BigIntSpinboxDelegate(QtWidgets.QItemDelegate):
    """delegate for very big integers.

    Attributes:
        maximum (int or long): minimum allowed number in BigIntSpinbox.
        minimum (int or long): maximum allowed number in BigIntSpinbox.
        singleStep (int): amount of steps to stepUp BigIntSpinbox.

    """

    def __init__(self, minimum=-18446744073709551616, maximum=18446744073709551615, singleStep=1, parent=None):
        """construct a new instance of a BigIntSpinboxDelegate.

        Args:
            maximum (int or long, optional): minimum allowed number in BigIntSpinbox. defaults to -18446744073709551616.
            minimum (int or long, optional): maximum allowed number in BigIntSpinbox. defaults to 18446744073709551615.
            singleStep (int, optional): amount of steps to stepUp BigIntSpinbox. defaults to 1.
        """
        super(BigIntSpinboxDelegate, self).__init__(parent)
        self.minimum = minimum
        self.maximum = maximum
        self.singleStep = singleStep

    def createEditor(self, parent, option, index):
        """Returns the widget used to edit the item specified by index for editing. The parent widget and style option are used to control how the editor widget appears.

        Args:
            parent (QWidget): parent widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        editor = BigIntSpinbox(parent)
        try:
            editor.setMinimum(self.minimum)
            editor.setMaximum(self.maximum)
            editor.setSingleStep(self.singleStep)
        except TypeError as err:
            # initiate the editor with default values
            pass
        return editor

    def setEditorData(self, spinBox, index):
        """Sets the data to be displayed and edited by the editor from the data model item specified by the model index.

        Args:
            spinBox (BigIntSpinbox): editor widget.
            index (QModelIndex): model data index.
        """
        if index.isValid():
            value = index.model().data(index, QtCore.Qt.EditRole)
            spinBox.setValue(value)

    def setModelData(self, spinBox, model, index):
        """Gets data from the editor widget and stores it in the specified model at the item index.

        Args:
            spinBox (BigIntSpinbox): editor widget.
            model (QAbstractItemModel): parent model.
            index (QModelIndex): model data index.
        """
        if index.isValid():
            spinBox.interpretText()
            value = spinBox.value()
            model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, spinBox, option, index):
        """Updates the editor for the item specified by index according to the style option given.

        Args:
            spinBox (BigIntSpinbox): editor widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        spinBox.setGeometry(option.rect)


class CustomDoubleSpinboxDelegate(QtWidgets.QItemDelegate):
    """delegate for floats.

    Attributes:
        maximum (float): minimum allowed number in QDoubleSpinBox.
        minimum (float): maximum allowed number in QDoubleSpinBox.
        singleStep (int): amount of steps to stepUp QDoubleSpinBox
        decimals (int): decimals to use

    """

    def __init__(self, minimum, maximum, decimals=2, singleStep=0.1, parent=None):
        """construct a new instance of a CustomDoubleSpinboxDelegate.

        Args:
            maximum (float): minimum allowed number in QDoubleSpinBox.
            minimum (float): maximum allowed number in QDoubleSpinBox.
            singleStep (int, optional): amount of steps to stepUp QDoubleSpinBox. defaults to 0.1.
            decimals (int, optional): decimals to use.  defaults to 2.

        """
        super(CustomDoubleSpinboxDelegate, self).__init__(parent)

        self.minimum = minimum
        self.maximum = maximum
        self.decimals = decimals
        self.singleStep = singleStep

    def createEditor(self, parent, option, index):
        """Returns the widget used to edit the item specified by index for editing. The parent widget and style option are used to control how the editor widget appears.

        Args:
            parent (QWidget): parent widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        editor = QtGui.QDoubleSpinBox(parent)
        try:
            editor.setMinimum(self.minimum)
            editor.setMaximum(self.maximum)
            editor.setSingleStep(self.singleStep)
            editor.setDecimals(self.decimals)
        except TypeError as err:
            # initiate the spinbox with default values.
            pass
        return editor

    def setEditorData(self, spinBox, index):
        """Sets the data to be displayed and edited by the editor from the data model item specified by the model index.

        Args:
            spinBox (QDoubleSpinBox): editor widget.
            index (QModelIndex): model data index.
        """
        value = index.model().data(index, QtCore.Qt.EditRole)
        spinBox.setValue(value)

    def setModelData(self, spinBox, model, index):
        """Gets data from the editor widget and stores it in the specified model at the item index.

        Args:
            spinBox (QDoubleSpinBox): editor widget.
            model (QAbstractItemModel): parent model.
            index (QModelIndex): model data index.
        """
        spinBox.interpretText()
        value = spinBox.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        """Updates the editor for the item specified by index according to the style option given.

        Args:
            spinBox (QDoubleSpinBox): editor widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        editor.setGeometry(option.rect)

class TextDelegate(QtWidgets.QItemDelegate):
    """delegate for all kind of text."""

    def __init__(self, parent=None):
        """construct a new instance of a BigIntSpinboxDelegate.

        Args:

        """
        super(TextDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        """Returns the widget used to edit the item specified by index for editing. The parent widget and style option are used to control how the editor widget appears.

        Args:
            parent (QWidget): parent widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        editor = QtGui.QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        """Sets the data to be displayed and edited by the editor from the data model item specified by the model index.

        Args:
            editor (QtGui.QLineEdit): editor widget.
            index (QModelIndex): model data index.
        """
        if index.isValid():
            value = index.model().data(index, QtCore.Qt.EditRole)
            editor.setText(str(value))

    def setModelData(self, editor, model, index):
        """Gets data from the editor widget and stores it in the specified model at the item index.

        Args:
            editor (QtGui.QLineEdit): editor widget.
            model (QAbstractItemModel): parent model.
            index (QModelIndex): model data index.
        """
        if index.isValid():
            value = editor.text()
            model.setData(index, value, QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        """Updates the editor for the item specified by index according to the style option given.

        Args:
            editor (QtGui.QLineEdit): editor widget.
            option (QStyleOptionViewItem): controls how editor widget appears.
            index (QModelIndex): model data index.
        """
        editor.setGeometry(option.rect)

class DtypeComboDelegate(QtWidgets.QStyledItemDelegate):
    """Combobox to set dtypes in a ColumnDtypeModel.

    Parent has to be a QTableView with a set model of type ColumnDtypeModel.

    """
    def __init__(self, parent=None):
        """Constructs a `DtypeComboDelegate` object with the given `parent`.

        Args:
            parent (Qtcore.QObject, optional): The parent argument causes this
                objected to be owned by Qt instead of PyQt if. Defaults to `None`.

        """
        super(DtypeComboDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        """Creates an Editor Widget for the given index.

        Enables the user to manipulate the displayed data in place. An editor
        is created, which performs the change.
        The widget used will be a `QComboBox` with all available datatypes in the
        `pandas` project.

        Args:
            parent (QtCore.QWidget): Defines the parent for the created editor.
            option (QtGui.QStyleOptionViewItem): contains all the information
                that QStyle functions need to draw the items.
            index (QtCore.QModelIndex): The item/index which shall be edited.

        Returns:
            QtGui.QWidget: he widget used to edit the item specified by index
                for editing.

        """
        combo = QtGui.QComboBox(parent)
        combo.addItems(SupportedDtypes.names())
        combo.currentIndexChanged.connect(self.currentIndexChanged)
        return combo

    def setEditorData(self, editor, index):
        """Sets the current data for the editor.

        The data displayed has the same value as `index.data(Qt.EditRole)`
        (the translated name of the datatype). Therefor a lookup for all items
        of the combobox is made and the matching item is set as the currently
        displayed item.

        Signals emitted by the editor are blocked during exection of this method.

        Args:
            editor (QtGui.QComboBox): The current editor for the item. Should be
                a `QtGui.QComboBox` as defined in `createEditor`.
            index (QtCore.QModelIndex): The index of the current item.

        """
        editor.blockSignals(True)
        data = index.data()
        dataIndex = editor.findData(data, role=Qt.EditRole)
        editor.setCurrentIndex(dataIndex)
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        """Updates the model after changing data in the editor.

        Args:
            editor (QtGui.QComboBox): The current editor for the item. Should be
                a `QtGui.QComboBox` as defined in `createEditor`.
            model (ColumnDtypeModel): The model which holds the displayed data.
            index (QtCore.QModelIndex): The index of the current item of the model.

        """
        model.setData(index, editor.itemText(editor.currentIndex()))

    @Slot()
    def currentIndexChanged(self):
        """Emits a signal after changing the selection for a `QComboBox`.

        """
        self.commitData.emit(self.sender())


