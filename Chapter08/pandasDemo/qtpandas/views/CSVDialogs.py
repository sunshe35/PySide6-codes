# -*- coding: utf-8 -*-
import os

from encodings.aliases import aliases as _encodings
import pandas

from qtpandas.compat import Qt, QtCore, QtGui, Slot, Signal
# from qtpandas.encoding import Detector
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.CustomDelegates import DtypeComboDelegate
from qtpandas.views._ui import icons_rc

from qtpandas.utils import fillNoneValues, convertTimestamps, superReadFile

class DelimiterValidator(QtGui.QRegExpValidator):
    """A Custom RegEx Validator.

    The validator checks, if the input has a length of 1.
    The input may contain any non-whitespace-character
    as denoted by the RegEx term `\S`.

    """

    def __init__(self, parent=None):
        """Constructs the object with the given parent.

        Args:
            parent (QObject, optional): Causes the objected to be owned
                by `parent` instead of Qt. Defaults to `None`.

        """
        super(DelimiterValidator, self).__init__(parent)
        re = QtCore.QRegExp('\S{1}')
        self.setRegExp(re)


class DelimiterSelectionWidget(QtGui.QGroupBox):
    """A custom widget with different text delimiter signs.

    A user can choose between 3 predefined and one user defined
    text delimiter characters. Default delimiters include `semicolon`,
    `colon` and `tabulator`. The user defined delimiter may only have
    a length of 1 and may not include any whitespace character.

    Attributes:
        delimiter (QtCore.pyqtSignal): This signal is emitted, whenever a
            delimiter character is selected by the user.
        semicolonRadioButton (QtGui.QRadioButton): A radio button to
            select the `semicolon` character as delimiter.
        commaRadioButton (QtGui.QRadioButton): A radio button to select
            the `comma` character as delimiter.
        tabRadioButton (QtGui.QRadioButton): A radio button to select
            the `tabulator` character as delimiter.
        otherRadioButton (QtGui.QRadioButton): A radio button to select
            the given input text as delimiter.
        otherSeparatorLineEdit (QtGui.QLineEdit): An input line to let the
            user enter one character only, which may be used as delimiter.

    """

    delimiter = Signal('QString')

    def __init__(self, parent=None):
        """Constructs the object with the given parent.

        Args:
            parent (QObject, optional): Causes the objected to be owned
                by `parent` instead of Qt. Defaults to `None`.

        """
        super(DelimiterSelectionWidget, self).__init__(parent)
        self.semicolonRadioButton = None
        self.commaRadioButton = None
        self.tabRadioButton = None
        self.otherRadioButton = None
        self.otherSeparatorLineEdit = None
        self._initUI()


    def _initUI(self):
        """Creates the inital layout with all subwidgets.

        The layout is a `QHBoxLayout`. Each time a radio button is
        selected or unselected, a slot
        `DelimiterSelectionWidget._delimiter` is called.
        Furthermore the `QLineEdit` widget has a custom regex validator
        `DelimiterValidator` enabled.

        """
        #layout = QtGui.QHBoxLayout(self)

        self.semicolonRadioButton = QtGui.QRadioButton('Semicolon')
        self.commaRadioButton = QtGui.QRadioButton('Comma')
        self.tabRadioButton = QtGui.QRadioButton('Tab')
        self.otherRadioButton = QtGui.QRadioButton('Other')
        self.commaRadioButton.setChecked(True)

        self.otherSeparatorLineEdit = QtGui.QLineEdit(self)
        #TODO: Enable this or add BAR radio and option.
        self.otherSeparatorLineEdit.setEnabled(False)

        self.semicolonRadioButton.toggled.connect(self._delimiter)
        self.commaRadioButton.toggled.connect(self._delimiter)
        self.tabRadioButton.toggled.connect(self._delimiter)

        self.otherRadioButton.toggled.connect(self._enableLine)
        self.otherSeparatorLineEdit.textChanged.connect(lambda: self._delimiter(True))
        self.otherSeparatorLineEdit.setValidator(DelimiterValidator(self))

        currentLayout = self.layout()
        # unset and delete the current layout in order to set a new one
        if currentLayout is not None:
            del currentLayout

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.semicolonRadioButton)
        layout.addWidget(self.commaRadioButton)
        layout.addWidget(self.tabRadioButton)
        layout.addWidget(self.otherRadioButton)
        layout.addWidget(self.otherSeparatorLineEdit)
        self.setLayout(layout)

    @Slot('QBool')
    def _enableLine(self, toggled):
        self.otherSeparatorLineEdit.setEnabled(toggled)

    def currentSelected(self):
        """Returns the currently selected delimiter character.

        Returns:
            str: One of `,`, `;`, `\t`, `*other*`.

        """
        if self.commaRadioButton.isChecked():
            return ','
        elif self.semicolonRadioButton.isChecked():
            return ';'
        elif self.tabRadioButton.isChecked():
            return '\t'
        elif self.otherRadioButton.isChecked():
            return self.otherSeparatorLineEdit.text()
        return


    @Slot('QBool')
    def _delimiter(self, checked):
        if checked:
            if self.commaRadioButton.isChecked():
                self.delimiter.emit(',')
            elif self.semicolonRadioButton.isChecked():
                self.delimiter.emit(';')
            elif self.tabRadioButton.isChecked():
                self.delimiter.emit('\t')
            elif self.otherRadioButton.isChecked():
                ret = self.otherSeparatorLineEdit.text()
                if len(ret) > 0:
                    self.delimiter.emit(ret)

    def reset(self):
        """Resets this widget to its initial state.

        """
        self.semicolonRadioButton.setChecked(True)
        self.otherSeparatorLineEdit.setText('')


class CSVImportDialog(QtGui.QDialog):
    """A dialog to import any csv file into a pandas data frame.

    This modal dialog enables the user to enter any path to a csv
    file and parse this file with or without a header and with special
    delimiter characters.

    On a successful load, the data can be previewed and the column data
    types may be edited by the user.

    After all configuration is done, the dataframe and the underlying model
    may be used by the main application.

    Attributes:
        load (QtCore.pyqtSignal): This signal is emitted, whenever the
            dialog is successfully closed, e.g. when the ok button is
            pressed. Returns DataFrameModel and path of chosen csv file.
    """

    load = Signal('QAbstractItemModel', str)

    def __init__(self, parent=None):
        """Constructs the object with the given parent.

        Args:
            parent (QObject, optional): Causes the objected to be owned
                by `parent` instead of Qt. Defaults to `None`.

        """
        super(CSVImportDialog, self).__init__(parent)
        self._modal = True
        self._windowTitle = 'Import CSV'
        self._encodingKey = None
        self._filename = None
        self._delimiter = None
        self._header = None
        # self._detector = Detector()
        self._initUI()

    def _initUI(self):
        """Initiates the user interface with a grid layout and several widgets.

        """
        self.setModal(self._modal)
        self.setWindowTitle(self._windowTitle)

        layout = QtGui.QGridLayout()

        self._filenameLabel = QtGui.QLabel('Choose File', self)
        self._filenameLineEdit = QtGui.QLineEdit(self)
        self._filenameLineEdit.textEdited.connect(self._updateFilename)
        chooseFileButtonIcon = QtGui.QIcon(QtGui.QPixmap(':/icons/document-open.png'))
        self._chooseFileAction = QtGui.QAction(self)
        self._chooseFileAction.setIcon(chooseFileButtonIcon)
        self._chooseFileAction.triggered.connect(self._openFile)

        self._chooseFileButton = QtGui.QToolButton(self)
        self._chooseFileButton.setDefaultAction(self._chooseFileAction)

        layout.addWidget(self._filenameLabel, 0, 0)
        layout.addWidget(self._filenameLineEdit, 0, 1, 1, 2)
        layout.addWidget(self._chooseFileButton, 0, 3)

        self._encodingLabel = QtGui.QLabel('File Encoding', self)

        encoding_names = list([x.upper() for x in sorted(list(set(_encodings.values())))])
        self._encodingComboBox = QtGui.QComboBox(self)
        self._encodingComboBox.addItems(encoding_names)
        self._encodingComboBox.activated.connect(self._updateEncoding)

        layout.addWidget(self._encodingLabel, 1, 0)
        layout.addWidget(self._encodingComboBox, 1, 1, 1, 1)

        self._hasHeaderLabel = QtGui.QLabel('Header Available?', self)
        self._headerCheckBox = QtGui.QCheckBox(self)
        self._headerCheckBox.toggled.connect(self._updateHeader)


        layout.addWidget(self._hasHeaderLabel, 2, 0)
        layout.addWidget(self._headerCheckBox, 2, 1)

        self._delimiterLabel = QtGui.QLabel('Column Delimiter', self)
        self._delimiterBox = DelimiterSelectionWidget(self)
        self._delimiter = self._delimiterBox.currentSelected()
        self._delimiterBox.delimiter.connect(self._updateDelimiter)

        layout.addWidget(self._delimiterLabel, 3, 0)
        layout.addWidget(self._delimiterBox, 3, 1, 1, 3)

        self._tabWidget = QtGui.QTabWidget(self)
        self._previewTableView = QtGui.QTableView(self)
        self._datatypeTableView = QtGui.QTableView(self)
        self._tabWidget.addTab(self._previewTableView, 'Preview')
        self._tabWidget.addTab(self._datatypeTableView, 'Change Column Types')
        layout.addWidget(self._tabWidget, 4, 0, 3, 4)

        self._datatypeTableView.horizontalHeader().setDefaultSectionSize(200)
        self._datatypeTableView.setItemDelegateForColumn(1, DtypeComboDelegate(self._datatypeTableView))


        self._loadButton = QtGui.QPushButton('Load Data', self)
        #self.loadButton.setAutoDefault(False)

        self._cancelButton = QtGui.QPushButton('Cancel', self)
        # self.cancelButton.setDefault(False)
        # self.cancelButton.setAutoDefault(True)

        self._buttonBox = QtGui.QDialogButtonBox(self)
        self._buttonBox.addButton(self._loadButton, QtGui.QDialogButtonBox.AcceptRole)
        self._buttonBox.addButton(self._cancelButton, QtGui.QDialogButtonBox.RejectRole)
        self._buttonBox.accepted.connect(self.accepted)
        self._buttonBox.rejected.connect(self.rejected)
        layout.addWidget(self._buttonBox, 9, 2, 1, 2)
        self._loadButton.setDefault(False)
        self._filenameLineEdit.setFocus()

        self._statusBar = QtGui.QStatusBar(self)
        self._statusBar.setSizeGripEnabled(False)
        self._headerCheckBox.setChecked(True)
        layout.addWidget(self._statusBar, 8, 0, 1, 4)
        self.setLayout(layout)

    @Slot('QString')
    def updateStatusBar(self, message):
        """Updates the status bar widget of this dialog with the given message.

        This method is also a `SLOT()`.
        The message will be shown for only 5 seconds.

        Args:
            message (QString): The new message which will be displayed.

        """
        self._statusBar.showMessage(message, 5000)

    @Slot()
    def _openFile(self):
        """Opens a file dialog and sets a value for the QLineEdit widget.

        This method is also a `SLOT`.

        """

        file_types = "Comma Separated Values (*.csv);;Text files (*.txt);;All Files (*)"
        ret = QtGui.QFileDialog.getOpenFileName(self,
                                                self.tr('open file'),
                                                filter=file_types)

        if isinstance(ret, tuple):
            ret = ret[0] #PySide6 compatibility maybe?

        if ret:
            self._filenameLineEdit.setText(ret)
            self._updateFilename()

    @Slot('QBool')
    def _updateHeader(self, toggled):
        """Changes the internal flag, whether the csv file contains a header or not.

        This method is also a `SLOT`.

        In addition, after toggling the corresponding checkbox, the
        `_previewFile` method will be called.

        Args:
            toggled (boolean): A flag indicating the status of the checkbox.
                The flag will be used to update an internal variable.

        """
        self._header = 0 if toggled else None
        self._previewFile()

    @Slot()
    def _updateFilename(self):
        """Calls several methods after the filename changed.

        This method is also a `SLOT`.
        It checks the encoding of the changed filename and generates a
        preview of the data.

        """
        self._filename = self._filenameLineEdit.text()
        self._guessEncoding(self._filename)
        self._previewFile()

    def _guessEncoding(self, path):
        """Opens a file from the given `path` and checks the file encoding.

        The file must exists on the file system and end with the extension
        `.csv`. The file is read line by line until the encoding could be
        guessed.
        On a successfull identification, the widgets of this dialog will be
        updated.

        Args:
            path (string): Path to a csv file on the file system.

        """
        if os.path.exists(path) and path.lower().endswith('csv'):
            # encoding = self._detector.detect(path)
            encoding = None

            if encoding is not None:
                if encoding.startswith('utf'):
                    encoding = encoding.replace('-', '')
                encoding = encoding.replace('-','_')

                viewValue = _encodings.get(encoding)

                self._encodingKey = encoding

                index = self._encodingComboBox.findText(viewValue.upper())
                self._encodingComboBox.setCurrentIndex(index)

    @Slot('int')
    def _updateEncoding(self, index):
        """Changes the value of the encoding combo box to the value of given index.

        This method is also a `SLOT`.
        After the encoding is changed, the file will be reloaded and previewed.

        Args:
            index (int): An valid index of the combo box.

        """
        encoding = self._encodingComboBox.itemText(index)
        encoding = encoding.lower()

        self._encodingKey = _calculateEncodingKey(encoding)
        self._previewFile()

    @Slot('QString')
    def _updateDelimiter(self, delimiter):
        """Changes the value of the delimiter for the csv file.

        This method is also a `SLOT`.

        Args:
            delimiter (string): The new delimiter.

        """
        self._delimiter = delimiter
        self._previewFile()

    def _previewFile(self):
        """Updates the preview widgets with new models for both tab panes.

        """
        dataFrame = self._loadCSVDataFrame()
        dataFrameModel = DataFrameModel(dataFrame, filePath=self._filename)
        dataFrameModel.enableEditing(True)
        self._previewTableView.setModel(dataFrameModel)
        columnModel = dataFrameModel.columnDtypeModel()
        columnModel.changeFailed.connect(self.updateStatusBar)
        self._datatypeTableView.setModel(columnModel)

    def _loadCSVDataFrame(self):
        """Loads the given csv file with pandas and generate a new dataframe.

        The file will be loaded with the configured encoding, delimiter
        and header.git
        If any execptions will occur, an empty Dataframe is generated
        and a message will appear in the status bar.

        Returns:
            pandas.DataFrame: A dataframe containing all the available
                information of the csv file.

        """
        if self._filename and os.path.exists(self._filename):
            # default fallback if no encoding was found/selected
            encoding = self._encodingKey or 'UTF_8'

            try:
                dataFrame = superReadFile(self._filename,
                    sep=self._delimiter, first_codec=encoding,
                    header=self._header)
                dataFrame = dataFrame.apply(fillNoneValues)
                dataFrame = dataFrame.apply(convertTimestamps)
            except Exception as err:
                self.updateStatusBar(str(err))
                print(err)
                return pandas.DataFrame()
            self.updateStatusBar('Preview generated.')
            return dataFrame
        self.updateStatusBar('File could not be read.')
        return pandas.DataFrame()

    def _resetWidgets(self):
        """Resets all widgets of this dialog to its inital state.

        """
        self._filenameLineEdit.setText('')
        self._encodingComboBox.setCurrentIndex(0)
        self._delimiterBox.reset()
        self._headerCheckBox.setChecked(False)
        self._statusBar.showMessage('')
        self._previewTableView.setModel(None)
        self._datatypeTableView.setModel(None)

    @Slot()
    def accepted(self):
        """Successfully close the widget and return the loaded model.

        This method is also a `SLOT`.
        The dialog will be closed, when the `ok` button is pressed. If
        a `DataFrame` was loaded, it will be emitted by the signal `load`.

        """
        model = self._previewTableView.model()
        if model is not None:
            df = model.dataFrame().copy()
            dfModel = DataFrameModel(df)
            self.load.emit(dfModel, self._filename)
            print(("Emitted model for {}".format(self._filename)))
        self._resetWidgets()
        self.accept()

    @Slot()
    def rejected(self):
        """Close the widget and reset its inital state.

        This method is also a `SLOT`.
        The dialog will be closed and all changes reverted, when the
        `cancel` button is pressed.

        """
        self._resetWidgets()
        self.reject()

class CSVExportDialog(QtGui.QDialog):
    """An widget to serialize a `DataFrameModel` to a `CSV-File`.

    """
    exported = Signal('QBool')

    def __init__(self, model=None, parent=None):
        super(CSVExportDialog, self).__init__(parent)
        self._model = model
        self._modal = True
        self._windowTitle = 'Export to CSV'
        self._idx = -1
        self._initUI()

    def _initUI(self):
        """Initiates the user interface with a grid layout and several widgets.

        """
        self.setModal(self._modal)
        self.setWindowTitle(self._windowTitle)

        layout = QtGui.QGridLayout()

        self._filenameLabel = QtGui.QLabel('Output File', self)
        self._filenameLineEdit = QtGui.QLineEdit(self)
        chooseFileButtonIcon = QtGui.QIcon(QtGui.QPixmap(':/icons/document-save-as.png'))
        self._chooseFileAction = QtGui.QAction(self)
        self._chooseFileAction.setIcon(chooseFileButtonIcon)
        self._chooseFileAction.triggered.connect(self._createFile)

        self._chooseFileButton = QtGui.QToolButton(self)
        self._chooseFileButton.setDefaultAction(self._chooseFileAction)

        layout.addWidget(self._filenameLabel, 0, 0)
        layout.addWidget(self._filenameLineEdit, 0, 1, 1, 2)
        layout.addWidget(self._chooseFileButton, 0, 3)

        self._encodingLabel = QtGui.QLabel('File Encoding', self)


        encoding_names = list(map(lambda x: x.upper(), sorted(list(set(_encodings.values())))))

        self._encodingComboBox = QtGui.QComboBox(self)
        self._encodingComboBox.addItems(encoding_names)
        self._idx = encoding_names.index('UTF_8')
        self._encodingComboBox.setCurrentIndex(self._idx)
        #self._encodingComboBox.activated.connect(self._updateEncoding)

        layout.addWidget(self._encodingLabel, 1, 0)
        layout.addWidget(self._encodingComboBox, 1, 1, 1, 1)

        self._hasHeaderLabel = QtGui.QLabel('Header Available?', self)
        self._headerCheckBox = QtGui.QCheckBox(self)
        #self._headerCheckBox.toggled.connect(self._updateHeader)

        layout.addWidget(self._hasHeaderLabel, 2, 0)
        layout.addWidget(self._headerCheckBox, 2, 1)

        self._delimiterLabel = QtGui.QLabel('Column Delimiter', self)
        self._delimiterBox = DelimiterSelectionWidget(self)

        layout.addWidget(self._delimiterLabel, 3, 0)
        layout.addWidget(self._delimiterBox, 3, 1, 1, 3)

        self._exportButton = QtGui.QPushButton('Export Data', self)
        self._cancelButton = QtGui.QPushButton('Cancel', self)

        self._buttonBox = QtGui.QDialogButtonBox(self)
        self._buttonBox.addButton(self._exportButton, QtGui.QDialogButtonBox.AcceptRole)
        self._buttonBox.addButton(self._cancelButton, QtGui.QDialogButtonBox.RejectRole)

        self._buttonBox.accepted.connect(self.accepted)
        self._buttonBox.rejected.connect(self.rejected)

        layout.addWidget(self._buttonBox, 5, 2, 1, 2)
        self._exportButton.setDefault(False)
        self._filenameLineEdit.setFocus()

        self._statusBar = QtGui.QStatusBar(self)
        self._statusBar.setSizeGripEnabled(False)
        layout.addWidget(self._statusBar, 4, 0, 1, 4)
        self.setLayout(layout)

    def setExportModel(self, model):
        if not isinstance(model, DataFrameModel):
            return False

        self._model = model
        return True

    @Slot()
    def _createFile(self):
        ret = QtGui.QFileDialog.getSaveFileName(self, 'Save File', filter='Comma Separated Value (*.csv)')
        if isinstance(ret, tuple):
            ret = ret[0]
        self._filenameLineEdit.setText(ret)

    def _saveModel(self):
        delimiter = self._delimiterBox.currentSelected()
        header = self._headerCheckBox.isChecked() # column labels
        filename = self._filenameLineEdit.text()
        index = False # row labels

        encodingIndex = self._encodingComboBox.currentIndex()
        encoding = self._encodingComboBox.itemText(encodingIndex)
        encoding = _calculateEncodingKey(encoding.lower())

        try:
            dataFrame = self._model.dataFrame()
        except AttributeError as err:
            raise AttributeError('No data loaded to export.')
        else:
            try:
                dataFrame.to_csv(filename, encoding=encoding, header=header, index=index, sep=delimiter)
            except IOError as err:
                raise IOError('No filename given')
            except UnicodeError as err:
                raise UnicodeError('Could not encode all data. Choose a different encoding')
            except Exception:
                raise

    def _resetWidgets(self):
        """Resets all widgets of this dialog to its inital state.

        """
        self._filenameLineEdit.setText('')
        self._encodingComboBox.setCurrentIndex(self._idx)
        self._delimiterBox.reset()
        self._headerCheckBox.setChecked(False)
        self._statusBar.showMessage('')

    @Slot()
    def accepted(self):
        """Successfully close the widget and emit an export signal.

        This method is also a `SLOT`.
        The dialog will be closed, when the `Export Data` button is
        pressed. If errors occur during the export, the status bar
        will show the error message and the dialog will not be closed.

        """
        try:
            self._saveModel()
        except Exception as err:
            self._statusBar.showMessage(str(err))
        else:
            self._resetWidgets()
            self.exported.emit(True)
            self.accept()

    @Slot()
    def rejected(self):
        """Close the widget and reset its inital state.

        This method is also a `SLOT`.
        The dialog will be closed and all changes reverted, when the
        `cancel` button is pressed.

        """
        self._resetWidgets()
        self.exported.emit(False)
        self.reject()



def _calculateEncodingKey(comparator):
    """Gets the first key of all available encodings where the corresponding
    value matches the comparator.

    Args:
        comparator (string): A view name for an encoding.

    Returns:
        str: A key for a specific encoding used by python.

    """
    encodingName = None
    for k, v in list(_encodings.dockWidget1()):
        if v == comparator:
            encodingName = k
            break
    return encodingName
