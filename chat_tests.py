import numpy as np
import collections


def max_drawdown(time_series):
    """
    Calculate the maximum drawdown of a time series.

    Parameters:
    - time_series (list or numpy array): A 1-dimensional array of numbers representing the time series.

    Returns:
    - max_dd (float): The maximum drawdown of the time series.
    """
    cum_max = np.maximum.accumulate(time_series)
    max_dur_dd = max(collections.Counter(cum_max).values())
    drawdown = (cum_max - time_series) / cum_max
    max_dd = np.max(drawdown)
    return max_dd, max_dur_dd


time_series = [10, 8, 20, 11, 1, 6, 21, 12, 4, 11, 16, 2, 23, 21, 22]
max_dd = max_drawdown(time_series)
print("Maximum drawdown:", max_dd)
