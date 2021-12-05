from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QToolButton, QAction, QMessageBox, QPushButton

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Home.View import VistaAccesso, VistaHomeSegretario
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni
from ProgettoAutoscuola.ListaPrenotazioni.View.VistaListaPrenotazioni import VistaListaPrenotazioni
from ProgettoAutoscuola.ListaPrenotazioni.View.VistaDisdettaPrenotazione import VistaDisdettaPrenotazione
from ProgettoAutoscuola.ListaPrenotazioni.View.VistaInserisciEsitoEsame import VistaInserisciEsitoEsame
from ProgettoAutoscuola.Prenotazione.View.VistaPrenotazione import VistaPrenotazione


class VistaHomeIstruttore(QWidget):  # Apre e visualizza la vista home con le funzioni consentite all'istruttore.
    def __init__(self, tipo):
        super(VistaHomeIstruttore, self).__init__()
        self.tipo = tipo

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Home Istruttore")
        self.resize(800, 600)
        self.setFixedSize(self.size())

        self.controller = ControllerListaPrenotazioni()
        self.controller.set_data()
        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Il seguente blocco crea le azioni che saranno svolte dai bottoni, i bottoni
        # che saranno presenti sulla schermata e i collegamenti tra i due.
        self.action_prenota = QAction()
        self.action_elenco_prenotazioni = QAction()
        self.action_disdetta = QAction()
        self.action_esiti = QAction()

        self.create_button1('Image/prenota.png', 'Lista orari', 210, self.action_elenco_prenotazioni)
        self.create_button1('Image/lista.png', 'Prenota cliente', 410, self.action_prenota)

        self.create_button2('Image/disdici_visita.png', 'Disdici prenotazione', 210, self.action_disdetta)
        self.create_button2('Image/patente.png', 'Esiti esami', 410, self.action_esiti)

        self.action_prenota.triggered.connect(self.go_prenota)
        self.action_elenco_prenotazioni.triggered.connect(self.go_lista)
        self.action_disdetta.triggered.connect(self.go_disdici)
        self.action_esiti.triggered.connect(self.go_esiti)

        # Se a questa classe viene passato  come parametro il tipo 'Segretario' allora questa vista verrà aperta
        # come vista che permette al segretario di gestire le prenotazioni.
        if self.tipo == "Segretario":
            self.button_back = QPushButton(self)
            self.button_back.setIcon(QIcon('Image/back.png'))
            self.button_back.setIconSize(QSize(90, 90))
            self.button_back.setGeometry(60, 490, 90, 90)
            self.button_back.clicked.connect(self.go_back)
        else:
            self.button_logout = QPushButton(self)
            self.button_logout.setIcon(QIcon('Image/logout.png'))
            self.button_logout.setIconSize(QSize(90, 90))
            self.button_logout.setGeometry(80, 480, 90, 90)
            self.button_logout.clicked.connect(self.logout)

    # == create_button ==
    # La funzione crea i bottoni che saranno presenti sulla schermata nella prima colonna prendendo per input
    # il path dell immagine che rappresenterà il bottone, il suo nome, la posizione che avrà nella
    # schermata e quale azione dovrà compiere una volta premuto.
    # La funzione si occupa dei bottoni anche dal punto di vista grafico.
    def create_button1(self, path_img, nome, posizione, action):
        button = QToolButton(self)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        font_button = QFont("Times", 11)
        button.setFont(font_button)
        button.setGeometry(posizione, 200, 180, 80)
        action.setIcon(QIcon(path_img))
        action.setText(nome)
        button.setIconSize(QSize(50, 50))
        button.setDefaultAction(action)
        button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; border-radius: 10px;}'
                             'QToolButton::Hover{background-color: #00afff}')

    # == create_button2 ==
    # La funzione crea i bottoni che saranno presenti sulla schermata nella seconda colonna prendendo per input
    # il path dell immagine che rappresenterà il bottone, il suo nome, la posizione che avrà nella
    # schermata e quale azione dovrà compiere una volta premuto.
    # La funzione si occupa dei bottoni anche dal punto di vista grafico.
    def create_button2(self, path_img, nome, posizione, action):
        button = QToolButton(self)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        font_button = QFont("Times", 11)
        button.setFont(font_button)
        button.setGeometry(posizione, 300, 180, 80)
        action.setIcon(QIcon(path_img))
        action.setText(nome)
        button.setIconSize(QSize(50, 50))
        button.setDefaultAction(action)
        button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; border-radius: 10px;}'
                             'QToolButton::Hover{background-color: #00afff}')

    # == go_lista ==
    # La funzione si occupa di aprire la VistaListaPrenotazioni.
    def go_lista(self):
        self.prenota_visita = VistaListaPrenotazioni(self.tipo)
        self.prenota_visita.show()
        self.close()

    # == go_prenota ==
    # La funzione si occupa di controllare che il pagamento iniziale da parte di un cliente è stato effettuato.
    # Successivamente, se sono presenti informazioni nella lista delle prenotazioni verrà aperta
    # la VistaPrenotazione, in caso contrario verrà inviato un messaggio di errore all'utente. Anche nel caso
    # in cui nessun cliente abbia effettuato il pagamento iniziale viene inviato un messaggio di errore.
    def go_prenota(self):
        trovato = False
        for cliente in self.controller_clienti.get_lista_clienti():
            controller_cliente = ControllerCliente(cliente)
            if controller_cliente.get_pagamento_iniziale() != "None":
                trovato = True
        if trovato:
            if self.controller.get_lista_prenotazioni():
                self.go_prenotazione = VistaPrenotazione(self.tipo)
                self.go_prenotazione.show()
                self.close()
            else:
                QMessageBox.information(self, "Errore", "Nessuna data disponibile per prenotarsi")

        else:
            QMessageBox.information(self, "Errore", "Nessun cliente ha pagato la rata iniziale")


    # == go_disdici ==
    # La funzione controlla innanzitutto che ci siano clienti nella lista_clienti a cui sono associate delle
    # prenotazioni. Se ce ne sono viene allora aperta la VistaDisdettaPrenotazione, altrimenti viene inviato un
    # messaggio di errore.
    def go_disdici(self):
        trovato = False
        for cliente in self.controller_clienti.get_lista_clienti():
            controller_cliente = ControllerCliente(cliente)
            if controller_cliente.get_prenotazione() != "None":
                trovato = True
        if trovato:
            self.vista_esiti = VistaDisdettaPrenotazione(self.tipo)
            self.vista_esiti.show()
            self.close()
        else:
            QMessageBox.information(self, "Attenzione", "Nessun cliente si è prenotato")

    # == go_esiti ==
    # La funzione per prima cosa controlla se ci sono clienti con prenotazioni per lezioni ad esso
    # associate. Se questo controllo è soddisfatto allora viene aperta la VistaInserisciEsitoEsame.
    # In caso contrario sarà inviato un messaggio di errore.
    def go_esiti(self):
        trovato = False
        for cliente in self.controller_clienti.get_lista_clienti():
            controller_cliente = ControllerCliente(cliente)
            if controller_cliente.get_prenotazione() != "None":
                nome = controller_cliente.get_prenotazione().split("-")
                if nome[2].strip() != "Lezione":
                    trovato = True
        if trovato:
            self.go_esito = VistaInserisciEsitoEsame(self.tipo)
            self.go_esito.show()
            self.close()
        else:
            QMessageBox.information(self, "Attenzione", "Nessun cliente prenotato per un esame")

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeSegretario.VistaHomeSegretario()
        self.go_home.show()
        self.close()

    def logout(self):
        QMessageBox.information(self, "Arrivederci", "Sessione terminata")
        self.vista_accesso = VistaAccesso.VistaAccesso()
        self.vista_accesso.show()
        self.close()
