import numpy as np

def evaluate_performance(strategy_returns):
    if not strategy_returns.empty:
        # 累计收益率
        cumulative_returns = (strategy_returns + 1).cumprod()

        # 夏普比率 (假设无风险利率为 0)
        daily_rf_rate = 0
        annual_rf_rate = daily_rf_rate * 252
        strategy_volatility = strategy_returns.std() * np.sqrt(252)
        sharpe_ratio = (strategy_returns.mean() - annual_rf_rate) / strategy_volatility if strategy_volatility != 0 else np.nan

        # 最大回撤
        cum_max = cumulative_returns.cummax()
        drawdown = (cumulative_returns - cum_max) / cum_max
        max_drawdown = drawdown.min()

        print("Cumulative Returns:")
        print(cumulative_returns.iloc[-1] if not cumulative_returns.empty else "No trades executed.")
        print("\nSharpe Ratio:")
        print(sharpe_ratio)
        print("\nMax Drawdown:")
        print(max_drawdown)
        return cumulative_returns, sharpe_ratio, drawdown, max_drawdown
    else:
        print("No trades executed. Cannot compute performance metrics.")
        return None, None, None, None
