import numpy as np
import pandas as pd

def calculate_daily_returns(price_df: pd.DataFrame):
    """
    Step 2 - 计算每日收益率和排名
    """
    # 计算每日收益率
    daily_stock_returns = (price_df - price_df.shift(1)) / price_df.shift(1)
    daily_stock_returns = daily_stock_returns.dropna()

    # 根据前一天的收益率进行降序排名
    df_rank = daily_stock_returns.rank(axis=1, ascending=False, method='min')

    return daily_stock_returns, df_rank
