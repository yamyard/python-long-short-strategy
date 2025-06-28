import os
import json
import numpy as np
import pandas as pd
from src.fetcher import load_data
from src.returns import calculate_daily_returns
from src.signals import generate_signals, calculate_strategy_returns
from src.metrics import evaluate_performance
from src.plotter import plot_results

# 可自定义股票池
def load_config_tickers(config_path="config.json"):
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            try:
                config = json.load(f)
                tickers = config.get("tickers")
                if isinstance(tickers, list) and tickers:
                    return tickers
            except Exception as e:
                print(f"读取 config.json 出错：{e}")
    return DEFAULT_TICKERS

if __name__ == "__main__":
    # Step 1: 获取数据
    tickers = load_config_tickers("config.json")
    data = load_data(tickers=tickers, start_date="2018-01-01", end_date="2024-03-01")

    # Step 2: 计算每日收益率和排名
    daily_stock_returns, df_rank = calculate_daily_returns(data)

    # Step 3: 生成交易信号和策略收益并输出信号数据示例
    df_signal = generate_signals(df_rank, tickers)
    strategy_returns, returns = calculate_strategy_returns(df_signal, daily_stock_returns, tickers)
    print("Signal DataFrame：")
    print(df_signal.head(3))

    # Step 4: 绩效指标
    cumulative_returns, sharpe_ratio, drawdown, max_drawdown = evaluate_performance(strategy_returns)

    # Step 5: 结果可视化
    if cumulative_returns is not None:
        plot_results(strategy_returns, cumulative_returns, drawdown, max_drawdown, output_dir="output")
