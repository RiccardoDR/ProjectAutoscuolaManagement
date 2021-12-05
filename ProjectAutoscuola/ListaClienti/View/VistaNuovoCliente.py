from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QFrame, QRadioButton, QPushButton, QCalendarWidget, QMessageBox, \
    QComboBox

from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaClienti.View import VistaListaClienti
from ProgettoAutoscuola.Cliente.Model.Cliente import Cliente


class VistaNuovoCliente(QWidget):  # Apre la vista che permette di inserire un nuovo cliente nel sistema.
    def __init__(self, parent=None):
        super(VistaNuovoCliente, self).__init__(parent)
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
        self.setWindowTitle("Nuovo Cliente")
        self.resize(1250, 650)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 50, 1150, 440)

        # Usa la funzione 'create_label1' e 'create_label2' per creare due colonne di etichette.
        self.create_label1("Nome", 100)
        self.create_label1("Cognome", 150)
        self.create_label1("Codice Fiscale", 200)
        self.create_label1("Indirizzo", 250)
        self.create_label1("Email", 300)
        self.create_label1("Telefono", 350)
        self.create_label1("Tipo patente", 400)
        self.create_label2("Data di nascita", 100)

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni del nuovo cliente.
        self.edit_nome = QLineEdit(self)
        self.edit_nome.setGeometry(250, 100, 200, 30)

        self.edit_cognome = QLineEdit(self)
        self.edit_cognome.setGeometry(250, 150, 200, 30)

        self.edit_cf = QLineEdit(self)
        self.edit_cf.setGeometry(250, 200, 200, 30)

        self.edit_indirizzo = QLineEdit(self)
        self.edit_indirizzo.setGeometry(250, 250, 200, 30)

        self.edit_email = QLineEdit(self)
        self.edit_email.setGeometry(250, 300, 200, 30)

        self.edit_telefono = QLineEdit(self)
        self.edit_telefono.setGeometry(250, 350, 200, 30)

        self.edit_tipo_patente = QComboBox(self)
        patenti = ['AM', 'A1', 'A2', 'A', 'B1', 'B', 'C1', 'C', 'D1', 'D']
        self.edit_tipo_patente.addItems(patenti)
        self.edit_tipo_patente.setGeometry(250, 400, 200, 30)

        self.edit_eta = QCalendarWidget(self)
        self.edit_eta.setGridVisible(True)
        self.edit_eta.setGeometry(630, 100, 500, 254)

        # Inserimento e impostazioni grafiche del radio button "Maschio".
        self.button_male = QRadioButton(self)
        self.button_male.setText("Uomo")
        self.button_male.setGeometry(800, 375, 100, 20)
        self.button_male.setStyleSheet('background-color: white')
        self.button_male.setChecked(True)

        # Inserimento e impostazioni grafiche del radio button "Femmina".
        self.button_female = QRadioButton(self)
        self.button_female.setText("Donna")
        self.button_female.setGeometry(950, 375, 100, 20)
        self.button_female.setStyleSheet('background-color: white')

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(50, 520, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per salvare le informazioni inserite.
        self.button_new_cliente = QPushButton(self)
        self.button_new_cliente.setText("Salva")
        self.font_button = QFont("Times", 11)
        self.button_new_cliente.setFont(self.font_button)
        self.button_new_cliente.setGeometry(1050, 540, 120, 50)
        self.button_new_cliente.setStyleSheet(self.stylesheet)
        self.button_new_cliente.clicked.connect(self.salva_cliente)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella prima colonna.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 110, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == create_label2 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella seconda colonna.
    def create_label2(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(500, posizione, 120, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == salva_cliente ==
    # La funzione ha il compito di salvare in 'Lista_clienti.json' le informazioni inserite
    # nelle varie caselle di testo. Dopodiché verrà aperta nuovamente la VistaListaClienti.
    def salva_cliente(self):
        if self.button_male.isChecked():
            sesso = self.button_male.text()
        else:
            sesso = self.button_female.text()

        if self.edit_nome.text() == "" or self.edit_cognome.text() == "" or \
                self.edit_indirizzo.text() == "" or self.edit_telefono.text() == "" or \
                self.edit_tipo_patente.currentText() == "" or self.edit_eta.selectedDate().toString() == "" or \
                sesso == "":
            QMessageBox.critical(self, "Attenzione", "Inserisci tutti i dati!")
        else:
            if len(self.edit_cf.text()) != 16:
                QMessageBox.critical(self, "Attenzione", "Il codice fiscale immesso non è valido")
                self.edit_cf.clear()
                return

            if not "@" in self.edit_email.text():
                QMessageBox.critical(self, "Attenzione", "l'indirizzo email immesso non è valido")
                self.edit_email.clear()

            if not self.edit_telefono.text().isdigit():
                QMessageBox.critical(self, "Attenzione", "il numero di telefono immesso non è valido")
                self.edit_telefono.clear()
            else:
                self.controller.aggiungi_cliente(Cliente(self.edit_nome.text(), self.edit_cognome.text(),
                                                         self.edit_cf.text(), self.edit_indirizzo.text(),
                                                         self.edit_email.text(), self.edit_telefono.text(),
                                                         self.edit_tipo_patente.currentText(),
                                                         self.edit_eta.selectedDate().toString("dd-MM-yyyy"), sesso))
                self.controller.save_data()
                self.go_lista_clienti = VistaListaClienti.VistaListaClienti()
                self.go_lista_clienti.show()
                self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_clienti = VistaListaClienti.VistaListaClienti()
        self.go_lista_clienti.show()
        self.close()
