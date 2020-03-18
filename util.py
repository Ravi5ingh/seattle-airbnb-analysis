import numpy as np
import matplotlib.pyplot as plt

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

def is_nan(value):
    """
    Returns true if value is NaN, false otherwise
    Parameters:
         value (Object): An object to test
    """

    return value != value

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