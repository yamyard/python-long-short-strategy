import yfinance as yf
import pandas as pd

DEFAULT_TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']

def load_data(
    tickers=None,
    start_date='2018-01-01',
    end_date='2024-03-01',
    verbose=True
):
    if tickers is None:
        tickers = DEFAULT_TICKERS

    df = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=verbose,
        auto_adjust=False,
        group_by='ticker'
    )

    if df.empty:
        if verbose:
            print("下载结果为空，所有ticker均无数据。")
        return pd.DataFrame()

    # 处理单 ticker 和多 ticker 情况
    data = pd.DataFrame()
    if isinstance(df.columns, pd.MultiIndex):
        # 多ticker时
        for ticker in tickers:
            if ticker in df.columns.get_level_values(0):
                try:
                    col = df[ticker]['Adj Close']
                    if not col.isna().all():
                        data[ticker] = col
                except KeyError:
                    continue
    else:
        # 单ticker时
        if 'Adj Close' in df.columns:
            data[tickers[0]] = df['Adj Close']

    # 只保留有实际数据的ticker
    data = data.dropna(axis=1, how='all')
    available = list(data.columns)
    missing = [t for t in tickers if t not in available]
    if verbose:
        print(f"下载成功股票数: {len(available)}")
        if missing:
            print(f"未能获取数据的股票: {missing}")
    return data