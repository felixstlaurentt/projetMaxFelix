import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QWidget, QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import time
import pickle
from importWidget import importWidget
from ptfWidget import ptfWidget
from derivativesWidget import derivativesWidget


class mainWidget(QMainWindow):

    def __init__(self, parent=None):
        super(mainWidget, self).__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(1277, 901)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 0, 1400, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)

        self.importWidget = importWidget(self.page_1)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.ptfWidget = ptfWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.derivativesWidget = derivativesWidget(self.page_4)

        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)

        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)

        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)

        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 161, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(self)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Importer \n"
                                                        "des données"))
        self.pushButton_2.setText(_translate("MainWindow", "Gestion de\n"
                                                            " portefeuille"))
        self.pushButton_3.setText(_translate("MainWindow", "Analyse \n"
                                                            "financière"))
        self.pushButton_4.setText(_translate("MainWindow", "Produits \n"
                                                            "dérivées"))
        self.pushButton_5.setText(_translate("MainWindow", "Live \n"
                                                            "data"))
        self.pushButton_6.setText(_translate("MainWindow", "Simulation de\n"
                                                            " Montecarlo"))
        self.pushButton_7.setText(_translate("MainWindow", "Régressions\n"
                                                            ""))
        self.pushButton_8.setText(_translate("MainWindow", "Obligations\n"
                                                            ""))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))

        self.pushButton.clicked.connect(self.importOpen)
        self.pushButton_2.clicked.connect(self.ptfOpen)
        self.pushButton_4.clicked.connect(self.derivativesOpen)

    def importOpen(self):
        self.stackedWidget.setCurrentIndex(0)

    def ptfOpen(self):
        self.stackedWidget.setCurrentIndex(1)

    def derivativesOpen(self):
        self.stackedWidget.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = mainWidget()
    main.show()

    sys.exit(app.exec_())


