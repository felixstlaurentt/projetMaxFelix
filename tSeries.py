import pandas as pd
import datetime as dt
import pickle
import numpy as np

"""
Classe qui contient les statistiques de chaque ticker

Attributes:
    frame:
    benchmark:
    beta:
    open:
    close:
    low:
    high:
    volume:
"""
class tSeries:

    def __init__(self, frame):
        """
        Constructeur de la classe tSeries

        :param frame: pandas Dataframe formatté dans le bon format par la classe seriesAnalysisMenu
        :param benchmark: numpy array du benchmark
        """

        self.frame = pd.DataFrame(frame)
        try:
            self.frame.set_index('Date', inplace=True)
        except:
            print('')
        self.frame.replace(0, np.nan, inplace=True)
        self.frame.dropna(axis=0, how='all', inplace=True)

        self.rend = pd.DataFrame()
        self.meanRend = 0
        self.var = 0
        self.std = 0
        self.cov = 0
        self.beta = 0

    def setBenchmark(self, benchmark):
        column = list(benchmark)
        self.frame = self.frame.join(benchmark, how='outer')
        self.frame.dropna(inplace=True)
        self.frame.rename(columns={column[0]: 'Benchmark'}, inplace=True)

    def calcStats(self):
        self.calcRend()
        self.calcRisk()

    def calcRend(self):
        """
        Fonction qui calcule le rendement des close et insère le vecteur dans self.rend

        :return: Void
        """
        self.rend = self.frame['Close'].pct_change()
        self.rend.dropna(inplace=True)
        self.meanRend = self.rend.mean()

    def calcRisk(self):
        """
        Fonction qui calcule l'écart-type et insère le résultat dans self.std

        :return: Void
        """
        self.var = self.rend.var()
        self.std = self.rend.std()

    def calcBeta(self):
        """
        Fonction qui calcule le beta seulement s'il y a un benchmark dans self.benchmark et insère le résultat dans self.beta

        :return: Void
        """
        self.cov = self.frame['Benchmark'].cov(self.frame['Close'])
        self.beta = self.cov / self.frame['Benchmark'].var()

if __name__ == '__main__':
    benchmark = pd.read_csv('benchmark.csv')
    benchmark.set_index('Date', inplace=True)
    test = tSeries(pd.read_csv('ford.csv'))
    test.setBenchmark(benchmark)
    test.calcRend()
    test.calcRisk()
    test.calcBeta()
    print(test.cov)
    print(test.beta)
    print(test.frame.head())
