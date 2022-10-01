import numpy as np
from qtpandas.compat import QtCore

class SupportedDtypesTranslator(QtCore.QObject):
    """Represents all supported datatypes and the translations (i18n).

    """
    def __init__(self, parent=None):
        """Constructs the object with the given parent.

        Args:
            parent (QtCore.QObject, optional): Causes the objected to be owned
                by `parent` instead of Qt. Defaults to `None`.

        """
        super(SupportedDtypesTranslator, self).__init__(parent)

        # we are not supposed to use str objects (str/ dtype('S'))
        self._strs = [(np.dtype(object), self.tr('text'))]

        self._ints = [(np.dtype(np.int8), self.tr('small integer (8 bit)')),
                      (np.dtype(np.int16), self.tr('small integer (16 bit)')),
                      (np.dtype(np.int32), self.tr('integer (32 bit)')),
                      (np.dtype(np.int64), self.tr('integer (64 bit)'))]

        self._uints = [(np.dtype(np.uint8), self.tr('unsigned small integer (8 bit)')),
                       (np.dtype(np.uint16), self.tr('unsigned small integer (16 bit)')),
                       (np.dtype(np.uint32), self.tr('unsigned integer (32 bit)')),
                       (np.dtype(np.uint64), self.tr('unsigned integer (64 bit)'))]

        self._floats = [(np.dtype(np.float16), self.tr('floating point number (16 bit)')),
                      (np.dtype(np.float32), self.tr('floating point number (32 bit)')),
                      (np.dtype(np.float64), self.tr('floating point number (64 bit)'))]

        self._datetime = [(np.dtype('<M8[ns]'), self.tr('date and time'))]

        self._bools = [(np.dtype(bool), self.tr('true/false value'))]

        self._all = self._strs + self._ints + self._uints + self._floats + self._bools + self._datetime

    def strTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported string datatypes.

        """
        return [dtype for (dtype, _) in self._strs]

    def intTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported interger datatypes.

        """
        return [dtype for (dtype, _) in self._ints]

    def uintTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported unsigned integer datatypes.

        """
        return [dtype for (dtype, _) in self._uints]

    def floatTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported float datatypes.

        """
        return [dtype for (dtype, _) in self._floats]

    def boolTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported boolean datatypes.

        """
        return [dtype for (dtype, _) in self._bools]

    def datetimeTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of supported datetime datatypes.

        """
        return [dtype for (dtype, _) in self._datetime]

    def allTypes(self):
        """Concatenates datatypes into a list.

        Returns:
            list: List of all supported datatypes.

        """
        return [dtype for (dtype, _) in self._all]


    def description(self, value):
        """Fetches the translated description for the given datatype.

        The given value will be converted to a `numpy.dtype` object, matched
        against the supported datatypes and the description will be translated
        into the preferred language. (Usually a settings dialog should be
        available to change the language).

        If the conversion fails or no match can be found, `None` will be returned.

        Args:
            value (type|numpy.dtype): Any object or type.

        Returns:
            str: The translated description of the datatype
            None: If no match could be found or an error occured during convertion.

        """
        # lists, tuples, dicts refer to numpy.object types and
        # return a 'text' description - working as intended or bug?
        try:
            value = np.dtype(value)
        except TypeError as e:
            return None
        for (dtype, string) in self._all:
            if dtype == value:
                return string

        # no match found return given value
        return None

    def dtype(self, value):
        """Gets the datatype for the given `value` (description).

        Args:
            value (str): A text description for any datatype.

        Returns:
            numpy.dtype: The matching datatype for the given text.
            None: If no match can be found, `None` will be returned.

        """
        for (dtype, string) in self._all:
            if string == value:
                return dtype

        return None

    def names(self):
        """Fetches all descriptions for the datatypes.

        Returns:
            list: A list of all datatype descriptions.

        """
        return [string for (_, string) in self._all]

    def tupleAt(self, index):
        """Gets the tuple (datatype, description) at the given position out of all supported types.

        Args:
            index (int): An index to access the list of supported datatypes.

        Returns:
            tuple: A tuple consisting of the (datatype, description) will be
                returned, if the index is valid. If not, an empty tuple is returned.

        """
        try:
            return self._all[index]
        except IndexError as e:
            return ()


SupportedDtypes = SupportedDtypesTranslator()