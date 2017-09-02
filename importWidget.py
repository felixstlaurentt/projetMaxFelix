
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtCore, QtGui
import time
import pickle
import datetime as dt
import pandas_datareader as web
import pandas as pd


class importWidget(QWidget):
    def __init__(self, parent=None):
        super(importWidget, self).__init__(parent)

        self.googleList = []
        self.googleDictionary = {}
        self.loadMenu()

        self.setObjectName("Importation de données")
        self.resize(1400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1400, 800))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 161, 117))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(170, 20, 191, 251))
        self.listWidget.setObjectName("listWidget")
        for item in self.googleList:
            self.listWidget.addItem(item)

        self.listWidget_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(370, 20, 191, 251))
        self.listWidget_2.setObjectName("listWidget_2")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(570, 20, 166, 117))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 310, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(1980, int(time.strftime('%Y')))
        self.spinBox.setValue(2010)
        self.horizontalLayout.addWidget(self.spinBox)

        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setRange(1, 12)
        self.horizontalLayout.addWidget(self.spinBox_2)

        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setRange(1, 31)
        self.horizontalLayout.addWidget(self.spinBox_3)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 280, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 340, 401, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setRange(1980, int(time.strftime('%Y')))
        self.spinBox_4.setValue(int(time.strftime('%Y')))
        self.horizontalLayout_3.addWidget(self.spinBox_4)

        self.spinBox_5 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setRange(1, 12)
        self.spinBox_5.setValue(int(time.strftime('%m')))
        self.horizontalLayout_3.addWidget(self.spinBox_5)

        self.spinBox_6 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setRange(1, 31)
        self.spinBox_6.setValue(int(time.strftime('%d')))
        self.horizontalLayout_3.addWidget(self.spinBox_6)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(160, 420, 401, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(160, 380, 401, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Créer liste"))
        self.pushButton.setText(_translate("Form", "Supprimer Liste"))
        self.pushButton_3.setText(_translate("Form", "Ajouter ticker"))
        self.pushButton_4.setText(_translate("Form", "Supprimer ticker"))
        self.label.setText(_translate("Form", "Date de début:"))
        self.label_4.setText(_translate("Form", "Année"))
        self.label_3.setText(_translate("Form", "Mois"))
        self.label_2.setText(_translate("Form", "Jour"))
        self.label_5.setText(_translate("Form", "Date de fin:    "))
        self.pushButton_5.setText(_translate("Form", "Sauvegarder"))
        self.pushButton_6.setText(_translate("Form", "Créer fichier csv"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Google Finance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Quandl"))

        self.tabWidget.setCurrentIndex(0)
        self.listWidget.currentItemChanged.connect(self.showList)
        self.pushButton.clicked.connect(self.deleteList)
        self.pushButton_2.clicked.connect(self.createList)
        self.pushButton_3.clicked.connect(self.addItem)
        self.pushButton_4.clicked.connect(self.deleteItem)
        self.pushButton_5.clicked.connect(self.saveMenu)
        self.pushButton_6.clicked.connect(self.importData)


    def showList(self):
        """
        Fonction qui imprime dans le tableau 2 les éléments de la liste sélectionnée dans le tableau 1

        :return: Void
        """
        try:
            self.listWidget_2.clear()
            listName = self.listWidget.currentItem().text()
            for item in self.googleDictionary[listName]:
                self.listWidget_2.addItem(item)
        except:
            print("Nouvelle liste créée")

    def createList(self):
        """
        Fonction qui créer le tableau 1 à partir de self.googleList

        :return: Void
        """
        try:
            if self.lineEdit.text() != '':
                self.googleList.append(self.lineEdit.text())
                self.googleDictionary[self.lineEdit.text()] = []
                self.listWidget.clear()
                for item in self.googleList:
                    self.listWidget.addItem(item)
                print('Nouvelle liste créée')
        except:
            print("Erreur de création de liste")

    def deleteList(self):
        """
        Fonction qui supprime la liste selectionnée lorsqu'on pèse sur le bouton "supprimer"

        :return: Void
        """
        try:
            self.googleList.remove(self.listWidget.currentItem().text())
            buffer = {}
            for item in self.googleList:
                buffer[item] = self.googleDictionary[item]
            self.googleDictionary = buffer
            self.listWidget.clear()
            for item in self.googleList:
                self.listWidget.addItem(item)
        except:
            print("Erreur de suppression de liste")

    def addItem(self):
        """
        Fonction qui ajoute un élément à la liste de tickers lorsqu'on pèse sur le bouton "ajouter"

        :return: Void
        """
        try:
            self.listWidget_2.addItem(self.lineEdit_2.text())
            self.googleDictionary[self.listWidget.currentItem().text()].append(self.lineEdit_2.text())
        except:
            print("Erreur d'ajout")

    def deleteItem(self):
        """Fonction qui supprime un élément à la liste de tickers lorsqu'on pèse sur le bouton "supprimer"

        :return: Void
        """
        try:
            self.googleDictionary[self.listWidget.currentItem().text()].remove(self.listWidget_2.currentItem().text())
            self.listWidget_2.clear()
            listName = self.listWidget.currentItem().text()
            for item in self.googleDictionary[listName]:
                self.listWidget_2.addItem(item)
        except:
            print("Erreur de suppression")

    def saveMenu(self):
        """
        Fonction qui sauvegarde la googleList et le googleDictionary. Ce qui sauvegarde toutes les données même si l'on
        ferme le programme.

        :return: Void
        """
        pickle_out = open('importWidget_googleList.pickle', 'wb')
        pickle.dump(self.googleList, pickle_out)
        pickle_out.close()
        pickle_out = open('importWidget_googleDictionary.pickle', 'wb')
        pickle.dump(self.googleDictionary, pickle_out)
        pickle_out.close()

        print('workspace sauvegardé')

    def loadMenu(self):
        """
        Fonction qui remet en place les objets googleList et googleDictionary à l'état ou ils se trouvaient à la
        dernière sauvegarde.

        :return: Void
        """
        try:
            pickle_in = open('importWidget_googleList.pickle', 'rb')
            self.googleList = pickle.load(pickle_in)
            pickle_in = open('importWidget_googleDictionary.pickle', 'rb')
            self.googleDictionary = pickle.load(pickle_in)
            print('workspace chargé depuis le pickle')
        except:
            print("Première ouverture")

    def importData(self):
        """
        Fonction qui va importer les données dans un fichier csv
         :return: Void
        """
        tickerList = self.googleDictionary[self.listWidget.currentItem().text()]
        start = dt.datetime(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value())
        end = dt.datetime(self.spinBox_4.value(), self.spinBox_5.value(), self.spinBox_6.value())
        print(tickerList)
        dataList = ['Open', 'High', 'Low', 'Close', 'Volume']
        df_main = pd.DataFrame()
        for ticker in tickerList:
            try:
                df = web.DataReader(ticker, "google", start, end)
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

        csvName = self.lineEdit_3.text()
        df_main.to_csv(csvName + '.csv')

        self.fileCreatedBox()

    def fileCreatedBox(self):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Fichier créé sous le nom: ' + self.lineEdit_3.text())
            msgBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = importWidget()
    main.show()

    sys.exit(app.exec_())