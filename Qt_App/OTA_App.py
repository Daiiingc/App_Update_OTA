# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\OTA_App.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.OTA_Update = QtWidgets.QWidget()
        self.OTA_Update.setObjectName("OTA_Update")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.OTA_Update)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.OTA_Update)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.label_3 = QtWidgets.QLabel(self.OTA_Update)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Box_File_Tab_1 = QtWidgets.QComboBox(self.OTA_Update)
        self.Box_File_Tab_1.setMinimumSize(QtCore.QSize(240, 30))
        self.Box_File_Tab_1.setEditable(True)
        self.Box_File_Tab_1.setObjectName("Box_File_Tab_1")
        self.horizontalLayout_2.addWidget(self.Box_File_Tab_1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.Button_File_Tab_1 = QtWidgets.QPushButton(self.OTA_Update)
        self.Button_File_Tab_1.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_File_Tab_1.setFont(font)
        self.Button_File_Tab_1.setObjectName("Button_File_Tab_1")
        self.horizontalLayout_2.addWidget(self.Button_File_Tab_1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.Box_Port_Tab_1 = QtWidgets.QComboBox(self.OTA_Update)
        self.Box_Port_Tab_1.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Box_Port_Tab_1.setFont(font)
        self.Box_Port_Tab_1.setObjectName("Box_Port_Tab_1")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.Box_Port_Tab_1.addItem("")
        self.horizontalLayout_2.addWidget(self.Box_Port_Tab_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Button_Upgrade_Tab_1 = QtWidgets.QPushButton(self.OTA_Update)
        self.Button_Upgrade_Tab_1.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Upgrade_Tab_1.setFont(font)
        self.Button_Upgrade_Tab_1.setObjectName("Button_Upgrade_Tab_1")
        self.horizontalLayout_3.addWidget(self.Button_Upgrade_Tab_1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        spacerItem21 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        spacerItem22 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        self.label_4 = QtWidgets.QLabel(self.OTA_Update)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem23 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem23)
        self.Box_LoRa_Tab_1 = QtWidgets.QComboBox(self.OTA_Update)
        self.Box_LoRa_Tab_1.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Box_LoRa_Tab_1.setFont(font)
        self.Box_LoRa_Tab_1.setEditable(False)
        self.Box_LoRa_Tab_1.setObjectName("Box_LoRa_Tab_1")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.Box_LoRa_Tab_1.addItem("")
        self.horizontalLayout_4.addWidget(self.Box_LoRa_Tab_1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TextBrowser_Tab1 = QtWidgets.QTextBrowser(self.OTA_Update)
        self.TextBrowser_Tab1.setMinimumSize(QtCore.QSize(150, 20))
        self.TextBrowser_Tab1.setObjectName("TextBrowser_Tab1")
        self.horizontalLayout_6.addWidget(self.TextBrowser_Tab1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Button_Start_Tab_1 = QtWidgets.QPushButton(self.OTA_Update)
        self.Button_Start_Tab_1.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Start_Tab_1.setFont(font)
        self.Button_Start_Tab_1.setObjectName("Button_Start_Tab_1")
        self.horizontalLayout_5.addWidget(self.Button_Start_Tab_1)
        self.progressBar_Tab_1 = QtWidgets.QProgressBar(self.OTA_Update)
        self.progressBar_Tab_1.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.progressBar_Tab_1.setFont(font)
        self.progressBar_Tab_1.setProperty("value", 24)
        self.progressBar_Tab_1.setObjectName("progressBar_Tab_1")
        self.horizontalLayout_5.addWidget(self.progressBar_Tab_1)
        self.Button_Stop_Tab_1 = QtWidgets.QPushButton(self.OTA_Update)
        self.Button_Stop_Tab_1.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Stop_Tab_1.setFont(font)
        self.Button_Stop_Tab_1.setChecked(False)
        self.Button_Stop_Tab_1.setObjectName("Button_Stop_Tab_1")
        self.horizontalLayout_5.addWidget(self.Button_Stop_Tab_1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.OTA_Update, "")
        self.UART_Update = QtWidgets.QWidget()
        self.UART_Update.setObjectName("UART_Update")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.UART_Update)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem25)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem26)
        self.label_5 = QtWidgets.QLabel(self.UART_Update)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem27)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem28)
        self.Box_Port_Tab_2 = QtWidgets.QComboBox(self.UART_Update)
        self.Box_Port_Tab_2.setEnabled(True)
        self.Box_Port_Tab_2.setMinimumSize(QtCore.QSize(120, 0))
        self.Box_Port_Tab_2.setObjectName("Box_Port_Tab_2")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.Box_Port_Tab_2.addItem("")
        self.horizontalLayout_8.addWidget(self.Box_Port_Tab_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Button_Upgrade_Tab_2 = QtWidgets.QPushButton(self.UART_Update)
        self.Button_Upgrade_Tab_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Upgrade_Tab_2.setFont(font)
        self.Button_Upgrade_Tab_2.setObjectName("Button_Upgrade_Tab_2")
        self.horizontalLayout_9.addWidget(self.Button_Upgrade_Tab_2)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem29)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.lineEdit = QtWidgets.QLineEdit(self.UART_Update)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.textBrowser_Tab_2 = QtWidgets.QTextBrowser(self.UART_Update)
        self.textBrowser_Tab_2.setObjectName("textBrowser_Tab_2")
        self.verticalLayout_3.addWidget(self.textBrowser_Tab_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Button_Start_Tab_2 = QtWidgets.QPushButton(self.UART_Update)
        self.Button_Start_Tab_2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Start_Tab_2.setFont(font)
        self.Button_Start_Tab_2.setObjectName("Button_Start_Tab_2")
        self.horizontalLayout_10.addWidget(self.Button_Start_Tab_2)
        self.progressBar_Tab_2 = QtWidgets.QProgressBar(self.UART_Update)
        self.progressBar_Tab_2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.progressBar_Tab_2.setFont(font)
        self.progressBar_Tab_2.setProperty("value", 24)
        self.progressBar_Tab_2.setObjectName("progressBar_Tab_2")
        self.horizontalLayout_10.addWidget(self.progressBar_Tab_2)
        self.Button_Stop_Tab_2 = QtWidgets.QPushButton(self.UART_Update)
        self.Button_Stop_Tab_2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_Stop_Tab_2.setFont(font)
        self.Button_Stop_Tab_2.setObjectName("Button_Stop_Tab_2")
        self.horizontalLayout_10.addWidget(self.Button_Stop_Tab_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.UART_Update, "")
        self.OTA_Config = QtWidgets.QWidget()
        self.OTA_Config.setObjectName("OTA_Config")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.OTA_Config)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.OTA_Config)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem30)
        self.label_11 = QtWidgets.QLabel(self.OTA_Config)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem31)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem32)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem33)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem34)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem35)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem36)
        self.label_6 = QtWidgets.QLabel(self.OTA_Config)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Box_Name_Tab_3 = QtWidgets.QComboBox(self.OTA_Config)
        self.Box_Name_Tab_3.setMinimumSize(QtCore.QSize(110, 30))
        self.Box_Name_Tab_3.setObjectName("Box_Name_Tab_3")
        self.horizontalLayout_13.addWidget(self.Box_Name_Tab_3)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem37)
        self.Box_File_Tab_3 = QtWidgets.QComboBox(self.OTA_Config)
        self.Box_File_Tab_3.setMinimumSize(QtCore.QSize(220, 30))
        self.Box_File_Tab_3.setEditable(True)
        self.Box_File_Tab_3.setObjectName("Box_File_Tab_3")
        self.horizontalLayout_13.addWidget(self.Box_File_Tab_3)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem38)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem39)
        self.Button_File_Tab_3 = QtWidgets.QPushButton(self.OTA_Config)
        self.Button_File_Tab_3.setMinimumSize(QtCore.QSize(150, 0))
        self.Button_File_Tab_3.setObjectName("Button_File_Tab_3")
        self.horizontalLayout_13.addWidget(self.Button_File_Tab_3)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem40)
        self.Box_Port_Tab_3 = QtWidgets.QComboBox(self.OTA_Config)
        self.Box_Port_Tab_3.setMinimumSize(QtCore.QSize(110, 30))
        self.Box_Port_Tab_3.setEditable(False)
        self.Box_Port_Tab_3.setObjectName("Box_Port_Tab_3")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.Box_Port_Tab_3.addItem("")
        self.horizontalLayout_13.addWidget(self.Box_Port_Tab_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem41)
        self.label_10 = QtWidgets.QLabel(self.OTA_Config)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem42)
        self.Box_LoRa_Tab_3 = QtWidgets.QComboBox(self.OTA_Config)
        self.Box_LoRa_Tab_3.setMinimumSize(QtCore.QSize(110, 30))
        self.Box_LoRa_Tab_3.setObjectName("Box_LoRa_Tab_3")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.Box_LoRa_Tab_3.addItem("")
        self.horizontalLayout_15.addWidget(self.Box_LoRa_Tab_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.OTA_Config)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem43)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.textEdit_Tab_3 = QtWidgets.QTextEdit(self.OTA_Config)
        self.textEdit_Tab_3.setObjectName("textEdit_Tab_3")
        self.horizontalLayout_17.addWidget(self.textEdit_Tab_3)
        self.textBrowser_Tab_3 = QtWidgets.QTextBrowser(self.OTA_Config)
        self.textBrowser_Tab_3.setMinimumSize(QtCore.QSize(400, 0))
        self.textBrowser_Tab_3.setObjectName("textBrowser_Tab_3")
        self.horizontalLayout_17.addWidget(self.textBrowser_Tab_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.Button_Setting_Tab_3 = QtWidgets.QPushButton(self.OTA_Config)
        self.Button_Setting_Tab_3.setMinimumSize(QtCore.QSize(0, 35))
        self.Button_Setting_Tab_3.setObjectName("Button_Setting_Tab_3")
        self.horizontalLayout_18.addWidget(self.Button_Setting_Tab_3)
        self.Button_Start_Tab_3 = QtWidgets.QPushButton(self.OTA_Config)
        self.Button_Start_Tab_3.setMinimumSize(QtCore.QSize(0, 35))
        self.Button_Start_Tab_3.setObjectName("Button_Start_Tab_3")
        self.horizontalLayout_18.addWidget(self.Button_Start_Tab_3)
        self.progressBar_Tab_3 = QtWidgets.QProgressBar(self.OTA_Config)
        self.progressBar_Tab_3.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.progressBar_Tab_3.setFont(font)
        self.progressBar_Tab_3.setProperty("value", 24)
        self.progressBar_Tab_3.setObjectName("progressBar_Tab_3")
        self.horizontalLayout_18.addWidget(self.progressBar_Tab_3)
        self.Button_Stop_Tab_3 = QtWidgets.QPushButton(self.OTA_Config)
        self.Button_Stop_Tab_3.setMinimumSize(QtCore.QSize(0, 35))
        self.Button_Stop_Tab_3.setObjectName("Button_Stop_Tab_3")
        self.horizontalLayout_18.addWidget(self.Button_Stop_Tab_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.tabWidget.addTab(self.OTA_Config, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dragino Sensor Management Toolv 1.1"))
        self.label.setText(_translate("MainWindow", "DEVEUI"))
        self.label_3.setText(_translate("MainWindow", "Port"))
        self.Button_File_Tab_1.setText(_translate("MainWindow", "DEUI_File"))
        self.Box_Port_Tab_1.setCurrentText(_translate("MainWindow", "COM1"))
        self.Box_Port_Tab_1.setItemText(0, _translate("MainWindow", "COM1"))
        self.Box_Port_Tab_1.setItemText(1, _translate("MainWindow", "COM2"))
        self.Box_Port_Tab_1.setItemText(2, _translate("MainWindow", "COM3"))
        self.Box_Port_Tab_1.setItemText(3, _translate("MainWindow", "COM4"))
        self.Box_Port_Tab_1.setItemText(4, _translate("MainWindow", "COM5"))
        self.Box_Port_Tab_1.setItemText(5, _translate("MainWindow", "COM6"))
        self.Box_Port_Tab_1.setItemText(6, _translate("MainWindow", "COM7"))
        self.Box_Port_Tab_1.setItemText(7, _translate("MainWindow", "COM8"))
        self.Box_Port_Tab_1.setItemText(8, _translate("MainWindow", "COM9"))
        self.Box_Port_Tab_1.setItemText(9, _translate("MainWindow", "COM10"))
        self.Button_Upgrade_Tab_1.setText(_translate("MainWindow", "Upgrade_File"))
        self.label_4.setText(_translate("MainWindow", "LoRa_FREQ"))
        self.Box_LoRa_Tab_1.setItemText(0, _translate("MainWindow", "EU868"))
        self.Box_LoRa_Tab_1.setItemText(1, _translate("MainWindow", "IN865"))
        self.Box_LoRa_Tab_1.setItemText(2, _translate("MainWindow", "KZ865"))
        self.Box_LoRa_Tab_1.setItemText(3, _translate("MainWindow", "KR920"))
        self.Box_LoRa_Tab_1.setItemText(4, _translate("MainWindow", "MA869"))
        self.Box_LoRa_Tab_1.setItemText(5, _translate("MainWindow", "US915"))
        self.Box_LoRa_Tab_1.setItemText(6, _translate("MainWindow", "CN470"))
        self.Box_LoRa_Tab_1.setItemText(7, _translate("MainWindow", "AU915"))
        self.Box_LoRa_Tab_1.setItemText(8, _translate("MainWindow", "AS923"))
        self.Box_LoRa_Tab_1.setItemText(9, _translate("MainWindow", "AS923-2"))
        self.Box_LoRa_Tab_1.setItemText(10, _translate("MainWindow", "AS923-3"))
        self.Box_LoRa_Tab_1.setItemText(11, _translate("MainWindow", "AS923-4"))
        self.Box_LoRa_Tab_1.setItemText(12, _translate("MainWindow", "EU433"))
        self.Box_LoRa_Tab_1.setItemText(13, _translate("MainWindow", "RU864"))
        self.Button_Start_Tab_1.setText(_translate("MainWindow", "Start"))
        self.Button_Stop_Tab_1.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OTA_Update), _translate("MainWindow", "OTA Update Firmware"))
        self.label_5.setText(_translate("MainWindow", "Port"))
        self.Box_Port_Tab_2.setItemText(0, _translate("MainWindow", "COM1"))
        self.Box_Port_Tab_2.setItemText(1, _translate("MainWindow", "COM2"))
        self.Box_Port_Tab_2.setItemText(2, _translate("MainWindow", "COM3"))
        self.Box_Port_Tab_2.setItemText(3, _translate("MainWindow", "COM4"))
        self.Box_Port_Tab_2.setItemText(4, _translate("MainWindow", "COM5"))
        self.Box_Port_Tab_2.setItemText(5, _translate("MainWindow", "COM6"))
        self.Box_Port_Tab_2.setItemText(6, _translate("MainWindow", "COM7"))
        self.Box_Port_Tab_2.setItemText(7, _translate("MainWindow", "COM8"))
        self.Box_Port_Tab_2.setItemText(8, _translate("MainWindow", "COM9"))
        self.Box_Port_Tab_2.setItemText(9, _translate("MainWindow", "COM10"))
        self.Button_Upgrade_Tab_2.setText(_translate("MainWindow", "Upgrade_File"))
        self.Button_Start_Tab_2.setText(_translate("MainWindow", "Start"))
        self.Button_Stop_Tab_2.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UART_Update), _translate("MainWindow", "UART Update Firmware"))
        self.label_12.setText(_translate("MainWindow", "Model Name"))
        self.label_11.setText(_translate("MainWindow", "DEVEUI"))
        self.label_6.setText(_translate("MainWindow", "Port"))
        self.Button_File_Tab_3.setText(_translate("MainWindow", "DEUI_File"))
        self.Box_Port_Tab_3.setItemText(0, _translate("MainWindow", "COM1"))
        self.Box_Port_Tab_3.setItemText(1, _translate("MainWindow", "COM2"))
        self.Box_Port_Tab_3.setItemText(2, _translate("MainWindow", "COM3"))
        self.Box_Port_Tab_3.setItemText(3, _translate("MainWindow", "COM4"))
        self.Box_Port_Tab_3.setItemText(4, _translate("MainWindow", "COM5"))
        self.Box_Port_Tab_3.setItemText(5, _translate("MainWindow", "COM6"))
        self.Box_Port_Tab_3.setItemText(6, _translate("MainWindow", "COM7"))
        self.Box_Port_Tab_3.setItemText(7, _translate("MainWindow", "COM8"))
        self.Box_Port_Tab_3.setItemText(8, _translate("MainWindow", "COM9"))
        self.Box_Port_Tab_3.setItemText(9, _translate("MainWindow", "COM10"))
        self.label_10.setText(_translate("MainWindow", "LoRa_FREQ"))
        self.Box_LoRa_Tab_3.setItemText(0, _translate("MainWindow", "EU868"))
        self.Box_LoRa_Tab_3.setItemText(1, _translate("MainWindow", "IN865"))
        self.Box_LoRa_Tab_3.setItemText(2, _translate("MainWindow", "KZ865"))
        self.Box_LoRa_Tab_3.setItemText(3, _translate("MainWindow", "KR920"))
        self.Box_LoRa_Tab_3.setItemText(4, _translate("MainWindow", "MA869"))
        self.Box_LoRa_Tab_3.setItemText(5, _translate("MainWindow", "US915"))
        self.Box_LoRa_Tab_3.setItemText(6, _translate("MainWindow", "CN470"))
        self.Box_LoRa_Tab_3.setItemText(7, _translate("MainWindow", "AU915"))
        self.Box_LoRa_Tab_3.setItemText(8, _translate("MainWindow", "AS923"))
        self.Box_LoRa_Tab_3.setItemText(9, _translate("MainWindow", "AS923-2"))
        self.Box_LoRa_Tab_3.setItemText(10, _translate("MainWindow", "AS923-3"))
        self.Box_LoRa_Tab_3.setItemText(11, _translate("MainWindow", "AS923-4"))
        self.Box_LoRa_Tab_3.setItemText(12, _translate("MainWindow", "EU433"))
        self.Box_LoRa_Tab_3.setItemText(13, _translate("MainWindow", "RU864"))
        self.label_13.setText(_translate("MainWindow", "AT Command"))
        self.Button_Setting_Tab_3.setText(_translate("MainWindow", "Verify Settings"))
        self.Button_Start_Tab_3.setText(_translate("MainWindow", "Start"))
        self.Button_Stop_Tab_3.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OTA_Config), _translate("MainWindow", "OTA Update Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
