from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QComboBox, QPushButton, QTextEdit, QMessageBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.VisitaMedica.Controller.ControllerVisitaMedica import ControllerVisitaMedica
from ProgettoAutoscuola.Home.View import VistaHomeMedico
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.ListaVisiteMediche.View import VistaListaVisiteMediche


class VistaInserisciEsitoVisita(QWidget):  # Apre la vista che consente al medico di inserire l'esito di una visita.
    def __init__(self, parent=None):
        super(VistaInserisciEsitoVisita, self).__init__(parent)

        self.controller = ControllerListaVisiteMediche()
        self.controller.set_data()
        self.lista_visite = self.controller.get_lista_visite()

        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()
        self.lista_clienti = self.controller_clienti.get_lista_clienti()

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
        self.setWindowTitle("Inserisci Esito")
        self.resize(1000, 450)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Inserisci Dati Esito'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Inserisci Dati Esito")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 400, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 900, 250)

        self.create_label("Seleziona cliente", 150)
        self.create_label("Descrizione", 250)

        # Inserimento e impostazioni grafiche del menù a tendina contenente la lista dei clienti.
        # La colonna dell'esito della visita potrà essere modificata solamente se il cliente
        # non ha ancora effettuato la visita e quindi non è presente alcun valore su 'Esito'.
        self.edit_cf_cliente = QComboBox(self)
        for visita in self.lista_visite:
            controller_visita = ControllerVisitaMedica(visita)

            if controller_visita.get_esito() == "None":
                self.edit_cf_cliente.addItem(controller_visita.get_cliente() + " - " + controller_visita.get_data())
        self.edit_cf_cliente.setGeometry(250, 150, 250, 30)

        # Inserimento e impostazioni grafiche della casella di testo.
        self.edit_descrizione = QTextEdit(self)
        self.edit_descrizione.setGeometry(250, 250, 200, 50)

        # Inserimento e impostazioni grafiche dell'etichetta 'Esito'.
        self.label_edit = QLabel(self)
        self.label_edit.setText("Esito")
        self.label_edit.setGeometry(600, 150, 60, 20)
        self.font_label = QFont("Times", 9)
        self.label_edit.setFont(self.font_label)

        # Inserimento e impostazioni grafiche del menù a tendina per selezionare l'esito della visita.
        self.edit_esito = QComboBox(self)
        self.edit_esito.addItem("IDONEO")
        self.edit_esito.addItem("NON IDONEO")
        self.edit_esito.setGeometry(670, 150, 110, 20)

        # Inserimento e impostazioni grafiche del bottone per confermare l'inserimento dell'esito.
        self.button_ricevuta = QPushButton(self)
        self.button_ricevuta.setText("Inserisci esito")
        self.font_button = QFont("Times", 11)
        self.button_ricevuta.setFont(self.font_button)
        self.button_ricevuta.setGeometry(800, 375, 150, 50)
        self.button_ricevuta.setStyleSheet(self.stylesheet)
        self.button_ricevuta.clicked.connect(self.go_ricevuta)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(65, 65))
        self.button_back.setGeometry(20, 375, 150, 50)
        self.button_back.clicked.connect(self.go_back)

    # == create_label ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    def create_label(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 110, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == go_ricevuta ==
    # La funzione salva nella variabile 'nome' il cliente selezionato e successivamente, dopo aver controllato se il
    # cliente è presente nella lista_clienti, lo salva in cliente_visitato. Se non è presente un pagamento iniziale
    # mandato un messaggio di errore, altrimenti viene salvata in 'lista_visite.pickle' una nuova visita con le
    # informazioni relative. Infine la funzione rimanda alla VistaListaVisiteMediche.
    def go_ricevuta(self):
        if self.edit_descrizione.toPlainText() != '':
            nome = self.edit_cf_cliente.currentText().split("-")
            for cliente in self.lista_clienti:
                controller_cliente = ControllerCliente(cliente)

                if controller_cliente.get_nome() + " " + controller_cliente.get_cognome() == nome[0].strip():
                    controller_cliente.set_visita_medica("Effettuato")
                    self.cliente_visitato = cliente

            self.controller_clienti.save_data()

            for visita in self.lista_visite:
                controller_visita = ControllerVisitaMedica(visita)

                if controller_visita.get_cliente() == nome[0].strip():
                    controller_visita.set_descrizione(self.edit_descrizione.toPlainText())
                    controller_visita.set_esito(self.edit_esito.currentText())
            self.controller.save_data()
            QMessageBox.information(self, "Confermato", "Esito aggiunto al sistema")
            self.go_pagamenti = VistaListaVisiteMediche.VistaListaVisiteMediche()
            self.go_pagamenti.show()
            self.close()
        else:
            QMessageBox.critical(self, "Attenzione", "Inserisci tutti i dati")

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_pagamenti = VistaHomeMedico.VistaHomeMedico()
        self.go_lista_pagamenti.show()
        self.close()
