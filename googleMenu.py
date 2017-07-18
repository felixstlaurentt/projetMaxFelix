import sys
from googleTseries import googleTseries


class googleMenu():

    def __init__(self):
        self.googleSeries = googleTseries()

    def createGoogleMenu(self):
        print("""
        A-Ajouter un titre à votre liste
        B-Supprimer un titre de votre liste
        C-Imprimer votre liste
        D-Charger une liste
        E-Sauvegarder une liste
        F-Travailler avec votre liste
        R-Revenir en arrière
        Q-Quitter
        """)
        optionGoogle = str.upper(input("Quelle option choisissez-vous?"))

        while optionGoogle != 'Q':

            if optionGoogle == 'A':
                newTicker = input('Quel ticker voulez-vous ajouter?')
                self.googleSeries.ajouterTicker(newTicker)
                print(self.googleSeries.tickers)
                return self.createGoogleMenu()

            elif optionGoogle == 'B':
                delTicker = input('Quel ticker vouluez-vous supprimer?')
                self.googleSeries.supprimerTicker(delTicker)
                print(self.googleSeries.tickers)
                return self.createGoogleMenu()

            elif optionGoogle == 'C':
                print(self.googleSeries.tickers)
                return self.createGoogleMenu()

            elif optionGoogle == 'D':
                print("""
                Option non-disponible pour le moment
                """)
                return self.createGoogleMenu()

            elif optionGoogle == 'E':
                print("""
                Option non-disponible pour le moment
                """)
                return self.createGoogleMenu()

            elif optionGoogle == 'F':
                return self.workMenu()

            elif optionGoogle == 'R':
                return 0

            elif optionGoogle == 'Q':
                sys.exit()

            else:
                print("""
                A-Ajouter un titre à votre liste
                B-Supprimer un titre de votre liste
                C-Imprimer votre liste
                D-Charger une liste
                E-Sauvegarder une liste
                F-Travailler avec votre liste
                R-Revenir en arrière
                Q-Quitter
                """)
                optionGoogle = str.upper(input("Quelle option choisissez-vous?"))

    def workMenu(self):
        print("""
        A-Importer les time series de votre liste
        B-Calculer les rendements historiques
        C-Calculer les volatilités historiques
        D-Sauvegarder votre workspace
        E-Charger un workspace
        R-Revenir en arrière
        Q-Quitter
        """)
        optionWork = str.upper(input("Quelle option choisissez-vous?"))

        while optionWork != 'Q':

            if optionWork == 'A':
                print("""
                Option non-disponible pour le moment
                """)
                return self.workMenu()

            if optionWork == 'B':
                print("""
                Option non-disponible pour le moment
                """)
                return self.workMenu()

            if optionWork == 'C':
                print("""
                Option non-disponible pour le moment
                """)
                return self.workMenu()

            if optionWork == 'D':
                print("""
                Option non-disponible pour le moment
                """)
                return self.workMenu()

            if optionWork == 'E':
                print("""
                Option non-disponible pour le moment
                """)
                return self.workMenu()

            if optionWork == 'R':
                return self.createGoogleMenu()

            if optionWork == 'Q':
                sys.exit()
