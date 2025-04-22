
import os
from datetime import datetime, timedelta, timezone
import multiprocessing
import pandas as pd
import yfinance as yf

def timeframe_select(interval):
    # Finds maximum data available relative to TF
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
    # Function to pull the data
    stock = yf.Ticker(ticker)
    data = {}
    period = timeframe_select(interval)
    data = stock.history(period=period, interval=interval)
    return data

def ticker_name(ticker):
    # Renames the ticker relative for more clear file naming
    if ticker == "^FTSE":
        name = "FTSE100"
    if ticker == "^GDAXI":
        name = "DAX40"
    if ticker == "^NDX":
        name = "NASDAQ"
    if ticker == "^DJI":
        name = "DJ30"
    return name

def filepath_namer(ticker,timeframes):
    # create a list of all the filepaths for reference purposes
    filepaths = []
    tick = ticker_name(ticker)
    for intervals in timeframes:
        filepaths.append(f'{tick}-{intervals}.csv')
    return filepaths
 
def data_check(ticker,timeframes):
    # Provide a BOOL, checking if there is already a file name matching the filename in the folder
    for intervals in timeframes:
        tick = ticker_name(ticker)
        filepath = f'{tick}-{intervals}.csv'
        all_exist = True
        if not os.path.exists(filepath):
            all_exist= False
            df = pd.DataFrame(pulling_all_data(ticker,intervals))
            if df.index.name == 'Date':
                df.index.name = 'Datetime'
            df.to_csv(filepath, index=True, encoding="utf-8")
    all_exist = True
    return all_exist

def recent_data_check(csv_data):
    # CHECK whether the most recent DATETIME on the .CSV is the same or more recent than yesterday - returns a BOOL
    data_match = False

    #Find most recent date on CSV DATA
    df = pd.read_csv(csv_data)
    df['Datetime'] = pd.to_datetime(df['Datetime'],utc=True)
    recent = df.loc[df['Datetime'].idxmax()]
    recent = recent['Datetime'].strftime('%y-%m-%d')    

    # find date yesterday
    yesterday1 = datetime.now(timezone.utc) - timedelta(days=1)

    if yesterday1.weekday() == 5:
        yesterday1 = datetime.now(timezone.utc) - timedelta(days=2)

    if yesterday1.weekday() == 6:
        yesterday1 = datetime.now(timezone.utc) - timedelta(days=3)

    yesterday = yesterday1.strftime('%y-%m-%d')
    
    # if yesterdays date is less than or equal
    if yesterday <= recent:
        print(f"{csv_data} is up to date with {yesterday} data")
        data_match = True
    else:
        print(f"Data for {csv_data} is outdated, data goes to {recent}.... proceeding to update")


    return data_match

def data_merge(csv_data,ticker):
    # MERGE he pulled data from yfinance with the .csv, then append with update

    timeframe = csv_data.split("-")[-1].split(".")[0]
    import_data = pulling_all_data(ticker,timeframe)
    import_data = pd.DataFrame(import_data)
    import_data.index.name = 'Datetime'
    stock_df = pd.read_csv(csv_data, parse_dates=['Datetime'], index_col='Datetime')

    merged_df = pd.concat([stock_df,import_data], ignore_index=False)

    merged_df = merged_df[~merged_df.index.duplicated(keep='last')]

    merged_df.to_csv(csv_data, index=True, encoding= "utf-8")
    print(f"Merge of {csv_data} complete.")



def main(ticker):
    # Run the main script
    print(f'Script Running on {ticker} at {datetime.now()}')
    timeframes = ['1m','5m','15m','30m','1h','1d']

    check = data_check(ticker,timeframes)
    if check:                                               # IF ticker timeframe exists 
        filepaths = filepath_namer(ticker,timeframes)       # Name of the FILEPATHS with all the timeframes - LIST
        for filename in filepaths:                          # run checks to see if columns are UP-TO-Date   
            if not recent_data_check(filename):             # IF files are NOT up to date.
                data_merge(filename,ticker)                 # MERGE DF with Yfinance Data

def fullscript():

    print("running main script")

    tickers = ["^FTSE","^GDAXI","^NDX","^DJI"]
    pool = multiprocessing.Pool()

    pool.map(main,tickers)

    pool.close()
    pool.join()

    print("All stock data fetched!")


    

