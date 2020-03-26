import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def normalize_confusion_matrix(cm_df):
    """
    Normalize the values in a confusion matrix to be between 0 and 1
    :param corr_df: The dataframe of the conusion matrix
    :return: The normalized matrix
    """

    for col in cm_df.columns:
        cm_df[col] = cm_df[col].apply(lambda x: x / cm_df[col].sum())

    return cm_df


def plot_scatter(data_frame, x, y, x_label = '', y_label = ''):

    x_label = x if x_label == '' else x_label
    y_label = y if y_label == '' else y_label

    data_frame = data_frame.dropna()

    standardize_plot_fonts()

    df_plot = pd.DataFrame()
    df_plot[x] = data_frame[x]
    df_plot[y] = data_frame[y]

    plot = df_plot.plot.scatter(x = x, y = y)
    plot.set_xlabel(x_label)
    plot.set_ylabel(y_label)
    plot.set_title(y_label + ' vs. ' + x_label)

    plt.show()

def parse_price(price_string):
    """
    Parses a price of the format '$1,445' and returns a float
    :param price_string: The readable price string
    :return: A float
    """

    return float(price_string.replace('$', '').replace(',', ''))

def pad(ser, result_len, default_val = np.nan):
    """
    Pad a Series with values at the end to make it the length provided. Default padding is NaN
    :param ser: The Series
    :param result_len: The resulting length. This should be more than the current length of the series
    :param default_val: The value to pad with
    :return: The padded Series
    """

    if ser.size > result_len:
        raise ValueError('Result length ' + str(result_len) + ' needs to be more than ' + str(ser.size))

    return ser.reset_index(drop=True).reindex(range(result_len), fill_value=default_val)

def row_count(dataframe):
    """
    Gets the number of rows in a dataframe (most efficient way)
    :param dataframe: The dataframe to get the rows of
    :return: The row count
    """

    return len(dataframe.index)

def parse_calendar_date(calendar_date):
    """
     Parses a date in the format 'YYYY-MM-DD'
     Parameters:
        calendar_date (object): Formatted as 'YYYY-MM-DD'
    """

    # Return the parsed value
    return datetime.strptime(calendar_date, '%Y-%m-%d')

def describe_hist(histogram, title, x_label, y_label):
    """
    Syntactic sugar to label the histogram axes and title
    :param histogram: The histogram
    :param title: The title to set
    :param x_label: The x-axis label to set
    :param y_label: The y-axis label to set
    """

    for ax in histogram.flatten():
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

def standardize_plot_fonts():
    """
    Standardize the title and axis fonts (Defaults to Title: 22, Axes: 15)
    """

    plt.rc('axes', labelsize=15) # Axis Font
    plt.rc('axes', titlesize=22) # Title Font

def whats(thing) :
    """
    Prints the type of object passed in
    Parameters:
        thing (Object): The object for which the type needs to be printed
    """

    print(type(thing))

def is_nan(value):
    """
    Returns true if value is NaN, false otherwise
    Parameters:
         value (Object): An object to test
    """

    return value != value

def read_csv(file_path, verbose=True):
    """
    Reads a csv file and returns the smallest possible dataframe
    :param file_path: The file path
    :param verbose: Whether or not to be verbose about the memory savings
    :return: An optimized dataframe
    """

    return pd.read_csv(file_path).pipe(reduce_mem_usage)

def reduce_mem_usage(df, verbose=True):
    """
    Takes a dataframe and returns one that takes the least memory possible.
    This works by going over each column and representing it with the smallest possible data structure.
    Example usage: my_data = pd.read_csv('D:/SomeFile.csv').pipe(reduce_mem_usage)
    Source: (https://www.kaggle.com/arjanso/reducing-dataframe-memory-size-by-65)
    Parameters:
        df (DataFrame): The dataframe to optimize
        verbose (bool): Whether or not to be verbose about the savings
    """

    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024 ** 2
    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df