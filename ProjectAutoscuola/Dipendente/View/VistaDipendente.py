import shutil
import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QFileDialog, QLineEdit, QComboBox, QMessageBox

from ProgettoAutoscuola.Dipendente.Controller.ControllerDipendente import ControllerDipendente
from ProgettoAutoscuola.ListaDipendenti.View import VistaListaDipendenti
from ProgettoAutoscuola.ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti


class VistaDipendente(QWidget):  # Apre la vista che visualizza le informazioni del dipendente.
    def __init__(self, dipendente, modifica):
        super(VistaDipendente, self).__init__()
        self.dipendente = dipendente
        self.modifica = modifica

        self.controller = ControllerListaDipendenti()
        self.controller.set_data()
        self.lista_dipendenti = self.controller.get_lista_dipendenti()

        self.stylesheet = """
            QPushButton{
                border-radius: 15px;
                background-color: #007fff;
                color: white;
            }

            QPushButton::pressed{
                background-color: grey;
            }
        """

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Info Dipendente")
        self.resize(600, 700)
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
        self.frame.setGeometry(75, 30, 450, 580)

        # Usa la funzione 'create_label1' e 'create_label2' per creare due colonne di etichette.
        self.create_label1("Nome", 210)
        self.create_label1("Cognome", 250)
        self.create_label1("Codice Fiscale", 290)
        self.create_label1("Luogo di nascita", 330)
        self.create_label1("Email", 370)
        self.create_label1("Telefono", 410)
        self.create_label1("Data di nascita", 450)
        self.create_label1("Tipo contratto", 490)
        self.create_label1("Mansione", 530)
        self.create_label1("Sesso", 570)

        if not self.modifica:
            self.create_label2(self.dipendente.get_nome(), 210)
            self.create_label2(self.dipendente.get_cognome(), 250)
            self.create_label2(self.dipendente.get_cf(), 290)
            self.create_label2(self.dipendente.get_luogo_nascita(), 330)
            self.create_label2(self.dipendente.get_email(), 370)
            self.create_label2(self.dipendente.get_telefono(), 410)
            self.create_label2(self.dipendente.get_data_nascita(), 450)
            self.create_label2(self.dipendente.get_contratto(), 490)
            self.create_label2(self.dipendente.get_mansione(), 530)
        else:
            self.font_label = QFont("Arial", 12)

            self.nome_edit = QLineEdit(self)
            self.nome_edit.setText(self.dipendente.get_nome())
            self.nome_edit.setGeometry(300, 210, 180, 30)

            self.cognome_edit = QLineEdit(self)
            self.cognome_edit.setText(self.dipendente.get_cognome())
            self.cognome_edit.setGeometry(300, 250, 180, 30)

            self.cf_edit = QLineEdit(self)
            self.cf_edit.setText(self.dipendente.get_cf())
            self.cf_edit.setGeometry(300, 290, 180, 30)

            self.luogo_di_nascita_edit = QLineEdit(self)
            self.luogo_di_nascita_edit.setText(self.dipendente.get_luogo_nascita())
            self.luogo_di_nascita_edit.setGeometry(300, 330, 180, 30)

            self.email_edit = QLineEdit(self)
            self.email_edit.setText(self.dipendente.get_email())
            self.email_edit.setGeometry(300, 370, 180, 30)

            self.telefono_edit = QLineEdit(self)
            self.telefono_edit.setText(self.dipendente.get_telefono())
            self.telefono_edit.setGeometry(300, 410, 180, 30)

            self.data_edit = QLineEdit(self)
            self.data_edit.setText(self.dipendente.get_data_nascita())
            self.data_edit.setGeometry(300, 450, 180, 30)

            self.tipo_contratto_edit = QComboBox(self)
            contratti = ['Tirocinio', 'Determinato 6 mesi', 'Determinato 1 anno', 'Determinato 3 anni', 'Indeterminato']
            self.tipo_contratto_edit.addItems(contratti)
            self.tipo_contratto_edit.setGeometry(300, 490, 180, 30)

            self.mansione_edit = QComboBox(self)
            mansioni = ['Segretario', 'Istruttore', "Medico"]
            self.mansione_edit.addItems(mansioni)
            self.mansione_edit.setGeometry(300, 530, 180, 30)

        self.create_label2(self.dipendente.get_sesso(), 570)

        # Inserimento e impostazioni grafiche del bottone che consente di cambiare la fototessera del dipendente.
        self.button_foto = QPushButton(self)
        self.button_foto.setIcon(QIcon('Image/modifica.png'))
        self.button_foto.setIconSize(QSize(30, 30))
        self.button_foto.setGeometry(225, 105, 30, 30)
        self.button_foto.clicked.connect(self.upload_foto)

        # Inserimento e impostazioni grafiche del bottone che consente di eliminare la fototessera del cliente.
        self.button_rimuovi = QPushButton(self)
        self.button_rimuovi.setIcon(QIcon('Image/delete_black.png'))
        self.button_rimuovi.setIconSize(QSize(30, 30))
        self.button_rimuovi.setGeometry(225, 150, 30, 30)
        self.button_rimuovi.clicked.connect(self.rimuovi_foto)

        # Inserimento e impostazioni grafiche dell'etichetta 'Fototessera'.
        self.label_foto = QLabel(self)
        self.font = QFont("Times", 12, QFont.Bold)
        self.label_foto.setText("Fototessera")
        self.label_foto.setFont(self.font)
        self.label_foto.setGeometry(100, 110, 120, 30)

        # Inserimento e impostazioni grafiche del frame destinato alla fototessera..
        self.frame_foto = QFrame(self)
        self.frame_foto.setStyleSheet('background-color: white;')
        self.frame_foto.setGeometry(300, 45, 160, 160)

        # In base all'attributo 'sesso' del cliente viene inserita un immagine di default nel grame della fototessera.
        # Ciò avviente solo nel caso in cui non sia già stata inserita una fototessera.
        if self.dipendente.get_path() == "None":
            if self.dipendente.get_sesso() == "Uomo":
                self.imagePath = "Image/maschio.png"
                self.image = QImage(self.imagePath)
                self.label_maschio = QLabel(self)
                self.label_maschio.setPixmap(QPixmap.fromImage(self.image))
                self.label_maschio.setScaledContents(True)
                self.label_maschio.setGeometry(305, 50, 150, 150)
            else:
                self.imagePath = "Image/femmina.png"
                self.image = QImage(self.imagePath)
                self.label_femmina = QLabel(self)
                self.label_femmina.setPixmap(QPixmap.fromImage(self.image))
                self.label_femmina.setScaledContents(True)
                self.label_femmina.setGeometry(305, 50, 150, 150)
        else:
            self.imagePath = self.dipendente.get_path()
            self.image = QImage(self.imagePath)
            self.label_foto = QLabel(self)
            self.label_foto.setPixmap(QPixmap.fromImage(self.image))
            self.label_foto.setScaledContents(True)
            self.label_foto.setGeometry(305, 50, 150, 150)

        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(70, 70))
        self.button_back.setGeometry(75, 620, 70, 70)

        if not self.modifica:
            self.button_back.clicked.connect(self.go_back)
        else:
            self.button_back.clicked.connect(self.go_back_modifica)

        if not self.modifica:
            self.button_modifica = QPushButton(self)
            self.button_modifica.setText("Modifica dati")
            self.button_modifica.setStyleSheet(self.stylesheet)
            self.button_modifica.clicked.connect(self.modifica_dati)
            self.button_modifica.setGeometry(250, 630, 150, 50)
        else:
            self.button_salva = QPushButton(self)
            self.button_salva.setText("Salva")
            self.button_salva.setStyleSheet(self.stylesheet)
            self.button_salva.clicked.connect(self.salva_dati)
            self.button_salva.setGeometry(250, 630, 150, 50)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella prima colonna.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(100, posizione, 165, 30)
        font_label = QFont("Times", 12, QFont.Bold)
        label_edit.setFont(font_label)

    # == create_label2 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella seconda colonna.
    def create_label2(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(300, posizione, 200, 30)
        font_label = QFont("Times", 11)
        label_edit.setFont(font_label)

    # == upload_foto ==
    # La funzione permette di caricare un'immagine in formato .jpg oppure .png dal computer.
    def upload_foto(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', '/home', 'Images(*.jpg *.png)')
        if filename[0]:
            if self.dipendente.get_path() != "None":
                path = self.dipendente.get_path()
                os.remove(path)
            f = open(filename[0], 'r')
            src = f.name
            des = 'Image/'
            path = shutil.copy2(src, des)
            for dipendente in self.lista_dipendenti:
                controller_dipendente = ControllerDipendente(dipendente)

                if controller_dipendente.get_nome()+" "+controller_dipendente.get_cognome() == \
                        self.dipendente.get_nome()+" "+self.dipendente.get_cognome():
                    controller_dipendente.set_path(path)
                    self.dipendente = dipendente
            self.controller.save_data()
            self.refresh()
        else:
            return

    def refresh(self):
        self.go_vista_dipendente = VistaDipendente(self.cliente, False)
        self.go_vista_dipendente.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_dipendenti = VistaListaDipendenti.VistaListaDipendenti()
        self.go_lista_dipendenti.show()
        self.close()

    def go_back_modifica(self):
        self.go_dipendente = VistaDipendente(self.dipendente, False)
        self.go_dipendente.show()
        self.close()

    def modifica_dati(self):
        self.go_dipendente_modificato = VistaDipendente(self.dipendente, True)
        self.go_dipendente_modificato.show()
        self.close()

    def salva_dati(self):
        for dipendente in self.lista_dipendenti:
            controller_dipendente = ControllerDipendente(dipendente)

            if controller_dipendente.get_nome() + " " + controller_dipendente.get_cognome() == \
                    self.dipendente.get_nome() + " " + self.dipendente.get_cognome():
                controller_dipendente.set_nome(self.nome_edit.text())
                controller_dipendente.set_cognome(self.cognome_edit.text())
                controller_dipendente.set_cf(self.cf_edit.text())
                controller_dipendente.set_luogo_nascita(self.luogo_di_nascita_edit.text())
                controller_dipendente.set_email(self.email_edit.text())
                controller_dipendente.set_telefono(self.telefono_edit.text())
                controller_dipendente.set_data_nascita(self.data_edit.text())
                controller_dipendente.set_contratto(self.tipo_contratto_edit.currentText())
                controller_dipendente.set_mansione(self.mansione_edit.currentText())
                self.dipendente = dipendente
        self.controller.save_data()
        self.go_dipendente_mod = VistaDipendente(self.dipendente, False)
        self.go_dipendente_mod.show()
        self.close()

    def rimuovi_foto(self):
        for dipendente in self.lista_dipendenti:
            controller_dipendente = ControllerDipendente(dipendente)

            if controller_dipendente.get_nome() + " " + controller_dipendente.get_cognome() == \
                    self.dipendente.get_nome() + " " + self.dipendente.get_cognome():
                if controller_dipendente.get_path() == "None":
                    QMessageBox.information(self, "Attenzione", "Nessuna foto da eliminare")
                else:
                    path = self.controller_dipendente.get_path()
                    os.remove(path)
                    controller_dipendente.set_path("None")
                    self.dipendente = dipendente
                    self.controller.save_data()
        self.refresh()
