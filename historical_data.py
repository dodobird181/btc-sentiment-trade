import pandas as pd
import datetime as dt
import yfinance as yf


class FetchHistoricalDataError(Exception):
    """Something went wrong while fetching historical price data."""
    ...


class SymbolNotSupported(FetchHistoricalDataError):
    """The stock market or cryptocurrency symbol isn't supported."""
    ...


class ResolutionNotSupported(FetchHistoricalDataError):
    """The resolution of data you are trying to fetch isn't supported."""
    ...


class RangeUnavailable(FetchHistoricalDataError):
    """The range of time you are trying to fetch price data for is unavailable."""
    ...


def fetch_historical_data(
    symbol: str,
    resolution: dt.timedelta,
    start_dt: dt.datetime,
    end_dt: dt.datetime,
) -> pd.DataFrame:
    """
    Fetch historical stock market data of a given resolution from `start_dt`
    to `end_dt`, and return the data as a pandas `DataFrame` with the following
    columns: ["time", "low", "high", "open", "close", "volume"]. Raise a
    `FetchHistoricalDataError` if something went wrong while fetching the data.
    """
    data = yf.download(symbol, interval=resolution, start=start_dt, end=end_dt,)
    return data


data = fetch_historical_data('AAPL', '1d', dt.datetime.now() - dt.timedelta(days=10), dt.datetime.now())
print(data)