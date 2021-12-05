from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QLabel, QMessageBox

from ProgettoAutoscuola.Pagamento.Controller.ControllerPagamento import ControllerPagamento
from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPagamenti.Controller.ControllerListaPagamenti import ControllerListaPagamenti
from ProgettoAutoscuola.ListaPagamenti.View.VistaPagamento import VistaPagamento


class VistaListaPagamenti(QWidget):  # Apre la vista che visualizza la lista dei pagamenti.
    def __init__(self, parent=None):
        super(VistaListaPagamenti, self).__init__(parent)

        self.controller = ControllerListaPagamenti()
        self.controller.set_data()
        self.lista_pagamenti = self.controller.get_lista_pagamenti()

        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()
        self.lista_clienti = self.controller_clienti.get_lista_clienti()

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
        self.setWindowTitle("Lista Pagamenti")
        self.resize(1250, 700)
        self.setFixedSize(self.size())

        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento della tabella e intestazione delle colonne.
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Prezzo"))
        self.table.setItem(0, 2, QTableWidgetItem("Descrizione"))
        self.table.setItem(0, 3, QTableWidgetItem("Cliente"))

        self.set_data()  # Inserisce nella tabella i dati contenuti nella lista_pagamenti.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(50, 30, 1150, 550)
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
        self.button_back.setGeometry(70, 600, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per aggiungere un nuovo pagamento alla lista.
        self.button_new_dipendente = QPushButton(self)
        self.button_new_dipendente.setText("Nuovo Pagamento")
        self.font_button = QFont("Times", 11)
        self.button_new_dipendente.setFont(self.font_button)
        self.button_new_dipendente.setGeometry(1000, 620, 190, 50)
        self.button_new_dipendente.setStyleSheet(self.stylesheet)
        self.button_new_dipendente.clicked.connect(self.go_new_pagamento)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative al pagamento e contenute nel file
    # 'lista_pagamenti.pickle' nella tabella della VistaListaPagamenti.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_pagamenti)
        self.table.setRowCount(n_righe+1)
        for pagamento in self.lista_pagamenti:
            controller_pagamento = ControllerPagamento(pagamento)

            self.table.setItem(i, 0, QTableWidgetItem(controller_pagamento.get_id()))
            self.table.setItem(i, 1, QTableWidgetItem(controller_pagamento.get_prezzo()))
            self.table.setItem(i, 2, QTableWidgetItem(controller_pagamento.get_descrizione()))
            self.table.setItem(i, 3, QTableWidgetItem(controller_pagamento.get_cliente()))
            i += 1

    # == go_new_pagamento ==
    # La funzione si occupa di aprire la VistaPagamento.
    def go_new_pagamento(self):
        if not self.lista_clienti:
            QMessageBox.information(self, "Attenzione", "Nessun cliente presente nel sistema")
        else:
            self.vista_nuovo_pagamento = VistaPagamento()
            self.vista_nuovo_pagamento.show()
            self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.vista_home = VistaHomeSegretario.VistaHomeSegretario()
        self.vista_home.show()
        self.close()
