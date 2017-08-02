import numpy as np
import pandas_datareader as web
import pandas as pd

# df_main = pd.read_csv('EOD-V.csv')
# df_main.set_index('Date', inplace=True)
#
# open = np.array(df_main['Open'])
# close = np.array(df_main['Close'])
# hc = close - open
# print(open)
# print(close)
# print(hc)

data = []

# liste = ['NYSEARCA:SPY', 'NASDAQ:GOOGL', 'NASDAQ:AAPL', 'NYSE:BAC', 'NYSE:F']
liste = list(input('Entrez votre liste'))

open = False
newTick = ''
newList = []
for caracter in liste:
    if open == False and caracter == "'":
        open = True
        continue
    if open == True:
        if caracter != "'":
            newTick += caracter
        else:
            open = False
            newList.append(newTick)
            newTick = ''


print(newList)
