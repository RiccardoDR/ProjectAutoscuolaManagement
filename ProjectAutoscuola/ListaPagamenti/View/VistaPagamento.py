from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QComboBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPagamenti.View.VistaRiepilogo import VistaRiepilogo


class VistaPagamento(QWidget):  # Apre la vista che permette di inserire i dati relativi al pagamento.
    def __init__(self, parent=None):
        super(VistaPagamento, self).__init__(parent)

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
        self.setWindowTitle("Effettua Pagamento")
        self.resize(1000, 450)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Inserisci Dati Pagamento'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Inserisci Dati Pagamento")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 500, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 900, 250)

        # Usa la funzione 'create_label' per creare due etichette.
        self.create_label("Seleziona cliente", 150)
        self.create_label("Prezzo", 250)

        # Inserimento e impostazioni grafiche dell'etichetta 'Descrizione pagamento'.
        self.label_descrizione = QLabel(self)
        self.label_descrizione.setText("Descrizione pagamento")
        self.label_descrizione.setGeometry(475, 150, 185, 25)
        self.font_descrizione = QFont("Times", 9)
        self.label_descrizione.setFont(self.font_descrizione)

        # Inserimento e impostazioni grafiche del menù a tendina contenente i cliente deella lista_cliente.
        self.edit_cliente = QComboBox(self)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            self.edit_cliente.addItem(controller_cliente.get_nome() + " " + controller_cliente.get_cognome())
        self.edit_cliente.setGeometry(250, 150, 200, 30)

        # Inserimento e impostazioni grafiche del menù a tendina contenente la lista dei servizi per cui
        # è possibile effettuare un pagamento.
        self.edit_descrizione = QComboBox(self)
        self.edit_descrizione.addItem("Bollettini + visita medica + prima rata", ["250"])
        self.edit_descrizione.addItem("Esame teorico", ["60"])
        self.edit_descrizione.addItem("Guide obbligatorie", ["180"])
        self.edit_descrizione.addItem("Esame pratico", ["60"])
        self.edit_descrizione.addItem("Guide aggiuntive", ["30"])
        self.edit_descrizione.setGeometry(670, 150, 250, 30)

        # Inserimento e impostazioni grafiche del menù a tendina che permette di scegliere il prezzo da pagare.
        self.edit_prezzo = QComboBox(self)
        self.edit_prezzo.setGeometry(250, 250, 200, 30)

        # In base al servizio scelto viene cambiato anche il prezzo nel relativo menù a tendina.
        self.edit_descrizione.currentIndexChanged.connect(self.update_data)
        self.update_data(self.edit_descrizione.currentIndex())

        # Inserimento e impostazioni grafiche del bottone che permette di procedere con la stampa della ricevuta.
        self.button_ricevuta = QPushButton(self)
        self.button_ricevuta.setText("Procedi ricevuta")
        self.font_button = QFont("Times", 11)
        self.button_ricevuta.setFont(self.font_button)
        self.button_ricevuta.setGeometry(780, 375, 170, 50)
        self.button_ricevuta.setStyleSheet(self.stylesheet)
        self.button_ricevuta.clicked.connect(self.go_ricevuta)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(65, 65))
        self.button_back.setGeometry(50, 367, 65, 65)
        self.button_back.clicked.connect(self.go_back)

    # == create_label ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    def create_label(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 130, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == update_data ==
    # La funzione aggiunge al menù a tendina relativo al prezzo il prezzo del servizio selezionato.
    def update_data(self, index):
        self.edit_prezzo.clear()
        date = self.edit_descrizione.itemData(index)
        if date:
            self.edit_prezzo.addItems(date)

    # == go_ricevuta ==
    # La funzione, dopo aver controllato se il cliente selezionato è presente a sistema,
    # apre la VistaRiepilogo, passandogli le informazioni relative al pagamento da effettuare.
    def go_ricevuta(self):
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_nome() + " " + controller_cliente.get_cognome() == self.edit_cliente.currentText():
                self.cliente = cliente
        self.ricevuta = VistaRiepilogo(self.edit_prezzo.currentText(), self.edit_descrizione.currentText(),
                                       self.edit_descrizione.currentIndex(),
                                       self.cliente.get_nome() + " " + self.cliente.get_cognome())
        self.ricevuta.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_pagamenti = VistaHomeSegretario.VistaHomeSegretario()
        self.go_lista_pagamenti.show()
        self.close()
