import numpy as np
import pandas_datareader as web
import pandas as pd
from tSeries import tSeries
from odict import odict

# df_main = pd.read_csv('EOD-V.csv')
# df_main.set_index('Date', inplace=True)
#
# open = np.array(df_main['Open'])
# close = np.array(df_main['Close'])
# hc = close - open
# print(open)
# print(close)
# print(hc)

# data = []
#
# # liste = ['NYSEARCA:SPY', 'NASDAQ:GOOGL', 'NASDAQ:AAPL', 'NYSE:BAC', 'NYSE:F']
# liste = list(input('Entrez votre liste'))
#
# open = False
# newTick = ''
# newList = []
# for caracter in liste:
#     if open == False and caracter == "'":
#         open = True
#         continue
#     if open == True:
#         if caracter != "'":
#             newTick += caracter
#         else:
#             open = False
#             newList.append(newTick)
#             newTick = ''
#
#
# print(newList)
dictio = {}
data_frame = pd.read_csv('nasdaq.csv')
buffer_df = pd.DataFrame(data_frame['Date'])
new_df = pd.DataFrame(buffer_df)
new_df.set_index('Date', inplace=True)
data_frame.set_index('Date', inplace=True)
print(data_frame.head())

liste = list(data_frame)
ticker2 = liste[0].split('_')[0]
for item in liste:
    ticker1 = item.split('_')[0]
    data = item.split('_')[1]
    if ticker1 == ticker2:
        buffer_item = pd.DataFrame(data_frame[item])
        new_df = new_df.join(buffer_item, how='outer')
        new_df.rename(columns={item: data}, inplace=True)
        print(new_df.head())
    else:
        buffer_series = tSeries(new_df)
        dictio[ticker2] = buffer_series
        ticker2 = ticker1
        new_df = buffer_df
        new_df = new_df.join(data_frame[item])
        new_df.rename(columns={item: data}, inplace=True)

print(dictio)

# dictio = {}
# data_frame = pd.read_csv('nasdaq.csv')
# print(data_frame.head())
# buffer_df = pd.DataFrame(data_frame['Date'])
# new_df = pd.DataFrame(buffer_df)
# new_df.set_index('Date', inplace=True)
# print(new_df.head())
# data_frame.set_index('Date', inplace=True)
# print(data_frame.head())
#
# item = 'SPY_Open'
# buffer_item = pd.DataFrame(data_frame[item])
# print(buffer_item.head())
# new_df = new_df.join(buffer_item, how='outer')
# print(new_df.head())
# data = item.split('_')[1]
# new_df.rename(columns={item: data}, inplace=True)
# print(new_df.head())
