import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtCore, QtGui
import time
import pickle
import datetime as dt
import pandas_datareader as web
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from tSeries import tSeries
from matplotlib.finance import candlestick_ohlc
import random


class ptfWidget(QWidget):

    def __init__(self, parent=None):
        super(ptfWidget, self).__init__(parent)
        self.csvPath = ''
        self.csvFileOriginal = pd.DataFrame()
        self.csvFileModified = pd.DataFrame()
        self.debut = dt.datetime(1990, 1, 1)
        self.fin = dt.datetime.today()
        self.open = False
        self.close = False
        self.high = False
        self.low = False
        self.volume = False
        self.benchmark = False
        self.toModify = False
        self.source = ''
        self.noRisk = 0.02
        self.seriesList = []
        self.seriesDictionary = {}
        self.corrMatrix = np.array([])
        self.index = 0
        self.rendMatrix = pd.DataFrame()
        self.simulation = pd.DataFrame()
        self.cov = pd.DataFrame()
        self.mean = pd.DataFrame()
        self.results = np.array([])
        self.num_simul = 100
        self.max_sharpe = pd.DataFrame()
        self.min_var = pd.DataFrame()

        self.setObjectName("Gestion de portefeuille")
        self.resize(1400, 800)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(170, 10, 1400, 800))  #631, 581
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.graph = ptfGraphWidget(self.frame)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setText("Date de début: \n")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("Date de fin: \n")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Gestion de portefeuille"))
        self.pushButton.setText(_translate("Form", "Charger"))
        self.label.setText(_translate("Form", "fichier csv: "))
        self.pushButton_2.setText(_translate("Form", "Corrélations"))
        self.pushButton_3.setText(_translate("Form", "Time graph"))
        self.pushButton_4.setText(_translate("Form", "Frontière\n"
                                                    " efficiente"))
        self.pushButton_5.setText(_translate("Form", "Statistiques"))
        self.pushButton_6.setText(_translate("Form", "Options"))

        self.pushButton.clicked.connect(self.openLoadWidget)
        self.pushButton_2.clicked.connect(self.graph.corrPlot)
        self.pushButton_3.clicked.connect(self.graph.ohlcPlot)
        self.pushButton_4.clicked.connect(self.graph.frontierPlot)
        self.pushButton_5.clicked.connect(self.openStatsTable)
        self.pushButton_6.clicked.connect(self.openOptionsWidget)

    def openLoadWidget(self):
        """
        Fonction qui ouvre la fenêtre pour charger un fichier csv

        :return: Void
        """
        print(self.debut)
        print(self.fin)
        load = ptfLoadWidget()
        load.exec()
        if load.exec():
            self.csvPath = load.csvPath
            self.open = load.open
            self.close = load.close
            self.high = load.high
            self.low = load.low
            self.volume = load.volume
            self.benchmark = load.benchmark
            self.noRisk = load.noRisk
            self.source = load.source
            self.label_2.setText(self.csvPath.split('/')[-1])
            self.seriesList = []
            self.seriesDictionary = {}
            self.format()
            self.calcStats()
            self.graph.combo_1.clear()
            self.graph.combo_2.clear()
            self.graph.combo_1.addItems(self.seriesList)
            self.graph.combo_2.addItem('')
            self.graph.combo_2.addItems(self.seriesList)

    def openStatsTable(self):
        """
        Fonction qui ouvre la fenêtre pour afficher les statistiques

        :return: Void
        """
        load = statsWidget(len(self.seriesList))
        load.seriesList = self.seriesList
        load.seriesDict = self.seriesDictionary
        load.imprimerClassement()
        load.exec()

    def openOptionsWidget(self):
        """
        Fonction qui ouvre la fenêtre pour changer les options

        :return: Void
        """
        load = optionsWidget()
        load.noRisk = self.noRisk
        load.num_simul = self.num_simul

        if self.csvFileOriginal.empty:
            load.debut = dt.datetime(1990, 1, 1)
            fin = dt.datetime.today().strftime('%Y-%m-%d')
            annee, mois, jour = fin.split('-')
            load.fin = dt.datetime(int(annee), int(mois), int(jour))
        else:
            annee, mois, jour = self.csvFileOriginal['Date'][0].split('-')
            load.debut = dt.datetime(int(annee), int(mois), int(jour))
            annee, mois, jour = self.csvFileOriginal['Date'][len(self.csvFileOriginal) - 1].split('-')
            load.fin = dt.datetime(int(annee), int(mois), int(jour))

        load.spinBox_2.setRange(load.debut.year, load.fin.year)
        load.spinBox_2.setValue(load.debut.year)
        load.spinBox_3.setValue(load.debut.month)
        load.spinBox_4.setValue(load.debut.day)
        load.spinBox_5.setRange(load.debut.year, load.fin.year)
        load.spinBox_5.setValue(load.fin.year)
        load.spinBox_6.setValue(load.fin.month)
        load.spinBox_7.setValue(load.fin.day)

        load.exec()
        if load.exec():
            self.noRisk = load.noRisk
            self.num_simul = load.num_simul

            if load.debut > load.fin:
                erreur = QtWidgets.QMessageBox()
                erreur.setText('Erreur de dates')
                erreur.exec()
            else:
                self.debut = load.debut
                self.fin = load.fin

            if not self.csvFileOriginal.empty:
                self.seriesList = []
                self.seriesDictionary = {}
                self.format()
                self.calcStats()

    def format(self):
        """
        Fonction qui va formater le csv pour créer un tSeries pour chaque ticker qu'il contient et lui insérer leur
        propre DataFrame dans chaque objet

        :return: Void
        """
        self.seriesDictionary = {}
        self.csvFileOriginal = pd.read_csv(self.csvPath.split('/')[-1])

        index_debut = 0
        for date in self.csvFileOriginal['Date']:
            annee, mois, jour = date.split('-')
            new_date = dt.datetime(int(annee), int(mois), int(jour))
            print(new_date)
            if self.debut <= new_date:
                self.debut = new_date
                break
            index_debut += 1

        print(self.csvFileOriginal)
        print(self.fin)
        last_date = self.csvFileOriginal['Date'][(len(self.csvFileOriginal)) - 1]
        annee, mois, jour = last_date.split('-')
        last_date = dt.datetime(int(annee), int(mois), int(jour))
        index_fin = 0
        if self.fin >= last_date:
            self.fin = last_date
            index_fin = len(self.csvFileOriginal) - 1
        else:
            for date in self.csvFileOriginal['Date']:
                annee, mois, jour = date.split('-')
                new_date = dt.datetime(int(annee), int(mois), int(jour))
                # print(new_date)
                if self.fin <= new_date:
                    self.fin = new_date
                    break
                index_fin += 1

        self.csvFileModified = pd.DataFrame(self.csvFileOriginal[index_debut:index_fin])

        buffer_df = pd.DataFrame(self.csvFileModified['Date'])
        new_df = pd.DataFrame(buffer_df)
        new_df.set_index('Date', inplace=True)
        self.csvFileModified.set_index('Date', inplace=True)

        liste = list(self.csvFileModified)
        ticker2 = liste[0].split('_')[0]

        for item in liste:
            ticker1 = item.split('_')[0]
            data = item.split('_')[1]

            if ticker1 == ticker2:
                buffer_item = pd.DataFrame(self.csvFileModified [item])
                new_df = new_df.join(buffer_item, how='outer')
                new_df.rename(columns={item: data}, inplace=True)
            else:
                self.seriesList.append(ticker2)
                self.seriesDictionary[ticker2] = tSeries(new_df, self.noRisk)
                ticker2 = ticker1
                new_df = pd.DataFrame(buffer_df)
                new_df = new_df.join(self.csvFileModified[item])
                new_df.rename(columns={item: data}, inplace=True)

        self.seriesList.append(ticker2)
        self.seriesDictionary[ticker2] = tSeries(new_df, self.noRisk)

        for ticker in self.seriesList:
            if self.benchmark:
                self.seriesDictionary[ticker].setBenchmark(pd.DataFrame(self.seriesDictionary[self.seriesList[0]].frame['Close']))

        self.graph.liste = self.seriesList
        self.graph.dict = self.seriesDictionary
        self.graph.noRisk = self.noRisk
        self.graph.ohlcPlot()

        self.label_3.setText("Date de début: \n" + str(self.debut))
        self.label_4.setText("Date de fin: \n" + str(self.fin))

    def calcStats(self):
        """
        Fonction qui calcules les statistiques de chaque ticker et ceux du portfolio

        :return: Void
        """
        for ticker in self.seriesList:
            self.seriesDictionary[ticker].calcStats()

            self.seriesDictionary[ticker].capm = self.noRisk + (self.seriesDictionary[ticker].beta *
                                                ((self.seriesDictionary[self.seriesList[0]].meanRend * 252) - self.noRisk))
        self.rendMatrix = pd.DataFrame()
        for item in self.seriesList:
            rend = pd.DataFrame(self.seriesDictionary[item].rend)
            rend.rename(columns={'Close': item}, inplace=True)
            if self.rendMatrix.empty:
                self.rendMatrix = pd.DataFrame(rend)
            else:
                self.rendMatrix = self.rendMatrix.join(rend, how='outer')

        self.mean = self.rendMatrix.mean()
        self.cov = self.rendMatrix.cov()

        if self.benchmark:
            effListe = self.seriesList[1:]
            columns = list(self.rendMatrix)
            effRendMatrix = pd.DataFrame(self.rendMatrix)
            effRendMatrix.drop(columns[0], 1, inplace=True)
            effMean = effRendMatrix.mean()
            effCov = effRendMatrix.cov()
        else:
            effListe = self.seriesList
            effRendMatrix = self.rendMatrix
            effMean = effRendMatrix.mean()
            effCov = effRendMatrix.cov()

        self.results = np.zeros((4 + len(effListe) - 1, self.num_simul))

        for i in range(self.num_simul):
            weights = np.random.random(len(effListe))
            weights /= np.sum(weights)

            port_return = np.sum(effMean * weights) * 252
            port_std = np.sqrt(np.dot(weights.T, np.dot(effCov, weights))) * np.sqrt(252)

            self.results[0, i] = port_return
            self.results[1, i] = port_std
            self.results[2, i] = (port_return - self.noRisk) / port_std

            for j in range(len(weights)):
                self.results[j + 3, i] = weights[j]

        columns_name = ['Returns', 'Std_Dev', 'Sharpe']
        for i in effListe:
            columns_name.append(i)

        self.results = pd.DataFrame(self.results.T, columns=columns_name)

        self.max_sharpe = self.results.iloc[self.results['Sharpe'].idxmax()]
        self.min_var = self.results.iloc[self.results['Std_Dev'].idxmin()]

        self.graph.rendMatrix = self.rendMatrix
        self.graph.results = self.results
        self.graph.max_sharpe = self.max_sharpe
        self.graph.min_var = self.min_var

class ptfGraphWidget(QWidget):

    def __init__(self, parent=None):
        super(ptfGraphWidget, self).__init__(parent)

        self.liste = []
        self.dict = {}
        self.index = 0
        self.index_2 = 0
        self.rendMatrix = pd.DataFrame()
        self.max_sharpe = pd.DataFrame()
        self.results = pd.DataFrame()
        self.min_var = pd.DataFrame()
        self.noRisk = 0.02

        self.figure = plt.figure(figsize=(12, 6))

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.buttonPrevious = QPushButton('Previous')
        self.buttonNext = QPushButton('Next')
        self.combo_1 = QtWidgets.QComboBox()
        self.combo_2 = QtWidgets.QComboBox()
        self.radioOhlc = QtWidgets.QRadioButton('OHLC       ')
        self.radioOhlc.setChecked(True)
        self.radioClose = QtWidgets.QRadioButton('Close')

        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_1)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.horizontalLayout_1.addWidget(self.combo_1)
        self.horizontalLayout_1.addWidget(self.combo_2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.buttonPrevious)
        self.horizontalLayout_2.addWidget(self.buttonNext)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.radioOhlc)
        self.horizontalLayout_3.addWidget(self.radioClose)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.canvas)
        vlayout.addWidget(self.horizontalLayoutWidget_1)
        vlayout.addWidget(self.horizontalLayoutWidget_2)
        vlayout.addWidget(self.horizontalLayoutWidget_3)
        self.setLayout(vlayout)

        self.buttonPrevious.clicked.connect(self.previous)
        self.buttonNext.clicked.connect(self.next)
        self.radioOhlc.clicked.connect(self.ohlcPlot)
        self.radioClose.clicked.connect(self.ohlcPlot)
        self.combo_1.currentIndexChanged.connect(self.combo1Graph)
        self.combo_2.currentIndexChanged.connect(self.combo2Graph)

        self.ohlcPlot()

    def next(self):
        if self.index == len(self.liste) - 1:
            self.index = 0
        else:
            self.index += 1
        print(self.index)
        self.ohlcPlot()

    def previous(self):
        if self.index != 0:
            self.index -= 1
        print(self.index)
        self.ohlcPlot()

    def combo1Graph(self):
        if self.combo_1.currentIndex() != self.index:
            self.index = self.combo_1.currentIndex()
            self.ohlcPlot()

    def combo2Graph(self):
        if self.combo_2.currentIndex() != self.index_2:
            self.index_2 = self.combo_2.currentIndex()
            self.ohlcPlot()

    def ohlcPlot(self):
        print('salut2')
        self.figure.clear()
        plt.style.use("ggplot")

        if len(self.liste) != 0:
            frame = pd.DataFrame(self.dict[self.liste[self.index]].frame)
            open = frame['Open']
            close = frame['Close']
            high = frame['High']
            low = frame['Low']
            volume = frame['Volume']
        else:
            return 0
        if self.index_2 != 0:
            frame_2 = pd.DataFrame(self.dict[self.liste[self.index_2 - 1]].frame)
            close_2 = frame_2['Close']

        new_date = list(range(1, len(close) + 1))

        if self.radioOhlc.isChecked():

            i = 0
            ohlc_data = []
            while i < len(new_date):
                stats_1_day = new_date[i], open[i], high[i], low[i], close[i]
                ohlc_data.append(stats_1_day)
                i += 1

            ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
            plt.title(self.liste[self.index])
            candlestick_ohlc(ax1, ohlc_data, colorup='g', colordown='r')
            if self.index_2 > 0:
                ax2 = ax1.twinx()
                ax2.plot(new_date, close_2, color='b')

        elif self.radioClose.isChecked():
            ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
            plt.title(self.liste[self.index])
            ax1.plot(new_date, close)
            if self.index_2 > 0:
                ax2 = ax1.twinx()
                ax2.plot(new_date, close_2, color='b')

        ax3 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)
        ax3.bar(new_date, volume, 0.5, color='g')

        # refresh canvas
        self.canvas.draw()

    def corrPlot(self):

        self.figure.clear()

        df_corr = self.rendMatrix.corr()
        data1 = df_corr.values

        ax1 = self.figure.add_subplot(111)
        heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
        self.figure.colorbar(heatmap1)

        ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
        ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
        ax1.invert_yaxis()
        ax1.xaxis.tick_top()
        column_labels = df_corr.columns
        row_labels = df_corr.index
        ax1.set_xticklabels(column_labels)
        ax1.set_yticklabels(row_labels)
        plt.xticks(rotation=90)
        heatmap1.set_clim(-1, 1)
        plt.tight_layout()

        self.canvas.draw()

    def frontierPlot(self):

        self.figure.clear()

        if self.results.empty:
            return 0
        else:
            plt.scatter(self.results.Std_Dev, self.results.Returns, c=self.results.Sharpe, cmap='RdYlBu')
            plt.xlabel('Volatility')
            plt.ylabel('Returns')
            plt.colorbar()
            plt.scatter(self.max_sharpe[1], self.max_sharpe[0], marker=(5, 1, 0), color='r', s=250)
            plt.scatter(self.min_var[1], self.min_var[0], marker=(5, 1, 0), color='g', s=250)
            plt.plot([0, self.max_sharpe[1]], [self.noRisk, self.max_sharpe[0]])

        self.canvas.draw()

class ptfLoadWidget(QDialog):

    def __init__(self, parent=None):
        super(ptfLoadWidget, self).__init__(parent)
        self.csvPath = ''
        self.source = 'google'
        self.open = False
        self.close = False
        self.high = False
        self.low = False
        self.volume = False
        self.noRisk = 0.02
        self.benchmark = False
        self.setObjectName("Dialog")
        self.resize(640, 462)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 400, 621, 32))
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 581, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 100, 581, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 170, 251, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setProperty("value", 0.020)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 240, 377, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)

        self.radioButton_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_4.addWidget(self.radioButton_5)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 310, 581, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("BrowseFile")
        self.horizontalLayout_5.addWidget(self.pushButton)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Fenêtre de chargement"))
        self.label.setText(_translate("Dialog", "Provenance du csv:"))
        self.radioButton_3.setText(_translate("Dialog", "Google Finance"))
        self.radioButton_2.setText(_translate("Dialog", "Quandl"))
        self.radioButton.setText(_translate("Dialog", "Bloomberg"))
        self.label_2.setText(_translate("Dialog", "Contenu du csv:      "))
        self.checkBox_2.setText(_translate("Dialog", "Open"))
        self.checkBox.setText(_translate("Dialog", "Close"))
        self.checkBox_3.setText(_translate("Dialog", "High"))
        self.checkBox_4.setText(_translate("Dialog", "Low"))
        self.checkBox_5.setText(_translate("Dialog", "Volume"))
        self.label_3.setText(_translate("Dialog", "Quel est le taux sans risque? "))
        self.label_4.setText(_translate("Dialog", "Est-ce que le premier ticker est un benchmark?"))
        self.radioButton_4.setText(_translate("Dialog", "Oui"))
        self.radioButton_5.setText(_translate("Dialog", "Non"))
        self.label_5.setText(_translate("Dialog", "Entrez le nom du fichier csv:    "))
        self.pushButton.setText(_translate("Dialog", "Chercher fichier"))

        self.buttonBox.accepted.connect(self.acceptDialog)
        self.buttonBox.rejected.connect(self.reject)
        self.pushButton.clicked.connect(self.browseFile)
        QtCore.QMetaObject.connectSlotsByName(self)

    def browseFile(self):
        path = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit.setText(path[0])

    def acceptDialog(self):
        self.csvPath = self.lineEdit.text()

        if self.radioButton_3.isChecked():
            self.source = 'google'
        elif self.radioButton_2.isChecked():
            self.source = 'quandl'
        elif self.radioButton.isChecked():
            self.source = 'bloomberg'

        if self.checkBox_2.isChecked():
            self.open = True
        if self.checkBox.isChecked():
            self.close = True
        if self.checkBox_3.isChecked():
            self.high = True
        if self.checkBox_4.isChecked():
            self.low = True
        if self.checkBox_5.isChecked():
            self.volume = True
        self.noRisk = self.doubleSpinBox.value()
        if self.radioButton_4.isChecked():
            self.benchmark = True
        self.accept()

class optionsWidget(QDialog):

    def __init__(self, parent=None):
        super(optionsWidget, self).__init__(parent)

        self.noRisk = 0.020
        self.num_simul = 0
        self.debut = 0
        self.fin = 0
        self.freq = 'quot'
        self.estimation = 'hist'

        self.setObjectName("Dialog")
        self.resize(531, 385)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(40, 330, 441, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 441, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setProperty("value", 0.020)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 80, 441, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox.setMaximum(200000)
        self.spinBox.setProperty("value", 10000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 130, 441, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        # self.spinBox_2.setRange(self.debut.year, self.fin.year)
        # self.spinBox_2.setValue(self.debut.year)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)

        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_3.setRange(1, 12)
        # self.spinBox_3.setValue(self.debut.month)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_4.setRange(1, 31)
        # self.spinBox_4.setValue(self.debut.day)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_3.addWidget(self.spinBox_4)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 180, 441, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_5 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        # self.spinBox_5.setRange(self.debut.year, self.fin.year)
        # self.spinBox_5.setValue(self.fin.year)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_4.addWidget(self.spinBox_5)

        self.spinBox_6 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_6.setRange(1, 12)
        # self.spinBox_6.setValue(self.fin.month)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_4.addWidget(self.spinBox_6)

        self.spinBox_7 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        self.spinBox_7.setRange(1, 31)
        # self.spinBox_7.setValue(self.fin.day)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_4.addWidget(self.spinBox_7)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 230, 441, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)

        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(50, 280, 441, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)

        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setChecked(True)
        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_6)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_6.addWidget(self.radioButton_4)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Taux sans risque:     "))
        self.label_2.setText(_translate("Dialog", "Nombre de simulations:     "))
        self.label_3.setText(_translate("Dialog", "Date de début:     "))
        self.label_4.setText(_translate("Dialog", "Date de fin:     "))
        self.label_5.setText(_translate("Dialog", "Fréquence:     "))
        self.radioButton.setText(_translate("Dialog", "Quotidien"))
        self.radioButton_2.setText(_translate("Dialog", "Mensuel"))
        self.label_6.setText(_translate("Dialog", "Estimation:     "))
        self.radioButton_3.setText(_translate("Dialog", "Historique"))
        self.radioButton_4.setText(_translate("Dialog", "CAPM"))

        self.buttonBox.accepted.connect(self.acceptDialog)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def acceptDialog(self):
        self.noRisk = self.doubleSpinBox.value()
        self.num_simul = self.spinBox.value()
        annee = self.spinBox_2.value()
        mois = self.spinBox_3.value()
        jour = self.spinBox_4.value()
        try:
            self.debut = dt.datetime(annee, mois, jour)
        except:
            try:
                self.debut = dt.datetime(annee, mois, jour - 1)
            except:
                try:
                    self.debut = dt.datetime(annee, mois, jour - 2)
                except:
                    self.debut = dt.datetime(annee, mois, jour - 3)

        annee = self.spinBox_5.value()
        mois = self.spinBox_6.value()
        jour = self.spinBox_7.value()
        try:
            self.fin = dt.datetime(annee, mois, jour)
        except:
            try:
                self.fin = dt.datetime(annee, mois, jour - 1)
            except:
                try:
                    self.fin = dt.datetime(annee, mois, jour - 2)
                except:
                    self.fin = dt.datetime(annee, mois, jour - 3)
        if self.radioButton.isChecked():
            self.freq = 'quot'
        else:
            self.freq = 'mens'
        if self.radioButton_3.isChecked():
            self.estimation = 'hist'
        else:
            self.estimation = 'capm'
        self.accept()


class statsWidget(QDialog):

    def __init__(self, lenRow, parent=None):
        super(statsWidget, self).__init__(parent)

        self.lenRow = lenRow
        self.seriesList = []
        self.seriesDict = {}

        self.setObjectName("Statistiques")
        self.resize(1041, 619)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(5, 5))

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1001, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1001, 521))
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(24)
        self.tableWidget.setObjectName("tableWidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 550, 481, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Statistiques", "Form"))
        self.radioButton.setText(_translate("Statistiques", "Classements"))
        self.radioButton_2.setText(_translate("Statistiques", "Individuels"))

        QtCore.QMetaObject.connectSlotsByName(self)
        self.radioButton.clicked.connect(self.imprimerClassement)
        self.radioButton_2.clicked.connect(self.imprimerIndividuels)

    def imprimerClassement(self):
        """
        Fonction qui imprime les statistiques dans une table

        :return: Void
        """

        self.tableWidget.clear()
        self.tableWidget.setRowCount(self.lenRow + 1)
        self.tableWidget.setColumnCount(24)

# Betas
        beta = []
        for ticker in self.seriesList:
            beta.append(self.seriesDict[ticker].beta)

        beta = pd.DataFrame(beta, columns=['betas'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(beta)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='betas', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('betas')
        self.tableWidget.setItem(0, 1, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 0, item)
            index += 1

        index = 1
        for j in frame['betas']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 1, item)
            index += 1

# rendements
        meanRend = []
        for ticker in self.seriesList:
            meanRend.append(self.seriesDict[ticker].meanRend * 252)

        meanRend = pd.DataFrame(meanRend, columns=['rendements'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(meanRend)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='rendements', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('rendements')
        self.tableWidget.setItem(0, 4, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 3, item)
            index += 1

        index = 1
        for j in frame['rendements']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 4, item)
            index += 1

#CAPM
        capm = []
        for ticker in self.seriesList:
            capm.append(self.seriesDict[ticker].capm)

        capm = pd.DataFrame(capm, columns=['CAPM'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(capm)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='CAPM', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('CAPM')
        self.tableWidget.setItem(0, 7, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 6, item)
            index += 1

        index = 1
        for j in frame['CAPM']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 7, item)
            index += 1
#sharpe
        sharpe = []
        for ticker in self.seriesList:
            sharpe.append(self.seriesDict[ticker].sharpe)

        sharpe = pd.DataFrame(sharpe, columns=['Sharpe'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(sharpe)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='Sharpe', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('Sharpe')
        self.tableWidget.setItem(0, 10, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 9, item)
            index += 1

        index = 1
        for j in frame['Sharpe']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 10, item)
            index += 1

#treynor
        treynor = []
        for ticker in self.seriesList:
            treynor.append(self.seriesDict[ticker].treynor)

        treynor = pd.DataFrame(treynor, columns=['Treynor'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(treynor)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='Treynor', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('Treynor')
        self.tableWidget.setItem(0, 13, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 12, item)
            index += 1

        index = 1
        for j in frame['Treynor']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 13, item)
            index += 1

#mSquare
        mSquare = []
        for ticker in self.seriesList:
            mSquare.append(self.seriesDict[ticker].mSquare)

        mSquare = pd.DataFrame(mSquare, columns=['mSquare'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(mSquare)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='mSquare', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('mSquare')
        self.tableWidget.setItem(0, 16, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 15, item)
            index += 1

        index = 1
        for j in frame['mSquare']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 16, item)
            index += 1
#alpha
        alpha = []
        for ticker in self.seriesList:
            alpha.append(self.seriesDict[ticker].alpha)

        alpha = pd.DataFrame(alpha, columns=['Alpha'])
        frame = pd.DataFrame(self.seriesList, columns=['tickers'])
        frame = frame.join(alpha)
        frame.set_index('tickers', inplace=True)
        frame.sort_values(by='Alpha', inplace=True, ascending=False)
        frame.reset_index(inplace=True)

        item = QtWidgets.QTableWidgetItem('Alphas')
        self.tableWidget.setItem(0, 19, item)
        index = 1
        for i in frame['tickers']:
            item = QtWidgets.QTableWidgetItem(str(i))
            self.tableWidget.setItem(index, 18, item)
            index += 1

        index = 1
        for j in frame['Alpha']:
            item = QtWidgets.QTableWidgetItem(str(j))
            self.tableWidget.setItem(index, 19, item)
            index += 1

    def imprimerIndividuels(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(len(self.seriesList) * 3)

        tick_index = 0
        for ticker in self.seriesList:
            index = 0
            item = QtWidgets.QTableWidgetItem('ticker')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(ticker)
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('Beta')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].beta))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('Rendement')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].meanRend * 252))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('CAPM')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].capm))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('Sharpe')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].sharpe))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('Treynor')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].treynor))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('mSquare')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].mSquare))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)
            index += 1
            item = QtWidgets.QTableWidgetItem('Alpa')
            self.tableWidget.setItem(index, tick_index * 3, item)
            item = QtWidgets.QTableWidgetItem(str(self.seriesDict[ticker].alpha))
            self.tableWidget.setItem(index, tick_index * 3 + 1, item)

            tick_index += 1





if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = ptfWidget()
    main.show()

    sys.exit(app.exec_())

