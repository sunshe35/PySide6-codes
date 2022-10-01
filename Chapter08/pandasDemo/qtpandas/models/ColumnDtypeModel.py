# -*- coding: utf-8 -*-
"""Easy integration of DataFrame into pyqt framework

@author: Matthias Ludwig - Datalyze Solutions
"""

from qtpandas.compat import Qt, QtCore, QtGui, Slot, Signal


import pandas
import numpy as np

from qtpandas.models.SupportedDtypes import SupportedDtypes

DTYPE_ROLE = Qt.UserRole + 1
DTYPE_CHANGE_ROLE = Qt.UserRole + 3

class ColumnDtypeModel(QtCore.QAbstractTableModel):
    """Data model returning datatypes per column

    Attributes:
        dtypeChanged (Signal(columnName)): emitted after a column has changed it's data type.
        changeFailed (Signal('QString')): emitted if a column
            datatype could not be changed. An errormessage is provided.
    """
    dtypeChanged = Signal(int, object)
    changeFailed = Signal('QString', QtCore.QModelIndex, object)

    def __init__(self, dataFrame=None, editable=False):
        """the __init__ method.

        Args:
            dataFrame (pandas.core.frame.DataFrame, optional): initializes the model with given DataFrame.
                If none is given an empty DataFrame will be set. defaults to None.
            editable (bool, optional): apply changes while changing dtype. defaults to True.

        """
        super(ColumnDtypeModel, self).__init__()
        self.headers = ['column', 'data type']

        self._editable = editable

        self._dataFrame = pandas.DataFrame()
        if dataFrame is not None:
            self.setDataFrame(dataFrame)

    def dataFrame(self):
        """getter function to _dataFrame. Holds all data.

        Note:
            It's not implemented with python properties to keep Qt conventions.

        """
        return self._dataFrame

    def setDataFrame(self, dataFrame):
        """setter function to _dataFrame. Holds all data.

        Note:
            It's not implemented with python properties to keep Qt conventions.

        Raises:
            TypeError: if dataFrame is not of type pandas.core.frame.DataFrame.

        Args:
            dataFrame (pandas.core.frame.DataFrame): assign dataFrame to _dataFrame. Holds all the data displayed.

        """
        if not isinstance(dataFrame, pandas.core.frame.DataFrame):
            raise TypeError('Argument is not of type pandas.core.frame.DataFrame')

        self.layoutAboutToBeChanged.emit()
        self._dataFrame = dataFrame
        self.layoutChanged.emit()

    def editable(self):
        """getter to _editable """
        return self._editable

    def setEditable(self, editable):
        """setter to _editable. apply changes while changing dtype.

        Raises:
            TypeError: if editable is not of type bool.

        Args:
            editable (bool): apply changes while changing dtype.

        """
        if not isinstance(editable, bool):
            raise TypeError('Argument is not of type bool')
        self._editable = editable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """defines which labels the view/user shall see.

        Args:
            section (int): the row or column number.
            orientation (Qt.Orienteation): Either horizontal or vertical.
            role (Qt.ItemDataRole, optional): Defaults to `Qt.DisplayRole`.

        Returns
            str if a header for the appropriate section is set and the requesting
                role is fitting, None if not.

        """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            try:
                return self.headers[section]
            except (IndexError, ):
                return None

    def data(self, index, role=Qt.DisplayRole):
        """Retrieve the data stored in the model at the given `index`.

        Args:
            index (QtCore.QModelIndex): The model index, which points at a
                data object.
            role (Qt.ItemDataRole, optional): Defaults to `Qt.DisplayRole`. You
                have to use different roles to retrieve different data for an
                `index`. Accepted roles are `Qt.DisplayRole`, `Qt.EditRole` and
                `DTYPE_ROLE`.

        Returns:
            None if an invalid index is given, the role is not accepted by the
            model or the column is greater than `1`.
            The column name will be returned if the given column number equals `0`
            and the role is either `Qt.DisplayRole` or `Qt.EditRole`.
            The datatype will be returned, if the column number equals `1`. The
            `Qt.DisplayRole` or `Qt.EditRole` return a human readable, translated
            string, whereas the `DTYPE_ROLE` returns the raw data type.

        """

        # an index is invalid, if a row or column does not exist or extends
        # the bounds of self.columnCount() or self.rowCount()
        # therefor a check for col>1 is unnecessary.
        if not index.isValid():
            return None

        col = index.column()

        #row = self._dataFrame.columns[index.column()]
        columnName = self._dataFrame.columns[index.row()]
        columnDtype = self._dataFrame[columnName].dtype

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if col == 0:
                if columnName == index.row():
                    return index.row()
                return columnName
            elif col == 1:
                return SupportedDtypes.description(columnDtype)
        elif role == DTYPE_ROLE:
            if col == 1:
                return columnDtype
            else:
                return None

    def setData(self, index, value, role=DTYPE_CHANGE_ROLE):
        """Updates the datatype of a column.

        The model must be initated with a dataframe already, since valid
        indexes are necessary. The `value` is a translated description of the
        data type. The translations can be found at
        `qtpandas.translation.DTypeTranslator`.

        If a datatype can not be converted, e.g. datetime to integer, a
        `NotImplementedError` will be raised.

        Args:
            index (QtCore.QModelIndex): The index of the column to be changed.
            value (str): The description of the new datatype, e.g.
                `positive kleine ganze Zahl (16 Bit)`.
            role (Qt.ItemDataRole, optional): The role, which accesses and
                changes data. Defaults to `DTYPE_CHANGE_ROLE`.

        Raises:
            NotImplementedError: If an error during conversion occured.

        Returns:
            bool: `True` if the datatype could be changed, `False` if not or if
                the new datatype equals the old one.

        """
        if role != DTYPE_CHANGE_ROLE or not index.isValid():
            return False

        if not self.editable():
            return False

        self.layoutAboutToBeChanged.emit()

        dtype = SupportedDtypes.dtype(value)
        currentDtype = np.dtype(index.data(role=DTYPE_ROLE))

        if dtype is not None:
            if dtype != currentDtype:
                col = index.column()
                #row = self._dataFrame.columns[index.column()]
                columnName = self._dataFrame.columns[index.row()]

                try:
                    if dtype == np.dtype('<M8[ns]'):
                        if currentDtype in SupportedDtypes.boolTypes():
                            raise Exception("Can't convert a boolean value into a datetime value.")
                        self._dataFrame[columnName] = self._dataFrame[columnName].apply(pandas.to_datetime)
                    else:
                        self._dataFrame[columnName] = self._dataFrame[columnName].astype(dtype)
                    self.dtypeChanged.emit(index.row(), dtype)
                    self.layoutChanged.emit()

                    return True
                except Exception as e:
                    message = 'Could not change datatype %s of column %s to datatype %s' % (currentDtype, columnName, dtype)
                    self.changeFailed.emit(message, index, dtype)
                    raise
                    # self._dataFrame[columnName] = self._dataFrame[columnName].astype(currentDtype)
                    # self.layoutChanged.emit()
                    # self.dtypeChanged.emit(columnName)
                    #raise NotImplementedError, "dtype changing not fully working, original error:\n{}".format(e)
        return False


    def flags(self, index):
        """Returns the item flags for the given index as ored value, e.x.: Qt.ItemIsUserCheckable | Qt.ItemIsEditable

        Args:
            index (QtCore.QModelIndex): Index to define column and row

        Returns:
            for column 'column': Qt.ItemIsSelectable | Qt.ItemIsEnabled
            for column 'data type': Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

        """
        if not index.isValid():
            return Qt.NoItemFlags

        col = index.column()

        flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if col > 0 and self.editable():
            flags = Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

        return flags

    def rowCount(self, index=QtCore.QModelIndex()):
        """returns number of rows

        Args:
            index (QtCore.QModelIndex, optional): Index to define column and row. defaults to empty QModelIndex

        Returns:
            number of rows
        """
        return len(self._dataFrame.columns)

    def columnCount(self, index=QtCore.QModelIndex()):
        """returns number of columns

        Args:
            index (QtCore.QModelIndex, optional): Index to define column and row. defaults to empty QModelIndex

        Returns:
            number of columns
        """
        return len(self.headers)
