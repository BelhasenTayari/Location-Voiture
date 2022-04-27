from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from datetime import datetime
from datetime import date
from datetime import timedelta
from agence import Agence
from voiture import Voiture
from client import Client
from location import Location

tayariLocation = Agence()

def showMessageBox(title, content):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(content)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 811)
        MainWindow.setStyleSheet("QMenuBar{\n"
"        color:#FFFFFF;\n"
"}\n"
"QMenuBar::item {\n"
"    spacing: 3px;           \n"
"    padding: 2px 10px;\n"
"    background-color:#000000;\n"
"    color:#FFFFFF;  \n"
"}\n"
"QMenuBar::item:selected {    \n"
"    background-color: rgb(244,164,96);\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    background: #FFFFFF;\n"
"    color:#000000;\n"
"}\n"
"QMenu {\n"
"    background-color: #000000;   \n"
"}\n"
"QMenu::item {\n"
"    background-color: #000000;\n"
"    color:#FFFFFF;\n"
"}\n"
"QMenu::item:selected { \n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"}\n"
"QWidget{\n"
"    background-color:#000000;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 50, 961, 691))
        self.stackedWidget.setStyleSheet("\n"
"background-color:#000000;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(40, 180, 861, 121))
        font = QtGui.QFont()
        font.setPointSize(47)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#FFFFFF;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 861, 121))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#FFFFFF;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.btnAjouterVoiture = QtWidgets.QPushButton(self.page_2)
        self.btnAjouterVoiture.setGeometry(QtCore.QRect(390, 180, 120, 120))
        self.btnAjouterVoiture.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnAjouterVoiture.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/car.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAjouterVoiture.setIcon(icon)
        self.btnAjouterVoiture.setIconSize(QtCore.QSize(90, 90))
        self.btnAjouterVoiture.setObjectName("btnAjouterVoiture")
        self.btnRechercherVoiture = QtWidgets.QPushButton(self.page_2)
        self.btnRechercherVoiture.setGeometry(QtCore.QRect(390, 430, 120, 120))
        self.btnRechercherVoiture.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnRechercherVoiture.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRechercherVoiture.setIcon(icon1)
        self.btnRechercherVoiture.setIconSize(QtCore.QSize(90, 90))
        self.btnRechercherVoiture.setObjectName("btnRechercherVoiture")
        self.btnModifierVoiture = QtWidgets.QPushButton(self.page_2)
        self.btnModifierVoiture.setGeometry(QtCore.QRect(690, 420, 120, 120))
        self.btnModifierVoiture.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnModifierVoiture.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModifierVoiture.setIcon(icon2)
        self.btnModifierVoiture.setIconSize(QtCore.QSize(90, 90))
        self.btnModifierVoiture.setObjectName("btnModifierVoiture")
        self.btnSupprimerVoiture = QtWidgets.QPushButton(self.page_2)
        self.btnSupprimerVoiture.setGeometry(QtCore.QRect(100, 430, 120, 120))
        self.btnSupprimerVoiture.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnSupprimerVoiture.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSupprimerVoiture.setIcon(icon3)
        self.btnSupprimerVoiture.setIconSize(QtCore.QSize(90, 90))
        self.btnSupprimerVoiture.setObjectName("btnSupprimerVoiture")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(360, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(670, 560, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(370, 570, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(70, 570, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(240, 60, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.btnModifierClient = QtWidgets.QPushButton(self.page_3)
        self.btnModifierClient.setGeometry(QtCore.QRect(700, 410, 120, 120))
        self.btnModifierClient.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnModifierClient.setText("")
        self.btnModifierClient.setIcon(icon2)
        self.btnModifierClient.setIconSize(QtCore.QSize(90, 90))
        self.btnModifierClient.setObjectName("btnModifierClient")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(60, 560, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(250, 50, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(370, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(680, 550, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.btnSupprimerClient = QtWidgets.QPushButton(self.page_3)
        self.btnSupprimerClient.setGeometry(QtCore.QRect(110, 420, 120, 120))
        self.btnSupprimerClient.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnSupprimerClient.setText("")
        self.btnSupprimerClient.setIcon(icon3)
        self.btnSupprimerClient.setIconSize(QtCore.QSize(90, 90))
        self.btnSupprimerClient.setObjectName("btnSupprimerClient")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(380, 560, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btnRechercherClient = QtWidgets.QPushButton(self.page_3)
        self.btnRechercherClient.setGeometry(QtCore.QRect(400, 420, 120, 120))
        self.btnRechercherClient.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnRechercherClient.setText("")
        self.btnRechercherClient.setIcon(icon1)
        self.btnRechercherClient.setIconSize(QtCore.QSize(90, 90))
        self.btnRechercherClient.setObjectName("btnRechercherClient")
        self.btnAjouterClient = QtWidgets.QPushButton(self.page_3)
        self.btnAjouterClient.setGeometry(QtCore.QRect(400, 170, 120, 120))
        self.btnAjouterClient.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnAjouterClient.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAjouterClient.setIcon(icon4)
        self.btnAjouterClient.setIconSize(QtCore.QSize(90, 90))
        self.btnAjouterClient.setObjectName("btnAjouterClient")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.btnModifierLocation = QtWidgets.QPushButton(self.page_4)
        self.btnModifierLocation.setGeometry(QtCore.QRect(710, 420, 120, 120))
        self.btnModifierLocation.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnModifierLocation.setText("")
        self.btnModifierLocation.setIcon(icon2)
        self.btnModifierLocation.setIconSize(QtCore.QSize(90, 90))
        self.btnModifierLocation.setObjectName("btnModifierLocation")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(70, 570, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(260, 60, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(380, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(690, 560, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.btnSupprimerLocation = QtWidgets.QPushButton(self.page_4)
        self.btnSupprimerLocation.setGeometry(QtCore.QRect(120, 430, 120, 120))
        self.btnSupprimerLocation.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnSupprimerLocation.setText("")
        self.btnSupprimerLocation.setIcon(icon3)
        self.btnSupprimerLocation.setIconSize(QtCore.QSize(90, 90))
        self.btnSupprimerLocation.setObjectName("btnSupprimerLocation")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(380, 570, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.btnRechercherLocation = QtWidgets.QPushButton(self.page_4)
        self.btnRechercherLocation.setGeometry(QtCore.QRect(410, 430, 120, 120))
        self.btnRechercherLocation.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnRechercherLocation.setText("")
        self.btnRechercherLocation.setIcon(icon1)
        self.btnRechercherLocation.setIconSize(QtCore.QSize(90, 90))
        self.btnRechercherLocation.setObjectName("btnRechercherLocation")
        self.btnAjouterLocation = QtWidgets.QPushButton(self.page_4)
        self.btnAjouterLocation.setGeometry(QtCore.QRect(410, 180, 120, 120))
        self.btnAjouterLocation.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnAjouterLocation.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/add-to-cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAjouterLocation.setIcon(icon5)
        self.btnAjouterLocation.setIconSize(QtCore.QSize(90, 90))
        self.btnAjouterLocation.setObjectName("btnAjouterLocation")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_18 = QtWidgets.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(190, 40, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.btnChargerVoitures = QtWidgets.QPushButton(self.page_5)
        self.btnChargerVoitures.setGeometry(QtCore.QRect(200, 220, 120, 120))
        self.btnChargerVoitures.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnChargerVoitures.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/car (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChargerVoitures.setIcon(icon6)
        self.btnChargerVoitures.setIconSize(QtCore.QSize(90, 90))
        self.btnChargerVoitures.setObjectName("btnChargerVoitures")
        self.btnStockerVoitures = QtWidgets.QPushButton(self.page_5)
        self.btnStockerVoitures.setGeometry(QtCore.QRect(650, 220, 120, 120))
        self.btnStockerVoitures.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid black;\n"
"    border-radius:50px;\n"
"}")
        self.btnStockerVoitures.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/car (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStockerVoitures.setIcon(icon7)
        self.btnStockerVoitures.setIconSize(QtCore.QSize(90, 90))
        self.btnStockerVoitures.setObjectName("btnStockerVoitures")
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(130, 350, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:#FFFFFF;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setGeometry(QtCore.QRect(570, 350, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:#FFFFFF;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.page_5)
        self.label_22.setGeometry(QtCore.QRect(360, 550, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:#FFFFFF;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setGeometry(QtCore.QRect(360, 290, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:#FFFFFF;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
       

        

        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 25))
        self.menubar.setObjectName("menubar")
        self.menuGestion_de_parcautomobile = QtWidgets.QMenu(self.menubar)
        self.menuGestion_de_parcautomobile.setObjectName("menuGestion_de_parcautomobile")
        self.menuGestion_des_Clients = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_Clients.setObjectName("menuGestion_des_Clients")
        self.menuGestion_des_locations = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_locations.setObjectName("menuGestion_des_locations")
        self.menuLes_Fichier = QtWidgets.QMenu(self.menubar)
        self.menuLes_Fichier.setObjectName("menuLes_Fichier")
        self.menuAccueil = QtWidgets.QMenu(self.menubar)
        self.menuAccueil.setObjectName("menuAccueil")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAjouter_Voiture = QtWidgets.QAction(MainWindow)
        self.actionAjouter_Voiture.setObjectName("actionAjouter_Voiture")
        self.actionSuppression_d_une_voiture_donn_e = QtWidgets.QAction(MainWindow)
        self.actionSuppression_d_une_voiture_donn_e.setObjectName("actionSuppression_d_une_voiture_donn_e")
        self.actionSuppression_des_voiture_d_une_marque_donn_e = QtWidgets.QAction(MainWindow)
        self.actionSuppression_des_voiture_d_une_marque_donn_e.setObjectName("actionSuppression_des_voiture_d_une_marque_donn_e")
        self.actionSuppression_des_voitures_age_10_ans = QtWidgets.QAction(MainWindow)
        self.actionSuppression_des_voitures_age_10_ans.setObjectName("actionSuppression_des_voitures_age_10_ans")
        self.actionPrix = QtWidgets.QAction(MainWindow)
        self.actionPrix.setObjectName("actionPrix")
        self.actionCouleur = QtWidgets.QAction(MainWindow)
        self.actionCouleur.setObjectName("actionCouleur")
        self.actionContenu_du_dictionnaire_voitures = QtWidgets.QAction(MainWindow)
        self.actionContenu_du_dictionnaire_voitures.setObjectName("actionContenu_du_dictionnaire_voitures")
        self.actionrecherche_par_matricule = QtWidgets.QAction(MainWindow)
        self.actionrecherche_par_matricule.setObjectName("actionrecherche_par_matricule")
        self.actionRecherche_par_matricule = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_matricule.setObjectName("actionRecherche_par_matricule")
        self.actionRecherche_par_marque = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_marque.setObjectName("actionRecherche_par_marque")
        self.actionrecherche_par_couleur = QtWidgets.QAction(MainWindow)
        self.actionrecherche_par_couleur.setObjectName("actionrecherche_par_couleur")
        self.actionrecherche_par_voiture_disponible = QtWidgets.QAction(MainWindow)
        self.actionrecherche_par_voiture_disponible.setObjectName("actionrecherche_par_voiture_disponible")
        self.actionrecherche_par_voitures_lou_es = QtWidgets.QAction(MainWindow)
        self.actionrecherche_par_voitures_lou_es.setObjectName("actionrecherche_par_voitures_lou_es")
        self.actionrecherche_des_voitures_lou_es_entre_deux_dates = QtWidgets.QAction(MainWindow)
        self.actionrecherche_des_voitures_lou_es_entre_deux_dates.setObjectName("actionrecherche_des_voitures_lou_es_entre_deux_dates")
        self.actionAjouter_un_nouvel_client = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_nouvel_client.setObjectName("actionAjouter_un_nouvel_client")
        self.actionsupprimer_un_client = QtWidgets.QAction(MainWindow)
        self.actionsupprimer_un_client.setObjectName("actionsupprimer_un_client")
        self.actionAdresse = QtWidgets.QAction(MainWindow)
        self.actionAdresse.setObjectName("actionAdresse")
        self.actionT_l_phone = QtWidgets.QAction(MainWindow)
        self.actionT_l_phone.setObjectName("actionT_l_phone")
        self.actionMail = QtWidgets.QAction(MainWindow)
        self.actionMail.setObjectName("actionMail")
        self.actionContenu_du_dictionnaire_clients = QtWidgets.QAction(MainWindow)
        self.actionContenu_du_dictionnaire_clients.setObjectName("actionContenu_du_dictionnaire_clients")
        self.actionRecherche_par_cin = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_cin.setObjectName("actionRecherche_par_cin")
        self.actionRecherche_et_affichage_2 = QtWidgets.QAction(MainWindow)
        self.actionRecherche_et_affichage_2.setObjectName("actionRecherche_et_affichage_2")
        self.actionAjouter_une_nouvelle_location = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_nouvelle_location.setObjectName("actionAjouter_une_nouvelle_location")
        self.actionSupprimer_une_Location = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_Location.setObjectName("actionSupprimer_une_Location")
        self.actionDate_de_location = QtWidgets.QAction(MainWindow)
        self.actionDate_de_location.setObjectName("actionDate_de_location")
        self.actionDur_e = QtWidgets.QAction(MainWindow)
        self.actionDur_e.setObjectName("actionDur_e")
        self.actionOuvrir_Menu_Voiture = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_Menu_Voiture.setObjectName("actionOuvrir_Menu_Voiture")
        self.actionOuvrir_Menu_Clients = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_Menu_Clients.setObjectName("actionOuvrir_Menu_Clients")
        self.actionOuvrir_Menu_Locations = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_Menu_Locations.setObjectName("actionOuvrir_Menu_Locations")
        self.actionOuvrir_Menu_Fichier = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_Menu_Fichier.setObjectName("actionOuvrir_Menu_Fichier")
        self.menuGestion_de_parcautomobile.addAction(self.actionOuvrir_Menu_Voiture)
        self.menuGestion_des_Clients.addAction(self.actionOuvrir_Menu_Clients)
        self.menuGestion_des_locations.addAction(self.actionOuvrir_Menu_Locations)
        self.menuLes_Fichier.addAction(self.actionOuvrir_Menu_Fichier)
        self.menubar.addAction(self.menuAccueil.menuAction())
        self.menubar.addAction(self.menuGestion_de_parcautomobile.menuAction())
        self.menubar.addAction(self.menuGestion_des_Clients.menuAction())
        self.menubar.addAction(self.menuGestion_des_locations.menuAction())
        self.menubar.addAction(self.menuLes_Fichier.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tayari Location"))
        self.label_7.setText(_translate("MainWindow", "Bienvenue"))
        self.label_3.setText(_translate("MainWindow", "Ajouter Voiture"))
        self.label_4.setText(_translate("MainWindow", "Modifier Voiture"))
        self.label_5.setText(_translate("MainWindow", "Rechercher Voiture"))
        self.label_6.setText(_translate("MainWindow", "Supprimer Voiture"))
        self.label_2.setText(_translate("MainWindow", "Gestion des voitures"))
        self.label_8.setText(_translate("MainWindow", "Supprimer un Client"))
        self.label_9.setText(_translate("MainWindow", "Gestion des Clients"))
        self.label_10.setText(_translate("MainWindow", "Ajouter un Client"))
        self.label_11.setText(_translate("MainWindow", "Modifier un Client"))
        self.label_12.setText(_translate("MainWindow", "Trouver un client"))
        self.label_13.setText(_translate("MainWindow", "Supprimer Location"))
        self.label_14.setText(_translate("MainWindow", "Gestion des Locations"))
        self.label_15.setText(_translate("MainWindow", "Ajouter Location"))
        self.label_16.setText(_translate("MainWindow", "Modifier Location"))
        self.label_17.setText(_translate("MainWindow", "Rechercher Location"))
        self.label_18.setText(_translate("MainWindow", "Enregistrement et Chargement"))
        self.label_19.setText(_translate("MainWindow", "Charger Les Données"))
        self.label_20.setText(_translate("MainWindow", "stocker Les Données"))

        self.menuGestion_de_parcautomobile.setTitle(_translate("MainWindow", "Gestion de parc automobile"))
        self.menuGestion_des_Clients.setTitle(_translate("MainWindow", "Gestion des Clients"))
        self.menuGestion_des_locations.setTitle(_translate("MainWindow", "Gestion des locations"))
        self.menuLes_Fichier.setTitle(_translate("MainWindow", "Les Fichier"))
        self.menuAccueil.setTitle(_translate("MainWindow", "Accueil"))
        self.actionAjouter_Voiture.setText(_translate("MainWindow", "Ajouter Voiture"))
        self.actionSuppression_d_une_voiture_donn_e.setText(_translate("MainWindow", "Suppression d\'une voiture donnée"))
        self.actionSuppression_des_voiture_d_une_marque_donn_e.setText(_translate("MainWindow", "Suppression des voiture d\'une marque donnée"))
        self.actionSuppression_des_voitures_age_10_ans.setText(_translate("MainWindow", "Suppression des voitures(age > 10 ans)"))
        self.actionPrix.setText(_translate("MainWindow", "Prix"))
        self.actionCouleur.setText(_translate("MainWindow", "Couleur"))
        self.actionContenu_du_dictionnaire_voitures.setText(_translate("MainWindow", "Contenu du dictionnaire voitures"))
        self.actionrecherche_par_matricule.setText(_translate("MainWindow", "recherche par matricule"))
        self.actionRecherche_par_matricule.setText(_translate("MainWindow", "Recherche par matricule"))
        self.actionRecherche_par_marque.setText(_translate("MainWindow", "Recherche par marque"))
        self.actionrecherche_par_couleur.setText(_translate("MainWindow", "recherche par couleur"))
        self.actionrecherche_par_voiture_disponible.setText(_translate("MainWindow", "recherche par voiture disponible"))
        self.actionrecherche_par_voitures_lou_es.setText(_translate("MainWindow", "recherche par voitures louées"))
        self.actionrecherche_des_voitures_lou_es_entre_deux_dates.setText(_translate("MainWindow", "recherche des voitures louées entre deux dates"))
        self.actionAjouter_un_nouvel_client.setText(_translate("MainWindow", "Ajouter un nouvel client"))
        self.actionsupprimer_un_client.setText(_translate("MainWindow", "supprimer un client"))
        self.actionAdresse.setText(_translate("MainWindow", "Adresse"))
        self.actionT_l_phone.setText(_translate("MainWindow", "Téléphone"))
        self.actionMail.setText(_translate("MainWindow", "Mail"))
        self.actionContenu_du_dictionnaire_clients.setText(_translate("MainWindow", "Contenu du dictionnaire clients"))
        self.actionRecherche_par_cin.setText(_translate("MainWindow", "Recherche par cin"))
        self.actionRecherche_et_affichage_2.setText(_translate("MainWindow", "Recherche et affichage"))
        self.actionAjouter_une_nouvelle_location.setText(_translate("MainWindow", "Ajouter une nouvelle location"))
        self.actionSupprimer_une_Location.setText(_translate("MainWindow", "Supprimer une Location"))
        self.actionDate_de_location.setText(_translate("MainWindow", "Date de location"))
        self.actionDur_e.setText(_translate("MainWindow", "Durée"))
        self.actionOuvrir_Menu_Voiture.setText(_translate("MainWindow", "Ouvrir Menu Voiture"))
        self.actionOuvrir_Menu_Clients.setText(_translate("MainWindow", "Ouvrir Menu Clients"))
        self.actionOuvrir_Menu_Locations.setText(_translate("MainWindow", "Ouvrir Menu Locations"))
        self.actionOuvrir_Menu_Fichier.setText(_translate("MainWindow", "Ouvrir Menu Fichier"))

        self.actionOuvrir_Menu_Clients.triggered.connect(self.openClientMenu)
        self.actionOuvrir_Menu_Voiture.triggered.connect(self.openVoitureMenu)
        self.actionOuvrir_Menu_Locations.triggered.connect(self.openLocationsMenu)
        self.actionOuvrir_Menu_Fichier.triggered.connect(self.openFichierMenu)
        self.btnAjouterVoiture.clicked.connect(self.ouvrirFenetreAjouter)
        self.btnRechercherVoiture.clicked.connect(self.ouvrirAfficherVoiture)
        self.btnSupprimerVoiture.clicked.connect(self.ouvrirFenetreSupprimerVoiture)
        self.btnModifierVoiture.clicked.connect(self.ouvrirFenetreModifierVoiture)
        self.btnChargerVoitures.clicked.connect(self.chargerVoitures)
        self.btnStockerVoitures.clicked.connect(self.stockerVoitures)
        self.btnAjouterClient.clicked.connect(self.ouvrirFenetreAjouterClient)
        self.btnRechercherClient.clicked.connect(self.ouvrirAfficherClients)
        self.btnModifierClient.clicked.connect(self.ouvrirModifierClient)
        self.btnSupprimerClient.clicked.connect(self.ouvrirSupprimerClient)
        self.btnAjouterLocation.clicked.connect(self.ouvrirAjouterLocation)
        self.btnRechercherLocation.clicked.connect(self.ouvrirAfficherLocation)
        self.btnSupprimerLocation.clicked.connect(self.ouvrirSupprimerLocation)
        self.btnModifierLocation.clicked.connect(self.ouvrirmodifierLocation)

    def ouvrirmodifierLocation(self):
        if(tayariLocation.fileExist("locations.txt")) and (len(tayariLocation.locations) == 0):
            showMessageBox("Warning", "Charger Les Donnees depuis le ficher SVP")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ModifierLocation()
            self.ui.setupUi(self.window)
            self.window.show()

    def ouvrirSupprimerLocation(self):
        if(tayariLocation.fileExist("locations.txt")) and (len(tayariLocation.locations) == 0):
            showMessageBox("Warning", "Charger Les Donnees depuis le ficher SVP")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SupprimerLocation()
            self.ui.setupUi(self.window)
            self.window.show()

    def stockerLocations(self):
        if(len(tayariLocation.locations) == 0):
            showMessageBox("WARNING", "il n'ya pas des locations a stocker")
        else:
            tayariLocation.enregistrerLocationsDansFichier()
            showMessageBox("SUCCESS", "tous les locations sont stocké avec succees")

    def ouvrirAfficherLocation(self):
        if len(tayariLocation.locations) == 0:
            showMessageBox("Warning", "Pas de données a afficher")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AffichageLocations()
            self.ui.setupUi(self.window)
            self.window.show()
            
    def ouvrirAjouterLocation(self):
        if(len(tayariLocation.locations) == 0) and (tayariLocation.fileExist("locations.txt")):
            showMessageBox("Warning", "Charger les donnees SVP !")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AjouterLocation()
            self.ui.setupUi(self.window)
            self.window.show()
    
    def ouvrirSupprimerClient(self):
        if(len(tayariLocation.clients) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a supprimer")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SupprimerClient()
            self.ui.setupUi(self.window)
            self.window.show()


    def ouvrirModifierClient(self):
        if(len(tayariLocation.clients) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a modifier")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ModifierClient()
            self.ui.setupUi(self.window)
            self.window.show()
    
    def ouvrirAfficherClients(self):
        if(len(tayariLocation.clients) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a afficher")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AffichageClients()
            self.ui.setupUi(self.window)
            self.window.show()
        
   

    def ouvrirFenetreAjouterClient(self):
        if(tayariLocation.fileExist("clients.txt")) and (len(tayariLocation.clients) == 0):
            showMessageBox("Warning", "Charger Les Donnees depuis le ficher SVP")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AjouterClient()
            self.ui.setupUi(self.window)
            self.window.show()

    def chargerVoitures(self):
        if(tayariLocation.fileExist("voitures.txt")):
            tayariLocation.chargerVoituresDepuisFicher()
        if(tayariLocation.fileExist("clients.txt")):
            tayariLocation.chargerClientsDepuisFichier()
        if(tayariLocation.fileExist("locations.txt")):
            tayariLocation.chargerLocationsDepuisFichier()
        showMessageBox("SUCCESS", "Chargement effectué avec succées")
        self.btnChargerVoitures.setEnabled(False)
            
    def stockerVoitures(self):
        if(len(tayariLocation.voitures) != 0):
            tayariLocation.enregistrerVoituresDansFichier()
        if(len(tayariLocation.clients) != 0):
            tayariLocation.enregistrerClientsDansFichier()
        if(len(tayariLocation.locations) != 0):
            tayariLocation.enregistrerLocationsDansFichier()
        showMessageBox("SUCCESS", "Enregistrement effectué avec succées")
        self.btnStockerVoitures.setEnabled(False)
        
    



    def openAccueil(self):
        self.stackedWidget.setCurrentIndex(0)
    def openClientMenu(self):
        self.stackedWidget.setCurrentIndex(2)
    def openVoitureMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    def openLocationsMenu(self):
        self.stackedWidget.setCurrentIndex(3)
    def openFichierMenu(self):
        self.stackedWidget.setCurrentIndex(4)

    #methode pour ouvrir la fenetre d'ajout d'une voiture
    def ouvrirFenetreAjouter(self):
        if(tayariLocation.fileExist("voitures.txt")) and (len(tayariLocation.voitures) == 0):
            showMessageBox("Warning", "Charger Les Donnees depuis le ficher SVP")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AjouterVoiture()
            self.ui.setupUi(self.window)
            self.window.show()

    #methode pour ouvrir la fenetre dde suppression des voitures
    def ouvrirFenetreSupprimerVoiture(self):
        if(len(tayariLocation.voitures) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a supprimer")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SupprimerVoiture()
            self.ui.setupUi(self.window)
            self.window.show()

    #methode pour ouvrir la fenetre dde Recherche des voitures
    def ouvrirAfficherVoiture(self):
        if(len(tayariLocation.voitures) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a afficher")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_AffichageVoiture()
            self.ui.setupUi(self.window)
            self.window.show()
    
    def ouvrirFenetreModifierVoiture(self):
        if(len(tayariLocation.voitures) == 0):
            showMessageBox("Warning", "il n'ya pas des donnees a modifier")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_ModifierVoiture()
            self.ui.setupUi(self.window)
            self.window.show()

#fenetre d'ajout voiture
class Ui_AjouterVoiture(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 524)
        Form.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}\n"
"QWidget{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QLineEdit, QDateEdit{\n"
"    border: 1px solid white;\n"
"    border-radius:10px;\n"
"    color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#FFFFFF;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 60, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(170, 220, 251, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QLineEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(170, 340, 251, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.textEdit_3 = QtWidgets.QLineEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(170, 260, 251, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QLineEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(170, 300, 251, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QLineEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 380, 251, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.dateEdit.setPlaceholderText("YYYY-MM-DD")

        matriculeValidator = QRegExpValidator(QRegExp(r'\b[1-2][0-9][0-9] TUN [0-9][0-9][0-9][0-9]\b')) 
        dateValidator = QRegExpValidator(QRegExp(r'\b(0[1-9]|[12][0-9]|3[01]{1,2})-(0[1-9]|[12]{1,2})-(19[0-9][0-9]|20[0-9][0-9])\b'))
        priceValidator = QRegExpValidator(QRegExp(r'\b^(?:0|[1-9][0-9]*)\.[0-9]+$\b')) 


        self.textEdit.setValidator(matriculeValidator)
        self.dateEdit.setValidator(dateValidator)
        self.textEdit_2.setValidator(priceValidator)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.ajouterVoiture)

    def ajouterVoiture(self):
        matricule = self.textEdit.text()
        prixText = self.textEdit_2.text()
        marque = self.textEdit_3.text()
        date = self.dateEdit.text()
        couleur = self.textEdit_4.text()
        
        if(prixText == "")or(marque=="")or(date == "")or(couleur == "")or(matricule==""):
            showMessageBox("WARNING","Remplir tous les champs SVP")

        elif matricule in tayariLocation.voitures.keys():
            showMessageBox("WARNING","voiture avec matricule " + matricule + " existe deja ")
    
        else:
            prix = float(prixText)
            v = Voiture(matricule,marque,couleur,True,date,prix)
            tayariLocation.ajouterVoiture(v)
            msg = "voiture avec matricule " + matricule + " ajouté avec succées"
            showMessageBox("Succées",msg)
            self.textEdit.setText("")
            self.textEdit_2.setText("")
            self.textEdit_3.setText("")
            self.textEdit_4.setText("")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ajouter une Voiture"))
        self.pushButton.setText(_translate("Form", "Ajouter"))
        self.label_2.setText(_translate("Form", "Matricule"))
        self.label_3.setText(_translate("Form", "Marque"))
        self.label_4.setText(_translate("Form", "Couleur"))
        self.label_5.setText(_translate("Form", "Date d\'achat"))
        self.label_6.setText(_translate("Form", "Prix Location"))

#fenetre afficher Voiture
class Ui_AffichageVoiture(object):
    def setupUi(self, AffichageVoiture):
        AffichageVoiture.setObjectName("AffichageVoiture")
        AffichageVoiture.resize(1118, 599)
        AffichageVoiture.setStyleSheet("QWidget{\n"
"    background-color:white;\n"
"}\n"
"QLabel{\n"
"    color:black;\n"
"}\n"
"QTableWidget{\n"
"    background-color:white;\n"
"}\n"
"\n"
"")
        self.label = QtWidgets.QLabel(AffichageVoiture)
        self.label.setGeometry(QtCore.QRect(430, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidgetVoiture = QtWidgets.QTableWidget(AffichageVoiture)
        self.tableWidgetVoiture.setGeometry(QtCore.QRect(260, 150, 851, 441))
        self.tableWidgetVoiture.setObjectName("tableWidgetVoiture")
        self.tableWidgetVoiture.setColumnCount(0)
        self.tableWidgetVoiture.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(AffichageVoiture)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(AffichageVoiture)
        self.comboBox.setGeometry(QtCore.QRect(40, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:#FFFFFF;")
        self.comboBox.setObjectName("comboBox")
        self.stackedWidget = QtWidgets.QStackedWidget(AffichageVoiture)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 230, 221, 111))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.comboBoxMatricule = QtWidgets.QComboBox(self.page)
        self.comboBoxMatricule.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMatricule.setFont(font)
        self.comboBoxMatricule.setStyleSheet("background-color:white;\n"
"")
        self.comboBoxMatricule.setObjectName("comboBoxMatricule")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.comboBoxMarque = QtWidgets.QComboBox(self.page_2)
        self.comboBoxMarque.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMarque.setFont(font)
        self.comboBoxMarque.setStyleSheet("background-color:white;\n"
"")
        self.comboBoxMarque.setObjectName("comboBoxMarque")
        self.comboBoxMarque.addItem("")
        self.comboBoxMarque.setItemText(0, "")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.comboBoxCouleur = QtWidgets.QComboBox(self.page_5)
        self.comboBoxCouleur.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCouleur.setFont(font)
        self.comboBoxCouleur.setStyleSheet("background-color:white;\n"
"")
        self.comboBoxCouleur.setObjectName("comboBoxCouleur")
        self.comboBoxCouleur.addItem("")
        self.comboBoxCouleur.setItemText(0, "")
        self.stackedWidget.addWidget(self.page_5)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.stackedWidget.addWidget(self.page_9)
        items = ["Tous", "Matricule", "Marque", "Couleur", "Disponible", "Louée"]
        self.comboBox.addItems(items)
        self.retranslateUi(AffichageVoiture)
        self.stackedWidget.setCurrentIndex(3)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.comboBoxMatricule.currentIndexChanged.connect(self.on_combobox_matricule_changed)
        self.comboBoxCouleur.currentTextChanged.connect(self.on_combobox_couleur_changed)
        self.comboBoxMarque.currentTextChanged.connect(self.on_combobox_marque_changed)


        self.tableWidgetVoiture.setColumnCount(6)
        self.tableWidgetVoiture.setHorizontalHeaderLabels(['Matricule', 'Marque', 'couleur', 'Disponible', 'date achat', 'prix Location'])
        QtCore.QMetaObject.connectSlotsByName(AffichageVoiture)
        couleur = []
        marque = []
        self.comboBoxMatricule.addItem("")
        for i in tayariLocation.voitures.values():
            self.comboBoxMatricule.addItem(i.matricule)
            couleur = couleur + [i.couleur]
            marque = marque + [i.marque]
        couleur = list(set(couleur))
        marque = list(set(marque))
        for i in couleur:
            self.comboBoxCouleur.addItem(i)
        
        for i in marque:
            self.comboBoxMarque.addItem(i)
        

        self.afficherTousLesDonnes()

    def retranslateUi(self, AffichageVoiture):
        _translate = QtCore.QCoreApplication.translate
        AffichageVoiture.setWindowTitle(_translate("AffichageVoiture", "Form"))
        self.label.setText(_translate("AffichageVoiture", "Liste des voitures"))
        self.label_2.setText(_translate("AffichageVoiture", "Filtrer par :"))
    
    def on_combobox_changed(self, value):
        if value in [0,4,5]:
           self.stackedWidget.setCurrentIndex(3)
           if(value == 0):
                self.afficherTousLesDonnes()
           elif(value == 4):
                self.afficherVoituresDisponibles()
           else:
                self.afficherVoituresLouee()
        else:
           self.stackedWidget.setCurrentIndex(value-1)
    def on_combobox_matricule_changed(self,value):
        ch = str(self.comboBoxMatricule.itemText(value))
        for i in tayariLocation.voitures.values():
            if(i.matricule == ch):        
                self.tableWidgetVoiture.setRowCount(1)
                self.tableWidgetVoiture.setItem(0,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(0,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(0,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(0,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(0,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(0,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                break

    def on_combobox_couleur_changed(self,value):
        row  = 0
        for i in tayariLocation.voitures.values():
            if(i.couleur == value): 
                row+=1
        
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.couleur == value):        
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1
        
    def on_combobox_marque_changed(self,value):
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.marque == value):        
                row+=1
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.marque == value):        
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1
    
    def afficherDonnees(self):
        if self.lineEdit.text() == "" and (self.comboValue in [1,2,3]):
            showMessageBox("WARNING", "SVP entrer une citére de rehcerche")

        else :
            if self.comboValue == 0:
                self.afficherTousLesDonnes()
            elif self.comboValue == 1:
                self.afficherParMaTricule()
            elif self.comboValue == 2:
                self.afficherParMarque()
            elif self.comboValue == 3:
                self.afficherParCouleur()
            elif self.comboValue == 4:
                self.afficherVoituresDisponibles()
            else:
                self.afficherVoituresLouee()

    def afficherTousLesDonnes(self):
        self.tableWidgetVoiture.setRowCount(len(tayariLocation.voitures))
        row = 0
        for i in tayariLocation.voitures.values():
            self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
            self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
            self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
            self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
            self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
            self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
            row+=1
    def afficherParMaTricule(self):
        matricule = self.lineEdit.text()
        i = tayariLocation.voitures[matricule]
        self.tableWidgetVoiture.setRowCount(1)

        self.tableWidgetVoiture.setItem(0,0,QtWidgets.QTableWidgetItem(i.matricule))
        self.tableWidgetVoiture.setItem(0,1,QtWidgets.QTableWidgetItem(i.marque))
        self.tableWidgetVoiture.setItem(0,2,QtWidgets.QTableWidgetItem(i.couleur))
        self.tableWidgetVoiture.setItem(0,3,QtWidgets.QTableWidgetItem(str(i.etat)))
        self.tableWidgetVoiture.setItem(0,4,QtWidgets.QTableWidgetItem(i.dateAchat))
        self.tableWidgetVoiture.setItem(0,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))

    def afficherParCouleur(self):
        couleur = self.lineEdit.text()
        row  = 0
        for i in tayariLocation.voitures.values():
            if(i.couleur == couleur): 
                row+=1
        
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.couleur == couleur):
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1

    def afficherParMarque(self):
        marque = self.lineEdit.text()
        row  = 0
        for i in tayariLocation.voitures.values():
            if(i.couleur == marque): 
                row+=1
        
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.marque == marque):
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1

    def afficherVoituresDisponibles(self):
        row  = 0
        for i in tayariLocation.voitures.values():
            if(i.etat): 
                row+=1
        
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if(i.etat):
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1
        
    def afficherVoituresLouee(self):
        row  = 0
        for i in tayariLocation.voitures.values():
            if not (i.etat): 
                row+=1
        self.tableWidgetVoiture.setRowCount(row)
        row = 0
        for i in tayariLocation.voitures.values():
            if not(i.etat):
                self.tableWidgetVoiture.setItem(row,0,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetVoiture.setItem(row,1,QtWidgets.QTableWidgetItem(i.marque))
                self.tableWidgetVoiture.setItem(row,2,QtWidgets.QTableWidgetItem(i.couleur))
                self.tableWidgetVoiture.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.etat)))
                self.tableWidgetVoiture.setItem(row,4,QtWidgets.QTableWidgetItem(i.dateAchat))
                self.tableWidgetVoiture.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.prixLocation)))
                row+=1



# class Ui_AffichageVoiture(object):
#     def setupUi(self, AffichageVoiture):
#         AffichageVoiture.setObjectName("AffichageVoiture")
#         AffichageVoiture.resize(1118, 599)
#         self.label = QtWidgets.QLabel(AffichageVoiture)
#         self.label.setGeometry(QtCore.QRect(430, 20, 251, 31))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.tableWidgetVoiture = QtWidgets.QTableWidget(AffichageVoiture)
#         self.tableWidgetVoiture.setGeometry(QtCore.QRect(260, 150, 851, 441))
#         self.tableWidgetVoiture.setObjectName("tableWidgetVoiture")
#         self.tableWidgetVoiture.setColumnCount(0)
#         self.tableWidgetVoiture.setRowCount(0)
#         self.label_2 = QtWidgets.QLabel(AffichageVoiture)
#         self.label_2.setGeometry(QtCore.QRect(20, 150, 141, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#         self.comboBox = QtWidgets.QComboBox(AffichageVoiture)
#         self.comboBox.setGeometry(QtCore.QRect(20, 190, 141, 21))
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.lineEdit = QtWidgets.QLineEdit(AffichageVoiture)
#         self.lineEdit.setGeometry(QtCore.QRect(20, 230, 211, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.lineEdit.setFont(font)
#         self.lineEdit.setObjectName("lineEdit")
#         self.pushButton = QtWidgets.QPushButton(AffichageVoiture)
#         self.pushButton.setGeometry(QtCore.QRect(20, 280, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton.setEnabled(False)
#         self.lineEdit.setEnabled(False)
#         self.pushButton.clicked.connect(self.afficherDonnees)
#         self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
#         self.tableWidgetVoiture.setColumnCount(6)
#         self.tableWidgetVoiture.setHorizontalHeaderLabels(['Matricule', 'Marque', 'couleur', 'Disponible', 'date achat', 'prix Location'])
#         self.afficherTousLesDonnes()

#         self.retranslateUi(AffichageVoiture)
#         QtCore.QMetaObject.connectSlotsByName(AffichageVoiture)

#     def retranslateUi(self, AffichageVoiture):
#         _translate = QtCore.QCoreApplication.translate
#         AffichageVoiture.setWindowTitle(_translate("AffichageVoiture", "Form"))
#         self.label.setText(_translate("AffichageVoiture", "Liste des voitures"))
#         self.label_2.setText(_translate("AffichageVoiture", "Filtrer par :"))
#         self.comboBox.setItemText(0, _translate("AffichageVoiture", "Tous"))
#         self.comboBox.setItemText(1, _translate("AffichageVoiture", "Matricule"))
#         self.comboBox.setItemText(2, _translate("AffichageVoiture", "Marque"))
#         self.comboBox.setItemText(3, _translate("AffichageVoiture", "Couleur"))
#         self.comboBox.setItemText(4, _translate("AffichageVoiture", "Disponible"))
#         self.comboBox.setItemText(5, _translate("AffichageVoiture", "Louée"))
#         self.pushButton.setText(_translate("AffichageVoiture", "Valider"))


#fenetre Supprimer Voiture
class Ui_SupprimerVoiture(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1165, 718)
        Form.setStyleSheet("QLabel{\n"
"    color:white;\n"
"}\n"
"QRadioButton{\n"
"    color:white;\n"
"}\n"
"QStackedWidget, QWidget{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white;\n"
"    border: 1px solid white;\n"
"    background-color:red;\n"
"    border-radius:10px;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 10, 701, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(200, 160, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 160, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(740, 160, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 240, 991, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(450, 90, 311, 31))
        self.comboBox.setStyleSheet("background-color:white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(370, 210, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 90, 201, 31))
        self.comboBox_2.setStyleSheet("background-color:white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(270, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.chargerMatriculesDansComboBox2()
        self.chargerMatriculesDansComboBox()
        self.radioButton.clicked.connect(self.openPremierMenuSupprimer)
        self.radioButton_2.clicked.connect(self.openDeuxiemeMenuSupprimer)
        self.radioButton_3.clicked.connect(self.openTroisiemeMenuSupprimer)

        self.pushButton.clicked.connect(self.supprimerVoituresMatricule)
        self.pushButton_2.clicked.connect(self.supprimerVoituresMarque)
    
    def supprimerVoituresMatricule(self):
        matricule = self.comboBox.currentText()
        if(matricule != ""):
            tayariLocation.supprimerVoiture(matricule)
            showMessageBox("SUCCESS", "Voiture avec matricule "+matricule+"a ete supprimer avec succees")
            self.comboBox.removeItem(self.comboBox.currentIndex())
            self.comboBox.setCurrentIndex(0)
        else:
            showMessageBox("WARNING", "Choisir une matricule SVP")

        
    
    def supprimerVoituresMarque(self):
        marque = self.comboBox_2.currentText()
        tayariLocation.supprimerVoituresParMarque(marque)
        self.comboBox_2.removeItem(self.comboBox_2.currentIndex())
        self.comboBox_2.setCurrentIndex(0)


    def openPremierMenuSupprimer(self):
        self.stackedWidget.setCurrentIndex(0)
    def openDeuxiemeMenuSupprimer(self):
        self.stackedWidget.setCurrentIndex(1)
    def openTroisiemeMenuSupprimer(self):
        self.stackedWidget.setCurrentIndex(2)

    def chargerMatriculesDansComboBox(self):
        for i in tayariLocation.voitures.keys():
            self.comboBox.addItem(i)
    def chargerMatriculesDansComboBox2(self):
        l = []
        for i in tayariLocation.voitures.values():
            l = l + [i.marque] 
        l = list(set(l))
        for i in l:
            self.comboBox_2.addItem(i)

    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Menu Suppression Voitures"))
        self.radioButton.setText(_translate("Form", "Une voiture Données"))
        self.radioButton_2.setText(_translate("Form", "Les Voitures d\'une Marque"))
        self.radioButton_3.setText(_translate("Form", "Les Voitures (age > 10 ans)"))
        self.label_2.setText(_translate("Form", "Choisir la matricule:"))
        self.pushButton.setText(_translate("Form", "Supprimer"))
        self.label_3.setText(_translate("Form", "Choisir la marque:"))
        self.pushButton_2.setText(_translate("Form", "Supprimer"))
        self.pushButton_3.setText(_translate("Form", "Supprimer"))


#Fenetre Modifier Voiture

class Ui_ModifierVoiture(object):
    def setupUi(self, slm):
        slm.setObjectName("slm")
        slm.resize(593, 641)
        slm.setStyleSheet("background-color:white;")
        self.label = QtWidgets.QLabel(slm)
        self.label.setGeometry(QtCore.QRect(90, 40, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(slm)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(slm)
        self.line.setGeometry(QtCore.QRect(80, 230, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(slm)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(slm)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(slm)
        self.label_5.setGeometry(QtCore.QRect(60, 410, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(slm)
        self.label_6.setGeometry(QtCore.QRect(60, 470, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditCouleur = QtWidgets.QLineEdit(slm)
        self.lineEditCouleur.setEnabled(False)
        self.lineEditCouleur.setGeometry(QtCore.QRect(250, 340, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCouleur.setFont(font)
        self.lineEditCouleur.setInputMask("")
        self.lineEditCouleur.setText("")
        self.lineEditCouleur.setObjectName("lineEditCouleur")
        self.lineEditDateLocation = QtWidgets.QLineEdit(slm)
        self.lineEditDateLocation.setEnabled(False)
        self.lineEditDateLocation.setGeometry(QtCore.QRect(250, 400, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateLocation.setFont(font)
        self.lineEditDateLocation.setInputMask("")
        self.lineEditDateLocation.setText("")
        self.lineEditDateLocation.setObjectName("lineEditDateLocation")
        self.lineEditPrixLocation = QtWidgets.QLineEdit(slm)
        self.lineEditPrixLocation.setEnabled(False)
        self.lineEditPrixLocation.setGeometry(QtCore.QRect(250, 460, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPrixLocation.setFont(font)
        self.lineEditPrixLocation.setInputMask("")
        self.lineEditPrixLocation.setText("")
        self.lineEditPrixLocation.setObjectName("lineEditPrixLocation")
        self.lineEditMarque = QtWidgets.QLineEdit(slm)
        self.lineEditMarque.setEnabled(False)
        self.lineEditMarque.setGeometry(QtCore.QRect(250, 280, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMarque.setFont(font)
        self.lineEditMarque.setInputMask("")
        self.lineEditMarque.setText("")
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.pushButton_2 = QtWidgets.QPushButton(slm)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 570, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(slm)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 570, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBoxMatricule = QtWidgets.QComboBox(slm)
        self.comboBoxMatricule.setGeometry(QtCore.QRect(280, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMatricule.setFont(font)
        self.comboBoxMatricule.setObjectName("comboBoxMatricule")
        self.comboBoxMatricule.addItem("")
        self.comboBoxMatricule.setItemText(0, "")
        self.chargerMatriculesDansComboBox()
        self.comboBoxMatricule.currentTextChanged.connect(self.chargerDonneeVoiture)
        self.pushButton_2.clicked.connect(self.modifierDonner)
        self.retranslateUi(slm)
        dateValidator = QRegExpValidator(QRegExp(r'\b(0[1-9]|[12][0-9]|3[01]{1,2})-(0[1-9]|[12]{1,2})-(19[0-9][0-9]|20[0-9][0-9])\b'))
        priceValidator = QRegExpValidator(QRegExp(r'\b^(?:0|[1-9][0-9]*)\.[0-9]+$\b')) 

        self.lineEditPrixLocation.setValidator(priceValidator)
        self.lineEditDateLocation.setValidator(dateValidator)
        QtCore.QMetaObject.connectSlotsByName(slm)
    
    def modifierDonner(self):
        prixLocation = self.lineEditPrixLocation.text()
        dateAchat = self.lineEditDateLocation.text()
        if(prixLocation == "")or (dateAchat == ""):
            showMessageBox("WARNING","Remplir tous les champs SVP")
        else:
            matricule = self.comboBoxMatricule.currentText()
            tayariLocation.voitures[matricule].prixLocation = float(prixLocation)
            tayariLocation.voitures[matricule].dateAchat = dateAchat
            showMessageBox("SUCCESS","voiture avec matricule " + matricule + " a ete modifié avec succees")
            self.comboBoxMatricule.setCurrentIndex(0)
            self.lineEditCouleur.setText("")
            self.lineEditDateLocation.setText("")
            self.lineEditMarque.setText("")
            self.lineEditPrixLocation.setText("")


    def chargerDonneeVoiture(self , value):
        if value == "":
            self.lineEditMarque.setText("")
            self.lineEditMarque.setEnabled(False)
            self.lineEditDateLocation.setText("")
            self.lineEditDateLocation.setEnabled(False)
            self.lineEditCouleur.setText("")
            self.lineEditCouleur.setEnabled(False)
            self.lineEditPrixLocation.setText("")
            self.lineEditPrixLocation.setEnabled(False)
        else :
            v = tayariLocation.voitures[value]
            self.lineEditMarque.setText(v.marque)
            self.lineEditDateLocation.setText(v.dateAchat)
            self.lineEditDateLocation.setEnabled(True)
            self.lineEditCouleur.setText(v.couleur)
            self.lineEditPrixLocation.setText(str(v.prixLocation))
            self.lineEditPrixLocation.setEnabled(True)


    def retranslateUi(self, slm):
        _translate = QtCore.QCoreApplication.translate
        slm.setWindowTitle(_translate("slm", "Form"))
        self.label.setText(_translate("slm", "Modifier une voiture"))
        self.label_2.setText(_translate("slm", "Choisir la matricule"))
        self.label_3.setText(_translate("slm", "Marque"))
        self.label_4.setText(_translate("slm", "Couleur"))
        self.label_5.setText(_translate("slm", "Date d\'achat"))
        self.label_6.setText(_translate("slm", "Prix Location"))
        self.pushButton_2.setText(_translate("slm", "Modifier"))
        self.pushButton_3.setText(_translate("slm", "Annuler"))

    def chargerMatriculesDansComboBox(self):
        for i in tayariLocation.voitures.keys():
            self.comboBoxMatricule.addItem(i)


#Fenetre Ajouter Client
class Ui_AjouterClient(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 647)
        Form.setStyleSheet("QLabel{\n"
"    color:#FFFFFF;\n"
"}\n"
"QWidget{\n"
"    background-color:black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid white;\n"
"    border-radius:10px;\n"
"    color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#FFFFFF;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnAjouterClient = QtWidgets.QPushButton(Form)
        self.btnAjouterClient.setGeometry(QtCore.QRect(350, 530, 93, 28))
        self.btnAjouterClient.setObjectName("btnAjouterClient")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEditCin = QtWidgets.QLineEdit(Form)
        self.lineEditCin.setGeometry(QtCore.QRect(200, 220, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCin.setFont(font)
        self.lineEditCin.setObjectName("lineEditCin")
        self.lineEditNom = QtWidgets.QLineEdit(Form)
        self.lineEditNom.setGeometry(QtCore.QRect(200, 260, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNom.setFont(font)
        self.lineEditNom.setStyleSheet("color:white;")
        self.lineEditNom.setObjectName("lineEditNom")
        self.lineEditPrenom = QtWidgets.QLineEdit(Form)
        self.lineEditPrenom.setGeometry(QtCore.QRect(200, 300, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPrenom.setFont(font)
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.lineEditAge = QtWidgets.QLineEdit(Form)
        self.lineEditAge.setGeometry(QtCore.QRect(200, 340, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditAge.setFont(font)
        self.lineEditAge.setObjectName("lineEditAge")
        self.lineEditAdresse = QtWidgets.QLineEdit(Form)
        self.lineEditAdresse.setGeometry(QtCore.QRect(200, 380, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditAdresse.setFont(font)
        self.lineEditAdresse.setObjectName("lineEditAdresse")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 420, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEditEmail = QtWidgets.QLineEdit(Form)
        self.lineEditEmail.setGeometry(QtCore.QRect(200, 420, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditTel = QtWidgets.QLineEdit(Form)
        self.lineEditTel.setGeometry(QtCore.QRect(200, 460, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditTel.setFont(font)
        self.lineEditTel.setObjectName("lineEditTel")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnAjouterClient.clicked.connect(self.ajouterClient)

    def ajouterClient(self):
        cin = self.lineEditCin.text()
        nom = self.lineEditNom.text()
        prenom = self.lineEditPrenom.text()
        age = self.lineEditAge.text()
        adresse = self.lineEditAdresse.text()
        email = self.lineEditEmail.text()
        tel = self.lineEditTel.text()

        if(cin == "")or(nom == "")or(prenom == "")or(age == "")or(adresse == "")or(email=="")or(tel == ""):
            showMessageBox("WARNING", "Remplir tous les champs SVP")
        else:
            if cin in tayariLocation.clients.keys():
                showMessageBox("WARNING", cin + " est existe deja")
            else:
                c = Client(cin,nom,prenom,int(age),adresse,email,tel) 
                tayariLocation.ajouterClient(c)
                showMessageBox("SUCCESS",prenom + " " +  nom + " est ajouté avec succees")
       
    def remplirCin(self,cin):
        self.lineEditCin.setText(cin)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ajouter un Client"))
        self.btnAjouterClient.setText(_translate("Form", "Ajouter"))
        self.label_2.setText(_translate("Form", "CIN"))
        self.label_3.setText(_translate("Form", "Nom"))
        self.label_4.setText(_translate("Form", "Prenom"))
        self.label_5.setText(_translate("Form", "Age"))
        self.label_6.setText(_translate("Form", "Adresse"))
        self.label_7.setText(_translate("Form", "E-Mail"))
        self.label_8.setText(_translate("Form", "N-Tel"))


#Fenetre affichage Clients

class Ui_AffichageClients(object):
    def setupUi(self, AffichageClients):
        AffichageClients.setObjectName("AffichageClients")
        AffichageClients.resize(1225, 599)
        AffichageClients.setStyleSheet("\n"
"\n"
"")
        self.label = QtWidgets.QLabel(AffichageClients)
        self.label.setGeometry(QtCore.QRect(500, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidgetClient = QtWidgets.QTableWidget(AffichageClients)
        self.tableWidgetClient.setGeometry(QtCore.QRect(230, 150, 981, 441))
        self.tableWidgetClient.setObjectName("tableWidgetClient")
        self.tableWidgetClient.setColumnCount(0)
        self.tableWidgetClient.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(AffichageClients)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(AffichageClients)
        self.comboBox.setGeometry(QtCore.QRect(20, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:#FFFFFF;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.stackedWidget = QtWidgets.QStackedWidget(AffichageClients)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 270, 221, 111))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.comboBoxCin = QtWidgets.QComboBox(self.page_5)
        self.comboBoxCin.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCin.setFont(font)
        self.comboBoxCin.setStyleSheet("background-color:white;\n"
"")
        self.comboBoxCin.setObjectName("comboBoxCin")
        self.comboBoxCin.addItem("")
        self.comboBoxCin.setItemText(0, "")
        self.stackedWidget.addWidget(self.page_5)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.stackedWidget.addWidget(self.page_9)

        self.retranslateUi(AffichageClients)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AffichageClients)
        self.tableWidgetClient.setColumnCount(7)
        self.tableWidgetClient.setHorizontalHeaderLabels(["Cin", "Prenom", "Nom", "age", "adresse","email","num Tel"])
        self.chargerTousClients()
        self.comboBoxCin.addItems(tayariLocation.clients.keys())
        self.comboBox.currentIndexChanged.connect(self.changerInterface)
        self.comboBoxCin.currentTextChanged.connect(self.afficherClient)

        header = self.tableWidgetClient.horizontalHeader()
        header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
    
    def afficherClient(self,value):
        if(value != ""):
            self.tableWidgetClient.setRowCount(1)
            i = tayariLocation.clients[value]
            self.tableWidgetClient.setItem(0,0,QtWidgets.QTableWidgetItem(i.cin))
            self.tableWidgetClient.setItem(0,1,QtWidgets.QTableWidgetItem(i.prenom))
            self.tableWidgetClient.setItem(0,2,QtWidgets.QTableWidgetItem(i.nom))
            self.tableWidgetClient.setItem(0,3,QtWidgets.QTableWidgetItem(str(i.age)))
            self.tableWidgetClient.setItem(0,4,QtWidgets.QTableWidgetItem(i.adresse))
            self.tableWidgetClient.setItem(0,5,QtWidgets.QTableWidgetItem(i.email))
            self.tableWidgetClient.setItem(0,6,QtWidgets.QTableWidgetItem(i.tel))

    def chargerTousClients(self):
        row = 0
        self.tableWidgetClient.setRowCount(len(tayariLocation.clients))
        for i in tayariLocation.clients.values():
            self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(i.cin))
            self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.prenom))
            self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.nom))
            self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.age)))
            self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(i.adresse))
            self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(i.email))
            self.tableWidgetClient.setItem(row,6,QtWidgets.QTableWidgetItem(i.tel))
            row+=1

    def changerInterface(self,value):
        if(value == 0):
            self.stackedWidget.setCurrentIndex(1)
            self.chargerTousClients()
        else:
            self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, AffichageClients):
        _translate = QtCore.QCoreApplication.translate
        AffichageClients.setWindowTitle(_translate("AffichageClients", "Form"))
        self.label.setText(_translate("AffichageClients", "Liste des Clients"))
        self.label_2.setText(_translate("AffichageClients", "Filtrer par :"))
        self.comboBox.setItemText(0, _translate("AffichageClients", "Tous"))
        self.comboBox.setItemText(1, _translate("AffichageClients", "CIN"))

#Fenetre Modifier Client

class Ui_ModifierClient(object):
    def setupUi(self, slm):
        slm.setObjectName("slm")
        slm.resize(591, 743)
        slm.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}")
        self.label = QtWidgets.QLabel(slm)
        self.label.setGeometry(QtCore.QRect(90, 40, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(slm)
        self.label_2.setGeometry(QtCore.QRect(120, 150, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(slm)
        self.line.setGeometry(QtCore.QRect(80, 230, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(slm)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(slm)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(slm)
        self.label_5.setGeometry(QtCore.QRect(60, 410, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(slm)
        self.label_6.setGeometry(QtCore.QRect(60, 470, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditCouleur = QtWidgets.QLineEdit(slm)
        self.lineEditCouleur.setEnabled(False)
        self.lineEditCouleur.setGeometry(QtCore.QRect(250, 340, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCouleur.setFont(font)
        self.lineEditCouleur.setInputMask("")
        self.lineEditCouleur.setText("")
        self.lineEditCouleur.setObjectName("lineEditCouleur")
        self.lineEditDateLocation = QtWidgets.QLineEdit(slm)
        self.lineEditDateLocation.setEnabled(False)
        self.lineEditDateLocation.setGeometry(QtCore.QRect(250, 400, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateLocation.setFont(font)
        self.lineEditDateLocation.setInputMask("")
        self.lineEditDateLocation.setText("")
        self.lineEditDateLocation.setObjectName("lineEditDateLocation")
        self.lineEditPrixLocation = QtWidgets.QLineEdit(slm)
        self.lineEditPrixLocation.setEnabled(False)
        self.lineEditPrixLocation.setGeometry(QtCore.QRect(250, 460, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPrixLocation.setFont(font)
        self.lineEditPrixLocation.setInputMask("")
        self.lineEditPrixLocation.setText("")
        self.lineEditPrixLocation.setObjectName("lineEditPrixLocation")
        self.lineEditMarque = QtWidgets.QLineEdit(slm)
        self.lineEditMarque.setEnabled(False)
        self.lineEditMarque.setGeometry(QtCore.QRect(250, 280, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMarque.setFont(font)
        self.lineEditMarque.setInputMask("")
        self.lineEditMarque.setText("")
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.pushButton_2 = QtWidgets.QPushButton(slm)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 660, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(slm)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 660, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBoxMatricule = QtWidgets.QComboBox(slm)
        self.comboBoxMatricule.setGeometry(QtCore.QRect(280, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMatricule.setFont(font)
        self.comboBoxMatricule.setObjectName("comboBoxMatricule")
        self.comboBoxMatricule.addItem("")
        self.comboBoxMatricule.setItemText(0, "")
        self.label_7 = QtWidgets.QLabel(slm)
        self.label_7.setGeometry(QtCore.QRect(60, 530, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEditDateLocation_2 = QtWidgets.QLineEdit(slm)
        self.lineEditDateLocation_2.setEnabled(False)
        self.lineEditDateLocation_2.setGeometry(QtCore.QRect(250, 580, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateLocation_2.setFont(font)
        self.lineEditDateLocation_2.setInputMask("")
        self.lineEditDateLocation_2.setText("")
        self.lineEditDateLocation_2.setObjectName("lineEditDateLocation_2")
        self.lineEditCouleur_2 = QtWidgets.QLineEdit(slm)
        self.lineEditCouleur_2.setEnabled(False)
        self.lineEditCouleur_2.setGeometry(QtCore.QRect(250, 520, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCouleur_2.setFont(font)
        self.lineEditCouleur_2.setInputMask("")
        self.lineEditCouleur_2.setText("")
        self.lineEditCouleur_2.setObjectName("lineEditCouleur_2")
        self.label_9 = QtWidgets.QLabel(slm)
        self.label_9.setGeometry(QtCore.QRect(60, 590, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.comboBoxMatricule.addItems(tayariLocation.clients.keys())
        self.comboBoxMatricule.currentTextChanged.connect(self.afficherClient)
        self.pushButton_2.clicked.connect(self.modifierClient)


        self.retranslateUi(slm)
        QtCore.QMetaObject.connectSlotsByName(slm)

    def modifierClient(self):
        adresse = self.lineEditPrixLocation.text()
        tel = self.lineEditDateLocation_2.text()
        mail = self.lineEditCouleur_2.text()

        if(adresse == "")or(tel == "") or(mail==""):
            showMessageBox("WARNING", "remplir les champs vide SVP")
        else:
            cin = self.comboBoxMatricule.currentText()
            tayariLocation.clients[cin].adresse = adresse
            tayariLocation.clients[cin].tel = tel
            tayariLocation.clients[cin].email = mail
            showMessageBox("SUCCESS", "Client modifié avec succees")
            self.lineEditMarque.setText("")
            self.lineEditCouleur.setText("")
            self.lineEditDateLocation.setText("")
            self.lineEditPrixLocation.setText("")
            self.lineEditCouleur_2.setText("")
            self.lineEditDateLocation_2.setText("")

            self.lineEditDateLocation.setEnabled(False)
            self.lineEditDateLocation_2.setEnabled(False)
            self.lineEditCouleur_2.setEnabled(False)

            self.comboBoxMatricule.setCurrentIndex(0)


    def afficherClient(self, value):
        if(value != ""):
            c = tayariLocation.clients[value]
            self.lineEditMarque.setText(c.nom)
            self.lineEditCouleur.setText(c.prenom)
            self.lineEditDateLocation.setText(str(c.age))
            self.lineEditPrixLocation.setText(c.adresse)
            self.lineEditCouleur_2.setText(c.email)
            self.lineEditDateLocation_2.setText(c.tel)

            self.lineEditPrixLocation.setEnabled(True)
            self.lineEditDateLocation_2.setEnabled(True)
            self.lineEditCouleur_2.setEnabled(True)

        else:
            self.lineEditMarque.setText("")
            self.lineEditCouleur.setText("")
            self.lineEditDateLocation.setText("")
            self.lineEditPrixLocation.setText("")
            self.lineEditCouleur_2.setText("")
            self.lineEditDateLocation_2.setText("")

            self.lineEditDateLocation.setEnabled(False)
            self.lineEditDateLocation_2.setEnabled(False)
            self.lineEditCouleur_2.setEnabled(False)
            
    def retranslateUi(self, slm):
        _translate = QtCore.QCoreApplication.translate
        slm.setWindowTitle(_translate("slm", "Form"))
        self.label.setText(_translate("slm", "Modifier un Client"))
        self.label_2.setText(_translate("slm", "Choisir la matricule"))
        self.label_3.setText(_translate("slm", "Nom"))
        self.label_4.setText(_translate("slm", "Prenom"))
        self.label_5.setText(_translate("slm", "Age"))
        self.label_6.setText(_translate("slm", "Adresse"))
        self.pushButton_2.setText(_translate("slm", "Modifier"))
        self.pushButton_3.setText(_translate("slm", "Annuler"))
        self.label_7.setText(_translate("slm", "Email"))
        self.label_9.setText(_translate("slm", "Tel"))


#Fenetre supprimer client
class Ui_SupprimerClient(object):
    def setupUi(self, SupprimerClient):
        SupprimerClient.setObjectName("SupprimerClient")
        SupprimerClient.resize(564, 204)
        self.label = QtWidgets.QLabel(SupprimerClient)
        self.label.setGeometry(QtCore.QRect(160, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(SupprimerClient)
        self.comboBox.setGeometry(QtCore.QRect(230, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.pushButton = QtWidgets.QPushButton(SupprimerClient)
        self.pushButton.setGeometry(QtCore.QRect(240, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.comboBox.addItems(tayariLocation.clients.keys())

        self.pushButton.clicked.connect(self.supprimerClient)

        self.retranslateUi(SupprimerClient)
        QtCore.QMetaObject.connectSlotsByName(SupprimerClient)

    def supprimerClient(self):
        cin = self.comboBox.currentText()
        if(cin == ""):
            showMessageBox("WARNING", "Choisir un client a supprimer")
        else:
            tayariLocation.supprimerClient(cin)
            showMessageBox("SUCCESS", cin + " supprimé avec succees")
            self.comboBox.removeItem(self.comboBox.currentIndex())
            self.comboBox.setCurrentIndex(0)

    def retranslateUi(self, SupprimerClient):
        _translate = QtCore.QCoreApplication.translate
        SupprimerClient.setWindowTitle(_translate("SupprimerClient", "Form"))
        self.label.setText(_translate("SupprimerClient", "CIN"))
        self.pushButton.setText(_translate("SupprimerClient", "Supprimer"))


#fenetre ajouter Location
class Ui_AjouterLocation(object):
    def setupUi(self, AjouterLocation):
        AjouterLocation.setObjectName("AjouterLocation")
        AjouterLocation.resize(378, 425)
        self.label = QtWidgets.QLabel(AjouterLocation)
        self.label.setGeometry(QtCore.QRect(0, 40, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AjouterLocation)
        self.label_2.setGeometry(QtCore.QRect(60, 172, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AjouterLocation)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AjouterLocation)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AjouterLocation)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditCin = QtWidgets.QLineEdit(AjouterLocation)
        self.lineEditCin.setGeometry(QtCore.QRect(140, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCin.setFont(font)
        self.lineEditCin.setText("")
        self.lineEditCin.setObjectName("lineEditCin")
        self.lineEditDureeLocation = QtWidgets.QLineEdit(AjouterLocation)
        self.lineEditDureeLocation.setGeometry(QtCore.QRect(140, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDureeLocation.setFont(font)
        self.lineEditDureeLocation.setObjectName("lineEditDureeLocation")
        self.lineEditDateLocation = QtWidgets.QLineEdit(AjouterLocation)
        self.lineEditDateLocation.setGeometry(QtCore.QRect(140, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateLocation.setFont(font)
        self.lineEditDateLocation.setObjectName("lineEditDateLocation")
        self.comboBoxMatricule = QtWidgets.QComboBox(AjouterLocation)
        self.comboBoxMatricule.setGeometry(QtCore.QRect(140, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMatricule.setFont(font)
        self.comboBoxMatricule.setObjectName("comboBoxMatricule")
        self.btnAjouterLocation = QtWidgets.QPushButton(AjouterLocation)
        self.btnAjouterLocation.setGeometry(QtCore.QRect(260, 330, 75, 25))
        self.btnAjouterLocation.setObjectName("btnAjouterLocation")

        dateValidator = QRegExpValidator(QRegExp(r'\b^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$\b'))
        cinValidator = QRegExpValidator(QRegExp(r'\b([1]|[0])[0-9][0-9][0-9][0-9][0-9][0-9][0-9]\b'))

        self.lineEditDateLocation.setPlaceholderText("YYYY-MM-DD")
        self.lineEditDateLocation.setValidator(dateValidator)

        self.lineEditDateLocation.setText(str(datetime.now().date()))
        self.lineEditDureeLocation.setText("1")

        self.lineEditCin.setValidator(cinValidator)
        self.btnAjouterLocation.clicked.connect(self.actionAjouterLocation)
        self.comboBoxMatricule.addItems(tayariLocation.voitures.keys())
        self.retranslateUi(AjouterLocation)
        QtCore.QMetaObject.connectSlotsByName(AjouterLocation)

    def actionAjouterLocation(self):
        cin = self.lineEditCin.text()
        if(cin in tayariLocation.clients.keys()):
            matricule = self.comboBoxMatricule.currentText()
            dateLocation = self.lineEditDateLocation.text()
            dureeLocation = self.lineEditDureeLocation.text()

            if(tayariLocation.disponible(matricule,dateLocation,dureeLocation)):
                l = Location(cin,matricule,dateLocation,int(dureeLocation),tayariLocation.voitures[matricule].prixLocation)
                tayariLocation.ajouterLocation(l)
                showMessageBox("SUCCESS","Location est ajouté avec succees")
                self.lineEditCin.setText("")
                self.comboBoxMatricule.setCurrentIndex(0)

            else:
                showMessageBox("WARNING","cette voiture n'est pas disponible durant cette durée")
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Client " + cin + " n'existe pas !!!")
            msg.setInformativeText("voulez vous l'ajouter?")
            msg.setWindowTitle("WARNING")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
            if(retval == QMessageBox.Ok):
                self.ouvrirMenuAjouterClient()

    def ouvrirMenuAjouterClient(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AjouterClient()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.remplirCin(self.lineEditCin.text())

    def retranslateUi(self, AjouterLocation):
        _translate = QtCore.QCoreApplication.translate
        AjouterLocation.setWindowTitle(_translate("AjouterLocation", "Form"))
        self.label.setText(_translate("AjouterLocation", "Ajouter une location"))
        self.label_2.setText(_translate("AjouterLocation", "Cin"))
        self.label_3.setText(_translate("AjouterLocation", "Matricule"))
        self.label_4.setText(_translate("AjouterLocation", "Date Location"))
        self.label_5.setText(_translate("AjouterLocation", "Duree Location"))
        self.btnAjouterLocation.setText(_translate("AjouterLocation", "Ajouter"))


#Fenetre Affichage Locations
class Ui_AffichageLocations(object):
    def setupUi(self, AffichageClients):
        AffichageClients.setObjectName("AffichageClients")
        AffichageClients.resize(1000, 599)
        AffichageClients.setStyleSheet("")
        self.label = QtWidgets.QLabel(AffichageClients)
        self.label.setGeometry(QtCore.QRect(400, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidgetClient = QtWidgets.QTableWidget(AffichageClients)
        self.tableWidgetClient.setGeometry(QtCore.QRect(230, 150, 760, 441))
        self.tableWidgetClient.setObjectName("tableWidgetClient")
        self.tableWidgetClient.setColumnCount(0)
        self.tableWidgetClient.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(AffichageClients)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(AffichageClients)
        self.comboBox.setGeometry(QtCore.QRect(20, 220, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:#FFFFFF;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.stackedWidget = QtWidgets.QStackedWidget(AffichageClients)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 270, 221, 141))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.stackedWidget.addWidget(self.page_9)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.comboBoxCin = QtWidgets.QComboBox(self.page)
        self.comboBoxCin.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxCin.setFont(font)
        self.comboBoxCin.setStyleSheet("background-color:#FFFFFF;")
        self.comboBoxCin.setObjectName("comboBoxCin")
        self.comboBoxCin.addItem("")
        self.comboBoxCin.setItemText(0, "")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.comboBoxMatricule = QtWidgets.QComboBox(self.page_2)
        self.comboBoxMatricule.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxMatricule.setFont(font)
        self.comboBoxMatricule.setStyleSheet("background-color:#FFFFFF;")
        self.comboBoxMatricule.setObjectName("comboBoxMatricule")
        self.comboBoxMatricule.addItem("")
        self.comboBoxMatricule.setItemText(0, "")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.lineEditDateDonnee = QtWidgets.QLineEdit(self.page_3)
        self.lineEditDateDonnee.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        self.pushButtonValider = QtWidgets.QPushButton(self.page_3)
        self.pushButtonValider.setGeometry(QtCore.QRect(60,60,80,31))
        self.pushButtonValider.setText("Valider")
        font.setPointSize(10)
        self.lineEditDateDonnee.setFont(font)
        self.lineEditDateDonnee.setText("")
        self.lineEditDateDonnee.setObjectName("lineEditDateDonnee")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.lineEditDureeDonnee = QtWidgets.QLineEdit(self.page_4)
        self.lineEditDureeDonnee.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDureeDonnee.setFont(font)
        self.lineEditDureeDonnee.setText("")
        self.lineEditDureeDonnee.setObjectName("lineEditDureeDonnee")
        self.stackedWidget.addWidget(self.page_4)
        self.page_11 = QtWidgets.QWidget()
        self.pushButtonValider1 = QtWidgets.QPushButton(self.page_4)
        self.pushButtonValider1.setGeometry(QtCore.QRect(60,60,80,31))
        self.pushButtonValider1.setText("Valider")
        self.page_11.setObjectName("page_11")
        self.lineEditDateDebut = QtWidgets.QLineEdit(self.page_11)
        self.lineEditDateDebut.setGeometry(QtCore.QRect(40, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateDebut.setFont(font)
        self.lineEditDateDebut.setText("")
        self.lineEditDateDebut.setObjectName("lineEditDateDebut")
        self.lineEditDateDateFin = QtWidgets.QLineEdit(self.page_11)
        self.lineEditDateDateFin.setGeometry(QtCore.QRect(40, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateDateFin.setFont(font)
        self.lineEditDateDateFin.setText("")
        self.lineEditDateDateFin.setObjectName("lineEditDateDateFin")
        self.pushButton = QtWidgets.QPushButton(self.page_11)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidgetClient.setColumnCount(6)
        self.tableWidgetClient.setHorizontalHeaderLabels(["Num","Cin","Matricule","Date Location","Duree Location","Montant"])
        self.stackedWidget.addWidget(self.page_11)

        self.chargerTousLesDonnees()

        self.comboBox.currentIndexChanged.connect(self.changerFenetre)

        self.comboBoxCin.addItems(tayariLocation.clients.keys())
        self.comboBoxMatricule.addItems(tayariLocation.voitures.keys())

        self.lineEditDateDonnee.setPlaceholderText("date : YYYY-MM-DD")
        self.lineEditDureeDonnee.setPlaceholderText("saisir une durée")
        self.lineEditDateDebut.setPlaceholderText("début : YYYY-MM-DD")
        self.lineEditDateDateFin.setPlaceholderText("début : YYYY-MM-DD")
        self.pushButtonValider1.clicked.connect(self.filtrerParDuree)
        self.pushButtonValider.clicked.connect(self.filtrerParDate)

        self.comboBoxCin.currentTextChanged.connect(self.chargerLocationCin)
        self.comboBoxMatricule.currentTextChanged.connect(self.chargerLocationMatricule)

        self.retranslateUi(AffichageClients)    
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AffichageClients)


    def filtrerParDate(self):
        date = self.lineEditDateDonnee.text()
        row = 0
        for i in tayariLocation.locations.values():
            if(i.dateLocation == date):
                row+=1
        self.tableWidgetClient.setRowCount(row)

        row = 0
        for i in tayariLocation.locations.values():
            if(i.dateLocation == date):
                self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.num)))
                self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.cin))
                self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(i.dateLocation))
                self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.dureeLocation)))
                self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.montant)))
                row+=1

    def filtrerParDuree(self):
        duree = int(self.lineEditDureeDonnee.text())
        row = 0
        for i in tayariLocation.locations.values():
            if(i.dureeLocation == duree):
                row+=1
        self.tableWidgetClient.setRowCount(row)
        
        row = 0
        for i in tayariLocation.locations.values():
            if(i.dureeLocation == duree):
                self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.num)))
                self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.cin))
                self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(i.dateLocation))
                self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.dureeLocation)))
                self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.montant)))
                row+=1

    def chargerLocationMatricule(self,value):
        row = 0
        for i in tayariLocation.locations.values():
            if(i.matricule == value):
                row+=1
        self.tableWidgetClient.setRowCount(row)
        
        row = 0
        for i in tayariLocation.locations.values():
            if(i.matricule == value):
                self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.num)))
                self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.cin))
                self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(i.dateLocation))
                self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.dureeLocation)))
                self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.montant)))
                row+=1

    def chargerLocationCin(self,value):
        row = 0
        for i in tayariLocation.locations.values():
            if(i.cin == value):
                row+=1
        self.tableWidgetClient.setRowCount(row)
        
        row = 0
        for i in tayariLocation.locations.values():
            if(i.cin == value):
                self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.num)))
                self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.cin))
                self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.matricule))
                self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(i.dateLocation))
                self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.dureeLocation)))
                self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.montant)))
                row+=1


    def changerFenetre(self,value):
        self.stackedWidget.setCurrentIndex(value)
        if(value == 0):
            self.chargerTousLesDonnees()
        # elif value == 2:
        #     self.chargerLocationMatricule()
        
    
    def chargerTousLesDonnees(self):
        row = 0
        self.tableWidgetClient.setRowCount(len(tayariLocation.locations))
        for i in tayariLocation.locations.values():
            self.tableWidgetClient.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.num)))
            self.tableWidgetClient.setItem(row,1,QtWidgets.QTableWidgetItem(i.cin))
            self.tableWidgetClient.setItem(row,2,QtWidgets.QTableWidgetItem(i.matricule))
            self.tableWidgetClient.setItem(row,3,QtWidgets.QTableWidgetItem(i.dateLocation))
            self.tableWidgetClient.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.dureeLocation)))
            self.tableWidgetClient.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.montant)))
            row+=1


    def retranslateUi(self, AffichageClients):
        _translate = QtCore.QCoreApplication.translate
        AffichageClients.setWindowTitle(_translate("AffichageClients", "Form"))
        self.label.setText(_translate("AffichageClients", "Liste des Locations"))
        self.label_2.setText(_translate("AffichageClients", "Filtrer par :"))
        self.comboBox.setItemText(0, _translate("AffichageClients", "Tous"))
        self.comboBox.setItemText(1, _translate("AffichageClients", "CIN"))
        self.comboBox.setItemText(2, _translate("AffichageClients", "Matricule"))
        self.comboBox.setItemText(3, _translate("AffichageClients", "Une Date Donnée"))
        self.comboBox.setItemText(4, _translate("AffichageClients", "Duree de Location"))
        self.comboBox.setItemText(5, _translate("AffichageClients", "Entre deux date donnée"))
        self.pushButton.setText(_translate("AffichageClients", "Trouver"))

#Fenetre Supprimer Location

class Ui_SupprimerLocation(object):
    def setupUi(self, SupprimerClient):
        SupprimerClient.setObjectName("SupprimerClient")
        SupprimerClient.resize(564, 204)
        self.label = QtWidgets.QLabel(SupprimerClient)
        self.label.setGeometry(QtCore.QRect(50, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxNumeroLocation = QtWidgets.QComboBox(SupprimerClient)
        self.comboBoxNumeroLocation.setGeometry(QtCore.QRect(280, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNumeroLocation.setFont(font)
        self.comboBoxNumeroLocation.setObjectName("comboBoxNumeroLocation")
        self.comboBoxNumeroLocation.addItem("")
        self.comboBoxNumeroLocation.setItemText(0, "")
        self.pushButtonSupprimerLocation = QtWidgets.QPushButton(SupprimerClient)
        self.pushButtonSupprimerLocation.setGeometry(QtCore.QRect(240, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSupprimerLocation.setFont(font)
        self.pushButtonSupprimerLocation.setObjectName("pushButtonSupprimerLocation")
        for i in tayariLocation.locations.keys():
            self.comboBoxNumeroLocation.addItem(str(i))
        
        self.pushButtonSupprimerLocation.clicked.connect(self.supprimerLocation)


        self.retranslateUi(SupprimerClient)
        QtCore.QMetaObject.connectSlotsByName(SupprimerClient)
    
    def supprimerLocation(self):
        num = int(self.comboBoxNumeroLocation.currentText())
        self.comboBoxNumeroLocation.removeItem(self.comboBoxNumeroLocation.currentIndex())
        tayariLocation.supprimerLocation(num)
        showMessageBox("SUCCESS","Location à été supprimer avec succées")
        self.comboBoxNumeroLocation.setCurrentIndex(0)

    def retranslateUi(self, SupprimerClient):
        _translate = QtCore.QCoreApplication.translate
        SupprimerClient.setWindowTitle(_translate("SupprimerClient", "Form"))
        self.label.setText(_translate("SupprimerClient", "Numero de Location"))
        self.pushButtonSupprimerLocation.setText(_translate("SupprimerClient", "Supprimer"))


#Fenetre Modifier Location
class Ui_ModifierLocation(object):
    def setupUi(self, slm):
        slm.setObjectName("slm")
        slm.resize(593, 692)
        slm.setStyleSheet("background-color:white;")
        self.label = QtWidgets.QLabel(slm)
        self.label.setGeometry(QtCore.QRect(90, 40, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(slm)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(slm)
        self.line.setGeometry(QtCore.QRect(80, 230, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(slm)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(slm)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(slm)
        self.label_5.setGeometry(QtCore.QRect(60, 410, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(slm)
        self.label_6.setGeometry(QtCore.QRect(60, 470, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditMatricule = QtWidgets.QLineEdit(slm)
        self.lineEditMatricule.setEnabled(False)
        self.lineEditMatricule.setGeometry(QtCore.QRect(250, 340, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditMatricule.setFont(font)
        self.lineEditMatricule.setInputMask("")
        self.lineEditMatricule.setText("")
        self.lineEditMatricule.setObjectName("lineEditMatricule")
        self.lineEditDateLocation = QtWidgets.QLineEdit(slm)
        self.lineEditDateLocation.setEnabled(False)
        self.lineEditDateLocation.setGeometry(QtCore.QRect(250, 400, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDateLocation.setFont(font)
        self.lineEditDateLocation.setInputMask("")
        self.lineEditDateLocation.setText("")
        self.lineEditDateLocation.setObjectName("lineEditDateLocation")
        self.lineEditDureeLocation = QtWidgets.QLineEdit(slm)
        self.lineEditDureeLocation.setEnabled(False)
        self.lineEditDureeLocation.setGeometry(QtCore.QRect(250, 460, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDureeLocation.setFont(font)
        self.lineEditDureeLocation.setInputMask("")
        self.lineEditDureeLocation.setText("")
        self.lineEditDureeLocation.setObjectName("lineEditDureeLocation")
        self.lineEditCin = QtWidgets.QLineEdit(slm)
        self.lineEditCin.setEnabled(False)
        self.lineEditCin.setGeometry(QtCore.QRect(250, 280, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditCin.setFont(font)
        self.lineEditCin.setInputMask("")
        self.lineEditCin.setText("")
        self.lineEditCin.setObjectName("lineEditCin")
        self.pushButtonModifier = QtWidgets.QPushButton(slm)
        self.pushButtonModifier.setGeometry(QtCore.QRect(410, 610, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonModifier.setFont(font)
        self.pushButtonModifier.setObjectName("pushButtonModifier")
        self.pushButton_3 = QtWidgets.QPushButton(slm)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 610, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBoxNumero = QtWidgets.QComboBox(slm)
        self.comboBoxNumero.setGeometry(QtCore.QRect(280, 150, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxNumero.setFont(font)
        self.comboBoxNumero.setObjectName("comboBoxNumero")
        self.comboBoxNumero.addItem("")
        self.comboBoxNumero.setItemText(0, "")
        self.label_7 = QtWidgets.QLabel(slm)
        self.label_7.setGeometry(QtCore.QRect(60, 530, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEditDureeMontant = QtWidgets.QLineEdit(slm)
        self.lineEditDureeMontant.setEnabled(False)
        self.lineEditDureeMontant.setGeometry(QtCore.QRect(250, 520, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDureeMontant.setFont(font)
        self.lineEditDureeMontant.setInputMask("")
        self.lineEditDureeMontant.setText("")
        self.lineEditDureeMontant.setObjectName("lineEditDureeMontant")

        for i in tayariLocation.locations.keys():
            self.comboBoxNumero.addItem(str(i))
        
        self.comboBoxNumero.currentTextChanged.connect(self.chargerDonnee)
        self.pushButtonModifier.clicked.connect(self.modifierLocation)

        self.retranslateUi(slm)
        QtCore.QMetaObject.connectSlotsByName(slm)

    def modifierLocation(self):
        num = int(self.comboBoxNumero.currentText())
        date = self.lineEditDateLocation.text()
        duree = self.lineEditDureeLocation.text()
        if not duree.isnumeric() or float(duree)<0 or len(duree) == 0:
            showMessageBox("WARNING", "Duree est invalide")
        elif len(date) == 0:
            showMessageBox("WARNING", "Date est invalide")
        else:
            tayariLocation.locations[num].dateLocation = date
            tayariLocation.locations[num].dureeLocation = int(duree)
            tayariLocation.locations[num].montant = int(duree) * tayariLocation.voitures[self.lineEditMatricule.text()].prixLocation
            self.lineEditCin.setText("")
            self.lineEditDateLocation.setText("")
            self.lineEditMatricule.setText("")
            self.lineEditDureeLocation.setText("")
            self.lineEditDureeMontant.setText("")
            self.lineEditDateLocation.setEnabled(False)
            self.lineEditDureeLocation.setEnabled(False)
            self.comboBoxNumero.setCurrentIndex(0)
            showMessageBox("SUCCESS", "Location Modifié avec succées")



        

    def chargerDonnee(self,value):
        if len(value) != 0:            
            num = int(value)
            l = tayariLocation.locations[num]
            self.lineEditCin.setText(l.cin)
            self.lineEditDateLocation.setText(l.dateLocation)
            self.lineEditMatricule.setText(l.matricule)
            self.lineEditDureeLocation.setText(str(l.dureeLocation))
            self.lineEditDureeMontant.setText(str(l.montant))

            self.lineEditDateLocation.setEnabled(True)
            self.lineEditDureeLocation.setEnabled(True)
        else:
            self.lineEditCin.setText("")
            self.lineEditDateLocation.setText("")
            self.lineEditMatricule.setText("")
            self.lineEditDureeLocation.setText("")
            self.lineEditDureeMontant.setText("")
            self.lineEditDateLocation.setEnabled(False)
            self.lineEditDureeLocation.setEnabled(False)
           


    def retranslateUi(self, slm):
        _translate = QtCore.QCoreApplication.translate
        slm.setWindowTitle(_translate("slm", "Form"))
        self.label.setText(_translate("slm", "Modifier une Location"))
        self.label_2.setText(_translate("slm", "Choisir le numéro de Location"))
        self.label_3.setText(_translate("slm", "CIN"))
        self.label_4.setText(_translate("slm", "Matricule"))
        self.label_5.setText(_translate("slm", "Date Location"))
        self.label_6.setText(_translate("slm", "Durée Location"))
        self.pushButtonModifier.setText(_translate("slm", "Modifier"))
        self.pushButton_3.setText(_translate("slm", "Annuler"))
        self.label_7.setText(_translate("slm", "Montant"))
