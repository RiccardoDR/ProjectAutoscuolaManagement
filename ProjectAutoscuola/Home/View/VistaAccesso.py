from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QLineEdit, QMessageBox, QFrame

from ProgettoAutoscuola.Dipendente.Controller.ControllerDipendente import ControllerDipendente
from ProgettoAutoscuola.Home.View import VistaHomeIstruttore, VistaHomeMedico, VistaHomeSegretario
from ProgettoAutoscuola.ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti


class VistaAccesso(QWidget):  # Apre e visualizza la vista di accesso al programma.
    def __init__(self, parent=None):
        super(VistaAccesso, self).__init__(parent)

        self.esiste = None      # Variabile per controllare se il dipendente esiste al momento del login

        self.controller = ControllerListaDipendenti()
        self.controller.set_data()
        self.lista_dipendenti = self.controller.get_lista_dipendenti()

        self.stylesheet = """
                    QPushButton{
                        border-radius: 15px;
                        background-color: #007fff;
                        color: white;
                    }
                    QPushButton::Pressed{
                        background-color: grey;
                    }
        """

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Accesso")
        self.resize(450, 550)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/logo1.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.setGeometry(65, 50, 320, 150)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid grey; border-radius: 10px;')
        self.frame.setGeometry(50, 250, 350, 280)

        # Inserimento e impostazioni grafiche dell'etichetta 'Accedi'.
        self.label_accedi = QLabel(self)
        self.label_accedi.setText("Accedi")
        self.label_accedi.setAlignment(Qt.AlignCenter)
        self.font = QFont("Times", 16)
        self.label_accedi.setFont(self.font)
        self.label_accedi.setGeometry(150, 270, 150, 30)

        # Inserimento e impostazioni grafiche dell'etichetta 'Username', dell'icona per l'username
        # e della casella di testo per inserire l'username.
        self.imagePath = "Image/user.png"
        self.image = QImage(self.imagePath)
        self.label_user = QLabel(self)
        self.label_user.setPixmap(QPixmap.fromImage(self.image))
        self.label_user.setScaledContents(True)
        self.label_user.setGeometry(70, 320, 40, 40)
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.setGeometry(120, 320, 250, 40)

        # Inserimento e impostazioni grafiche dell'etichetta 'Password', dell'icona della password
        # e della casella di testo per inserire la password.
        self.imagePath = "Image/password.png"
        self.image = QImage(self.imagePath)
        self.label_pass = QLabel(self)
        self.label_pass.setPixmap(QPixmap.fromImage(self.image))
        self.label_pass.setScaledContents(True)
        self.label_pass.setGeometry(70, 380, 40, 40)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.setGeometry(120, 380, 250, 40)

        # Inserimento e impostazioni grafihce del bottone per accedere alla home del dipendente.
        self.button_login = QPushButton(self)
        self.font_button = QFont("Times", 11, QFont.Bold)
        self.button_login.setFont(self.font_button)
        self.button_login.setText("Login")
        self.button_login.setStyleSheet(self.stylesheet)
        self.button_login.clicked.connect(self.login)
        self.button_login.setGeometry(140, 460, 170, 40)

    # == login ==
    # La funzione controlla che le informazioni inserite nelle caselle di testo corrispondano a quelle
    # di un dipendente nel file json. Verrà quindi aperta la vista home in base al tipo di dipendente di
    # cui sono state inserite le credenziali. In caso di inserimento di informazioni errate verrà inviato
    # un messaggio di errore.

    def login(self):
        if self.password.text() == "admin" and self.username.text() == "admin":
            self.esiste = True
            self.go_vista_home_segretario()
        else:
            for dipendente in self.lista_dipendenti:
                controller_dipendenti = ControllerDipendente(dipendente)
                if self.password.text() == controller_dipendenti.get_password() and \
                        self.username.text() == controller_dipendenti.get_username():
                    self.esiste = True
                    if controller_dipendenti.get_mansione() == "Segretario":
                        self.go_vista_home_segretario()
                    if controller_dipendenti.get_mansione() == "Medico":
                        self.go_vista_home_medico()
                    if controller_dipendenti.get_mansione() == "Istruttore":
                        self.go_vista_home_istruttore()
        if not self.esiste:
            QMessageBox.critical(self, 'Errore', 'Username o Password errati')

    # == go_vista_home_segretario ==
    # La funzione si occupa di aprire la VistaHomeSegretario.
    def go_vista_home_segretario(self):
        self.vista_segretario = VistaHomeSegretario.VistaHomeSegretario()
        self.vista_segretario.show()
        self.close()

    # == go_vista_home_medico ==
    # La funzione si occupa di aprire la VistaHomeMedico.
    def go_vista_home_medico(self):
        self.vista_medico = VistaHomeMedico.VistaHomeMedico()
        self.vista_medico.show()
        self.close()

    # == go_vista_home_istruttore ==
    # La funzione si occupa di aprire la VistaHomeIstruttore.
    def go_vista_home_istruttore(self):
        self.vista_istruttore = VistaHomeIstruttore.VistaHomeIstruttore("Istruttore")
        self.vista_istruttore.show()
        self.close()
