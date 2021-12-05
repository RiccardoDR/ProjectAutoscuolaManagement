from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente


class VistaPagamentiEffettuati(QWidget):  # Apre la vista che visualizza quali pagamenti sono stati effettuati dal cliente.
    def __init__(self, cliente):
        super(VistaPagamentiEffettuati, self).__init__()

        self.controller_cliente = ControllerCliente(cliente)

        # Inserimento della tabella e intestazione delle colonne.
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(2)
        self.table.setItem(0, 0, QTableWidgetItem("Iscrizione"))
        self.table.setItem(0, 1, QTableWidgetItem("Esame teorico"))
        self.table.setItem(0, 2, QTableWidgetItem("Guide"))
        self.table.setItem(0, 3, QTableWidgetItem("Esame pratico"))

        # Impostazioni grafiche della tabella.
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().hide()
        self.table.horizontalScrollBar().setDisabled(True)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().hide()
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.setSelectionMode(self.table.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)

        # Inserimento e impostazioni grafiche delle icone nella tabella.
        self.icon_no = QIcon("Image/no.png")
        self.icon_si = QIcon("Image/si.png")
        self.icon_sino = QIcon("Image/sino.png")
        self.no = QTableWidgetItem()
        self.no.setIcon(self.icon_no)
        self.si = QTableWidgetItem()
        self.si.setIcon(self.icon_si)

        # I seguenti if-else impostano l'icona corretta se il pagamento è stato effettuato o meno.
        if self.controller_cliente.get_pagamento_iniziale() == "None":
            self.table.setItem(1, 0, QTableWidgetItem(self.no))
        else:
            self.table.setItem(1, 0, QTableWidgetItem(self.si))
        if self.controller_cliente.get_pagamento_esame_teorico() == "None":
            self.table.setItem(1, 1, QTableWidgetItem(self.no))
        else:
            self.table.setItem(1, 1, QTableWidgetItem(self.si))
        if self.controller_cliente.get_pagamento_lezioni_guida() == "None":
            self.table.setItem(1, 2, QTableWidgetItem(self.no))
        else:
            self.table.setItem(1, 2, QTableWidgetItem(self.si))
        if self.controller_cliente.get_pagamento_esame_pratico() == "None":
            self.table.setItem(1, 3, QTableWidgetItem(self.no))
        else:
            self.table.setItem(1, 3, QTableWidgetItem(self.si))

        # Impostazioni grafiche generali della finestra del programma.
        self.table.setGeometry(20, 20, 600, 76)
        self.resize(640, 140)
        self.setFixedSize(self.size())
        self.setWindowTitle("Pagamenti Cliente")
