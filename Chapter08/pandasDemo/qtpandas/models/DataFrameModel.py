# -*- coding: utf-8 -*-
"""
Easy integration of DataFrame into pyqt framework

@author: Jev Kuznetsov, Matthias Ludwig - Datalyze Solutions
"""

from datetime import datetime
from qtpandas.utils import superReadFile
from qtpandas.compat import Qt, QtCore, QtGui, Slot, Signal

import pandas
import numpy

#import parser
import re

from qtpandas.models.ColumnDtypeModel import ColumnDtypeModel
from qtpandas.models.DataSearch import DataSearch
from qtpandas.models.SupportedDtypes import SupportedDtypes

DATAFRAME_ROLE = Qt.UserRole + 2


def read_file(filepath, **kwargs):
    """
    Read a data file into a DataFrameModel.

    :param filepath: The rows/columns filepath to read.
    :param kwargs:
            xls/x files - see pandas.read_excel(**kwargs)
            .csv/.txt/etc - see pandas.read_csv(**kwargs)
    :return: DataFrameModel
    """
    return DataFrameModel(dataFrame=superReadFile(filepath, **kwargs),
                          filePath=filepath)


def read_sql(sql, con, filePath, index_col=None, coerce_float=True,
             params=None, parse_dates=None, columns=None, chunksize=None):
    """
    Read SQL query or database table into a DataFrameModel.
    Provide a filePath argument in addition to the *args/**kwargs from
    pandas.read_sql and get a DataFrameModel.

    NOTE: The chunksize option is overridden to None always (for now).

    Reference:
    http://pandas.pydata.org/pandas-docs/version/0.18.1/generated/pandas.read_sql.html
    pandas.read_sql(sql, con, index_col=None, coerce_float=True,
                    params=None, parse_dates=None, columns=None, chunksize=None)



    :return: DataFrameModel
    """

    # TODO: Decide if chunksize is worth keeping and how to handle?
    df = pandas.read_sql(sql, con, index_col, coerce_float,
                    params, parse_dates, columns, chunksize=None)
    return DataFrameModel(df, filePath=filePath)





class DataFrameModel(QtCore.QAbstractTableModel):
    """data model for use in QTableView, QListView, QComboBox, etc.

    Attributes:
        timestampFormat (unicode): formatting string for conversion of timestamps to QtCore.QDateTime.
            Used in data method.
        sortingAboutToStart (QtCore.pyqtSignal): emitted directly before sorting starts.
        sortingFinished (QtCore.pyqtSignal): emitted, when sorting finished.
        dtypeChanged (Signal(columnName)): passed from related ColumnDtypeModel
            if a columns dtype has changed.
        changingDtypeFailed (Signal(columnName, index, dtype)):
            passed from related ColumnDtypeModel.
            emitted after a column has changed it's data type.
        dataChanged (Signal):
            Emitted, if data has changed, e.x. finished loading, new columns added or removed.
            It's not the same as layoutChanged.
            Usefull to reset delegates in the view.
    """

    _float_precisions = {
        "float16": numpy.finfo(numpy.float16).precision - 2,
        "float32": numpy.finfo(numpy.float32).precision - 1,
        "float64": numpy.finfo(numpy.float64).precision - 1
    }

    """list of int datatypes for easy checking in data() and setData()"""
    _intDtypes = SupportedDtypes.intTypes() + SupportedDtypes.uintTypes()
    """list of float datatypes for easy checking in data() and setData()"""
    _floatDtypes = SupportedDtypes.floatTypes()
    """list of bool datatypes for easy checking in data() and setData()"""
    _boolDtypes = SupportedDtypes.boolTypes()
    """list of datetime datatypes for easy checking in data() and setData()"""
    _dateDtypes = SupportedDtypes.datetimeTypes()

    _timestampFormat = Qt.ISODate

    sortingAboutToStart = Signal()
    sortingFinished = Signal()
    dtypeChanged = Signal(int, object)
    changingDtypeFailed = Signal(object, QtCore.QModelIndex, object)
    dataChanged2 = Signal()
    dataFrameChanged = Signal()

    def __init__(self, dataFrame=None, copyDataFrame=False, filePath=None):
        """

        Args:
            dataFrame (pandas.core.frame.DataFrame, optional): initializes the model with given DataFrame.
                If none is given an empty DataFrame will be set. defaults to None.
            copyDataFrame (bool, optional): create a copy of dataFrame or use it as is. defaults to False.
                If you use it as is, you can change it from outside otherwise you have to reset the dataFrame
                after external changes.
            filePath (str, optional): stores the original path for tracking.

        """
        super(DataFrameModel, self).__init__()

        self._dataFrame = pandas.DataFrame()

        if dataFrame is not None:
            self.setDataFrame(dataFrame, copyDataFrame=copyDataFrame)

        self.dataChanged2.emit()

        self._dataFrameOriginal = None
        self._search = DataSearch("nothing", "")
        self.editable = False
        self._filePath = filePath

    @property
    def filePath(self):
        """
        Access to the internal _filepath property (could be None)
        :return: qtpandas.models.DataFrameModel._filepath
        """
        return self._filePath

    def dataFrame(self):
        """
        getter function to _dataFrame. Holds all data.

        Note:
            It's not implemented with python properties to keep Qt conventions.
            Not sure why??
        """
        return self._dataFrame

    def setDataFrameFromFile(self, filepath, **kwargs):
        """
        Sets the model's dataFrame by reading a file.
        Accepted file formats:
            - .xlsx (sheet1 is read unless specified in kwargs)
            - .csv (comma separated unless specified in kwargs)
            - .txt (any separator)

        :param filepath: (str)
            The path to the file to be read.
        :param kwargs:
            pandas.read_csv(**kwargs) or pandas.read_excel(**kwargs)
        :return: None
        """
        df = superReadFile(filepath, **kwargs)
        self.setDataFrame(df, filePath=filepath)

    def setDataFrame(self, dataFrame, copyDataFrame=False, filePath=None):
        """
        Setter function to _dataFrame. Holds all data.

        Note:
            It's not implemented with python properties to keep Qt conventions.

        Raises:
            TypeError: if dataFrame is not of type pandas.core.frame.DataFrame.

        Args:
            dataFrame (pandas.core.frame.DataFrame): assign dataFrame to _dataFrame. Holds all the data displayed.
            copyDataFrame (bool, optional): create a copy of dataFrame or use it as is. defaults to False.
                If you use it as is, you can change it from outside otherwise you have to reset the dataFrame
                after external changes.

        """
        if not isinstance(dataFrame, pandas.core.frame.DataFrame):
            raise TypeError("not of type pandas.core.frame.DataFrame")

        self.layoutAboutToBeChanged.emit()
        if copyDataFrame:
            self._dataFrame = dataFrame.copy()
        else:
            self._dataFrame = dataFrame

        self._columnDtypeModel = ColumnDtypeModel(dataFrame)
        self._columnDtypeModel.dtypeChanged.connect(self.propagateDtypeChanges)
        self._columnDtypeModel.changeFailed.connect(
            lambda columnName, index, dtype: self.changingDtypeFailed.emit(columnName, index, dtype)
        )
        if filePath is not None:
            self._filePath = filePath
        self.layoutChanged.emit()
        self.dataChanged2.emit()
        self.dataFrameChanged.emit()

    @Slot(int, object)
    def propagateDtypeChanges(self, column, dtype):
        """
        Emits a dtypeChanged signal with the column and dtype.

        :param column: (str)
        :param dtype: ??
        :return: None
        """
        self.dtypeChanged.emit(column, dtype)

    @property
    def timestampFormat(self):
        """getter to _timestampFormat"""
        return self._timestampFormat

    @timestampFormat.setter
    def timestampFormat(self, timestampFormat):
        """
        Setter to _timestampFormat. Formatting string for conversion of timestamps to QtCore.QDateTime

        Raises:
            AssertionError: if timestampFormat is not of type unicode.

        Args:
            timestampFormat (unicode): assign timestampFormat to _timestampFormat.
                Formatting string for conversion of timestamps to QtCore.QDateTime. Used in data method.

        """
        if not isinstance(timestampFormat, str):
            raise TypeError('not of type unicode')
        #assert isinstance(timestampFormat, unicode) or timestampFormat.__class__.__name__ == "DateFormat", "not of type unicode"
        self._timestampFormat = timestampFormat

    def rename(self, index=None, columns=None, **kwargs):
        """
        Renames the dataframe inplace calling appropriate signals.
        Wraps pandas.DataFrame.rename(*args, **kwargs) - overrides
        the inplace kwarg setting it to True.

        Example use:
        renames = {'colname1':'COLNAME_1', 'colname2':'COL2'}
        DataFrameModel.rename(columns=renames)

        :param args:
            see pandas.DataFrame.rename
        :param kwargs:
            see pandas.DataFrame.rename
        :return:
            None
        """
        kwargs['inplace'] = True
        self.layoutAboutToBeChanged.emit()
        self._dataFrame.rename(index, columns, **kwargs)
        self.layoutChanged.emit()
        self.dataChanged2.emit()
        self.dataFrameChanged.emit()

    def applyFunction(self, func):
        """
        Applies a function to the dataFrame with appropriate signals.
        The function must return a dataframe.
        :param func: A function (or partial function) that accepts a dataframe as the first argument.
        :return: None
        :raise:
            AssertionError if the func is not callable.
            AssertionError if the func does not return a DataFrame.
        """
        assert callable(func), "function {} is not callable".format(func)
        self.layoutAboutToBeChanged.emit()
        df = func(self._dataFrame)
        assert isinstance(df, pandas.DataFrame), "function {} did not return a DataFrame.".format(func.__name__)
        self._dataFrame = df
        self.layoutChanged.emit()
        self.dataChanged2.emit()
        self.dataFrameChanged.emit()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """
        Return the header depending on section, orientation and Qt::ItemDataRole

        Args:
            section (int): For horizontal headers, the section number corresponds to the column number.
                Similarly, for vertical headers, the section number corresponds to the row number.
            orientation (Qt::Orientations):
            role (Qt::ItemDataRole):

        Returns:
            None if not Qt.DisplayRole
            _dataFrame.columns.tolist()[section] if orientation == Qt.Horizontal
            section if orientation == Qt.Vertical
            None if horizontal orientation and section raises IndexError
        """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            try:
                label = self._dataFrame.columns.tolist()[section]
                if label == section:
                    label = section
                return label
            except (IndexError, ):
                return None
        elif orientation == Qt.Vertical:
            return section

    def data(self, index, role=Qt.DisplayRole):
        """return data depending on index, Qt::ItemDataRole and data type of the column.

        Args:
            index (QtCore.QModelIndex): Index to define column and row you want to return
            role (Qt::ItemDataRole): Define which data you want to return.

        Returns:
            None if index is invalid
            None if role is none of: DisplayRole, EditRole, CheckStateRole, DATAFRAME_ROLE

            if role DisplayRole:
                unmodified _dataFrame value if column dtype is object (string or unicode).
                _dataFrame value as int or long if column dtype is in _intDtypes.
                _dataFrame value as float if column dtype is in _floatDtypes. Rounds to defined precision (look at: _float16_precision, _float32_precision).
                None if column dtype is in _boolDtypes.
                QDateTime if column dtype is numpy.timestamp64[ns]. Uses timestampFormat as conversion template.

            if role EditRole:
                unmodified _dataFrame value if column dtype is object (string or unicode).
                _dataFrame value as int or long if column dtype is in _intDtypes.
                _dataFrame value as float if column dtype is in _floatDtypes. Rounds to defined precision (look at: _float16_precision, _float32_precision).
                _dataFrame value as bool if column dtype is in _boolDtypes.
                QDateTime if column dtype is numpy.timestamp64[ns]. Uses timestampFormat as conversion template.

            if role CheckStateRole:
                Qt.Checked or Qt.Unchecked if dtype is numpy.bool_ otherwise None for all other dtypes.

            if role DATAFRAME_ROLE:
                unmodified _dataFrame value.

            raises TypeError if an unhandled dtype is found in column.
        """

        if not index.isValid():
            return None

        def convertValue(row, col, columnDtype):
            value = None
            if columnDtype == object:
                value = self._dataFrame.loc[row, col]
            elif columnDtype in self._floatDtypes:
                value = round(float(self._dataFrame.loc[row, col]), self._float_precisions[str(columnDtype)])
            elif columnDtype in self._intDtypes:
                value = int(self._dataFrame.loc[row, col])
            elif columnDtype in self._boolDtypes:
                # TODO this will most likely always be true
                # See: http://stackoverflow.com/a/715455
                # well no: I am mistaken here, the data is already in the dataframe
                # so its already converted to a bool
                value = bool(self._dataFrame.loc[row, col])

            elif columnDtype in self._dateDtypes:
                #print numpy.datetime64(self._dataFrame.loc[row, col])
                value = pandas.Timestamp(self._dataFrame.loc[row, col])
                value = QtCore.QDateTime.fromString(str(value), self.timestampFormat)
                #print value
            # else:
            #     raise TypeError, "returning unhandled data type"
            return value

        row = self._dataFrame.index[index.row()]
        col = self._dataFrame.columns[index.column()]
        columnDtype = self._dataFrame[col].dtype

        if role == Qt.DisplayRole:
            # return the value if you wanne show True/False as text
            if columnDtype == numpy.bool:
                result = self._dataFrame.loc[row, col]
            else:
                result = convertValue(row, col, columnDtype)
        elif role  == Qt.EditRole:
            result = convertValue(row, col, columnDtype)
        elif role  == Qt.CheckStateRole:
            if columnDtype == numpy.bool_:
                if convertValue(row, col, columnDtype):
                    result = Qt.Checked
                else:
                    result = Qt.Unchecked
            else:
                result = None
        elif role == DATAFRAME_ROLE:
            result = self._dataFrame.loc[row, col]
        else:
            result = None
        return result

    def flags(self, index):
        """Returns the item flags for the given index as ored value, e.x.: Qt.ItemIsUserCheckable | Qt.ItemIsEditable

        If a combobox for bool values should pop up ItemIsEditable have to set for bool columns too.

        Args:
            index (QtCore.QModelIndex): Index to define column and row

        Returns:
            if column dtype is not boolean Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
            if column dtype is boolean Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        """
        flags = super(DataFrameModel, self).flags(index)

        if not self.editable:
            return flags

        col = self._dataFrame.columns[index.column()]
        if self._dataFrame[col].dtype == numpy.bool:
            flags |= Qt.ItemIsUserCheckable
        else:
            # if you want to have a combobox for bool columns set this
            flags |= Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role=Qt.DisplayRole):
        """Set the value to the index position depending on Qt::ItemDataRole and data type of the column

        Args:
            index (QtCore.QModelIndex): Index to define column and row.
            value (object): new value.
            role (Qt::ItemDataRole): Use this role to specify what you want to do.

        Raises:
            TypeError: If the value could not be converted to a known datatype.

        Returns:
            True if value is changed. Calls layoutChanged after update.
            False if value is not different from original value.

        """
        if not index.isValid() or not self.editable:
            return False

        if value != index.data(role):

            self.layoutAboutToBeChanged.emit()

            row = self._dataFrame.index[index.row()]
            col = self._dataFrame.columns[index.column()]
            #print 'before change: ', index.data().toUTC(), self._dataFrame.iloc[row][col]
            columnDtype = self._dataFrame[col].dtype

            if columnDtype == object:
                pass

            elif columnDtype in self._intDtypes:
                dtypeInfo = numpy.iinfo(columnDtype)
                if value < dtypeInfo.min:
                    value = dtypeInfo.min
                elif value > dtypeInfo.max:
                    value = dtypeInfo.max

            elif columnDtype in self._floatDtypes:
                value = numpy.float64(value).astype(columnDtype)

            elif columnDtype in self._boolDtypes:
                value = numpy.bool_(value)

            elif columnDtype in self._dateDtypes:
                # convert the given value to a compatible datetime object.
                # if the conversation could not be done, keep the original
                # value.
                if isinstance(value, QtCore.QDateTime):
                    value = value.toString(self.timestampFormat)
                try:
                    value = pandas.Timestamp(value)
                except Exception:
                    raise Exception("Can't convert '{0}' into a datetime".format(value))
                    return False
            else:
                raise TypeError("try to set unhandled data type")

            # self._dataFrame.set_value(row, col, value)
            self._dataFrame.loc[row, col] = value

            #print 'after change: ', value, self._dataFrame.iloc[row][col]
            self.layoutChanged.emit()
            return True
        else:
            return False


    def rowCount(self, index=QtCore.QModelIndex()):
        """returns number of rows

        Args:
            index (QtCore.QModelIndex, optional): Index to define column and row. defaults to empty QModelIndex

        Returns:
            number of rows
        """
        # len(df.index) is faster, so use it:
        # In [12]: %timeit df.shape[0]
        # 1000000 loops, best of 3: 437 ns per loop
        # In [13]: %timeit len(df.index)
        # 10000000 loops, best of 3: 110 ns per loop
        # %timeit df.__len__()
        # 1000000 loops, best of 3: 215 ns per loop
        return len(self._dataFrame.index)

    def columnCount(self, index=QtCore.QModelIndex()):
        """returns number of columns

        Args:
            index (QtCore.QModelIndex, optional): Index to define column and row. defaults to empty QModelIndex

        Returns:
            number of columns
        """
        # speed comparison:
        # In [23]: %timeit len(df.columns)
        # 10000000 loops, best of 3: 108 ns per loop

        # In [24]: %timeit df.shape[1]
        # 1000000 loops, best of 3: 440 ns per loop
        return len(self._dataFrame.columns)

    def sort(self, columnId, order=Qt.AscendingOrder):
        """
        Sorts the model column

        After sorting the data in ascending or descending order, a signal
        `layoutChanged` is emitted.

        :param: columnId (int)
            the index of the column to sort on.
        :param: order (Qt::SortOrder, optional)
            descending(1) or ascending(0). defaults to Qt.AscendingOrder

        """
        self.layoutAboutToBeChanged.emit()
        self.sortingAboutToStart.emit()
        column = self._dataFrame.columns[columnId]
        self._dataFrame.sort(column, ascending=not bool(order), inplace=True)
        self.layoutChanged.emit()
        self.sortingFinished.emit()

    def setFilter(self, search):
        """
        Apply a filter and hide rows.

        The filter must be a `DataSearch` object, which evaluates a python
        expression.
        If there was an error while parsing the expression, the data will remain
        unfiltered.

        Args:
            search(qtpandas.DataSearch): data search object to use.

        Raises:
            TypeError: An error is raised, if the given parameter is not a
                `DataSearch` object.

        """
        if not isinstance(search, DataSearch):
            raise TypeError('The given parameter must an `qtpandas.DataSearch` object')

        self._search = search

        self.layoutAboutToBeChanged.emit()

        if self._dataFrameOriginal is not None:
            self._dataFrame = self._dataFrameOriginal
        self._dataFrameOriginal = self._dataFrame.copy()

        self._search.setDataFrame(self._dataFrame)
        searchIndex, valid = self._search.search()

        if valid:
            self._dataFrame = self._dataFrame[searchIndex]
            self.layoutChanged.emit()
        else:
            self.clearFilter()
            self.layoutChanged.emit()

        self.dataFrameChanged.emit()

    def clearFilter(self):
        """
        Clear all filters.
        """
        if self._dataFrameOriginal is not None:
            self.layoutAboutToBeChanged.emit()
            self._dataFrame = self._dataFrameOriginal
            self._dataFrameOriginal = None
            self.layoutChanged.emit()

    def columnDtypeModel(self):
        """
        Getter for a ColumnDtypeModel.

        :return:
            qtpandas.models.ColumnDtypeModel
        """
        return self._columnDtypeModel


    def enableEditing(self, editable=True):
        """
        Sets the DataFrameModel and columnDtypeModel's
        editable properties.
        :param editable: bool
            defaults to True,
            False disables most editing methods.
        :return:
            None
        """
        self.editable = editable
        self._columnDtypeModel.setEditable(self.editable)

    def dataFrameColumns(self):
        """
        :return: list containing dataframe columns
        """
        return self._dataFrame.columns.tolist()

    def addDataFrameColumn(self, columnName, dtype=str, defaultValue=None):
        """
        Adds a column to the dataframe as long as
        the model's editable property is set to True and the
        dtype is supported.

        :param columnName: str
            name of the column.
        :param dtype: qtpandas.models.SupportedDtypes option
        :param defaultValue: (object)
            to default the column's value to, should be the same as the dtype or None
        :return: (bool)
            True on success, False otherwise.
        """
        if not self.editable or dtype not in SupportedDtypes.allTypes():
            return False

        elements = self.rowCount()
        columnPosition = self.columnCount()

        newColumn = pandas.Series([defaultValue]*elements, index=self._dataFrame.index, dtype=dtype)

        self.beginInsertColumns(QtCore.QModelIndex(), columnPosition - 1, columnPosition - 1)
        try:
            self._dataFrame.insert(columnPosition, columnName, newColumn, allow_duplicates=False)
        except ValueError as e:
            # columnName does already exist
            return False

        self.endInsertColumns()

        self.propagateDtypeChanges(columnPosition, newColumn.dtype)

        return True

    def addDataFrameRows(self, count=1):
        """

        Adds rows to the dataframe.

        :param count: (int)
            The number of rows to add to the dataframe.
        :return: (bool)
            True on success, False on failure.

        """
        # don't allow any gaps in the data rows.
        # and always append at the end

        if not self.editable:
            return False

        position = self.rowCount()

        if count < 1:
            return False

        if len(self.dataFrame().columns) == 0:
            # log an error message or warning
            return False

        # Note: This function emits the rowsAboutToBeInserted() signal which
        # connected views (or proxies) must handle before the data is
        # inserted. Otherwise, the views may end up in an invalid state.
        self.beginInsertRows(QtCore.QModelIndex(), position, position + count - 1)

        defaultValues = []
        for dtype in self._dataFrame.dtypes:
            if dtype.type == numpy.dtype('<M8[ns]'):
                val = pandas.Timestamp('')
            elif dtype.type == numpy.dtype(object):
                val = ''
            else:
                val = dtype.type()
            defaultValues.append(val)

        for i in range(count):
            self._dataFrame.loc[position + i] = defaultValues
        self._dataFrame.reset_index()
        self.endInsertRows()
        return True

    def removeDataFrameColumns(self, columns):
        """
        Removes columns from the dataframe.
        :param columns: [(int, str)]
        :return: (bool)
            True on success, False on failure.
        """
        if not self.editable:
            return False

        if columns:
            deleted = 0
            errored = False
            for (position, name) in columns:
                position = position - deleted
                if position < 0:
                    position = 0
                self.beginRemoveColumns(QtCore.QModelIndex(), position, position)
                try:
                    self._dataFrame.drop(name, axis=1, inplace=True)
                except ValueError as e:
                    errored = True
                    continue
                self.endRemoveColumns()
                deleted += 1
            self.dataChanged2.emit()

            if errored:
                return False
            else:
                return True
        return False

    def removeDataFrameRows(self, rows):
        """
        Removes rows from the dataframe.

        :param rows: (list)
            of row indexes to removes.
        :return: (bool)
            True on success, False on failure.
        """
        if not self.editable:
            return False

        if rows:
            position = min(rows)
            count = len(rows)
            self.beginRemoveRows(QtCore.QModelIndex(), position, position + count - 1)

            removedAny = False
            for idx, line in self._dataFrame.iterrows():
                if idx in rows:
                    removedAny = True
                    self._dataFrame.drop(idx, inplace=True)

            if not removedAny:
                return False

            self._dataFrame.reset_index(inplace=True, drop=True)

            self.endRemoveRows()
            return True
        return False
