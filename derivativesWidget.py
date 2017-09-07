# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'derivativesUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
import sys


class derivativesWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(derivativesWidget, self).__init__(parent)

        self.setObjectName("Form")
        self.resize(990, 601)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        self.optionTypes = ['Call Européen', 'Put Européen']
        self.underlying = ['Action', 'Indice', 'Devise']

        """
        MENU GAUCHE
        """
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 184, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        """
        STACKED WIDGET
        """
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 10, 731, 561))
        self.stackedWidget.setObjectName("stackedWidget")

        """
        PAGE 1
        """
        """
        RANGÉE 1
        """
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 281, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.comboBox.addItems(self.optionTypes)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.comboBox_2.addItems(self.underlying)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(dt.datetime.today())
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox_8)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_9.addWidget(self.dateEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.horizontalLayout_10.addWidget(self.doubleSpinBox_9)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_10.addWidget(self.dateEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_10)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_11.addWidget(self.dateEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_11)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.horizontalLayout_12.addWidget(self.dateEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_12)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.horizontalLayout_13.addWidget(self.dateEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        """
        RANGÉE 2
        """
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(370, 0, 241, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        font = QtGui.QFont()
        font.setPointSize(15)

        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)

        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)

        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setFont(font)
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_17.addWidget(self.label_16)

        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_17.setFont(font)
        self.label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")

        self.horizontalLayout_17.addWidget(self.label_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")

        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)

        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)

        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")

        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setFont(font)
        self.label_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_19.addWidget(self.label_20)

        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setFont(font)
        self.label_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_19.addWidget(self.label_21)

        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")

        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_22.setFont(font)
        self.label_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_20.addWidget(self.label_22)

        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_23.setFont(font)
        self.label_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_20.addWidget(self.label_23)

        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")

        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_21.addWidget(self.label_28)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_21.addWidget(self.lineEdit_11)

        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)

        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)

        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")

        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_22.addWidget(self.label_30)

        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.horizontalLayout_22.addWidget(self.doubleSpinBox_14)

        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.Label_volimp = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Label_volimp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Label_volimp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Label_volimp.setMidLineWidth(0)
        self.Label_volimp.setText("")
        self.Label_volimp.setObjectName("Label_volimp")
        self.verticalLayout_3.addWidget(self.Label_volimp)

        self.stackedWidget.addWidget(self.page)

        """
        PAGE 2
        """
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 141, 551))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_4.addWidget(self.label_24)

        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_4.addWidget(self.label_25)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_4.addWidget(self.doubleSpinBox)

        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_4.addWidget(self.label_26)

        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_4.addWidget(self.doubleSpinBox_2)

        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_4.addWidget(self.label_27)

        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_4.addWidget(self.doubleSpinBox_3)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_4.addWidget(self.listWidget_2)

        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(170, 10, 541, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget.addWidget(self.page_2)

        """
        PAGE 3
        """
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Calculateur d\'options"))
        self.pushButton_2.setText(_translate("Form", "Graphique payoff"))
        self.pushButton_3.setText(_translate("Form", "Portefeuille "))
        self.label.setText(_translate("Form", "Type d\'option"))
        self.label_2.setText(_translate("Form", "Sous-jacent"))
        self.label_3.setText(_translate("Form", "Date d\'expiration"))
        self.label_4.setText(_translate("Form", "Prix du sous-jacent"))
        self.label_5.setText(_translate("Form", "Prix du strike        "))
        self.label_6.setText(_translate("Form", "Volatilité               "))
        self.label_7.setText(_translate("Form", "Taux sans risque   "))
        self.label_8.setText(_translate("Form", "Dividendes"))
        self.label_9.setText(_translate("Form", "Montant"))
        self.label_10.setText(_translate("Form", "Date"))
        self.label_11.setText(_translate("Form", "Taux continu         "))
        self.pushButton_4.setText(_translate("Form", "Calculer"))
        self.label_12.setText(_translate("Form", "Coût"))
        self.label_14.setText(_translate("Form", "Delta"))
        self.label_16.setText(_translate("Form", "Gamma"))
        self.label_18.setText(_translate("Form", "Vega"))
        self.label_20.setText(_translate("Form", "Theta"))
        self.label_22.setText(_translate("Form", "Rho"))
        self.label_28.setText(_translate("Form", "Nom     "))
        self.pushButton_7.setText(_translate("Form", "Sauvegarder"))
        self.label_29.setText(_translate("Form", "Volatilité implicite"))
        self.label_30.setText(_translate("Form", "Prix"))
        self.pushButton_9.setText(_translate("Form", "Calculer"))
        self.label_24.setText(_translate("Form", "Option"))
        self.label_25.setText(_translate("Form", "Prix du sous-jacent"))
        self.label_26.setText(_translate("Form", "Strike"))
        self.label_27.setText(_translate("Form", "Coût"))
        self.pushButton_5.setText(_translate("Form", "Ajouter"))
        self.pushButton_6.setText(_translate("Form", "Supprimer"))

        self.pushButton.clicked.connect(self.openCalculator)
        self.pushButton_2.clicked.connect(self.openGraph)
        self.pushButton_3.clicked.connect(self.openPtf)

    def openCalculator(self):
        self.stackedWidget.setCurrentIndex(0)

    def openGraph(self):
        self.stackedWidget.setCurrentIndex(1)

    def openPtf(self):
        self.stackedWidget.setCurrentIndex(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = derivativesWidget()
    main.show()

    sys.exit(app.exec_())
