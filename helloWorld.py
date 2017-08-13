import pandas as pd
import pickle
from matplotlib import style, dates
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import time


# style.use('dark_background')
#
# MA1 = 10
# MA2 = 30
#
#
# def moving_average(values, window):
#     weights = np.repeat(1.0, window)/window
#     smas = np.convolve(values, weights, 'valid')
#     return smas
#
#
# def high_minus_low(highs, lows):
#     return highs-lows
#
#
# pickle_in = open('seriesAnalysisMenu.pickle', 'rb')
# buffer = pickle.load(pickle_in)
#
# buffer.frame.reset_index(inplace=True)
#
# new_frame = pd.DataFrame(buffer.frame)
#
# data_dates = []
# for date in new_frame['Date']:
#     new_Date = dates.datestr2num(date)
#     data_dates.append(new_Date)
#
# i = 0
# ohlc_data = []
# while i < len(data_dates):
#     stats_1_day = data_dates[i], new_frame['Open'][i], new_frame['High'][i], new_frame['Low'][i], new_frame['Close'][i]
#     ohlc_data.append(stats_1_day)
#     i += 1
#
# # Moving average
# ma1 = moving_average(new_frame['Close'], MA1)
# ma2 = moving_average(new_frame['Close'], MA2)
# start = len(data_dates[MA2-1:])
#
# # dayFormatter = dates.DateFormatter('%d-%b-%Y')
#
# fig = plt.figure()
#
# ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
# plt.title('Googl')
# plt.ylabel('Price')
#
# ax2 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)
# plt.xlabel('Date')
#
# candlestick_ohlc(ax1, ohlc_data, colorup='g', colordown='r')
# ax2.bar(data_dates, new_frame['Volume'], 0.5, color='g')
#
# for label in ax2.xaxis.get_ticklabels():
#     label.set_rotation(45)
#
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
#
# # ax1.grid(True)
# #
# # ax1.annotate('Big News!', (data_dates[-1], new_frame['High'][new_frame.index[-1]]), xytext=(0.8, 0.9), textcoords='axes fraction',
# #              arrowprops=dict(facecolor='grey', color='grey'))
# #
# # ax1.text(data_dates[100], new_frame['Close'][400], 'Google price')
#
# # bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
# #
# # ax1.annotate((new_frame['Close'][new_frame.index[-1]]), (data_dates[-1], new_frame['Close'][new_frame.index[-1]]),
# #              xytext=(data_dates[-1] + 3, new_frame['Close'][new_frame.index[-1]]), bbox=bbox_props)
# # print(len(data_dates), len(ma1))
# #
# ax1.plot(data_dates[-start:], ma1[-start:])
# ax1.plot(data_dates[-start:], ma2[-start:])
#
# plt.legend()
# plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
# plt.show()
#
dictio = {'salut': ['yoy', 'taleut', 'ark'], 'yoyo': ['taleut', 'niggah', 'enfant'], 'sperme': ['vagin', 'penis']}
liste = ['salut', 'yoyo', 'sperme']
liste.remove('yoyo')
buffer = {}
for item in liste:
    buffer[item] = dictio[item]
dictio = buffer
print(dictio)