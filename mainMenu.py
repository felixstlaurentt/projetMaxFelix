import sys
from importMenu import importMenu
from seriesAnalysisMenu import seriesAnalysisMenu
"""
Classe qui constitue le menu principal

Attributes:
    None

"""

class mainMenu():

    def __init__(self):
        """
        Constructeur de la classe mainMenu
        """
        pass

    def createMenu(self):
        """
        Fonction qui crée le tout premier menu

        :return: soi-même, menuEF (états financiers) ou menuTS (time series)
        """
        print("""
        A-États financiers
        B-Séries temporelles
        Q-Quitter le programme
        """)
        optionMain = str.upper(input("Quelle option choisissez-vous?"))

        if optionMain == 'A':
            return self.menuEF()

        elif optionMain == 'B':
            return self.menuTS()

        elif optionMain == 'Q':
            return sys.exit()

        else:
            return self.createMenu()

    def menuEF(self):
        """
        Fonction qui créer le menu principal pour les états financiers

        :return:
        """
        print("""
        Option non-disponible pour le moment
        """)
        return self.createMenu()

    def menuTS(self):
        """
        Fonction qui créer le menu principal pour les time series

        :return: soi-même, createCsv (pour créer un fichier csv à partir d'une source web),
        workCsv (pour travailler sur un fichier csv),
        createMenu (pour revenir en arrière), sys.exit(pour quitter)
        """
        print("""
        A-Créer un fichier csv
        B-Travailler sur un fichier csv
        R-Revenir en arrière
        Q-Quitter
        """)
        optionTS = str.upper(input("Quelle option choisissez-vous?"))

        if optionTS == 'A':
            return self.createCsv()

        elif optionTS == 'B':
            return self.workCsv()

        elif optionTS == 'R':
            return self.createMenu()

        elif optionTS == 'Q':
            return sys.exit()

        else:
            return self.menuTS()

    def createCsv(self):
        """
        Fonction qui ouvre la classe menu pour les options d'importations web

        :return: soi-même, après avoir ouvert le menu suivant
        """
        iMenu = importMenu()
        iMenu.createImportMenu()
        return self.menuTS()

    def workCsv(self):
        """
        Fonction qui ouvre les menu pour travailler sur nos time series

        :return:
        """
        wMenu = seriesAnalysisMenu()
        wMenu.createAnalysisMenu()
        return self.menuTS()


if __name__ == '__main__':
    menu = mainMenu()
    menu.createMenu()