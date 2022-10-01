import re

from qtpandas.compat import *
from qtpandas.models.SupportedDtypes import SupportedDtypes

import numpy
from pandas import Timestamp
# from pandas.tslib import NaTType
import warnings


class DefaultValueValidator(QValidator):
    def __init__(self, parent=None):
        super(DefaultValueValidator, self).__init__(parent)
        self.dtype = None

        self.intPattern = re.compile('[-+]?\d+')
        self.uintPattern = re.compile('\d+')
        self.floatPattern = re.compile('[+-]? *(?:\d+(?:\.\d*)?|\.\d+)')
        self.boolPattern = re.compile('(1|t|0|f){1}$')

    @Slot(numpy.dtype)
    def validateType(self, dtype):
        self.dtype = dtype


    def fixup(self, string):
        pass

    def validate(self, s, pos):
        if not s:
            # s is emtpy
            return (QValidator.Acceptable, s, pos)

        if self.dtype in SupportedDtypes.strTypes():
            return (QValidator.Acceptable, s, pos)

        elif self.dtype in SupportedDtypes.boolTypes():
            match = re.match(self.boolPattern, s)
            if match:
                return (QValidator.Acceptable, s, pos)
            else:
                return (QValidator.Invalid, s, pos)

        elif self.dtype in SupportedDtypes.datetimeTypes():
            try:
                ts = Timestamp(s)
            except ValueError as e:
                return (QValidator.Intermediate, s, pos)
            return (QValidator.Acceptable, s, pos)

        else:
            dtypeInfo = None
            if self.dtype in SupportedDtypes.intTypes():
                match = re.search(self.intPattern, s)
                if match:
                    try:
                        value = int(match.string)
                    except ValueError as e:
                        return (QValidator.Invalid, s, pos)

                    dtypeInfo = numpy.iinfo(self.dtype)

            elif self.dtype in SupportedDtypes.uintTypes():
                match = re.search(self.uintPattern, s)
                if match:
                    try:
                        value = int(match.string)
                    except ValueError as e:
                        return (QValidator.Invalid, s, pos)

                    dtypeInfo = numpy.iinfo(self.dtype)

            elif self.dtype in SupportedDtypes.floatTypes():
                match = re.search(self.floatPattern, s)
                print(match)
                if match:
                    try:
                        value = float(match.string)
                    except ValueError as e:
                        return (QValidator.Invalid, s, pos)

                    dtypeInfo = numpy.finfo(self.dtype)


            if dtypeInfo is not None:
                if value >= dtypeInfo.min and value <= dtypeInfo.max:
                    return (QValidator.Acceptable, s, pos)
                else:
                    return (QValidator.Invalid, s, pos)
            else:
                return (QValidator.Invalid, s, pos)

        return (QValidator.Invalid, s, pos)


class AddAttributesDialog(QDialog):

    accepted2 = Signal(str, object, object)

    def __init__(self, parent=None):
        super(AddAttributesDialog, self).__init__(parent)

        self.initUi()

    def initUi(self):
        self.setModal(True)
        self.resize(303, 168)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setSizePolicy(sizePolicy)

        self.verticalLayout = QVBoxLayout(self)

        self.dialogHeading = QLabel(self.tr('Add a new attribute column'), self)

        self.gridLayout = QGridLayout()

        self.columnNameLineEdit = QLineEdit(self)
        self.columnNameLabel = QLabel(self.tr('Name'), self)
        self.dataTypeComboBox = QComboBox(self)

        self.dataTypeComboBox.addItems(SupportedDtypes.names())

        self.columnTypeLabel = QLabel(self.tr('Type'), self)
        self.defaultValueLineEdit = QLineEdit(self)
        self.lineEditValidator = DefaultValueValidator(self)
        self.defaultValueLineEdit.setValidator(self.lineEditValidator)
        self.defaultValueLabel = QLabel(self.tr('Inital Value(s)'), self)

        self.gridLayout.addWidget(self.columnNameLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.columnNameLineEdit, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.columnTypeLabel, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.dataTypeComboBox, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.defaultValueLabel, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.defaultValueLineEdit, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialogHeading)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.dataTypeComboBox.currentIndexChanged.connect(self.updateValidatorDtype)
        self.updateValidatorDtype(self.dataTypeComboBox.currentIndex())

    def accept(self):
        super(AddAttributesDialog, self).accept()

        newColumn = self.columnNameLineEdit.text()
        dtype = SupportedDtypes.dtype(self.dataTypeComboBox.currentText())

        defaultValue = self.defaultValueLineEdit.text()
        try:
            if dtype in SupportedDtypes.intTypes() + SupportedDtypes.uintTypes():
                defaultValue = int(defaultValue)
            elif dtype in SupportedDtypes.floatTypes():
                defaultValue = float(defaultValue)
            elif dtype in SupportedDtypes.boolTypes():
                defaultValue = defaultValue.lower() in ['t', '1']
            elif dtype in SupportedDtypes.datetimeTypes():
                defaultValue = Timestamp(defaultValue)
                # if isinstance(defaultValue, NaTType):
                #     defaultValue = Timestamp('')
            else:
                defaultValue = dtype.type()
        except ValueError as e:
            defaultValue = dtype.type()

        self.accepted2.emit(newColumn, dtype, defaultValue)

    @Slot(int)
    def updateValidatorDtype(self, index):
        (dtype, name) = SupportedDtypes.tupleAt(index)
        self.defaultValueLineEdit.clear()
        self.lineEditValidator.validateType(dtype)


class RemoveAttributesDialog(QDialog):

    accepted2 = Signal(list)

    def __init__(self, columns, parent=None):
        super(RemoveAttributesDialog, self).__init__(parent)
        self.columns = columns
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.tr('Remove Attributes'))
        self.setModal(True)
        self.resize(366, 274)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)

        self.gridLayout = QGridLayout(self)

        self.dialogHeading = QLabel(self.tr('Select the attribute column(s) which shall be removed'), self)

        self.listView = QListView(self)

        model = QStandardItemModel()
        for column in self.columns:
            item = QStandardItem(column)
            model.appendRow(item)

        self.listView.setModel(model)
        self.listView.setSelectionMode(QListView.MultiSelection)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.dialogHeading, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)



    def accept(self):
        selection = self.listView.selectedIndexes()
        names = []
        for index in selection:
            position = index.row()
            names.append((position, index.data(QtCore.Qt.DisplayRole)))

        super(RemoveAttributesDialog, self).accept()
        self.accepted2.emit(names)
