# Project Structure

- `main.py` - 项目的主入口脚本，用于运行整体流程。
- `src/` - 源代码目录，包含核心功能模块：
    - `__init__.py` - 使 `src` 成为 Python 包。
    - `data_loader.py` - 数据加载与预处理相关函数。
    - `returns_calculator.py` - 计算收益率等相关函数。
    - `trading_signal.py` - 交易信号的生成逻辑。
    - `performance_metrics.py` - 性能评估相关指标计算。
    - `visualization.py` - 可视化相关函数。
- `requirements.txt` - Python 依赖库列表。
- `README.md` - 项目说明文档。
