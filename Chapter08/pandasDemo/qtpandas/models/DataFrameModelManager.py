# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:57:39 2016

@author: Zeke
"""
import os
import pandas as pd
from qtpandas.models.DataFrameModel import DataFrameModel, read_file
from collections import defaultdict
import datetime
from qtpandas.compat import QtCore


class DataFrameModelManager(QtCore.QObject):
    """
    A central storage unit for managing
    DataFrameModels.
    """
    signalNewModelRead = QtCore.Signal(str)
    signalModelDestroyed = QtCore.Signal(str)

    def __init__(self):
        QtCore.QObject.__init__(self)
        self._models = {}
        self._updates = defaultdict(list)
        self._paths_read = []
        self._paths_updated = []

    @property
    def file_paths(self):
        """Returns a list of the currently stored file paths"""
        return list(self._models.keys())

    @property
    def models(self):
        """Returns a list of all currently stored DataFrameModels"""
        return list(self._models.values())

    @property
    def last_path_read(self):
        """Returns the last path read (via the DataFrameModelManager.read_file method)"""
        if self._paths_read:
            return self._paths_read[-1]
        else:
            return None

    @property
    def last_path_updated(self):
        """Returns the last path to register an update. (or None)"""
        if self._paths_updated:
            return self._paths_updated[-1]
        else:
            return None

    def save_file(self, filepath, save_as=None, keep_orig=False, **kwargs):
        """
        Saves a DataFrameModel to a file.

        :param filepath: (str)
            The filepath of the DataFrameModel to save.
        :param save_as: (str, default None)
            The new filepath to save as.
        :param keep_orig: (bool, default False)
            True keeps the original filepath/DataFrameModel if save_as is specified.
        :param kwargs:
            pandas.DataFrame.to_excel(**kwargs) if .xlsx
            pandas.DataFrame.to_csv(**kwargs) otherwise.
        :return: None
        """
        df = self._models[filepath].dataFrame()
        kwargs['index'] = kwargs.get('index', False)

        if save_as is not None:
            to_path = save_as
        else:
            to_path = filepath

        ext = os.path.splitext(to_path)[1].lower()

        if ext == ".xlsx":
            kwargs.pop('sep', None)
            df.to_excel(to_path, **kwargs)

        elif ext in ['.csv','.txt']:
            df.to_csv(to_path, **kwargs)

        else:
            raise NotImplementedError("Cannot save file of type {}".format(ext))

        if save_as is not None:
            if  keep_orig is False:
                # Re-purpose the original model
                # Todo - capture the DataFrameModelManager._updates too
                model = self._models.pop(filepath)
                model._filePath = to_path
            else:
                # Create a new model.
                model = DataFrameModel()
                model.setDataFrame(df, copyDataFrame=True, filePath=to_path)

            self._models[to_path] = model

    def set_model(self, df_model: DataFrameModel, file_path):
        """
        Sets a DataFrameModel and registers it to the given file_path.
        :param df_model: (DataFrameModel)
            The DataFrameModel to register.
        :param file_path:
            The file path to associate with the DataFrameModel.
            *Overrides the current filePath on the DataFrameModel (if any)
        :return: None
        """
        assert isinstance(df_model, DataFrameModel), "df_model argument must be a DataFrameModel!"
        df_model._filePath = file_path

        try:
            self._models[file_path]
        except KeyError:
            self.signalNewModelRead.emit(file_path)

        self._models[file_path] = df_model

    def get_model(self, filepath):
        """
        Returns the DataFrameModel registered to filepath
        """
        return self._models[filepath]

    def get_frame(self, filepath):
        """Returns the DataFrameModel.dataFrame() registered to filepath """
        return self._models[filepath].dataFrame()

    def update_file(self, filepath, df, notes=None):
        """
        Sets a new DataFrame for the DataFrameModel registered to filepath.
        :param filepath (str)
            The filepath to the DataFrameModel to be updated
        :param df (pandas.DataFrame)
            The new DataFrame to register to the model.

        :param notes (str, default None)
            Optional notes to register along with the update.

        """
        assert isinstance(df, pd.DataFrame), "Cannot update file with type '{}'".format(type(df))

        self._models[filepath].setDataFrame(df, copyDataFrame=False)

        if notes:
            update = dict(date=pd.Timestamp(datetime.datetime.now()),
                                                     notes=notes)

            self._updates[filepath].append(update)
        self._paths_updated.append(filepath)

    def remove_file(self, filepath):
        """
        Removes the DataFrameModel from being registered.
        :param filepath: (str)
            The filepath to delete from the DataFrameModelManager.
        :return: None
        """
        self._models.pop(filepath)
        self._updates.pop(filepath, default=None)
        self.signalModelDestroyed.emit(filepath)

    def read_file(self, filepath, **kwargs) -> DataFrameModel:
        """
        Reads a filepath into a DataFrameModel and registers
        it.
        Example use:
            dfmm = DataFrameModelManger()
            dfmm.read_file(path_to_file)
            dfm = dfmm.get_model(path_to_file)
            df = dfm.get_frame(path_to_file)

        :param filepath: (str)
            The filepath to read
        :param kwargs:
            .xlsx files: pandas.read_excel(**kwargs)
            .csv files: pandas.read_csv(**kwargs)
        :return: DataFrameModel
        """
        try:
            model = self._models[filepath]
        except KeyError:
            model = read_file(filepath, **kwargs)
            self._models[filepath] = model
            self.signalNewModelRead.emit(filepath)
        finally:
            self._paths_read.append(filepath)

        return self._models[filepath]
