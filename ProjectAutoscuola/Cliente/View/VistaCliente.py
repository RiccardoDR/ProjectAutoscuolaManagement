import shutil
import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QFileDialog, QLineEdit, QMessageBox, QComboBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.ListaClienti.View import VistaListaClienti
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class VistaCliente(QWidget):  # Apre la vista che visualizza le informazioni del cliente.
    def __init__(self, cliente, modifica):
        super(VistaCliente, self).__init__()
        self.cliente = cliente
        self.modifica = modifica

        self.controller = ControllerListaClienti()
        self.controller.set_data()
        self.lista_clienti = self.controller.get_lista_clienti()

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
        self.setWindowTitle("Info Cliente")
        self.resize(600, 730)
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
        self.create_label1("Nome", 220)
        self.create_label1("Cognome", 265)
        self.create_label1("Tipo Patente", 310)
        self.create_label1("Codice Fiscale", 355)
        self.create_label1("Indirizzo", 400)
        self.create_label1("Email", 445)
        self.create_label1("Telefono", 490)
        self.create_label1("Data di nascita", 535)
        self.create_label1("Sesso", 575)

        if not self.modifica:
            self.create_label2(self.cliente.get_nome(), 220)
            self.create_label2(self.cliente.get_cognome(), 265)
            self.create_label2(self.cliente.get_tipo_patente(), 310)
            self.create_label2(self.cliente.get_cf(), 355)
            self.create_label2(self.cliente.get_indirizzo(), 400)
            self.create_label2(self.cliente.get_email(), 445)
            self.create_label2(self.cliente.get_telefono(), 490)
            self.create_label2(self.cliente.get_data_nascita(), 535)
        else:
            self.font_label = QFont("Arial", 12)

            self.nome_edit = QLineEdit(self)
            self.nome_edit.setText(self.cliente.get_nome())
            self.nome_edit.setGeometry(300, 220, 180, 30)

            self.cognome_edit = QLineEdit(self)
            self.cognome_edit.setText(self.cliente.get_cognome())
            self.cognome_edit.setGeometry(300, 265, 180, 30)

            self.patente = QComboBox(self)
            patenti = ['AM', 'A1', 'A2', 'A', 'B1', 'B', 'C1', 'C', 'D1', 'D']
            self.patente.addItems(patenti)
            self.patente.setCurrentIndex(patenti.index(self.cliente.get_tipo_patente()))
            self.patente.setGeometry(300, 310, 180, 30)

            self.cf_edit = QLineEdit(self)
            self.cf_edit.setText(self.cliente.get_cf())
            self.cf_edit.setGeometry(300, 355, 180, 30)

            self.indirizzo_edit = QLineEdit(self)
            self.indirizzo_edit.setText(self.cliente.get_indirizzo())
            self.indirizzo_edit.setGeometry(300, 400, 180, 30)

            self.email_edit = QLineEdit(self)
            self.email_edit.setText(self.cliente.get_email())
            self.email_edit.setGeometry(300, 445, 180, 30)

            self.telefono_edit = QLineEdit(self)
            self.telefono_edit.setText(self.cliente.get_telefono())
            self.telefono_edit.setGeometry(300, 490, 180, 30)

            self.data_edit = QLineEdit(self)
            self.data_edit.setText(self.cliente.get_data_nascita())
            self.data_edit.setGeometry(300, 535, 180, 30)

        self.create_label2(self.cliente.get_sesso(), 575)

        # Inserimento e impostazioni grafiche del bottone che consente di cambiare la fototessera del cliente.
        self.button_foto = QPushButton(self)
        self.button_foto.setIcon(QIcon('Image/modifica.png'))
        self.button_foto.setIconSize(QSize(30, 30))
        self.button_foto.setGeometry(235, 105, 30, 30)
        self.button_foto.clicked.connect(self.upload_foto)

        # Inserimento e impostazioni grafiche del bottone che consente di eliminare la fototessera del cliente.
        self.button_rimuovi = QPushButton(self)
        self.button_rimuovi.setIcon(QIcon('Image/delete_black.png'))
        self.button_rimuovi.setIconSize(QSize(30, 30))
        self.button_rimuovi.setGeometry(235, 150, 30, 30)
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
        if self.cliente.get_path() == "None":
            if self.cliente.get_sesso() == "Uomo":
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
            self.imagePath = self.cliente.get_path()
            self.image = QImage(self.imagePath)
            self.label_foto = QLabel(self)
            self.label_foto.setPixmap(QPixmap.fromImage(self.image))
            self.label_foto.setScaledContents(True)
            self.label_foto.setGeometry(305, 50, 150, 150)

        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(70, 70))
        self.button_back.setGeometry(75, 635, 70, 70)

        if not self.modifica:
            self.button_back.clicked.connect(self.go_back)
        else:
            self.button_back.clicked.connect(self.go_back_modifica)

        if not self.modifica:
            self.button_modifica = QPushButton(self)
            self.button_modifica.setText("Modifica dati")
            self.font_button = QFont("Times", 11)
            self.button_modifica.setFont(self.font_button)
            self.button_modifica.clicked.connect(self.modifica_dati)
            self.button_modifica.setStyleSheet(self.stylesheet)
            self.button_modifica.setGeometry(250, 645, 150, 50)
        else:
            self.button_salva = QPushButton(self)
            self.button_salva.setText("Salva")
            self.button_salva.clicked.connect(self.salva_dati)
            self.button_salva.setStyleSheet(self.stylesheet)
            self.button_salva.setGeometry(250, 645, 150, 50)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella prima colonna.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(100, posizione, 150, 30)
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
            if self.cliente.get_path() != "None":
                path = self.cliente.get_path()
                os.remove(path)
            f = open(filename[0], 'r')
            src = f.name
            des = 'Image/'
            path = shutil.copy2(src, des)
            for cliente in self.lista_clienti:
                controller_cliente = ControllerCliente(cliente)

                if controller_cliente.get_nome() + " " + controller_cliente.get_cognome() == \
                        self.cliente.get_nome() + " " + self.cliente.get_cognome():
                    controller_cliente.set_path(path)
                    self.cliente = cliente
            self.controller.save_data()
            self.refresh()
        else:
            return

    def refresh(self):
        self.go_vista_cliente = VistaCliente(self.cliente, False)
        self.go_vista_cliente.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_clienti = VistaListaClienti.VistaListaClienti()
        self.go_lista_clienti.show()
        self.close()

    def go_back_modifica(self):
        self.go_cliente = VistaCliente(self.cliente, False)
        self.go_cliente.show()
        self.close()

    def modifica_dati(self):
        self.go_cliente_modificato = VistaCliente(self.cliente, True)
        self.go_cliente_modificato.show()
        self.close()

    def salva_dati(self):
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_nome() + " " + controller_cliente.get_cognome() == \
                    self.cliente.get_nome() + " " + self.cliente.get_cognome():
                controller_cliente.set_nome(self.nome_edit.text())
                controller_cliente.set_cognome(self.cognome_edit.text())
                controller_cliente.set_tipo_patente(self.patente.currentText())
                controller_cliente.set_cf(self.cf_edit.text())
                controller_cliente.set_indirizzo(self.indirizzo_edit.text())
                controller_cliente.set_email(self.email_edit.text())
                controller_cliente.set_telefono(self.telefono_edit.text())
                controller_cliente.set_data_nascita(self.data_edit.text())
                self.cliente = cliente
        self.controller.save_data()
        self.go_cliente_mod = VistaCliente(self.cliente, False)
        self.go_cliente_mod.show()
        self.close()

    def rimuovi_foto(self):
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_nome() + " " + controller_cliente.get_cognome() == \
                    self.cliente.get_nome() + " " + self.cliente.get_cognome():
                if controller_cliente.get_path() == "None":
                    QMessageBox.information(self, "Attenzione", "Nessuna foto da eliminare")
                else:
                    path = controller_cliente.get_path()
                    os.remove(path)
                    controller_cliente.set_path("None")
                    self.cliente = cliente
                    self.controller.save_data()
        self.refresh()
