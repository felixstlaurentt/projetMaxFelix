from tSeries import tSeries

"""
Classe qui va ouvrir le menu pour les analyses de données temporelles

Attributes:
    seriesDictionnary: Dictionnaire qui comprend tous les objets de la classe tSeries qui sont comprises dans le csv
"""
class seriesAnalysisMenu():

    def __init__(self):
        self.csvFile = ''
        self.seriesDictionnary = {}