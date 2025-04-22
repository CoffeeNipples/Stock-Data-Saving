from gitautouploader import gitautoupload
from updateyfinance import financelibraryupdate
import main
import schedule
import time

# schedule.every(8).hours.do(financelibraryupdate())


def datapull():

    print("running datapull")
    tickers = ["^FTSE", "^GDAXI", "^NDX", "^DJI"]

    for items in tickers:
        main.main(items)
    print("datapull COMPLETE")
    gitautoupload()

if __name__ == "__main__":
    
    financelibraryupdate()
    datapull()

    schedule.every(5).hours.do(datapull)
    schedule.every(1).week.do(financelibraryupdate)

    while True:
        schedule.run_pending()
        time.sleep(1)
