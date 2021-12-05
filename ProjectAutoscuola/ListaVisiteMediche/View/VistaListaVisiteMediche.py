from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QPushButton, QLabel

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.VisitaMedica.Controller.ControllerVisitaMedica import ControllerVisitaMedica
from ProgettoAutoscuola.Home.View import VistaHomeMedico
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.ListaVisiteMediche.View import VistaPrenotaVisitaMedica


class VistaListaVisiteMediche(QWidget):  # Apre la vista che visualizza la lista delle visite mediche.
    def __init__(self, parent=None):
        super(VistaListaVisiteMediche, self).__init__(parent)

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
        self.setWindowTitle("Lista Visite Mediche")
        self.resize(1250, 750)
        self.setFixedSize(self.size())

        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento della tabella e intestazione delle colonne.
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Cliente"))
        self.table.setItem(0, 2, QTableWidgetItem("Data visita"))
        self.table.setItem(0, 3, QTableWidgetItem("Descrizione"))
        self.table.setItem(0, 4, QTableWidgetItem("Esito"))

        self.icon_no = QIcon("Image/no.png")
        self.icon_si = QIcon("Image/si.png")
        self.no = QTableWidgetItem()
        self.no.setIcon(self.icon_no)
        self.si = QTableWidgetItem()
        self.si.setIcon(self.icon_si)

        self.set_data()  # Inserisce nella tabella i dati contenuti nella lista_visite.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(70, 50, 1100, 550)
        #self.table.setStyleSheet(self.stylesheet_table)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().hide()
        self.table.horizontalScrollBar().setDisabled(True)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().hide()
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.setSelectionMode(self.table.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(70, 630, 90, 90)
        #self.button_back.setStyleSheet(self.stylesheet_button_back)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per inserire una nuova prenotazione
        # per una visita medica.
        self.button_new_visita = QPushButton(self)
        self.button_new_visita.setText("Prenota Visita")
        self.font_button = QFont("Times", 11)
        self.button_new_visita.setFont(self.font_button)
        self.button_new_visita.setGeometry(980, 650, 190, 50)
        self.button_new_visita.setStyleSheet(self.stylesheet)
        self.button_new_visita.clicked.connect(self.go_new_visita)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative alle prenotazioni e contenute nel file
    # 'lista_visite.pickle' nella tabella della VistaListaVisiteMediche.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_visite)
        self.table.setRowCount(n_righe + 1)
        for visita in self.lista_visite:
            controller_visita = ControllerVisitaMedica(visita)

            self.table.setItem(i, 0, QTableWidgetItem(controller_visita.get_id()))
            self.table.setItem(i, 1, QTableWidgetItem(controller_visita.get_cliente()))
            self.table.setItem(i, 2, QTableWidgetItem(controller_visita.get_data()))

            if controller_visita.get_descrizione() == "None":
                self.table.setItem(i, 3, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 3, QTableWidgetItem(controller_visita.get_descrizione()))
            if controller_visita.get_esito() == "None":
                self.table.setItem(i, 4, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 4, QTableWidgetItem(controller_visita.get_esito()))
            i += 1

    # == go_new_visita ==
    # La funzione si occupa di aprire la VistaPrenotaVisitaMedica.
    def go_new_visita(self):
        trovato = False
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_visita_medica() == "None":
                trovato = True
        if not trovato:
            QMessageBox.information(self, "Attenzione", "Nessun cliente disponibile per prenotarsi")
        else:
            self.vista_nuovo_dipendente = VistaPrenotaVisitaMedica.VistaPrenotaVisitaMedica()
            self.vista_nuovo_dipendente.show()
            self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeMedico.VistaHomeMedico()
        self.go_home.show()
        self.close()
