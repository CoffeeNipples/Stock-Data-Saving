
import yfinance as yf
import multiprocessing
import os
from datetime import datetime,timedelta

dax = '^GDAXI'
timeframes = ['1m','5m','15m','30m','1h','1d']


def pulling_all_data(ticker,interval):
    #function to pull the data
    stock = yf.Ticker(ticker)
    data = {}
    data = stock.history(period="max", interval=interval)
    return data

print(type(pulling_all_data(dax,'30m')))
