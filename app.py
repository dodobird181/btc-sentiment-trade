import os
import strategy

print('Starting app...')

if strategy_clsname := os.getenv('BACKTEST'):
    # app is running in backtesting mode
    strategy_cls = getattr(strategy, strategy_clsname)
    strategy = strategy_cls()