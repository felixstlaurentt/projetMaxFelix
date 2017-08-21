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
        self.csvFile = pd.DataFrame()
        self.open = False
        self.close = False
        self.high = False
        self.low = False
        self.volume = False
        self.benchmark = False
        self.source = ''
        self.noRisk = 0.02
        self.seriesList = []
        self.seriesDictionary = {}
        self.corrMatrix = np.array([])
        self.index = 0

        self.setObjectName("Gestion de portefeuille")
        self.resize(850, 700)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(170, 10, 750, 750))  #631, 581
        font = QtGui.QFont()
        font.setPointSize(13)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.graph = ptfGraphWidget(self.frame)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 351))
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

        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 141, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Charger"))
        self.label.setText(_translate("Form", "fichier csv: "))
        self.pushButton_2.setText(_translate("Form", "Corrélations"))
        self.pushButton_3.setText(_translate("Form", "Time graph"))
        self.pushButton_4.setText(_translate("Form", "Frontière\n"
                                                    " efficiente"))

        self.pushButton.clicked.connect(self.openLoadWidget)
        self.pushButton_2.clicked.connect(self.graph.corrPlot)
        self.pushButton_3.clicked.connect(self.graph.ohlcPlot)

    def openLoadWidget(self):
        """
        Fonction qui ouvre la fenêtre pour charger un fichier csv

        :return: Void
        """
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
            self.format()
            self.calcStats()

    def format(self):
        """
        Fonction qui va formater le csv pour créer un tSeries pour chaque ticker qu'il contient et lui insérer leur propre DataFrame dans chaque objet

        :return: Void
        """
        self.seriesDictionary = {}
        self.csvFile = pd.read_csv(self.csvPath.split('/')[-1])
        buffer_df = pd.DataFrame(self.csvFile['Date'])
        new_df = pd.DataFrame(buffer_df)
        new_df.set_index('Date', inplace=True)
        self.csvFile.set_index('Date', inplace=True)

        liste = list(self.csvFile)
        ticker2 = liste[0].split('_')[0]

        for item in liste:
            ticker1 = item.split('_')[0]
            data = item.split('_')[1]

            if ticker1 == ticker2:
                buffer_item = pd.DataFrame(self.csvFile[item])
                new_df = new_df.join(buffer_item, how='outer')
                new_df.rename(columns={item: data}, inplace=True)
                print(new_df.head())
            else:
                self.seriesList.append(ticker2)
                self.seriesDictionary[ticker2] = tSeries(new_df, self.noRisk)
                ticker2 = ticker1
                new_df = pd.DataFrame(buffer_df)
                new_df = new_df.join(self.csvFile[item])
                new_df.rename(columns={item: data}, inplace=True)

        self.seriesList.append(ticker2)
        self.seriesDictionary[ticker2] = tSeries(new_df, self.noRisk)

        for ticker in self.seriesList:
            if self.benchmark:
                self.seriesDictionary[ticker].setBenchmark(pd.DataFrame(self.seriesDictionary[self.seriesList[0]].frame['Close']))

        self.graph.liste = self.seriesList
        self.graph.dict = self.seriesDictionary
        self.graph.ohlcPlot()

    def calcStats(self):
        """
        Fonction qui calcules les statistiques de chaque ticker et ceux du portfolio

        :return: Void
        """
        for ticker in self.seriesList:
            self.seriesDictionary[ticker].calcStats()

        self.saveToPickle()

    def saveToPickle(self):
        """
        Fonction qui sauvegarde l'objet seriesAnalysisMenu en entier. Ce qui sauvegarde toutes les données même si l'on ferme le programme

        :return: Void
        """
        pickle_out = open('ptfWidget_seriesList.pickle', 'wb')
        pickle.dump(self.seriesList, pickle_out)
        pickle_out.close()
        pickle_out = open('ptfWidget_seriesDictionary.pickle', 'wb')
        pickle.dump(self.seriesDictionary, pickle_out)
        pickle_out.close()

        print('workspace sauvegardé')
    #
    # def loadFromPickle(self):
    #     """
    #     Fonction qui remet en place l'objet seriesAnalysisMenu à l'état ou il se trouvait à la dernière sauvegarde
    #
    #     :return: Void
    #     """
    #     pickle_in = open('seriesAnalysisMenu.pickle', 'rb')
    #     buffer = pickle.load(pickle_in)
    #     self.csvName = buffer.csvName
    #     self.csvFile = buffer.csvFile
    #     self.benchmark = buffer.benchMark
    #     self.seriesList = buffer.seriesList
    #     self.seriesDictionary = buffer.seriesDictionary
    #     self.corrMatrix = buffer.corrMatrix


class ptfGraphWidget(QWidget):
    def __init__(self, parent=None):
        super(ptfGraphWidget, self).__init__(parent)

        self.liste = []
        self.dict = {}
        self.index = 0

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.buttonPrevious = QPushButton('Previous')
        self.buttonNext = QPushButton('Next')

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.buttonPrevious)
        layout.addWidget(self.buttonNext)
        self.setLayout(layout)

        self.buttonPrevious.clicked.connect(self.previous)
        self.buttonNext.clicked.connect(self.next)

        self.ohlcPlot()

    def next(self):
        if self.index == len(self.liste) - 1:
            self.index = 0
        else:
            self.index += 1
        self.ohlcPlot()

    def previous(self):
        if self.index == 0:
            self.index = len(self.liste) - 1
        else:
            self.index -= 1
        self.ohlcPlot()

    def ohlcPlot(self):

        self.figure.clear()

        if len(self.liste) != 0:
            frame = pd.DataFrame(self.dict[self.liste[self.index]].frame)
            frame.reset_index(inplace=True)
            date = frame['Date']
            open = frame['Open']
            close = frame['Close']
            high = frame['High']
            low = frame['Low']
            volume = frame['Volume']
        else:
            return 0

        new_date = list(range(1, len(close)+1))

        i = 0
        ohlc_data = []
        while i < len(new_date):
            stats_1_day = new_date[i], open[i], high[i], low[i], close[i]
            ohlc_data.append(stats_1_day)
            i += 1

        ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=4, colspan=1)
        plt.title(self.liste[self.index])
        candlestick_ohlc(ax1, ohlc_data, colorup='g', colordown='r')

        ax2 = plt.subplot2grid((6, 1), (4, 0), rowspan=2, colspan=1, sharex=ax1)
        ax2.bar(new_date, volume, 0.5, color='g')

        # refresh canvas
        self.canvas.draw()

    def corrPlot(self):

        pass
        self.figure.clear()

        df_corr = pd.DataFrame()
        for item in self.liste:
            rend = pd.DataFrame(self.dict[item].rend)
            rend.rename(columns={'Close': item}, inplace=True)
            if df_corr.empty:
                df_corr = pd.DataFrame(rend)
            else:
                df_corr = df_corr.join(rend, how='outer')
        df_corr = df_corr.corr()
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
        self.doubleSpinBox.setProperty("value", 0.02)
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
        self.setWindowTitle(_translate("Dialog", "Dialog"))
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = ptfWidget()
    main.show()

    sys.exit(app.exec_())

