import talib
import numpy as np

def execute_strategy(prices):
    if len(prices) < 30:
        return "HOLD"
    prices_array = np.array(prices)
    rsi = talib.RSI(prices_array, timeperiod=14)[-1]
    macd, macdsignal, _ = talib.MACD(prices_array, fastperiod=12, slowperiod=26, signalperiod=9)
    if rsi < 30 and macd[-1] > macdsignal[-1]:
        return "BUY"
    elif rsi > 70 and macd[-1] < macdsignal[-1]:
        return "SELL"
    else:
        return "HOLD"
