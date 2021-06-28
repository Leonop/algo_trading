#
#Python Module with Class
#for Vectorized Backtesting
#of SMA-based strategies
#
#Python for Alogrithmic Trading

import numpy as np
import pandas as pd
from scipy.optimize import brute

class SMAVectorBacktester(object):
    '''
        Attributes
        ==========
        symbol: str
            RIC symbol with which to work
        SMA1: int
            time window in days for shorter SMA
        SMA2: str
            start date for data retrieval
        end: str
            end date for data retrieval
        Methods
        ==========
        get_data:
            retrieves and prepares the base data set
        set_parameters:
            set one or two new SMA parameters
        run_strategy:
            runs the backtest for the SMA-based strategy
        plot_results:
            plots the backtest for the SMA-based strategy
    '''