from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QFrame, QCalendarWidget, QMessageBox

from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.VisitaMedica.Model.VisitaMedica import VisitaMedica
from ProgettoAutoscuola.ListaPagamenti.View.VistaRiepilogo import VistaRiepilogo


class VistaRinnovoPatente(QWidget):  # Apre la vista che permette di rinnovare una patente
    def __init__(self, parent=None):
        super(VistaRinnovoPatente, self).__init__(parent)

        self.controller = ControllerListaVisiteMediche()
        self.controller.set_data()

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
        self.setWindowTitle("Rinnovo Patente")
        self.resize(1250, 600)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Rinnovo Patente'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Rinnovo Patente")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 300, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 1150, 330)

        # Usa la funzione 'create_label1' e 'create_label2' per creare due colonne di etichette.
        self.create_label1("Nome", 150)
        self.create_label1("Cognome", 200)
        self.create_label1("Numero patente", 300)
        self.create_label2("Visita medica", 150)

        # Inserimento e impostazioni grafiche delle caselle di testo per inserire le informazioni
        # della patente da rinnovare.
        self.edit_nome = QLineEdit(self)
        self.edit_nome.setGeometry(250, 150, 200, 30)

        self.edit_cognome = QLineEdit(self)
        self.edit_cognome.setGeometry(250, 200, 200, 30)

        self.edit_patente = QLineEdit(self)
        self.edit_patente.setGeometry(250, 300, 200, 30)

        # Inserimento e impostazioni grafiche del calendario.
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(670, 150, 475, 250)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(50, 470, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per procedere col pagamento della
        # procedura di rinnovo della patente.
        self.button_pagamento = QPushButton(self)
        self.button_pagamento.setText("Procedi pagamento")
        self.font_button = QFont("Times", 11)
        self.button_pagamento.setFont(self.font_button)
        self.button_pagamento.setGeometry(1000, 490, 200, 50)
        self.button_pagamento.setStyleSheet(self.stylesheet)
        self.button_pagamento.clicked.connect(self.go_pagamento)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella prima colonna.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 130, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == create_label2 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    # Le etichette create con questa funzione verranno collocate nella seconda colonna.
    def create_label2(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(500, posizione, 135, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.vista_home = VistaHomeSegretario.VistaHomeSegretario()
        self.vista_home.show()
        self.close()

    # == go_pagamento ==
    # La funzione apre la VistaRiepilogo e gli passa i parametri di pagamento
    # per il rinnovo della patente.
    def go_pagamento(self):
        if self.edit_nome.text() == "" or self.edit_cognome.text() == "" or self.edit_patente.text() == "":
            QMessageBox.critical(self, "Attenzione", "Inserisci tutti i dati!")
        else:
            if len(self.edit_patente.text()) != 10:
                QMessageBox.critical(self, "Errore", "Il numero patente immesso non è valido")
                self.edit_patente.clear()
            else:
                self.visita_medica = VisitaMedica(self.edit_nome.text()+" "+self.edit_cognome.text(),
                                                  self.calendar.selectedDate().toString("dd-MM-yyyy"))
                self.controller.aggiungi_visita(self.visita_medica)
                self.controller.save_data()

                self.pagamento = VistaRiepilogo("80", "Bollettini + visita medica (Rinnovo patente)", -1,
                                                self.edit_nome.text()+" "+self.edit_cognome.text())
                self.pagamento.show()
                self.close()
