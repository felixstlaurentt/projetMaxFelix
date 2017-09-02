import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pickle
from matplotlib import style, dates
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import sys
import datetime as dt


style.use('ggplot')

# pickle_in = open('ptfWidget_seriesList.pickle', 'rb')
# liste = pickle.load(pickle_in)
# pickle_in = open('ptfWidget_seriesDictionary.pickle', 'rb')
# dict = pickle.load(pickle_in)

csvFile = pd.read_csv('nasdaq.csv')

csvFile.set_index('Date', inplace=True)
csvFile = pd.DataFrame(csvFile['SPY_Open'])
# csvFile.reset_index(inplace=True)

# new_dates = []
# for date in csvFile['Date']:
#     annee, mois, jour = date.split('-')
#     new_date = dt.datetime(int(annee), int(mois), int(jour))
#     new_dates.append(new_date)

# new_frame = pd.DataFrame(new_dates, columns=['Date'])
# new_frame = new_frame.join(csvFile['SPY_Open'])
# new_frame.set_index('Date')
csvFile.resample('M').mean()
print(csvFile)