import pandas as pd
import pandas_datareader.data as web
import datetime as dt


class googleTseries:

    def __init__(self):

        self.tickers = []
        self.dataMatrix = pd.DataFrame
        self.__start = dt.datetime
        self.__end = dt.datetime
        print("Une t series a ete creee")

    def setStart(self, annee, mois, jour):
        if self.verifierDate(annee, mois, jour) == True:
            self.__start = dt.datetime(annee, mois, jour)
        else:
            print('Erreur de date')

    def setEnd(self, annee, mois, jour):
        if self.verifierDate(annee, mois, jour) == True:
            self.__start = dt.datetime(annee, mois, jour)
        else:
            print('Erreur de date')

    def verifierDate(self, annee, mois, jour):
        if annee <= 2017 and annee >= 1960:
            if mois <= 12 and mois >= 0:
                if jour <= 31 and jour >= 0:
                    return True
        return False

    def imprimerDates(self):
        print(self.__end)
        print(self.__start)

    def ajouterTicker(self, ticker):
        self.tickers.append(ticker)

    def supprimerTicker(self, ticker):
        if ticker in self.tickers:
            self.tickers.remove(ticker)
        else:
            print("Ce ticker n'est pas dans votre liste")

    def googleImport(self, ticker):
        df = web.DataReader(ticker, "google", self.__start, self.__end)
        return df

if __name__ == '__main__':
    j = googleTseries()
    j.imprimerDates()

    annee = int(input('annee?'))
    mois = int(input('mois?'))
    jour = int(input('jour?'))

    while j.verifierDate(annee, mois, jour) == False:
        annee = int(input('annee?'))
        mois = int(input('mois?'))
        jour = int(input('jour?'))
