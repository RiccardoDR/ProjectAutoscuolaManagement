from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QCalendarWidget, QPushButton, QComboBox, QMessageBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.VisitaMedica.Controller.ControllerVisitaMedica import ControllerVisitaMedica
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.ListaVisiteMediche.View import VistaListaVisiteMediche
from ProgettoAutoscuola.VisitaMedica.Model.VisitaMedica import VisitaMedica


class VistaPrenotaVisitaMedica(QWidget):  # Apre la vista per consente di prenotare una visita medica
    def __init__(self, parent=None):
        super(VistaPrenotaVisitaMedica, self).__init__(parent)

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
        self.setWindowTitle("Prenota Visita")
        self.resize(1050, 600)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Prenota Visita'.
        self.label = QLabel(self)
        self.font = QFont("Times", 18)
        self.label.setText("Prenota Visita")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 250, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 950, 330)

        # Usa la funzione 'create_label1' e 'create_label2' per creare due colonne di etichette.
        self.create_label1("Cliente", 150)
        self.create_label2("Data visita", 150)

        # Inserimento e impostazioni grafiche del menù a tendina contenente la lista dei clienti.
        self.edit_cf_cliente = QComboBox(self)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_visita_medica() == "None" and \
                    controller_cliente.get_pagamento_iniziale() != "None":
                    self.edit_cf_cliente.addItem(controller_cliente.get_nome() + " " + controller_cliente.get_cognome())
        self.edit_cf_cliente.setGeometry(175, 150, 200, 30)

        # Inserimento e impostazioni grafiche del calendario.
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setGeometry(500, 150, 475, 250)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(50, 470, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone che consente di confermare la prenotazione
        self.button_prenota = QPushButton(self)
        self.button_prenota.setText("Prenota visita")
        self.font_button = QFont("Times", 11)
        self.button_prenota.setFont(self.font_button)
        self.button_prenota.setGeometry(750, 490, 200, 50)
        self.button_prenota.setStyleSheet(self.stylesheet)
        self.button_prenota.clicked.connect(self.go_prenotazione)

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
        label_edit.setGeometry(400, posizione, 115, 20)
        font_label = QFont("Times", 9)
        label_edit.setFont(font_label)

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.vista_home = VistaListaVisiteMediche.VistaListaVisiteMediche()
        self.vista_home.show()
        self.close()

    # == go_prenotazione ==
    # La funzione aggiunge la visita fissata per la data selezionata dal calendario nella lista_visite.
    # Successivamente viene mandato un messaggio di conferma all'utente e infine viene riaperta la
    # VistaListaVisiteMediche.
    def go_prenotazione(self):
        trovato = False
        for visita in self.lista_visite:
            controller_visita = ControllerVisitaMedica(visita)

            if controller_visita.get_cliente() == self.edit_cf_cliente.currentText():
                trovato = True

        if trovato:
            conferma = QMessageBox.question(self, "Attenzione",
                                            "Il cliente si è già prenotato, vuoi prenotarlo di nuovo?"
                                            , QMessageBox.Yes, QMessageBox.No)
            if conferma == QMessageBox.Yes:
                for visita in self.lista_visite:
                    controller_visita = ControllerVisitaMedica(visita)

                    if controller_visita.get_cliente() == self.edit_cf_cliente.currentText():
                        controller_visita.set_data(self.calendar.selectedDate().toString("dd-MM-yyyy"))
                        self.controller.save_data()
                        self.go_lista_visite = VistaListaVisiteMediche.VistaListaVisiteMediche()
                        self.go_lista_visite.show()
                        self.close()
            else:
                return
        else:
            self.controller.aggiungi_visita(VisitaMedica(self.edit_cf_cliente.currentText(),
                                                         self.calendar.selectedDate().toString("dd-MM-yyyy")))
            QMessageBox.information(self, "Prenotato",
                                    "Visita prenotata per il " + self.calendar.selectedDate().toString("dd-MM-yyyy"))
            self.controller.save_data()
            self.go_lista_visite = VistaListaVisiteMediche.VistaListaVisiteMediche()
            self.go_lista_visite.show()
            self.close()
