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
        self.csvFile = ''
        self.benchmark = False
        self.seriesList = {}
        self.seriesDictionary = {}
        self.corrMatrix = np.array([])

    def createAnalysisMenu(self):
        print("""
        A-Travailler avec un csv provenant de google finance
        B-Travailler avec un csv provenant de bloomberg
        R-Revenir en arrière
        Q-Quitter
        """)
        optionMenu = str.upper(input('Quelle option choisissez-vous?'))

        if optionMenu == 'A':
            return self.createGFinMenu()

        elif optionMenu == 'B':
            return self.createBloomMenu()

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
            df_first = pd.read_csv(newCSV)
            self.csvFile = newCSV
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
                return self.formatAndCalculate()
            if optionReady == 'N':
                return self.createAnalysisMenu()

    def formatAndCalculate(self):
        self.createAnalysisMenu()

    def createBloomMenu(self):
        print('Option non-disponible pour le moment')
        return self.createAnalysisMenu()