from tSeries import tSeries
import sys

"""
Classe qui va ouvrir le menu pour les analyses de données temporelles

Attributes:
    seriesDictionnary: Dictionnaire qui comprend tous les objets de la classe tSeries qui sont comprises dans le csv
"""
class seriesAnalysisMenu():

    def __init__(self):
        """
        Constructeur de la classe seriesAnalysisMenu
        """
        self.csvFile = ''
        self.seriesDictionnary = {}

    def createAnalysisMenu(self):
        print("""
        A-Travailler avec un csv provenant de google finance
        B-Travailler avec un csv provenant de bloomberg
        R-Revenir en arrière
        Q-Quitter
        """)
        optionMenu = str.upper(input('Quelle option choisissezz-vous?'))

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
        print('Option non-disponible pour le moment')
        return self.createAnalysisMenu()

    def createBloomMenu(self):
        print('Option non-disponible pour le moment')
        return self.createAnalysisMenu()