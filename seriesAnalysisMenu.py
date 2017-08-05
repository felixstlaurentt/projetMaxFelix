from tSeries import tSeries
import sys
import numpy as np
import pandas as pd
import pickle

"""
Classe qui va ouvrir le menu pour les analyses de données temporelles

Attributes:
    csvFile: string qui contient le nom du csv à travailler
    benchmark: True si le premier ticker est un benchmark, False autrement
    seriesList: Liste qui contient les tickers
    seriesDictionary: Dictionnaire qui contient les objets de la classe tSeries pour chaque ticker
    corrMatrix: Matrice de correlations de tous nos tickers
"""
class seriesAnalysisMenu():

    def __init__(self):
        """
        Constructeur de la classe seriesAnalysisMenu
        """
        self.csvName = ''
        self.csvFile = pd.DataFrame()
        self.benchmark = False
        self.seriesList = []
        self.seriesDictionary = {}
        self.corrMatrix = np.array([])

        try:
            self.loadFromPickle()
        except:
            print('new')

    def createAnalysisMenu(self):
        """
        Fonction qui créer le menu principal pour les time series

        :return: createGFinMenu, createBloomMenu, printTest, 0, sys.exit
        """
        print('Fichier en cours: ', self.csvName)
        print("""
        A-Travailler avec un csv provenant de google finance
        B-Travailler avec un csv provenant de bloomberg
        C-Imprimer Tests
        R-Revenir en arrière
        Q-Quitter
        """)
        optionMenu = str.upper(input('Quelle option choisissez-vous?'))

        if optionMenu == 'A':
            return self.createGFinMenu()

        elif optionMenu == 'B':
            return self.createBloomMenu()

        elif optionMenu == 'C':
            return self.printTest()

        elif optionMenu == 'R':
            return 0

        elif optionMenu == 'Q':
            return sys.exit()

        else:
            return self.createAnalysisMenu()

    def createGFinMenu(self):
        """
        Fonction qui créer le menu pour importer le fichier csv, le formatter et faire les calculs

        :return:
        """
        newCSV = str(input("Entrez le nom du fichier csv que vous voulez utiliser (incluant l'extension): "))

        try:
            self.csvFile = pd.read_csv(newCSV)
            print('Le fichier à été chargé avec succès')
            self.csvName = newCSV
        except:
            print("Le fichier n'a pas pu se charger")
            return self.createAnalysisMenu()

        optionBench = ''
        while optionBench != 'O' and optionBench != 'N':
            optionBench = str.upper(input("Est-ce que le premier ticker est un benchmark? (O pour oui, N pour non) "))
            if optionBench == 'O':
                self.benchmark = True
            else:
                self.benchmark = False

        optionReady = ''
        while optionReady != 'O' or optionReady != 'N':
            optionReady = str.upper(input("Tout est prêt. Passer aux calculs? (O pour oui, N pour non) "))
            if optionReady == 'O':
                self.format()
                self.calcStats()
                return self.createAnalysisMenu()
            if optionReady == 'N':
                return self.createAnalysisMenu()

    def format(self):
        """
        Fonction qui va formater le csv pour créer un tSeries pour chaque ticker qu'il contient et lui insérer leur propre DataFrame dans chaque objet

        :return: Void
        """
        self.seriesDictionary = {}
        buffer_df = pd.DataFrame(self.csvFile['Date'])
        new_df = pd.DataFrame(buffer_df)
        new_df.set_index('Date', inplace=True)
        self.csvFile.set_index('Date', inplace=True)

        liste = list(self.csvFile)
        ticker2 = liste[0].split('_')[0]

        for item in liste:
            ticker1 = item.split('_')[0]
            data = item.split('_')[1]

            if ticker1 == ticker2:
                buffer_item = pd.DataFrame(self.csvFile[item])
                new_df = new_df.join(buffer_item, how='outer')
                new_df.rename(columns={item: data}, inplace=True)
                print(new_df.head())
            else:
                self.seriesList.append(ticker2)
                self.seriesDictionary[ticker2] = tSeries(new_df)
                ticker2 = ticker1
                new_df = pd.DataFrame(buffer_df)
                new_df = new_df.join(self.csvFile[item])
                new_df.rename(columns={item: data}, inplace=True)

        self.seriesList.append(ticker2)
        self.seriesDictionary[ticker2] = tSeries(new_df)

        for ticker in self.seriesList:
            if self.benchmark:
                self.seriesDictionary[ticker].benchmark = np.array(self.seriesDictionary[self.seriesList[0]].close)

    def calcStats(self):
        """
        Fonction qui calcules les statistiques de chaque ticker et ceux du portfolio

        :return: Void
        """
        for ticker in self.seriesList:
            self.seriesDictionary[ticker].calcStats()

    def createBloomMenu(self):
        """
        Fonction qui créer le menu pour travailler sur un csv qui provient de bloomberg

        :return: self.createAnalysisMenu
        """
        print("""
        Option non-disponible pour le moment
        """)
        return self.createAnalysisMenu()

    def printTest(self):
        """
        Fonction qui imprime certains test dans la console pour s'assurer que tout est beau

        :return: self.createAnalysisMenu
        """
        for ticker in self.seriesList:
            print(ticker)
            print('close: ', self.seriesDictionary[ticker].frame.head())
            print('bench: ', self.seriesDictionary[ticker].benchmark)
            print('Std: ', self.seriesDictionary[ticker].std)
            print('beta: ', self.seriesDictionary[ticker].beta)

        print(self.seriesList)

        return self.createAnalysisMenu()

    def saveToPickle(self):
        """
        Fonction qui sauvegarde l'objet seriesAnalysisMenu en entier. Ce qui sauvegarde toutes les données même si l'on ferme le programme

        :return: Void
        """
        pickle_out = open('seriesAnalysisMenu.pickle', 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        print('workspace sauvegardé')

    def loadFromPickle(self):
        """
        Fonction qui remet en place l'objet seriesAnalysisMenu à l'état ou il se trouvait à la dernière sauvegarde

        :return: Void
        """
        pickle_in = open('seriesAnalysisMenu.pickle', 'rb')
        buffer = pickle.load(pickle_in)
        self.csvName = buffer.csvName
        self.csvFile = buffer.csvFile
        self.benchmark = buffer.benchMark
        self.seriesList = buffer.seriesList
        self.seriesDictionary = buffer.seriesDictionary
        self.corrMatrix = buffer.corrMatrix
