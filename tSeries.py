import pandas as pd
import pandas_datareader.data as web
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

    def __init__(self, frame, benchmark=np.array([])):
        """
        Constructeur de la classe tSeries

        :param frame: pandas Dataframe formatté dans le bon format par la classe seriesAnalysisMenu
        :param benchmark: numpy array du benchmark
        """

        self.frame = frame
        try:
            self.frame.set_index('Date', inplace=True)
        except:
            print("Erreur dans l'attribution de l'index date")

        self.benchmark = benchmark
        self.beta = 0

        try:
            self.open = np.array(self.frame['Open'])
        except:
            self.open = np.array([])

        try:
            self.close = np.array(self.frame['Close'])
        except:
            self.close = np.array([])

        try:
            self.low = np.array(self.frame['Low'])
        except:
            self.low = np.array([])

        try:
            self.high = np.array(self.frame['High'])
        except:
            self.high = np.array([])

        try:
            self.volume = np.array(self.frame['Volume'])
        except:
            self.volume = np.array([])

        self.rend = np.array([])
        self.std = 0

    def calcRend(self):
        """
        Fonction qui calcule le rendement des close et insère le vecteur dans self.rend

        :return: Void
        """
        self.rend = np.diff(self.close) / self.close[:-1]

    def calcStd(self):
        """
        Fonction qui calcule l'écart-type et insère le résultat dans self.std

        :return: Void
        """
        self.std = self.rend.std()

    def calcBeta(self):
        """
        Fonction qui calcule le beta seulement s'il y a un benchmark dans self.benchmark et insère le résultat dans self.beta

        :return: Void
        """
        pass

if __name__ == '__main__':
    test = tSeries(pd.read_csv('aapl.csv'))
    print(test.frame.head())

    print(test.close)
    test.calcRend()
    print(test.rend)
    test.calcStd()
    print(test.std)
    print(test.benchmark)
