import talib
import numpy as np

def execute_strategy(prices):
    if len(prices) < 30:
        return "HOLD"
    prices_array = np.array(prices)
    upper, middle, lower = talib.BBANDS(prices_array, timeperiod=20)
    if prices_array[-1] < lower[-1]:
        return "BUY"
    elif prices_array[-1] > upper[-1]:
        return "SELL"
    else:
        return "HOLD"
