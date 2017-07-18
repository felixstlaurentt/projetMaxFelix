import sys
from googleMenu import googleMenu


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
        A-Importer via Google finance
        B-Importer via Yahoo finance
        C-Importer via Quandl
        D-Importer fichier csv
        E-Importer fichier excel
        R-Revenir en arrière
        Q-Quitter
        """)
        optionTS = str.upper(input("Quelle option choisissez-vous?"))

        while optionTS != 'Q':

            if optionTS == 'A':
                return self.importGoogle()

            elif optionTS == 'B':
                return self.importYahoo()

            elif optionTS == 'C':
                return self.importQuandl()

            elif optionTS == 'D':
                return self.importCsv()

            elif optionTS == 'E':
                return self.importExcel()

            elif optionTS == 'R':
                return self.createMenu()

            elif optionTS == 'Q':
                sys.exit()

            else:
                print("""
                A-Importer via Google finance
                B-Importer via Yahoo finance
                C-Importer via Quandl
                D-Importer fichier csv
                E-Importer fichier excel
                R-Revenir en arrière
                Q-Quitter
                """)
                optionTS = str.upper(input("Quelle option choisissez-vous?"))

    def importGoogle(self):
        gMenu = googleMenu()
        gMenu.createGoogleMenu()
        return self.menuTS()

    def importYahoo(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.menuTS()

    def importQuandl(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.menuTS()

    def importCsv(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.menuTS()

    def importExcel(self):
        print("""
        Option non-disponible pour le moment
        """)
        return self.menuTS()


if __name__ == '__main__':
    menu = mainMenu()
    menu.createMenu()