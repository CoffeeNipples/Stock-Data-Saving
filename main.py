#4 core processes - Have each stock taking running on each core, for smoothing running and less likely to run into processing issues

'''THINK of all data we may want in the future:
        >NAS
        >DJ
        >DAX
        >UK100
        >Crpyto

    TIMEFRAMES:
        >1m
        >3m???
        >5m
        >15m
        >1hr
        >4hr

Possible things to look into...
    >Pulling the list somehow to ORRR a seperate list to check that we have all the dates and fill in any missing BLANKS
    >I GUESS WE WANT ALL OF DATA TO START OFF WITH...
    >PUSH DATA TO CLOUD ASWELL AS HARD DRIVE??? INCASE OF DAMAGE??
    > Can we AUTO push the data onto git from python?!?!?! would be so fking cool
        '''


'''NEED to try and check the period in accordance with what data there is and collect available data'''
import yfinance as yf
import multiprocessing
import os
from datetime import datetime,timedelta

uk100 = "^FTSE"
dax40 = "^GDAXI"
nasdaq = "NDQ"
dj30 = "^DJI"

timeframes = ['1m','5m','15m','30m','1h','1d']

def pulling_all_data(ticker,timeframes):
    #function to pull the data
    stock = yf.Ticker(ticker)
    data = {}
    for time in timeframes:
        data[time] = stock.history(period="max", interval=time)
    return data

def process_1(ticker,timeframes):

    for intervals in timeframes:
        current_time = datetime.now()
        yesterday = current_time - timedelta(days=1)

        yesterday = yesterday.strftime('%Y-%m-%d %H:%M:%S')
        current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        
        filepath = f'{ticker}check{intervals}.txt'

        if os.path.exists(filepath):                
            with open(filepath,"r", encoding="utf-8") as file:
                contents = file.read()
        else:
            with open(filepath,"w") as file:
                hist_data = pulling_all_data(ticker,intervals)
                file.write(yesterday)

                
            



def process_2():
    pass

def process_3():
    pass

def process_4():
    pass
