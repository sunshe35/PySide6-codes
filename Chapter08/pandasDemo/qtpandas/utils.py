from random import randint
from pandas import to_datetime
import pandas as pd
import numpy as np
import os


def fillNoneValues(column):
    """Fill all NaN/NaT values of a column with an empty string

    Args:
        column (pandas.Series): A Series object with all rows.

    Returns:
        column: Series with filled NaN values.
    """
    if column.dtype == object:
        column.fillna('', inplace=True)
    return column


def convertTimestamps(column):
    """Convert a dtype of a given column to a datetime.

    This method tries to do this by brute force.

    Args:
        column (pandas.Series): A Series object with all rows.

    Returns:
        column: Converted to datetime if no errors occured, else the
            original column will be returned.

    """
    tempColumn = column

    try:
        # Try to convert the first row and a random row instead of the complete
        # column, might be faster
        tempValue = np.datetime64(column[0])
        tempValue = np.datetime64(column[randint(0, len(column.index) - 1)])
        tempColumn = column.apply(to_datetime)
    except:
        pass
    return tempColumn


def superReadCSV(filepath, first_codec='UTF_8', usecols=None,
                 low_memory=False, dtype=None, parse_dates=True,
                 sep=',', chunksize=None, verbose=False, **kwargs):

        """
        A wrap to pandas read_csv with mods to accept a dataframe or
        filepath. returns dataframe untouched, reads filepath and returns
        dataframe based on arguments.
        """

        if isinstance(filepath, pd.DataFrame):
            return filepath

        assert isinstance(first_codec, str), "first_codec must be a string"

        codecs = list(set([first_codec] + ['UTF_8', 'ISO-8859-1', 'ASCII',
                                           'UTF_16', 'UTF_32']))
        errors = []
        for c in codecs:
            try:

                return pd.read_csv(filepath,
                                   usecols=usecols,
                                   low_memory=low_memory,
                                   encoding=c,
                                   dtype=dtype,
                                   parse_dates=parse_dates,
                                   sep=sep,
                                   chunksize=chunksize,
                                   **kwargs)

            except (UnicodeDecodeError, UnboundLocalError) as e:
                errors.append(e)
            except Exception as e:
                errors.append(e)
                if 'tokenizing' in str(e):
                    pass
                else:
                    raise
        if verbose:
            [print(e) for e in errors]

        raise UnicodeDecodeError("Tried {} codecs and failed on all: \n CODECS: {} \n FILENAME: {}".format(
                        len(codecs), codecs, os.path.basename(filepath)))


def _count(item, string):
    if len(item) == 1:
        return len(''.join(x for x in string if x == item))
    return len(str(string.split(item)))


def identify_sep(filepath):
    """
    Identifies the separator of data in a filepath.
    It reads the first line of the file and counts supported separators.
    Currently supported separators: ['|', ';', ',','\t',':']
    """
    ext = os.path.splitext(filepath)[1].lower()
    allowed_exts = ['.csv', '.txt', '.tsv']
    assert ext in ['.csv', '.txt'], "Unexpected file extension {}. \
                                    Supported extensions {}\n filename: {}".format(
                                    ext, allowed_exts, os.path.basename(filepath))
    maybe_seps = ['|',
                  ';',
                  ',',
                  '\t',
                  ':']

    with open(filepath,'r') as fp:
        header = fp.__next__()

    count_seps_header = {sep: _count(sep, header) for sep in maybe_seps}
    count_seps_header = {sep: count for sep,
                         count in count_seps_header.items() if count > 0}

    if count_seps_header:
        return max(count_seps_header.__iter__(),
                   key=(lambda key: count_seps_header[key]))
    else:
        raise Exception("Couldn't identify the sep from the header... here's the information:\n HEADER: {}\n SEPS SEARCHED: {}".format(header, maybe_seps))


def superReadText(filepath, **kwargs):
    """
    A wrapper to superReadCSV which wraps pandas.read_csv().
    The benefit of using this function is that it automatically identifies the
    column separator.
    .tsv files are assumed to have a \t (tab) separation
    .csv files are assumed to have a comma separation.
    .txt (or any other type) get the first line of the file opened
    and get tested for various separators as defined in the identify_sep
    function.
    """

    if isinstance(filepath, pd.DataFrame):
        return filepath
    sep = kwargs.get('sep', None)
    ext = os.path.splitext(filepath)[1].lower()

    if sep is None:
        if ext == '.tsv':
            kwargs['sep'] = '\t'

        elif ext == '.csv':
            kwargs['sep'] = ','

        else:
            found_sep = identify_sep(filepath)
            print(found_sep)
            kwargs['sep'] = found_sep

    return superReadCSV(filepath, **kwargs)


def superReadFile(filepath, **kwargs):
    """
    Uses pandas.read_excel (on excel files) and returns a dataframe of the
    first sheet (unless sheet is specified in kwargs)
    Uses superReadText (on .txt,.tsv, or .csv files) and returns a dataframe of
    the data. One function to read almost all types of data files.
    """
    if isinstance(filepath, pd.DataFrame):
        return filepath

    ext = os.path.splitext(filepath)[1].lower()

    if ext in ['.xlsx', '.xls']:
        df = pd.read_excel(filepath, **kwargs)

    elif ext in ['.pkl', '.p', '.pickle', '.pk']:
        df = pd.read_pickle(filepath)

    else:
        # Assume it's a text-like file and try to read it.
        try:
            df = superReadText(filepath, **kwargs)
        except Exception as e:
            # TODO: Make this trace back better? Custom Exception? Raise original?
            raise Exception("Error reading file: {}".format(e))
    return df


def dedupe_cols(frame):
    """
    Need to dedupe columns that have the same name.
    """

    cols = list(frame.columns)
    for i, item in enumerate(frame.columns):
        if item in frame.columns[:i]:
            cols[i] = "toDROP"
    frame.columns = cols
    return frame.drop("toDROP", 1, errors='ignore')


def rename_dupe_cols(cols):
    """
    Takes a list of strings and appends 2,3,4 etc to duplicates. Never
    appends a 0 or 1. Appended #s are not always in order...but if you wrap
    this in a dataframe.to_sql function you're guaranteed to not have dupe
    column name errors importing data to SQL...you'll just have to check
    yourself to see which fields were renamed.
    """
    counts = {}
    positions = {pos: fld for pos, fld in enumerate(cols)}

    for c in cols:
        if c in counts.keys():
            counts[c] += 1
        else:
            counts[c] = 1

    fixed_cols = {}

    for pos, col in positions.items():
        if counts[col] > 1:
            fix_cols = {pos: fld for pos, fld in positions.items() if fld == col}
            keys = [p for p in fix_cols.keys()]
            min_pos = min(keys)
            cnt = 1
            for p, c in fix_cols.items():
                if not p == min_pos:
                    cnt += 1
                    c = c + str(cnt)
                    fixed_cols.update({p: c})

    positions.update(fixed_cols)

    cols = [x for x in positions.values()]

    return cols
