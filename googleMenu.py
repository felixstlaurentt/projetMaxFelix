import sys
from googleTseries import googleTseries


class googleMenu():

    def __init__(self):
        self.googleSeries = googleTseries()

    def googleMainMenu(self):
        print("""
        A-Ajouter un titre à votre liste
        B-Supprimer un titre de votre liste
        C-Imprimer votre liste
        D-importer une liste
        R-Revenir en arrière
        Q-Quitter
        """)
        optionGoogle = str.upper(input("Quelle option choisissez-vous?"))

        while optionGoogle != 'Q':

            if optionGoogle == 'A':
                newTicker = input('Quelle ticker voulez-vous ajouter?')
                self.googleSeries.ajouterTicker(newTicker)
                print(self.googleSeries.tickers)
                return self.googleMainMenu()

            elif optionGoogle == 'B':
                print("""
                Option non-disponible pour le moment
                """)
                return self.googleMainMenu()

            elif optionGoogle == 'C':
                print("""
                Option non-disponible pour le moment
                """)
                return self.googleMainMenu()

            elif optionGoogle == 'D':
                print("""
                Option non-disponible pour le moment
                """)
                return self.googleMainMenu()

            elif optionGoogle == 'R':
                print("""
                Option non-disponible pour le moment
                """)
                return self.googleMainMenu()

            elif optionGoogle == 'Q':
                sys.exit()

            else:
                print("""
                A-Ajouter un titre à votre liste
                B-Supprimer un titre de votre liste
                C-Imprimer votre liste
                D-importer une liste
                R-Revenir en arrière
                Q-Quitter
                """)
                optionGoogle = str.upper(input("Quelle option choisissez-vous?"))