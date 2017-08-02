import sys
from importMenu import importMenu


class mainMenu():

    def __init__(self):
        pass

    def createMenu(self):

        print("""
        A-États financiers
        B-Séries temporelles
        Q-Quitter le programme
        """)
        optionMain = str.upper(input("Quelle option choisissez-vous?"))

        while optionMain != 'Q':

            if optionMain == 'A':
                return self.menuEF()

            elif optionMain == 'B':
                return self.menuTS()

            elif optionMain == 'Q':
                sys.exit()
            else:
                print("""
                A-États financiers
                B-Séries temporelles
                Q-Quitter le programme
                """)
                optionMain = str.upper(input("Quelle option choisissez-vous?"))

    def menuEF(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.createMenu()

    def menuTS(self):
        print("""
        A-Créer un fichier csv
        B-Travailler sur un fichier csv
        R-Revenir en arrière
        Q-Quitter
        """)
        optionTS = str.upper(input("Quelle option choisissez-vous?"))

        while optionTS != 'Q':

            if optionTS == 'A':
                return self.createCsv()

            elif optionTS == 'B':
                return self.workCsv()

            elif optionTS == 'R':
                return self.createMenu()

            elif optionTS == 'Q':
                sys.exit()

            else:
                print("""
                A-Créer un fichier csv
                B-Travailler sur un fichier csv
                R-Revenir en arrière
                Q-Quitter
                """)
                optionTS = str.upper(input("Quelle option choisissez-vous?"))

    def createCsv(self):
        iMenu = importMenu()
        iMenu.createImportMenu()
        return self.menuTS()

    def workCsv(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.menuTS()


if __name__ == '__main__':
    menu = mainMenu()
    menu.createMenu()