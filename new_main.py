import yfinance as yf
import multiprocessing
import os
from datetime import datetime,timedelta
import pandas as pd

uk100 = "^FTSE"
dax40 = "^GDAXI"
nasdaq = "NDQ"
dj30 = "^DJI"


timeframes = ['1m','5m','15m','30m','1h','1d']

def pulling_all_data(ticker,interval):
    #function to pull the data
    stock = yf.Ticker(ticker)
    data = {}
    data = stock.history(period="max", interval=interval)
    return data
                
def data_check2(ticker,timeframes):
    for intervals in timeframes:
        filepath = f'{ticker}check{intervals}.csv'
        all_exist= True
        if not os.path.exists(filepath):
            all_exist= False
            df = pd.DataFrame(pulling_all_data(ticker,intervals))
            df.to_csv(filepath, index=True, encoding="utf-8")

print(data_check2(dax40,timeframes))

