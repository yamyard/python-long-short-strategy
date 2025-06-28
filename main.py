import numpy as np
import pandas as pd
from src.data_loader import load_data, DEFAULT_TICKERS
from src.returns_calculator import calculate_daily_returns
from src.trading_signal import generate_signals, calculate_strategy_returns
from src.performance_metrics import evaluate_performance
from src.visualization import plot_results

if __name__ == "__main__":
    # Step 1: 获取数据
    tickers = DEFAULT_TICKERS  # 可自定义股票池
    data = load_data(tickers=tickers, start_date="2018-01-01", end_date="2024-03-01")

    # Step 2: 计算每日收益率和排名
    daily_stock_returns, df_rank = calculate_daily_returns(data)

    # Step 3: 生成交易信号和策略收益
    df_signal = generate_signals(df_rank, tickers)
    strategy_returns, returns = calculate_strategy_returns(df_signal, daily_stock_returns, tickers)

    # 输出信号数据示例
    print("信号数据 DataFrame 示例：")
    print(df_signal.head(3))

    # Step 4: 绩效指标
    cumulative_returns, sharpe_ratio, drawdown, max_drawdown = evaluate_performance(strategy_returns)

    # Step 5: 结果可视化
    if cumulative_returns is not None:
        plot_results(strategy_returns, cumulative_returns, drawdown, max_drawdown)
