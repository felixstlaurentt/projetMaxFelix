from tSeries import tSeries
import sys
import numpy as np
import pandas as pd

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
        self.csvFile = pd.DataFrame()
        self.benchmark = False
        self.seriesList = {}
        self.seriesDictionary = {}
        self.corrMatrix = np.array([])

    def createAnalysisMenu(self):
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
                return self.format()
            if optionReady == 'N':
                return self.createAnalysisMenu()

    def format(self):
        """
        Fonction qui va formater le csv pour créer un tSeries pour chaque ticker qu'il contient et lui insérer leur propre DataFrame dans chaque objet

        :return: self.createAnalysisMenu
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
                buffer_series = tSeries(new_df)
                self.seriesDictionary[ticker2] = buffer_series
                ticker2 = ticker1
                new_df = buffer_df
                new_df = new_df.join(self.csvFile[item])
                new_df.rename(columns={item: data}, inplace=True)

        buffer_series = tSeries(new_df)
        self.seriesDictionary[ticker2] = buffer_series

        return self.createAnalysisMenu()

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
        for item in self.seriesDictionary:
            print(item)

        return self.createAnalysisMenu()