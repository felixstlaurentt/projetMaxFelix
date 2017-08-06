import pandas as pd
import pickle
from matplotlib import style, dates
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.ticker as mticker


style.use('ggplot')

pickle_in = open('seriesAnalysisMenu.pickle', 'rb')
buffer = pickle.load(pickle_in)

buffer.frame.reset_index(inplace=True)

new_frame = pd.DataFrame(buffer.frame)

data_dates = []
for date in new_frame['Date']:
    new_Date = dates.datestr2num(date)
    data_dates.append(new_Date)

i = 0
ohlc_data = []
while i < len(data_dates):
    stats_1_day = data_dates[i], new_frame['Open'][i], new_frame['High'][i], new_frame['Low'][i], new_frame['Close'][i]
    ohlc_data.append(stats_1_day)
    i += 1

print(ohlc_data)

dayFormatter = dates.DateFormatter('%d-%b-%Y')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

candlestick_ohlc(ax1, ohlc_data)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax1.grid(True)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock')
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
