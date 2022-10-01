import pickle as pickle
from qtpandas.models.SupportedDtypes import SupportedDtypes
from qtpandas.compat import QtCore

PandasCellMimeType = "application/pandas-cell" # comparable to a QModelIndex for DataFrames

class MimeData(QtCore.QMimeData):
    
    def __init__(self, mimeType=PandasCellMimeType):
        """create a new MimeData object.   
        
        Args:
            mimeType (str): the mime type.
        """
        super(MimeData, self).__init__()
        self._mimeType = mimeType
        
    def mimeType(self):
        """return mimeType
        
        Returns:
            str
        """
        return self._mimeType

    def setData(self, data):
        """Add some data.
        
        Args:
            data (object): Object to add as data. This object has to be pickable. 
                Qt objects don't work!
        
        Raises:
            TypeError if data is not pickable
        """
        try:
            bytestream = pickle.dumps(data)
            super(MimeData, self).setData(self._mimeType, bytestream)
        except TypeError:
            raise TypeError(self.tr("can not pickle added data"))
        except:
            raise
        
    def data(self):
        """return stored data
        
        Returns:
            unpickled data
        """
        try:
            bytestream = super(MimeData, self).data(self._mimeType).data()
            return pickle.loads(bytestream)
        except:
            raise
        
class MimeDataPayload(object):
    
    def __init__(self):
        """base class for your own payload"""
        super(MimeDataPayload, self).__init__()
        
    def isValid(self):
        """Will be checked in the dragEnterEvent to check if our payload can be accepted.
           e.x. data is a filepath its valid if the file exists.
        
        Hint:
            Implement your own validation criterias.
            
        Returns:
            True if valid
            False if invalid
        """
        return False

class PandasCellPayload(MimeDataPayload):
    
    _allowedDtypes = SupportedDtypes.allTypes()

    def __init__(self, dfindex, column, value, dtype, parentId):
        """store dataframe information in a pickable object
        
        Args:
            dfindex (pandas.index): index of the dragged data.
            column (str): name of column to be dragged.
            value (object): value on according position.
            dtype (pandas dtype): data type of column.
            parentId (str): hex(id(...)) of according DataFrameModel.

        """
        super(PandasCellPayload, self).__init__()
        self.dfindex = dfindex
        self.column = column
        self.value = value
        self.dtype = dtype
        self.parentId = parentId
        
    def setAllowedDtypes(self, dtypes):
        """set the allowed dtypes used by the dropped widget to determin if we accept or decline the data.
        Defaults to allTypes.
        
        Args:
            dtypes(SupportedDtypes type): combination of SupportedDtypes types. 
                e.x. SupportedDtypes.intTypes() + SupportedDtypes.floatTypes()
        
        """
        self._allowedDtypes = dtypes

    def allowedDtypes(self):
        """return allowedDtypes"""
        return self._allowedDtypes
    
    def isValid(self):
        """check if the dtype is in allowedDtypes. Used to accept or decline a drop in the view."""
        if self.dtype in self._allowedDtypes:
            return True
        else:
            return False