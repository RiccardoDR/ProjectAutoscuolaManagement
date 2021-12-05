from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QLineEdit, QRadioButton, QPushButton, QMessageBox, QCalendarWidget, \
    QComboBox

from ProgettoAutoscuola.ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti
from ProgettoAutoscuola.ListaDipendenti.View import VistaListaDipendenti
from ProgettoAutoscuola.Dipendente.Model.Dipendente import Dipendente


class VistaNuovoDipendente(QWidget):  # Apre la vista che permette di inserire un nuovo dipendente nel sistema.
    def __init__(self, parent=None):
        super(VistaNuovoDipendente, self).__init__(parent)

        self.controller = ControllerListaDipendenti()
        self.controller.set_data()
        self.lista_dipendenti = self.controller.get_lista_dipendenti()

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
        self.setWindowTitle("Nuovo Dipendente")
        self.resize(1000, 660)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Nuovo Dipendente'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Nuovo Dipendente")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 20, 350, 45)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 60, 900, 480)

        # Usa la funzione 'create_label1' e 'create_label2' per creare due colonne di etichette.
        self.create_label1("Nome", 100)
        self.create_label1("Cognome", 150)
        self.create_label1("Cod. Fisc.", 200)
        self.create_label1("Luogo Nascita", 250)
        self.create_label1("Email", 300)
        self.create_label1("Telefono", 350)
        self.create_label1("Username", 430)
        self.create_label2("Data Nascita", 100)
        self.create_label2("Mansione", 300)
        self.create_label2("Tipo Contratto", 350)
        self.create_label2("Passoword", 430)
        self.create_label2("Conferma password", 470)

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni del nuovo dipendente.
        self.edit_nome = QLineEdit(self)
        self.edit_nome.setGeometry(250, 100, 200, 30)

        self.edit_cognome = QLineEdit(self)
        self.edit_cognome.setGeometry(250, 150, 200, 30)

        self.edit_cf = QLineEdit(self)
        self.edit_cf.setGeometry(250, 200, 200, 30)

        self.edit_luogo_di_nascita = QLineEdit(self)
        self.edit_luogo_di_nascita.setGeometry(250, 250, 200, 30)

        self.edit_email = QLineEdit(self)
        self.edit_email.setGeometry(250, 300, 200, 30)

        self.edit_telefono = QLineEdit(self)
        self.edit_telefono.setGeometry(250, 350, 200, 30)

        self.edit_data_di_nascita = QCalendarWidget(self)
        self.edit_data_di_nascita.setGridVisible(True)
        self.edit_data_di_nascita.setGeometry(600, 80, 320, 200)

        self.edit_mansione = QComboBox(self)
        mansioni = ['Segretario', 'Istruttore', "Medico"]
        self.edit_mansione.addItems(mansioni)
        self.edit_mansione.setGeometry(670, 300, 200, 30)

        self.edit_tipo_contratto = QComboBox(self)
        contratti = ['Tirocinio', 'Determinato 6 mesi', 'Determinato 1 anno', 'Determinato 3 anni', 'Indeterminato']
        self.edit_tipo_contratto.addItems(contratti)
        self.edit_tipo_contratto.setGeometry(670, 350, 200, 30)

        # Inserimento e impostazioni grafiche del radio button "Maschio".
        self.button_male = QRadioButton(self)
        self.button_male.setText("Uomo")
        self.button_male.setGeometry(250, 395, 100, 20)
        self.button_male.setStyleSheet('background-color: white')
        self.button_male.setChecked(True)

        # Inserimento e impostazioni grafiche del radio button "Femmina".
        self.button_female = QRadioButton(self)
        self.button_female.setText("Donna")
        self.button_female.setGeometry(380, 395, 100, 20)
        self.button_female.setStyleSheet('background-color: white')

        self.edit_username = QLineEdit(self)
        self.edit_username.setGeometry(250, 430, 200, 30)

        self.edit_password = QLineEdit(self)
        self.edit_password.setGeometry(670, 430, 200, 30)
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_password.setPlaceholderText("Minimo 8 caratteri")

        self.edit_password_conferma = QLineEdit(self)
        self.edit_password_conferma.setGeometry(670, 470, 200, 30)
        self.edit_password_conferma.setEchoMode(QLineEdit.Password)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(80, 80))
        self.button_back.setGeometry(50, 560, 80, 80)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per salvare le informazioni inserite.
        self.button_new_dipendente = QPushButton(self)
        self.button_new_dipendente.setText("Salva")
        self.font_button = QFont("Times", 11)
        self.button_new_dipendente.setFont(self.font_button)
        self.button_new_dipendente.setGeometry(800, 580, 120, 50)
        self.button_new_dipendente.setStyleSheet(self.stylesheet)
        self.button_new_dipendente.clicked.connect(self.salva_dipendente)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella prima colonna.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 100, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == create_label2 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella seconda colonna.
    def create_label2(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(500, posizione, 140, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == salva_dipendente ==
    # La funzione ha il compito di salvare in 'lista_dipendenti.pickle' le informazioni inserite
    # nelle varie caselle di testo. Dopodiché verrà aperta nuovamente la VistaListaDipendenti.
    def salva_dipendente(self):
        if self.button_male.isChecked():
            sesso = self.button_male.text()
        else:
            sesso = self.button_female.text()

        if self.edit_nome.text() == "" or self.edit_cognome.text() == "" or self.edit_cf.text() == "" or \
                self.edit_data_di_nascita.selectedDate().toString() == "" or self.edit_luogo_di_nascita.text() == "" or \
                self.edit_email.text() == "" or self.edit_telefono.text() == "" or \
                self.edit_mansione.currentText() == "" or self.edit_username.text() == "" or \
                self.edit_password_conferma.text() == "" or self.edit_password.text() == "" or \
                self.edit_tipo_contratto.currentText() == "" or sesso == "":
            QMessageBox.critical(self, "Attenzione", "Inserisci tutti i dati")
            return
        else:
            if len(self.edit_cf.text()) != 16:
                QMessageBox.critical(self, "Attenzione", "Il codice fiscale immesso non è valido")
                self.edit_cf.clear()
                return
            if not "@" in self.edit_email.text():
                QMessageBox.critical(self, "Errore", "l'indirizzo email immesso non è valido", QMessageBox.Ok)
                self.edit_email.clear()
                return
            if not self.edit_telefono.text().isdigit():
                QMessageBox.critical(self, "Errore", "il numero di telefono immesso non è valido", QMessageBox.Ok)
                self.edit_telefono.clear()
                return
            if self.edit_password.text() != self.edit_password_conferma.text():
                QMessageBox.critical(self, "Attenzione", "Passoword non corretta")
                return
            if len(self.edit_password.text()) < 8:
                QMessageBox.critical(self, "Attenzione", "Password troppo corta")
                return
            else:
                self.controller.add_dipendente(Dipendente(self.edit_nome.text(), self.edit_cognome.text(),
                                                          self.edit_username.text(), self.edit_password.text(),
                                                          self.edit_cf.text(),
                                                          self.edit_data_di_nascita.selectedDate().toString("dd-MM-yyyy"),
                                                          self.edit_luogo_di_nascita.text(), self.edit_email.text(),
                                                          self.edit_telefono.text(), self.edit_mansione.currentText(),
                                                          self.edit_tipo_contratto.currentText(), sesso))
                self.controller.save_data()
                self.go_lista_dipendenti = VistaListaDipendenti.VistaListaDipendenti()
                self.go_lista_dipendenti.show()
                self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_dipendenti = VistaListaDipendenti.VistaListaDipendenti()
        self.go_lista_dipendenti.show()
        self.close()
