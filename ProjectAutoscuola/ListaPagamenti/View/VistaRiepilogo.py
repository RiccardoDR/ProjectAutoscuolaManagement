import random

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QTextEdit, QPushButton, QMessageBox, QRadioButton

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Pagamento.Controller.ControllerPagamento import ControllerPagamento
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPagamenti.Controller.ControllerListaPagamenti import ControllerListaPagamenti
from ProgettoAutoscuola.ListaPagamenti.View import VistaListaPagamenti
from ProgettoAutoscuola.Pagamento.Model.Pagamento import Pagamento


class VistaRiepilogo(QWidget):  # Apre la vista che riepiloga le informazioni sul pagamento
    def __init__(self, prezzo, descrizione, n_pagamento, cliente):
        super(VistaRiepilogo, self).__init__()

        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()
        self.lista_clienti = self.controller_clienti.get_lista_clienti()

        self.controller_pagamenti = ControllerListaPagamenti()
        self.controller_pagamenti.set_data()

        self.pagamento = Pagamento(prezzo, descrizione, cliente)

        self.controller = ControllerPagamento(self.pagamento)

        self.n_pagamento = n_pagamento
        self.cliente = cliente

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
        self.resize(600, 500)
        self.setWindowTitle("Riepilogo")
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta che contiene il nome del cliente che effettua il pagamento
        self.label_cliente = QLabel(self)
        self.label_cliente.setText(cliente)
        self.font = QFont("Times", 18, QFont.Bold)
        self.label_cliente.setFont(self.font)
        self.label_cliente.setGeometry(170, 50, 350, 30)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 500, 310)

        # Inizializzazione dei font per le etichette.
        self.font1 = QFont("Times", 12, QFont.Bold)
        self.font2 = QFont("Helvetica", 10)

        # Inserimento e impostazioni grafiche dell'etichetta 'Pagamento N° : '.
        self.label_id = QLabel(self)
        self.label_id.setText("Pagamento N°: ")
        self.label_id.setGeometry(80, 150, 280, 30)
        self.label_id.setFont(self.font1)

        # Inserimento e impostazioni grafiche dell'etichetta che contiene l'id del pagamento.
        self.label_id_pagamento = QLabel(self)
        self.label_id_pagamento.setText("#" + str(self.controller.get_id()))
        self.label_id_pagamento.setGeometry(275, 155, 200, 20)
        self.label_id_pagamento.setFont(self.font2)

        # Inserimento e impostazioni grafiche dell'etichetta 'Prezzo :'.
        self.label_prezzo = QLabel(self)
        self.label_prezzo.setText("Prezzo: ")
        self.label_prezzo.setGeometry(80, 210, 100, 20)
        self.label_prezzo.setFont(self.font1)

        # Inserimento e impostazioni grafiche dell'etichetta che contiene il prezzo.
        self.label_prezzo_pagamento = QLabel(self)
        self.label_prezzo_pagamento.setText(self.controller.get_prezzo()+"€")
        self.label_prezzo_pagamento.setGeometry(190, 210, 250, 20)
        self.label_prezzo_pagamento.setFont(self.font2)

        # Inserimento e impostazioni grafiche dell'etichetta 'Descrizione :'.
        self.label_descrizione = QLabel(self)
        self.label_descrizione.setText("Descrizione: ")
        self.label_descrizione.setGeometry(80, 260, 150, 20)
        self.label_descrizione.setFont(self.font1)

        # Inserimento e impostazioni grafiche della casella di testo che contiene la descrizione del pagamento.
        self.label_descrizione_pagamento = QTextEdit(self)
        self.label_descrizione_pagamento.setText(self.controller.get_descrizione())
        self.label_descrizione_pagamento.setGeometry(230, 255, 300, 150)
        self.label_descrizione_pagamento.setStyleSheet('border-color: transparent;')
        self.label_descrizione_pagamento.setFont(self.font2)
        self.label_descrizione_pagamento.setReadOnly(True)

        # Inserimento e impostazioni grafiche dei bottoni relativi ai metodi di pagamento.
        self.button_pagamento = QRadioButton(self)
        self.button_pagamento.setIcon(QIcon("Image/contanti.png"))
        self.button_pagamento.setIconSize(QSize(70, 70))
        self.button_pagamento.setGeometry(80, 300, 90, 75)
        self.button_pagamento.setChecked(True)

        self.button_pagamento2 = QRadioButton(self)
        self.button_pagamento2.setIcon(QIcon("Image/mastercard.png"))
        self.button_pagamento2.setIconSize(QSize(65, 65))
        self.button_pagamento2.setGeometry(200, 300, 90, 75)

        self.button_pagamento3 = QRadioButton(self)
        self.button_pagamento3.setIcon(QIcon("Image/visa.png"))
        self.button_pagamento3.setIconSize(QSize(65, 65))
        self.button_pagamento3.setGeometry(320, 300, 90, 75)

        # Inserimento e impostazioni grafiche del bottone di conferma del pagamento.
        self.button_ricevuta = QPushButton(self)
        self.button_ricevuta.setText("Conferma pagamento")
        self.font_button = QFont("Times", 10)
        self.button_ricevuta.setFont(self.font_button)
        self.button_ricevuta.setGeometry(350, 430, 200, 50)
        self.button_ricevuta.setStyleSheet(self.stylesheet)
        self.button_ricevuta.clicked.connect(self.go_pagamento)

    # == go_pagamento ==
    # La funzione controlla se il cliente che effettua il pagamento ha effettuato o meno i pagamenti.
    # Se li ha effettuati questi vengono aggiunti alla lista_pagamenti e i dati vengono salvati.
    # Ciò viene comunicato con un messaggio all'utente che viene poi reindirizzato alla VistaListaPagamenti.
    def go_pagamento(self):
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_nome()+" "+controller_cliente.get_cognome() == self.cliente:
                if self.n_pagamento == 0:
                    controller_cliente.set_pagamento_iniziale("Effettuato")
                if self.n_pagamento == 1:
                    controller_cliente.set_pagamento_esame_teorico("Effettuato")
                if self.n_pagamento == 2:
                    controller_cliente.set_pagamento_lezioni_guida("Effettuato")
                if self.n_pagamento == 3:
                    controller_cliente.set_pagamento_esame_pratico("Effettuato")
                if controller_cliente.get_id() == "None":
                    controller_cliente.set_id(str(random.randint(10000, 99999)))

        self.controller_clienti.save_data()
        self.controller_pagamenti.aggiungi_pagamento(self.pagamento)
        self.controller_pagamenti.save_data()
        QMessageBox.information(self, "Confermato", "Pagamento effettuato con successo")
        self.go_pagamenti = VistaListaPagamenti.VistaListaPagamenti()
        self.go_pagamenti.show()
        self.close()
