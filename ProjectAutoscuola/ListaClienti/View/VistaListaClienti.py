from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QLabel, \
    QButtonGroup

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPagamenti.Controller.ControllerListaPagamenti import ControllerListaPagamenti
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.Cliente.View.VistaCliente import VistaCliente
from ProgettoAutoscuola.ListaClienti.View.VistaNuovoCliente import VistaNuovoCliente
from ProgettoAutoscuola.ListaClienti.View.VistaPagamentiEffettuati import VistaPagamentiEffettuati


class VistaListaClienti(QWidget):  # Apre la vista che contiene la lista dei clienti
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        self.controller = ControllerListaClienti()
        self.controller.set_data()
        self.lista_clienti = self.controller.get_lista_clienti()

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
        self.setWindowTitle("Lista Clienti")
        self.resize(1400, 750)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento della tabella e intestazione delle colonne.
        self.table = QTableWidget(self)
        self.table.setColumnCount(10)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("Apri"))
        self.table.setItem(0, 1, QTableWidgetItem("ID"))
        self.table.setItem(0, 2, QTableWidgetItem("Nome"))
        self.table.setItem(0, 3, QTableWidgetItem("Cognome"))
        self.table.setItem(0, 4, QTableWidgetItem("Patente"))
        self.table.setItem(0, 5, QTableWidgetItem("Esame teorico"))
        self.table.setItem(0, 6, QTableWidgetItem("Esame pratico"))
        self.table.setItem(0, 7, QTableWidgetItem("Pagamenti"))
        self.table.setItem(0, 8, QTableWidgetItem("Prenotazione"))
        self.table.setItem(0, 9, QTableWidgetItem("Cancella"))

        self.button_group_apri = QButtonGroup()
        self.button_group_elimina = QButtonGroup()
        self.button_group_pagamenti = QButtonGroup()
        self.icon_no = QIcon("Image/no.png")
        self.icon_si = QIcon("Image/si.png")
        self.icon_sino = QIcon("Image/sino.png")
        self.apri_icon = QIcon("Image/apri_icon.png")
        self.cancella_icon = QIcon("Image/delete.png")
        self.no = QTableWidgetItem()
        self.no.setIcon(self.icon_no)
        self.si = QTableWidgetItem()
        self.si.setIcon(self.icon_si)
        self.button_group_apri.buttonClicked.connect(self.on_selection_apri)
        self.button_group_elimina.buttonClicked.connect(self.on_selection_elimina)
        self.button_group_pagamenti.buttonClicked.connect(self.on_selection_pagamenti)

        self.set_data()  # Inserisce nella tabella i dati contenuti nella lista_clienti.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(50, 50, 1300, 550)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 220)
        self.table.setColumnWidth(3, 220)
        self.table.setColumnWidth(4, 90)
        self.table.setColumnWidth(5, 110)
        self.table.setColumnWidth(6, 110)
        self.table.setColumnWidth(7, 110)
        self.table.setColumnWidth(8, 190)
        self.table.setColumnWidth(9, 70)
        self.table.horizontalHeader().setStretchLastSection(True)
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
        self.button_back.setGeometry(60, 630, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per inserire un nuovo cliente nella lista.
        self.button_new_cliente = QPushButton(self)
        self.button_new_cliente.setText("Nuovo cliente")
        self.font_button = QFont("Times", 11, QFont.DemiBold)
        self.button_new_cliente.setFont(self.font_button)
        self.button_new_cliente.setGeometry(1210, 650, 140, 50)
        self.button_new_cliente.setStyleSheet(self.stylesheet)
        self.button_new_cliente.clicked.connect(self.go_new_cliente)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative al cliente e contenute nel file
    # 'lista_clienti.pickle' nella tabella della VistaListaClienti. Per ogni cliente è disponibile
    # aprire e visualizzare le sue informazioni attraverso un bottone 'Apri' ed è possibile cancellarle
    # attraverso un bottone 'Elimina'.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_clienti)
        self.table.setRowCount(n_righe + 1)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            sino = QPushButton()
            sino.setIcon(self.icon_sino)
            self.button_group_pagamenti.addButton(sino, i)

            apri = QPushButton()
            apri.setIcon(self.apri_icon)
            apri.setIconSize(QSize(30, 30))
            self.button_group_apri.addButton(apri, i)
            self.table.setCellWidget(i, 0, apri)

            if controller_cliente.get_id() == "None":
                self.table.setItem(i, 1, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 1, QTableWidgetItem(controller_cliente.get_id()))
            self.table.setItem(i, 2, QTableWidgetItem(controller_cliente.get_nome()))
            self.table.setItem(i, 3, QTableWidgetItem(controller_cliente.get_cognome()))
            self.table.setItem(i, 4, QTableWidgetItem(controller_cliente.get_tipo_patente()))
            if controller_cliente.get_esame_teorico() == "None":
                self.table.setItem(i, 5, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 5, QTableWidgetItem(self.si))
            if controller_cliente.get_esame_pratico() == "None":
                self.table.setItem(i, 6, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 6, QTableWidgetItem(self.si))
            if controller_cliente.get_pagamento_iniziale() == "None" and \
                    controller_cliente.get_pagamento_esame_teorico() == "None" and \
                    controller_cliente.get_pagamento_lezioni_guida() == "None" and \
                    controller_cliente.get_pagamento_esame_pratico() == "None":
                self.table.setItem(i, 7, QTableWidgetItem(self.no))
            else:
                if controller_cliente.get_pagamento_iniziale() != "None" and \
                        controller_cliente.get_pagamento_esame_teorico() != "None" and \
                        controller_cliente.get_pagamento_lezioni_guida() != "None" and \
                        controller_cliente.get_pagamento_esame_pratico() != "None":
                    self.table.setItem(i, 7, QTableWidgetItem(self.si))
                else:
                    self.table.setCellWidget(i, 7, sino)
            if controller_cliente.get_prenotazione() == "None":
                if controller_cliente.get_esame_pratico() == "Effettuato" and \
                        controller_cliente.get_esame_teorico() == "Effettuato":
                    self.table.setItem(i, 8, QTableWidgetItem(self.si))
                else:
                    self.table.setItem(i, 8, QTableWidgetItem(self.no))
            else:
                self.table.setItem(i, 8, QTableWidgetItem(controller_cliente.get_prenotazione()))

            delete = QPushButton()
            delete.setIcon(self.cancella_icon)
            delete.setIconSize(QSize(35, 35))
            self.button_group_elimina.addButton(delete, i)
            self.table.setCellWidget(i, 9, delete)
            i += 1

    # == go_new_cliente ==
    # La funzione si occupa di aprire la VistaNuovoCliente.
    def go_new_cliente(self):
        self.vista_nuovo_cliente = VistaNuovoCliente()
        self.vista_nuovo_cliente.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_clienti = VistaHomeSegretario.VistaHomeSegretario()
        self.go_lista_clienti.show()
        self.close()

    # == go_pagamenti ==
    # La funzione si occupa di aprire la VistaPagamentiEffettuati.
    def go_pagamenti(self, i):
        pagamento = self.lista_clienti[i-1]
        self.go_vedi_pagamenti = VistaPagamentiEffettuati(pagamento)
        self.go_vedi_pagamenti.show()

    # == go_apri ==
    # La funzione si occupa di aprire la VistaCliente corrispondente al cliente scelto.
    def go_apri(self, i):
        cliente = self.lista_clienti[i - 1]
        self.go_cliente = VistaCliente(cliente, False)
        self.go_cliente.show()
        self.close()

    # == go_elimina ==
    # La funzione, dopo aver chiesto conferma all'utente, cancella le informazioni relative al
    # cliente scelto.
    def go_elimina(self, i):
        conferma = QMessageBox.question(self, "Attenzione", "Sei sicuro di voler eliminare questo cliente?",
                                        QMessageBox.No, QMessageBox.Yes)
        if conferma == QMessageBox.Yes:
            controller_pagamenti = ControllerListaPagamenti()
            controller_pagamenti.elimina_pagamento_by_cliente(i-1)

            controller_visite = ControllerListaVisiteMediche()
            controller_visite.elimina_visite_by_cliente(i-1)

            controller_pagamenti.save_data()
            controller_visite.save_data()

            self.controller.rimuovi_cliente_by_index(i-1)
            self.controller.save_data()
            self.refresh()
        else:
            return

    def refresh(self):
        self.go_lista = VistaListaClienti()
        self.go_lista.show()
        self.close()

    def on_selection_apri(self, selected):
        self.go_apri(self.button_group_apri.id(selected))

    def on_selection_elimina(self, selected):
        self.go_elimina(self.button_group_elimina.id(selected))

    def on_selection_pagamenti(self, selected):
        self.go_pagamenti(self.button_group_pagamenti.id(selected))
