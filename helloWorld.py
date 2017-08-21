import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pickle
from matplotlib import style


style.use('ggplot')

pickle_in = open('ptfWidget_seriesList.pickle', 'rb')
liste = pickle.load(pickle_in)
pickle_in = open('ptfWidget_seriesDictionary.pickle', 'rb')
dict = pickle.load(pickle_in)


df_rend = pd.DataFrame()
for item in liste[1:]:
    rend = pd.DataFrame(dict[item].rend)
    rend.rename(columns={'Close': item}, inplace=True)
    if df_rend.empty:
        df_rend = pd.DataFrame(rend)
    else:
        df_rend = df_rend.join(rend, how='outer')

mean = df_rend.mean()
cov = df_rend.cov()

num_port = 25000

results = np.zeros((4 + len(liste) - 2, num_port))

for i in range(num_port):
    weights = np.random.random(len(liste)-1)
    weights /= np.sum(weights)

    port_return = np.sum(mean * weights) * 252
    port_std = np.sqrt(np.dot(weights.T, np.dot(cov, weights))) * np.sqrt(252)

    results[0, i] = port_return
    results[1, i] = port_std
    results[2, i] = port_return / port_std

    for j in range(len(weights)):
        results[j + 3, i] = weights[j]

columns_name = ['Returns', 'Std_Dev', 'Sharpe']
for i in liste[1:]:
    columns_name.append(i)

results_frame = pd.DataFrame(results.T, columns=columns_name)
print(results_frame.head())

max_sharpe = results_frame.iloc[results_frame['Sharpe'].idxmax()]
min_var = results_frame.iloc[results_frame['Std_Dev'].idxmin()]

print(max_sharpe)
print(min_var)

plt.scatter(results_frame.Std_Dev, results_frame.Returns, c=results_frame.Sharpe, cmap='RdYlBu')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.colorbar()
plt.scatter(max_sharpe[1], max_sharpe[0], marker=(5, 1, 0), color='r', s=250)
plt.scatter(min_var[1], min_var[0], marker=(5, 1, 0), color='g', s=250)
plt.show()

