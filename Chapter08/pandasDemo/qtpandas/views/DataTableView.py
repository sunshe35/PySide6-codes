# -*- coding: utf-8 -*-
from qtpandas.compat import *
from qtpandas.models.DataFrameModel import DataFrameModel
from qtpandas.views.EditDialogs import AddAttributesDialog, RemoveAttributesDialog
from qtpandas.views.CustomDelegates import createDelegate
from qtpandas.models.mime import PandasCellPayload, MimeData
from qtpandas.models.SupportedDtypes import SupportedDtypes

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
class DragTable(QTableView):
    
    def __init__(self, parent=None):
        """create a table view with the ability to start drag operations"""
        super(DragTable, self).__init__(parent)
        self.setDragEnabled(True)

    def startDrag(self, index):
        """start a drag operation with a PandasCellPayload on defined index.
        
        Args:
            index (QModelIndex): model index you want to start the drag operation.
        """

        if not index.isValid():
            return
        
        dataFrame = self.model().dataFrame()

        # get all infos from dataFrame
        dfindex = dataFrame.iloc[[index.row()]].index
        columnName = dataFrame.columns[index.column()]
        dtype = dataFrame[columnName].dtype
        value = dataFrame[columnName][dfindex]

        # create the mime data
        mimePayload = PandasCellPayload(
            dfindex,
            columnName,
            value,
            dtype,
            hex(id(self.model()))
        )
        mimeData = MimeData()
        mimeData.setData(mimePayload)
                
        # create the drag icon and start drag operation
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        pixmap = QPixmap(":/icons/insert-table.png")
        drag.setHotSpot(QtCore.QPoint(pixmap.width()/3, pixmap.height()/3))
        drag.setPixmap(pixmap)
        result = drag.start(Qt.MoveAction)

    def mouseMoveEvent(self, event):
        super(DragTable, self).mouseMoveEvent(event)
        self.startDrag(self.indexAt(event.pos()))

class DataTableWidget(QWidget):
    """A Custom widget with a TableView and a toolbar.

    This widget shall display all `DataFrameModels` and
    enable the editing of this (edit data, adding/removing,
    rows/columns).

    """
    def __init__(self, parent=None, iconSize=QtCore.QSize(36, 36)):
        """Constructs the object with the given parent.

        Args:
            parent (QObject, optional): Causes the objected to be owned
                by `parent` instead of Qt. Defaults to `None`.
            iconSize (QSize, optional): Size of edit buttons. Defaults to QSize(36, 36).

        """
        super(DataTableWidget, self).__init__(parent)
        self._iconSize = iconSize
        self.initUi()


    def initUi(self):
        """Initalizes the Uuser Interface with all sub widgets.

        """
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.buttonFrame = QFrame(self)
        #self.buttonFrame.setMinimumSize(QtCore.QSize(250, 50))
        #self.buttonFrame.setMaximumSize(QtCore.QSize(250, 50))
        self.buttonFrame.setFrameShape(QFrame.NoFrame)
        spacerItemButton = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonFrameLayout = QGridLayout(self.buttonFrame)
        self.buttonFrameLayout.setContentsMargins(0, 0, 0, 0)

        self.editButton = QToolButton(self.buttonFrame)
        self.editButton.setObjectName('editbutton')
        self.editButton.setText(self.tr('edit'))
        self.editButton.setToolTip(self.tr('toggle editing mode'))
        icon = QIcon(QPixmap(_fromUtf8(':/icons/document-edit.png')))

        self.editButton.setIcon(icon)

        self.addColumnButton = QToolButton(self.buttonFrame)
        self.addColumnButton.setObjectName('addcolumnbutton')
        self.addColumnButton.setText(self.tr('+col'))
        self.addColumnButton.setToolTip(self.tr('add new column'))
        icon = QIcon(QPixmap(_fromUtf8(':/icons/edit-table-insert-column-right.png')))

        self.addColumnButton.setIcon(icon)

        self.addRowButton = QToolButton(self.buttonFrame)
        self.addRowButton.setObjectName('addrowbutton')
        self.addRowButton.setText(self.tr('+row'))
        self.addRowButton.setToolTip(self.tr('add new row'))
        icon = QIcon(QPixmap(_fromUtf8(':/icons/edit-table-insert-row-below.png')))

        self.addRowButton.setIcon(icon)

        self.removeColumnButton = QToolButton(self.buttonFrame)
        self.removeColumnButton.setObjectName('removecolumnbutton')
        self.removeColumnButton.setText(self.tr('-col'))
        self.removeColumnButton.setToolTip(self.tr('remove a column'))
        icon = QIcon(QPixmap(_fromUtf8(':/icons/edit-table-delete-column.png')))

        self.removeColumnButton.setIcon(icon)

        self.removeRowButton = QToolButton(self.buttonFrame)
        self.removeRowButton.setObjectName('removerowbutton')
        self.removeRowButton.setText(self.tr('-row'))
        self.removeRowButton.setToolTip(self.tr('remove selected rows'))
        icon = QIcon(QPixmap(_fromUtf8(':/icons/edit-table-delete-row.png')))

        self.removeRowButton.setIcon(icon)

        self.buttons = [self.editButton, self.addColumnButton, self.addRowButton, self.removeColumnButton, self.removeRowButton]

        for index, button in enumerate(self.buttons):
            button.setMinimumSize(self._iconSize)
            button.setMaximumSize(self._iconSize)
            button.setIconSize(self._iconSize)
            button.setCheckable(True)
            self.buttonFrameLayout.addWidget(button, 0, index, 1, 1)
        self.buttonFrameLayout.addItem(spacerItemButton, 0, index+1, 1, 1)

        for button in self.buttons[1:]:
            button.setEnabled(False)

        #self.tableView = QTableView(self)
        self.tableView = DragTable(self)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        
        self.gridLayout.addWidget(self.buttonFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        self.editButton.toggled.connect(self.enableEditing)
        self.addColumnButton.toggled.connect(self.showAddColumnDialog)
        self.addRowButton.toggled.connect(self.addRow)
        self.removeRowButton.toggled.connect(self.removeRow)
        self.removeColumnButton.toggled.connect(self.showRemoveColumnDialog)

    def setButtonsVisible(self, visible):
        """hide/show the edit buttons"""
        self.buttonFrame.setVisible(visible)
        
    @Slot(bool)
    def enableEditing(self, enabled):
        """Enable the editing buttons to add/remove rows/columns and to edit the data.

        This method is also a slot.
        In addition, the data of model will be made editable,
        if the `enabled` parameter is true.

        Args:
            enabled (bool): This flag indicates, if the buttons
                shall be activated.

        """
        for button in self.buttons[1:]:
            button.setEnabled(enabled)
            if button.isChecked():
                button.setChecked(False)

        model = self.tableView.model()

        if model is not None:
            model.enableEditing(enabled)

    @Slot()
    def uncheckButton(self):
        """Removes the checked stated of all buttons in this widget.

        This method is also a slot.

        """
        #for button in self.buttons[1:]:
        for button in self.buttons:
            # supress editButtons toggled event
            button.blockSignals(True)
            if button.isChecked():
                button.setChecked(False)
            button.blockSignals(False)

    @Slot(str, object, object)
    def addColumn(self, columnName, dtype, defaultValue):
        """Adds a column with the given parameters to the underlying model

        This method is also a slot.
        If no model is set, nothing happens.

        Args:
            columnName (str): The name of the new column.
            dtype (numpy.dtype): The datatype of the new column.
            defaultValue (object): Fill the column with this value.

        """
        model = self.tableView.model()

        if model is not None:
            model.addDataFrameColumn(columnName, dtype, defaultValue)

        self.addColumnButton.setChecked(False)

    @Slot(bool)
    def showAddColumnDialog(self, triggered):
        """Display the dialog to add a column to the model.

        This method is also a slot.

        Args:
            triggered (bool): If the corresponding button was
                activated, the dialog will be created and shown.

        """
        if triggered:
            dialog = AddAttributesDialog(self)
            dialog.accepted2.connect(self.addColumn)
            dialog.rejected.connect(self.uncheckButton)
            dialog.show()

    @Slot(bool)
    def addRow(self, triggered):
        """Adds a row to the model.

        This method is also a slot.

        Args:
            triggered (bool): If the corresponding button was
                activated, the row will be appended to the end.

        """
        if triggered:
            model = self.tableView.model()
            model.addDataFrameRows()
            self.sender().setChecked(False)


    @Slot(bool)
    def removeRow(self, triggered):
        """Removes a row to the model.

        This method is also a slot.

        Args:
            triggered (bool): If the corresponding button was
                activated, the selected row will be removed
                from the model.

        """
        if triggered:
            model = self.tableView.model()
            selection = self.tableView.selectedIndexes()

            rows = [index.row() for index in selection]
            model.removeDataFrameRows(set(rows))
            self.sender().setChecked(False)

    @Slot(list)
    def removeColumns(self, columnNames):
        """Removes one or multiple columns from the model.

        This method is also a slot.

        Args:
            columnNames (list): A list of columns, which shall
                be removed from the model.

        """
        model = self.tableView.model()

        if model is not None:
            model.removeDataFrameColumns(columnNames)

        self.removeColumnButton.setChecked(False)

    @Slot(bool)
    def showRemoveColumnDialog(self, triggered):
        """Display the dialog to remove column(s) from the model.

        This method is also a slot.

        Args:
            triggered (bool): If the corresponding button was
                activated, the dialog will be created and shown.

        """
        if triggered:
            model = self.tableView.model()
            if model is not None:
                columns = model.dataFrameColumns()
                dialog = RemoveAttributesDialog(columns, self)
                dialog.accepted2.connect(self.removeColumns)
                dialog.rejected.connect(self.uncheckButton)
                dialog.show()

    def setViewModel(self, model):
        """Sets the model for the enclosed TableView in this widget.

        Args:
            model (DataFrameModel): The model to be displayed by
                the Table View.

        """
        if isinstance(model, DataFrameModel):
            self.enableEditing(False)
            self.uncheckButton()
            
            selectionModel = self.tableView.selectionModel()
            self.tableView.setModel(model)
            model.dtypeChanged.connect(self.updateDelegate)
            model.dataChanged.connect(self.updateDelegates)
            del selectionModel
            
    def setModel(self, model):
        """Sets the model for the enclosed TableView in this widget.

        Args:
            model (DataFrameModel): The model to be displayed by
                the Table View.

        """
        self.setViewModel(model)

    def model(self):
        """Gets the viewModel"""
        return self.view().model()

    def viewModel(self):
        """Gets the viewModel"""
        return self.view().model()

    def view(self):
        """Gets the enclosed TableView

        Returns:
            QTableView: A Qt TableView object.

        """
        return self.tableView

    def updateDelegate(self, column, dtype):
        """update the delegates for a specific column
        
        Args:
            column (int): column index.
            dtype (str): data type of column.
        
        """
        # as documented in the setDelegatesFromDtype function
        # we need to store all delegates, so going from
        # type A -> type B -> type A
        # would cause a segfault if not stored.
        createDelegate(dtype, column, self.tableView)

    def updateDelegates(self):
        """reset all delegates"""
        for index, column in enumerate(self.tableView.model().dataFrame().columns):
            dtype = self.tableView.model().dataFrame()[column].dtype
            self.updateDelegate(index, dtype)
            
    def selectionModel(self):
        """return the table views selectionModel"""
        return self.view().selectionModel()