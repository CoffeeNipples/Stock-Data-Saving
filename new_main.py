import yfinance as yf
import multiprocessing
import os
from datetime import datetime,timedelta
import pandas as pd



def timeframe_select(interval):
    if interval == '1m':
        timelimit = '7d'
    elif interval == '5m':
        timelimit = '60d'
    elif interval == '15m':
        timelimit = '60d'
    elif interval == '30m':
        timelimit = '60d'
    elif interval == '1h':
        timelimit = '730d'
    elif interval == '1d':
        timelimit = 'max'
    return timelimit


def pulling_all_data(ticker,interval):
    #function to pull the data
    stock = yf.Ticker(ticker)
    data = {}
    period = timeframe_select(interval)
    data = stock.history(period=period, interval=interval)
    return data

def filepath_namer(ticker,timeframes):
    #create a list of all the filepaths for reference purposes
    filepaths = []
    for intervals in timeframes:
        filepaths.append(f'{ticker}-{intervals}.csv')
    return filepaths
 
def data_check(ticker,timeframes):
    for intervals in timeframes:
        filepath = f'{ticker}-{intervals}.csv'
        all_exist= True
        if not os.path.exists(filepath):
            all_exist= False
            df = pd.DataFrame(pulling_all_data(ticker,intervals))
            if df.index.name == 'Date':
                df.index.name = 'Datetime'
            df.to_csv(filepath, index=True, encoding="utf-8")
    all_exist = True
    return all_exist

def recent_data_check(csv_data):

    data_match = False

    #Find most recent date on CSV DATA
    df = pd.read_csv(csv_data)
    df['Datetime'] = pd.to_datetime(df['Datetime'],utc=True)
    recent = df.loc[df['Datetime'].idxmax()]
    recent = recent['Datetime'].strftime('%y-%m-%d')    

    #find date yesterday
    yesterday1 = datetime.today() - timedelta(days=1)

    if yesterday1.weekday() == 5:
        yesterday1 = datetime.today() - timedelta(days=2)

    if yesterday1.weekday() == 6:
        yesterday1 = datetime.today() - timedelta(days=3)

    yesterday = yesterday1.strftime('%y-%m-%d')
    
    #if yesterdays date is less than or equal
    if yesterday <= recent:
        print(f"{csv_data} is up to date with {yesterday1} data")
        data_match = True
    else:
        print(yesterday1.weekday(), yesterday)

    return data_match


def main():

    uk100 = "^FTSE"
    dax40 = "^GDAXI"
    nasdaq = "NDQ"
    dj30 = "^DJI"

    timeframes = ['1m','5m','15m','30m','1h','1d']

    check = data_check(dax40,timeframes)
    if check:
        filepaths = filepath_namer(dax40,timeframes)
        for filename in filepaths:
            print(recent_data_check(filename))

if __name__ == "__main__":
    main()

    

