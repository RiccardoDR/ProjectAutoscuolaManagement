from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QToolButton, QAction, QMessageBox, QPushButton

from ProgettoAutoscuola.VisitaMedica.Controller.ControllerVisitaMedica import ControllerVisitaMedica
from ProgettoAutoscuola.Home.View import VistaAccesso
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.ListaVisiteMediche.View.VistaListaVisiteMediche import VistaListaVisiteMediche
from ProgettoAutoscuola.ListaVisiteMediche.View.VistaDisdiciVisitaMedica import VistaDisdiciVisitaMedica
from ProgettoAutoscuola.ListaVisiteMediche.View.VistaInserisciEsitoVisita import VistaInserisciEsitoVisita


class VistaHomeMedico(QWidget):  # Apre e visualizza la vista home con le funzioni consentite al medico.
    def __init__(self, parent=None):
        super(VistaHomeMedico, self).__init__(parent)

        self.controller = ControllerListaVisiteMediche()
        self.controller.set_data()

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Home Medico")
        self.resize(800, 500)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Il seguente blocco crea le azioni che saranno svolte dai bottoni, i bottoni
        # che saranno presenti sulla schermata e i collegamenti tra i due.
        self.action_visita = QAction()
        self.action_esiti = QAction()
        self.action_disdetta = QAction()

        self.create_button('Image/dottore.png', 'Lista prenotazioni', 110, self.action_visita)
        self.create_button('Image/esito.png', 'Esito visita', 310, self.action_esiti)
        self.create_button('Image/disdici_visita.png', 'Disdici visita', 510, self.action_disdetta)

        self.action_visita.triggered.connect(self.go_visita)
        self.action_esiti.triggered.connect(self.go_esiti)
        self.action_disdetta.triggered.connect(self.go_disdici)

        self.button_logout = QPushButton(self)
        self.button_logout.setIcon(QIcon('Image/logout.png'))
        self.button_logout.setIconSize(QSize(90, 90))
        self.button_logout.setGeometry(80, 380, 90, 90)
        self.button_logout.clicked.connect(self.logout)

    # == create_button ==
    # La funzione crea i bottoni che saranno presenti sulla schermata prendendo per input
    # il path dell immagine che rappresenterà il bottone, il suo nome, la posizione che avrà nella
    # schermata e quale azione dovrà compiere una volta premuto.
    # La funzione si occupa dei bottoni anche dal punto di vista grafico.
    def create_button(self, path_img, nome, posizione, action):
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

    # == go_visita ==
    # La funzione si occupa di aprire la VistaListaVisiteMediche
    # presa dal file 'lista_visite.pickle'.
    def go_visita(self):
        self.prenota_visita = VistaListaVisiteMediche()
        self.prenota_visita.show()
        self.close()

    # == go_esiti ==
    # Questa funzione consente di aprire la VistaInserisciEsitoVisita che consente
    # al medico di inserire l'esito di una visita medica. Viene anche fatto un controllo
    # sulla lista: se la 'lista-visite.json' non contiene elementi viene inviato un
    # messaggio di errore.
    def go_esiti(self):
        trovato = False
        if self.controller.get_lista_visite():
            for visita in self.controller.get_lista_visite():
                controller_visita = ControllerVisitaMedica(visita)
                if controller_visita.get_descrizione() == "None":
                    trovato = True
                    self.go_esito = VistaInserisciEsitoVisita()
                    self.go_esito.show()
                    self.close()
            if not trovato:
                QMessageBox.information(self, "Attenzione", "Nessuna prenotazione nel sistema")
        else:
            QMessageBox.information(self, "Attenzione", "Nessuna prenotazione nel sistema")

    # == go_disdici ==
    # Questa funzione consente di aprire la VistaDisdiciVisitaMedica. Viene anche fatto
    # un controllo su 'lista-visita.json': se il file è vuoto viene inviato un messaggio
    # di errore all'utente.
    def go_disdici(self):
        trovato = False
        if self.controller.get_lista_visite():
            for visita in self.controller.get_lista_visite():
                controller_visita = ControllerVisitaMedica(visita)
                if controller_visita.get_esito() == "None":
                    trovato = True
                    self.go_disdire = VistaDisdiciVisitaMedica()
                    self.go_disdire.show()
                    self.close()
            if not trovato:
                QMessageBox.information(self, "Attenzione", "Nessun cliente prenotato")
        else:
            QMessageBox.information(self, "Attenzione", "Nessuna prenotazione nel sistema")

    def logout(self):
        QMessageBox.information(self, "Arrivederci", "Sessione terminata")
        self.vista_accesso = VistaAccesso.VistaAccesso()
        self.vista_accesso.show()
        self.close()