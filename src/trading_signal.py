import numpy as np
import pandas as pd

def generate_signals(df_rank: pd.DataFrame, tickers, threshold=22):
    """
    Step 3 - 生成交易信号
    """
    df_signal = df_rank.copy()
    for ticker in tickers:
        # 排名靠前的做空 ( -1 )，排名靠后的做多 ( +1 )
        df_signal[ticker] = np.where(df_signal[ticker] < threshold, -1, 1)
    return df_signal

def calculate_strategy_returns(df_signal: pd.DataFrame, daily_stock_returns: pd.DataFrame, tickers):
    # 计算根据信号带来的下一日收益
    returns = df_signal.mul(daily_stock_returns.shift(-1), axis=0)
    # 对所有股票的收益做平均
    strategy_returns = np.sum(returns, axis=1) / len(tickers)
    return strategy_returns, returns
