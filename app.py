import os
import inspect
import strategy

print('Starting app...')

if strategy_clsname := os.getenv('BACKTEST'):
    # app is running in backtesting mode
    try:
        strategy_cls = getattr(strategy, strategy_clsname)
        strategy = strategy_cls()
    except AttributeError:
        print(
            f'Could not find backtesting strategy "{strategy_clsname}". ' +
            f"Currently defined strategies are: {[
                name for name, cls in inspect.getmembers(strategy, inspect.isclass)
                if cls.__module__ == strategy.__name__
            ]}."
        )
