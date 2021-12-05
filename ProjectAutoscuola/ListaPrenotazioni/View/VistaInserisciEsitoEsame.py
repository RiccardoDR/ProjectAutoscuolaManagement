from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QComboBox, QPushButton, QMessageBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Home.View import VistaHomeIstruttore
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class VistaInserisciEsitoEsame(QWidget):  # Apre la vista che permette di inserire l'esito di un esame.
    def __init__(self, tipo):
        super(VistaInserisciEsitoEsame, self).__init__()
        self.tipo = tipo

        self.controller = ControllerListaClienti()
        self.controller.set_data()
        self.lista_clienti = self.controller.get_lista_clienti()

        self.stylesheet = """
                    QPushButton{
                        background-color: #007fff;
                        color: white;
                        border-radius: 15px
                    }

                    QPushButton::Pressed{
                        background-color: grey
                    }      
        """

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Esito esame")
        self.resize(700, 500)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Esito Esame'.
        self.label_titolo = QLabel(self)
        self.font_titolo = QFont("Times", 18, QFont.Bold)
        self.label_titolo.setText("Inserisci Esito")
        self.label_titolo.setFont(self.font_titolo)
        self.label_titolo.setGeometry(50, 55, 300, 40)

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

        # Inserimento e impostazioni grafiche del menù a tendina contenente le prenotazioni dei clienti.
        self.selezione_cliente = QComboBox(self)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_prenotazione() != "None":
                nome = controller_cliente.get_prenotazione().split("-")
                if nome[2].strip() != "Lezione":
                    self.selezione_cliente.addItem(controller_cliente.get_nome() + " " + controller_cliente.get_cognome())
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if self.selezione_cliente.currentText() == controller_cliente.get_nome() + " " + controller_cliente.get_cognome():
                self.prenotazione = controller_cliente.get_prenotazione()
        self.selezione_cliente.setGeometry(250, 190, 300, 30)

        # Inserimento e impostazioni grafiche dell'etichetta 'Esito'.
        self.label_id = QLabel(self)
        self.font_id = QFont("Times", 9)
        self.label_id.setFont(self.font_id)
        self.label_id.setText("Esito")
        self.label_id.setGeometry(60, 230, 160, 30)

        # Inserimento e impostazioni grafiche del menù a tendina che consente di determinare
        # l'idoneità o meno del cliente.
        self.esito_esame = QComboBox(self)
        self.esito_esame.addItem("IDONEO")
        self.esito_esame.addItem("NON IDONEO")
        self.esito_esame.setGeometry(250, 230, 300, 30)

        # Inserimento e impostazioni grafiche del bottone che permette di inserire l'esito dell'esame.
        self.button_esito = QPushButton(self)
        self.button_esito.setText("Inserisci esito")
        self.font_button = QFont("Times", 11)
        self.button_esito.setFont(self.font_button)
        self.button_esito.setGeometry(495, 410, 150, 50)
        self.button_esito.setStyleSheet(self.stylesheet)
        self.button_esito.clicked.connect(self.inserisci_esito)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(60, 60))
        self.button_back.setGeometry(50, 390, 90, 90)
        self.button_back.clicked.connect(self.go_back)

    # == inserisci_esito ==
    # La funzione permette di confermare l'inserimento dell'esito dell'esame relativo al cliente
    # selezionatodal menù a tendina.
    def inserisci_esito(self):
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if self.selezione_cliente.currentText() == controller_cliente.get_nome()+" "+controller_cliente.get_cognome():
                if self.esito_esame.currentText() == "IDONEO":
                    nome = controller_cliente.get_prenotazione().split("-")
                    if nome[2].strip() == "Esame teorico":
                        controller_cliente.set_esame_teorico("Effettuato")
                    if nome[2].strip() == "Esame pratico":
                        controller_cliente.set_esame_pratico("Effettuato")
                    controller_cliente.set_prenotazione("None")
                else:
                    controller_cliente.set_prenotazione("None")
        QMessageBox.information(self, "Confermato", "Esito inserito con successo")
        self.controller.save_data()
        self.go_home_istruttore = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_home_istruttore.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_home.show()
        self.close()
