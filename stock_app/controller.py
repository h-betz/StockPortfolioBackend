import datetime as dt
import pandas as pd
import pandas_datareader.data as pdr

#data_source = 'google'

#todays_date = dt.datetime.today()

class Controller():

    def __init__(self):
        #now = dt.datetime.now()
        self.todays_date = dt.datetime.now().date()
        self.data_source = 'yahoo'
    

    def get_ticker_data(self, ticker, start_date=None, end_date=None):
        if not start_date and not end_date:
            start_date = self.todays_date
            end_date = self.todays_date
        #panel_data = pdr.DataReader([ticker], self.data_source, start_date, end_date)
        todays_data = pdr.get_quote_yahoo(ticker)
        #todays_data = panel_data.ix['2017-09-19']
        return todays_data