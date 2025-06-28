import matplotlib.pyplot as plt
import numpy as np

def plot_results(strategy_returns, cumulative_returns, drawdown, max_drawdown, output_dir="."):
    """
    Step 5 - 结果可视化
    保存图片到本地，不直接弹窗。
    """
    if not strategy_returns.empty:
        # 累计收益曲线
        plt.figure(figsize=(10, 6))
        cumulative_returns.plot()
        plt.title('Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.grid(True)
        plt.savefig(f"{output_dir}/cumulative_returns.png", bbox_inches='tight')
        plt.close()

        # 6个月滚动夏普比率
        rolling_window = 126
        rolling_sharpe_ratio = (strategy_returns.rolling(window=rolling_window).mean() /
                                strategy_returns.rolling(window=rolling_window).std()) * np.sqrt(252)
        plt.figure(figsize=(10, 6))
        rolling_sharpe_ratio.plot()
        plt.title('Rolling 6-Month Sharpe Ratio')
        plt.xlabel('Date')
        plt.ylabel('Sharpe Ratio')
        plt.grid(True)
        plt.savefig(f"{output_dir}/rolling_sharpe_ratio.png", bbox_inches='tight')
        plt.close()

        # 最大回撤
        plt.figure(figsize=(10, 6))
        drawdown.plot()
        plt.title('Maximum Drawdown')
        plt.xlabel('Date')
        plt.ylabel('Drawdown')
        plt.axhline(max_drawdown, color='red', linestyle='--', label='Max Drawdown')
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{output_dir}/max_drawdown.png", bbox_inches='tight')
        plt.close()
