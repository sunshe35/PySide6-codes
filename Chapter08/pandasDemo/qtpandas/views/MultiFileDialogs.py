import os
from qtpandas.compat import QtCore
from qtpandas.views.CSVDialogs import (CSVExportDialog, CSVImportDialog,
                                       _calculateEncodingKey, Slot,
                                       DataFrameModel)



class DataFrameExportDialog(CSVExportDialog):
    """
    Extends the CSVExportDialog with support for
    exporting to .txt and .xlsx
    """
    signalExportFilenames = QtCore.Signal(str, str)
    signalModelChanged = QtCore.Signal(DataFrameModel)

    def __init__(self, model=None, parent=None):
        CSVExportDialog.__init__(self, model=None, parent=None)
        if model is not None:
            self._filename = model.filePath
        else:
            self._filename = None
        self._windowTitle = "Export Data"
        self.setWindowTitle(self._windowTitle)

    @Slot(DataFrameModel)
    def swapModel(self, model):
        good = self.setExportModel(model)
        if good:
            self.signalModelChanged.emit(model)

    @Slot()
    def accepted(self):
        """Successfully close the widget and emit an export signal.

        This method is also a `SLOT`.
        The dialog will be closed, when the `Export Data` button is
        pressed. If errors occur during the export, the status bar
        will show the error message and the dialog will not be closed.

        """
        #return super(DataFrameExportDialog, self).accepted
        try:
            self._saveModel()
        except Exception as err:
            self._statusBar.showMessage(str(err))
            raise
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

    def _saveModel(self):
        """
        Reimplements _saveModel to utilize all of the
        Pandas export options based on file extension.
        :return: None
        """
        delimiter = self._delimiterBox.currentSelected()
        header = self._headerCheckBox.isChecked() # column labels
        if self._filename is None:
            filename = self._filenameLineEdit.text()
        else:
            filename = self._filename
        ext = os.path.splitext(filename)[1].lower()
        index = False # row labels

        encodingIndex = self._encodingComboBox.currentIndex()
        encoding = self._encodingComboBox.itemText(encodingIndex)
        encoding = _calculateEncodingKey(encoding.lower())

        try:
            dataFrame = self._model.dataFrame()
        except AttributeError as err:
            raise AttributeError('No data loaded to export.')
        else:
            print("Identifying export type for {}".format(filename))
            try:
                if ext in ['.txt','.csv']:
                    dataFrame.to_csv(filename, encoding=encoding, header=header, index=index, sep=delimiter)
                elif ext == '.tsv':
                    sep = '\t'
                    dataFrame.to_csv(filename, encoding=encoding, header=header, index=index, sep=delimiter)
                elif ext in ['.xlsx','.xls']:
                    dataFrame.to_excel(filename, encoding=encoding, header=header, index=index, sep=delimiter)
            except IOError as err:
                raise IOError('No filename given')
            except UnicodeError as err:
                raise UnicodeError('Could not encode all data. Choose a different encoding')
            except Exception:
                raise
            self.signalExportFilenames.emit(self._model._filePath, filename)
