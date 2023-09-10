import datetime
import pandas_datareader.data as pdr
import yfinance as yf

# fix pdr issue with yahoo finance
yf.pdr_override()


def get_dataframe(ticker: str, start: datetime, end: datetime):
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')

    return pdr.get_data_yahoo(ticker, start, end)
