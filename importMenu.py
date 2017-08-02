import sys
from tSeries import tSeries
import pickle
import datetime as dt
import pandas_datareader as web
import pandas as pd

"""
Classe qui constitue le menu pour les importations

Attributes:
    newList: nouvelle liste de ticker qui n'est pas encore enregistrée
    currentList: La liste avec laquelle nous allons travailler
    googleLists: dictionnaire qui contient toutes les listes de tickers qui ont été enregistrées pour importation via google finance
    quandlLists: dictionnaire qui contient toutes les listes de tickers qui ont été enregistrées pour importation via quandl
    benchmark: string qui contient benchmark qui sera utilisé avec la liste à importer
    start: objet datetime qui contient la date de début pour l'importation
    end: objet datetime qui contient la date de fin pour l'importation
"""


class importMenu():

    def __init__(self):
        """
            Constructeur de la classe importMenu
        """
        self.newList = []
        self.currentList = []
        self.googleLists = {}
        self.quandlLists = {}
        self.__start = dt.datetime(2000, 1, 1)
        self.__end = dt.datetime(2017, 1, 2)
        try:
            self.loadFromPickle()
        except:
            print('new')

    def createImportMenu(self):
        """
        Fonction qui créer le menu principal d'importation

        :return: menu suivant, lui-même, 0 (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        print("""
        A-Importer via Google Finance
        B-Importer via Quandl
        R-Revenir en arrière
        Q-Quitter
        """)
        optionImport = str.upper(input("Quelle option choisissez-vous?"))

        if optionImport == 'A':
            return self.createGoogleMenu()

        elif optionImport == 'B':
            return self.createQuandlMenu()

        elif optionImport == 'R':
            return 0

        elif optionImport == 'Q':
            return sys.exit()

        else:
            return self.createImportMenu()

    def createGoogleMenu(self):
        """
        Fonction qui créer le menu d'importation via google finance

        :return: menu suivant, lui-même, 0 (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        print("""
        A-Créer une nouvelle liste
        B-Créer votre fichier csv
        C-Voir listes existantes
        D-Supprimer une liste
        R-Revenir en arrière
        Q-Quitter
        """)
        optionGoogle = str.upper(input('Quelle option choisissez-vous?'))

        if optionGoogle == 'A':
            self.newList = []
            return self.createGoogleList()

        elif optionGoogle == 'B':
            print(self.googleLists)
            liste = str(input('Quelle liste voulez-vous importer en CSV?'))
            if liste in self.googleLists:
                self.currentList = self.googleLists[liste]
                return self.createCSV()
            else:
                print("La liste demandé n'existe pas")
                return self.createGoogleMenu()

        elif optionGoogle == 'C':
            print(self.googleLists)
            return self.createGoogleMenu()

        elif optionGoogle == 'D':
            self.deleteGoogleList()
            return self.createGoogleMenu()

        elif optionGoogle == 'R':
            return self.createImportMenu()

        elif optionGoogle == 'Q':
            return sys.exit()

        else:
            return self.createGoogleMenu()

    def createGoogleList(self):
        """
        Fonction qui créer le menu pour créer une liste de tickers pour importation via google finance.
        On ne peut pas aller plus loin par ce chemin dans les menus

        :return: lui-même, 0 (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        print("Votre liste: ", self.newList)
        print("""
        A-Ajouter un ticker à la liste
        B-Supprimer un ticker de la liste
        C-Ajouter une liste complète
        D-Sauvegarder la liste
        R-Revenir en arrière
        Q-Quitter
        """)
        optionList = str.upper(input('Quelle option choisissez-vous?'))

        if optionList == 'A':
            self.addTicker()
            return self.createGoogleList()

        elif optionList == 'B':
            self.deleteTicker()
            return self.createGoogleList()

        elif optionList == 'C':
            self.addList()
            return self.createGoogleList()

        elif optionList == 'D':
            name = str(input('Quel nom voulez-vous donner à votre liste?'))
            self.googleLists[name] = self.newList
            self.saveToPickle()
            return self.createGoogleList()

        elif optionList == 'R':
            return self.createGoogleMenu()

        elif optionList == 'Q':
            return sys.exit()

        else:
            return self.createGoogleList()

    def createCSV(self):
        """
        Fonction qui créer le menu pour créer un fichier csv avec les éléments importés via google finance.

        :param liste: liste de ticker que l'on va importer
        :return: inconnu
        """

        print('date de début: ', self.__start)
        print('date de fin: ', self.__end)
        print("""
        A-Modifier les dates
        B-Importer les données dans un csv
        R-Revenir en arrière
        Q-Quitter
        """)
        optionCSV = str.upper(input('Quelle option choisissez-vous?'))

        if optionCSV == 'A':
            return self.modifyDatesMenu()

        elif optionCSV == 'B':
            return self.importData()

        elif optionCSV == 'R':
            return self.createGoogleMenu()

        elif optionCSV == 'Q':
            return sys.exit()

        else:
            return self.createCSV()

    def modifyDatesMenu(self):
        """
        Fonction qui lance le menu pour modifier les dates

        :return: lui-même (pour continuer dans le menu, self.createCSV (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        print('Date de départ: ', self.__start)
        print('Date de fin: ', self.__end)
        print("""
        A-modifier la date de départ
        B-Modifier la date de fin
        R-Revenir en arrière
        Q-Quitter
        """)
        optionMod = str.upper(input('Quelle option choisissez-vous?'))

        if optionMod == 'A':
            self.modifyStartDate()
            return self.modifyDatesMenu()

        elif optionMod == 'B':
            self.modifyEndDate()
            return self.modifyDatesMenu()

        elif optionMod == 'R':
            return self.createCSV()

        elif optionMod == 'Q':
            return sys.exit()

        else:
            return self.modifyDatesMenu()

    def modifyStartDate(self):
        """
        Fonction qui lance le menu pour modifier la date de départ

        :return: Void
        """
        print('Nouvelle date de départ: ')
        annee = int(input("Entrez l'année de départ: "))
        mois = int(input("Entrez le mois de départ: "))
        jour = int(input("Entrez le jour de départ"))

        self.setStart(annee, mois, jour)
        self.saveToPickle()

    def modifyEndDate(self):
        """
        Fonction qui lance le menu pour modifier la date de fin

        :return: Void
        """
        print('Nouvelle date de fin: ')
        annee = int(input("Entrez l'année de fin: "))
        mois = int(input("Entrez le mois de fin: "))
        jour = int(input("Entrez le jour de fin"))

        self.setEnd(annee, mois, jour)
        self.saveToPickle()

    def setStart(self, annee, mois, jour):
        """
        Fonction qui modifie la date de départ

        :param annee: année à modifier
        :param mois: mois à modifier
        :param jour: jour à modifier
        :return:  Void
        """
        if self.verifyDate(annee, mois, jour):
            self.__start = dt.datetime(annee, mois, jour)
        else:
            print('Erreur de date')

    def setEnd(self, annee, mois, jour):
        """
        Fonction qui modifie la date de fin

        :param annee: année à modifier
        :param mois: mois à modifier
        :param jour: jour à modifier
        :return:  Void
        """
        if self.verifyDate(annee, mois, jour):
            self.__end = dt.datetime(annee, mois, jour)
        else:
            print('Erreur de date')

    def verifyDate(self, annee, mois, jour):
        """
        Fonction qui vérifie si la date entrée est une date valide

        :param annee: année rentrée
        :param mois: mois rentré
        :param jour: jour rentré
        :return: Retourne True si la date est valide, False autrement
        """
        if annee <= 2017 and annee >= 1960:
            if mois <= 12 and mois >= 0:
                if jour <= 31 and jour >= 0:
                    return True
        return False

    def importData(self):
        """
        Fonction qui va importer les données dans un fichier csv

        :return: self.createImportMenu
        """
        tickerList = self.currentList
        print(tickerList)
        dataList = ['Open', 'High', 'Low', 'Close', 'Volume']

        df_main = pd.DataFrame()

        for ticker in tickerList:
            try:
                df = web.DataReader(ticker, "google", self.__start, self.__end)
                df.fillna(0, inplace=True)
            except:
                print("Le ticker ", ticker, "n'a pas fonctionné")
                continue

            newTick = ''
            count = 0
            for caracter in ticker:
                if caracter == ':':
                    count = 1
                if count == 1 and caracter != ':':
                    newTick += caracter
            print(newTick)
            print(df.head())

            for data in dataList:
                df.rename(columns={data: newTick + '_' + data}, inplace=True)

            if df_main.empty:
                df_main = df
            else:
                df_main = df_main.join(df, how='outer')

        df_main.fillna(0, inplace=True)

        csvName = str(input("Quel nom voulez-vous donner à votre fichier csv? (ne pas mettre l'extension)"))
        df_main.to_csv(csvName + '.csv')

        return self.createImportMenu()


    def deleteGoogleList(self):
        """
        Fonction que l'on utilise pour supprimer une liste de tickers google qui a auparavant été sauvegardée

        :return:  Void
        """
        list = str(input('Quelle liste voulez-vous supprimer?'))
        if list in self.googleLists:
            del self.googleLists[list]
            self.saveToPickle()
        else:
            print("La liste demandé n'existe pas")

    def createQuandlList(self):
        """
        Fonction qui créer le menu pour créer une liste de tickers pour importation via quandl.
        On ne peut pas aller plus loin par ce chemin dans les menus

        :return: lui-même, 0 (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        pass

    def addTicker(self):
        """
        Fonction pour ajouter un ticker à newList (liste de tickers qui n'a pas encore été enregistrée)

        :return: Void
        """
        newTicker = str(input('Quel ticker voulez-vous ajouter?'))
        self.newList.append(newTicker)

    def deleteTicker(self):
        """
        Fonction pour supprimer un ticker à newList (liste de tickers qui n'a pas encore été enregistrée)

        :return: Void
        """
        delTicker = input('Quel ticker voulez-vous supprimer?')
        if delTicker in self.newList:
            self.newList.remove(delTicker)
        else:
            print("Ce ticker n'est pas dans votre liste")

    def addList(self):
        """
        Fonction pour ajouter une liste complète à notre liste

        :return: Void
        """
        liste = list(input('Entrez votre liste: '))

        open = False
        newTick = ''
        newList = []
        for caracter in liste:
            if open == False and caracter == "'":
                open = True
                continue
            if open == True:
                if caracter != "'":
                    newTick += caracter
                else:
                    open = False
                    newList.append(newTick)
                    newTick = ''
        for ticker in newList:
            self.newList.append(ticker)

    def createQuandlMenu(self):
        """
        Fonction qui créer le menu d'importation via quandl.

        :return: menu suivant, lui-même, 0 (pour revenir en arrière) ou sys.exit (pour quitter)
        """
        print('Option non-disponible pour le moment')
        return 0

    def saveToPickle(self):
        """
        Fonction qui sauvegarde l'objet importMenu en entier. Ce qui sauvegarde toutes les données même si l'on ferme le programme

        :return: Void
        """
        pickle_out = open('importMenu.pickle', 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        print('workspace sauvegardé')

    def loadFromPickle(self):
        """
        Fonction qui remet en place l'objet importMenu à l'état ou il se trouvait à la dernière sauvegarde

        :return: Void
        """
        pickle_in = open('importMenu.pickle', 'rb')
        buffer = pickle.load(pickle_in)
        self.googleLists = buffer.googleLists
        self.quandlLists = buffer.quandlLists
        print('workspace chargé depuis le pickle')