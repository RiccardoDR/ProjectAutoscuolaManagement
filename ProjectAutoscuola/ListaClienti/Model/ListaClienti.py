import os
import pickle


class ListaClienti:  # Gestisce i dati e le operazioni relative alla lista clienti.
    def __init__(self):
        self.lista_clienti = []
        self.sorted = []

    # Il seguente blocco carica nella variabile lista_clienti la lista
    # dei clienti contenuta nel file 'lista-clienti.pickle'.
    def set_data(self):
        if os.stat('ListaClienti/Data/lista_clienti.pickle').st_size != 0:
            if os.path.isfile('ListaClienti/Data/lista_clienti.pickle'):
                with open('ListaClienti/Data/lista_clienti.pickle', 'rb') as f:
                    self.lista_clienti = pickle.load(f)
                    self.sorted = sorted(self.lista_clienti, key=lambda x: (x.get_cognome()))

    # == aggiungi_cliente ==
    # La funzione si occupa di aggiungere le informazioni relative al nuovo cliente
    # nel file 'lista_clienti.pickle' in append.
    def aggiungi_cliente(self, cliente):
        self.sorted.append(cliente)
        self.sorted = sorted(self.sorted, key=lambda x: (x.get_cognome()))

    # == rimuovi_cliente_by_id ==
    # La funzione ha il compito di eliminare dal file 'lista_clienti.pickle' tutte le
    # informazioni relative al cliente con l'id corrispondente a quello preso in input.
    def rimuovi_cliente_by_index(self, i):
        cliente = self.sorted[i]
        self.sorted.remove(cliente)

    # == get_lista_clienti ==
    # La funzione ritorna la lista_clienti.
    def get_lista_clienti(self):
        return self.sorted

    # == save_data ==
    # La funzione si occupa di salvare eventuali modifiche dei
    # dati relativi ai clienti e contenuti nella lista_clienti.
    def save_data(self):
        with open('ListaClienti/Data/lista_clienti.pickle', 'wb') as handle:
            pickle.dump(self.sorted, handle, pickle.HIGHEST_PROTOCOL)



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moonesfYqz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 850)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"../Image/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.000000000000000)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Logo = QToolButton(self.centralwidget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(50, 30, 120, 120))
        self.Logo.setMinimumSize(QSize(50, 50))
        self.Logo.setMaximumSize(QSize(150, 150))
        self.Logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet(u"background-color: transparent;")
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QSize(110, 110))
        self.Logo.setCheckable(False)
        self.Logo.setPopupMode(QToolButton.DelayedPopup)
        self.Logo.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.Logo.setAutoRaise(False)
        self.Logo.setArrowType(Qt.NoArrow)
        self.Search = QLineEdit(self.centralwidget)
        self.Search.setObjectName(u"Search")
        self.Search.setEnabled(True)
        self.Search.setGeometry(QRect(250, 70, 690, 40))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.Search.setFont(font)
        self.Search.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Search.setAcceptDrops(True)
        self.Search.setStyleSheet(u"background-color: black; color:white; border: 1px solid white; border-radius: 10px;")
        self.Search.setMaxLength(100)
        self.Search.setFrame(True)
        self.Search.setDragEnabled(False)
        self.Search.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.Search.setClearButtonEnabled(False)
        self.Menu = QToolButton(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setEnabled(True)
        self.Menu.setGeometry(QRect(1160, 60, 60, 59))
        self.Menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.Menu.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"../Image/navigation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon1)
        self.Menu.setIconSize(QSize(50, 50))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1050, 950))
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet(u"background-color: rgba(,0,0,0.6)")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setPixmap(QPixmap(u"../Image/universe.jpg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(275, 225, 500, 500))
        self.label_2.setStyleSheet(u"border: 2px solid white; border-radius: 10px;")
        self.label_2.setPixmap(QPixmap(u"../Image/navigation.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(275, 525, 500, 200))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"backgroud-color: transparent; color: white")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(2)
        self.label_3.setIndent(0)
        self.label_3.setOpenExternalLinks(False)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(275, 225, 500, 500))
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(u"background-color: transparent;")
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(97, 435, 80, 80))
        self.toolButton_2.setStyleSheet(u"background-color: transparent;")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QSize(80, 80))
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(872, 435, 80, 80))
        self.toolButton_3.setStyleSheet(u"background-color: transparent")
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QSize(80, 80))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 500, 55, 16))
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.Logo.raise_()
        self.Search.raise_()
        self.Menu.raise_()
        self.label_2.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        self.toolButton_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Moon", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Search.setText("")
        self.Search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.Menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Descrizioneeeeeeeeeeeeeeee", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dataaaaaaa", None))
    # retranslateUi

