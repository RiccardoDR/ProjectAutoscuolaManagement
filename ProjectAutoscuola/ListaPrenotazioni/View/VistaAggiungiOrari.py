from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QCalendarWidget, QPushButton, QMessageBox, QComboBox

from ProgettoAutoscuola.Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione
from ProgettoAutoscuola.ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni
from ProgettoAutoscuola.ListaPrenotazioni.View import VistaListaPrenotazioni
from ProgettoAutoscuola.Prenotazione.Model.Prenotazione import Prenotazione


class VistaAggiungiOrari(QWidget):  # Apre la vista che consente di aggiungere un oraario per le prenotazioni.
    def __init__(self, tipo):
        super(VistaAggiungiOrari, self).__init__()
        self.tipo = tipo

        self.controller = ControllerListaPrenotazioni()
        self.controller.set_data()
        self.lista_prenotazioni = self.controller.get_lista_prenotazioni()

        self.stylesheet = """
                    QPushButton{
                        background-color: #007fff;
                        color: white;
                        border-radius: 15px;
                    }

                    QPushButton::Pressed{
                        background-color: grey
                    }        
        """

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Nuovo Orario")
        self.resize(1050, 600)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Nuovo Orario'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Nuovo Orario")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 250, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 950, 330)

        # Usa la funzione 'create_label' per creare un etichetta.
        self.create_label("Tipo", 150)

        # Inserimento e impostazioni grafiche del menù a tendina per scegliere l'orario di un nuovo servizio.
        self.edit_tipo = QComboBox(self)
        attivita = ['Lezione', 'Esame teorico', 'Lezione guida', 'Esame pratico']
        self.edit_tipo.addItems(attivita)
        self.edit_tipo.setGeometry(250, 150, 200, 30)

        # Inserimento e impostazioni grafiche dell'etichetta 'Data'.
        self.label_data = QLabel(self)
        self.label_data.setText("Data")
        self.label_data.setGeometry(500, 150, 100, 20)
        self.font_label = QFont("Times", 9)
        self.label_data.setFont(self.font_label)

        # Inserimento e impostazioni grafiche del calendario.
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(575, 150, 350, 250)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(50, 470, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche per il bottone che permette di effettuare l'aggiunta dell'orario.
        self.button_prenota = QPushButton(self)
        self.button_prenota.setText("Aggiungi orario")
        self.font_button = QFont("Times", 11)
        self.button_prenota.setFont(self.font_button)
        self.button_prenota.setGeometry(750, 490, 200, 50)
        self.button_prenota.setStyleSheet(self.stylesheet)
        self.button_prenota.clicked.connect(self.go_aggiungi_orario)

    # == create_label ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    def create_label(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 110, 20)
        font_label1 = QFont("Times", 9)
        label_edit.setFont(font_label1)

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.vista_home = VistaListaPrenotazioni.VistaListaPrenotazioni(self.tipo)
        self.vista_home.show()
        self.close()

    # == go_aggiungi_orario ==
    # La funzione aggiunge l'orario inserito alla lista delle prenotazioni, invia un messaggio di conferma
    # all'utente e reindirizza l'utente alla VistaListaPrenotazioni.
    def go_aggiungi_orario(self):
        trovato = False
        for orario in self.lista_prenotazioni:
            controller_prenotazione = ControllerPrenotazione(orario)

            if self.calendar.selectedDate().toString("dd-MM") == controller_prenotazione.get_data() and \
                    self.edit_tipo.currentText() == controller_prenotazione.get_tipo():
                trovato = True
                QMessageBox.information(self, "Errore", "Orario già presente nel sistema")
        if not trovato:
            self.controller.aggiungi_prenotazione(Prenotazione(self.edit_tipo.currentText(),
                                                               self.calendar.selectedDate().toString("dd-MM")))
            QMessageBox.information(self, "Confermato", "Orario aggiunto nel sistema")
            self.controller.save_data()

        self.go_lista_visite = VistaListaPrenotazioni.VistaListaPrenotazioni(self.tipo)
        self.go_lista_visite.show()
        self.close()
