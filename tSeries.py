import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import pickle
import numpy as np


class tSeries:

    def __init__(self, frame):

        self.frame = frame
        try:
            self.frame.set_index('Date', inplace=True)
        except:
            print("Erreur dans l'attribution de l'index date")

        try:
            self.open = np.array(self.frame['Open'])
        except:
            self.open = np.empty([0, 0])

        try:
            self.close = np.array(self.frame['Close'])
        except:
            self.close = np.empty([0, 0])

        try:
            self.low = np.array(self.frame['Low'])
        except:
            self.low = np.empty([0, 0])

        try:
            self.high = np.array(self.frame['High'])
        except:
            self.high = np.empty([0, 0])

        try:
            self.volume = np.array(self.frame['Volume'])
        except:
            self.volume = np.empty([0, 0])

if __name__ == '__main__':
    test = tSeries(pd.read_csv('EOD-V.csv'))
    print(test.frame.head())
    print(test.open)
    print(test.close)
    print(test.low)
    print(test.high)
    print(test.volume)