import datetime as dt
import yfinance as yf
import pandas as pd
import os


class Prices(pd.DataFrame):
    """
    Get price data as a Pandas `DataFrame`. The price data is downloaded using yfinance and cached
    locally to prevent unecessary re-downloads. You can search ticker options here: https://ca.finance.yahoo.com/lookup.

    **Parameters**:
        ticker : str
            The ticker to download
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
        start: datetime
            Download start date (inclusive.)
            Default is 99 years ago
        end: datetime
            Download end date (exclusive.)
            Default is now

    **Example usage**:
        ```
        prices = Prices('BTC-USD')
        prices.head()
        ```
    """

    CACHE_LOC = '.price_cache'

    def __init__(self, ticker: str, *args, interval="1d", start=pd.Timestamp.min, end=pd.Timestamp.max, **kwargs):

        if not os.path.exists(self.CACHE_LOC):
            # make sure price cache directory exists
            os.mkdir(self.CACHE_LOC)

        cache_loc = f'{self.CACHE_LOC}/{ticker.lower()}.csv'
        if os.path.exists(cache_loc):
            breakpoint()
            cached_data = pd.read_csv(cache_loc)
            if len(cached_data) > 0:
                cached_start = dt.datetime.fromisoformat(cached_data['Date'].min())
                cached_end = dt.datetime.fromisoformat(cached_data['Date'].max())
                if cached_start <= start and cached_end >= end:
                    # use cached data
                    print('loading previously cached data...')
                    return super().__init__(data=cached_data)

        # otherwise, download and cache
        super().__init__(data=yf.download(ticker, *args,  interval=interval, start=start, end=end, **kwargs))
        self.to_csv(cache_loc)


btc = Prices("BTC-USD")
print(btc.head())