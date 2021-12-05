from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QComboBox, QPushButton, QMessageBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Home.View import VistaHomeIstruttore
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class VistaDisdettaPrenotazione(QWidget):  # Apre la vista che permette di effettuare la disdetta di una prenotazione.
    def __init__(self, tipo):
        super(VistaDisdettaPrenotazione, self).__init__()
        self.tipo = tipo

        self.controller = ControllerListaClienti()
        self.controller.set_data()
        self.lista_clienti = self.controller.get_lista_clienti()

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
        self.setWindowTitle("Disdici prenotazione")
        self.resize(700, 500)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Disdetta Prenotazione'.
        self.label_titolo = QLabel(self)
        self.font_titolo = QFont("Times", 18, QFont.Bold)
        self.label_titolo.setText("Disdetta Prenotazione")
        self.label_titolo.setFont(self.font_titolo)
        self.label_titolo.setGeometry(50, 55, 350, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 600, 250)

        # Inserimento e impostazioni grafiche dell'etichetta 'Selezionare il cliente'.
        self.label_id = QLabel(self)
        self.font_id = QFont("Times", 9)
        self.label_id.setFont(self.font_id)
        self.label_id.setText("Selezionare il cliente")
        self.label_id.setGeometry(60, 190, 160, 30)

        # Inserimento e impostazioni grafiche del menù a tendina contenente le prenotazioni effettuate
        # dai rispettivi cliente.
        self.selezione_cliente = QComboBox(self)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_prenotazione() != "None":
                self.selezione_cliente.addItem(controller_cliente.get_nome() + " " + controller_cliente.get_cognome())
        self.selezione_cliente.setGeometry(250, 190, 300, 30)

        # Inserimento e impostazioni grafiche del bottone per confermare la disdetta del servizio selezionato.
        self.button_disdici = QPushButton(self)
        self.button_disdici.setText("Disdici")
        self.font_button = QFont("Times", 11)
        self.button_disdici.setFont(self.font_button)
        self.button_disdici.setGeometry(525, 410, 120, 50)
        self.button_disdici.setStyleSheet(self.stylesheet)
        self.button_disdici.clicked.connect(self.disdici_prenotazione)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(60, 60))
        self.button_back.setGeometry(50, 390, 90, 90)
        self.button_back.clicked.connect(self.go_back)

    # == disdici_prenotazione ==
    # La funzione, dopo aver chiesto conferma all'utente, cancella la prenotazione selezionata e, successivamente,
    # riporta l'utente alla VistaHomeIstruttore, dopo aver salvato le modifiche avvenute.
    def disdici_prenotazione(self):
        conferma = QMessageBox.question(self, "Conferma", "Sei sicuro di voler disdire la prenotazione?", QMessageBox.Yes,
                                        QMessageBox.No)
        if conferma == QMessageBox.Yes:
            for cliente in self.lista_clienti:
                controller_cliente = ControllerCliente(cliente)

                if self.selezione_cliente.currentText() == \
                        controller_cliente.get_nome() + " " + controller_cliente.get_cognome():
                    controller_cliente.set_prenotazione("None")
            self.controller.save_data()
            self.go_home_istruttore = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
            self.go_home_istruttore.show()
            self.close()
        else:
            return

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_home.show()
        self.close()