import numpy as np
import pandas_datareader as web
import pandas as pd

df_main = pd.read_csv('EOD-V.csv')
df_main.set_index('Date', inplace=True)

open = np.array(df_main['Open'])
close = np.array(df_main['Close'])
hc = close - open
print(open)
print(close)
print(hc)