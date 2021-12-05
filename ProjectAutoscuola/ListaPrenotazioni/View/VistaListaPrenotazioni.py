from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QButtonGroup, QMessageBox

from ProgettoAutoscuola.Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione
from ProgettoAutoscuola.Home.View import VistaHomeIstruttore
from ProgettoAutoscuola.ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni
from ProgettoAutoscuola.ListaPrenotazioni.View.VistaAggiungiOrari import VistaAggiungiOrari


class VistaListaPrenotazioni(QWidget):  # Apre la vista che visualizza la lista delle prenotazioni.
    def __init__(self, tipo):
        super(VistaListaPrenotazioni, self).__init__()
        self.tipo = tipo

        self.controller = ControllerListaPrenotazioni()
        self.controller.set_data()
        self.lista_prenotazioni = self.controller.get_lista_prenotazioni()

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
        self.setWindowTitle("Lista Prenotazioni")
        self.resize(970, 700)
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
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QTableWidgetItem("Tipo"))
        self.table.setItem(0, 2, QTableWidgetItem("Data"))
        self.table.setItem(0, 3, QTableWidgetItem("Elimina"))

        self.button_group_elimina = QButtonGroup()
        self.cancella_icon = QIcon("Image/delete.png")
        self.button_group_elimina.buttonClicked.connect(self.on_selection_elimina)

        self.set_data()   # Inserisce nella tabella i dati contenuti nella lista_prenotazioni.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(50, 30, 870, 550)
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 350)
        self.table.setColumnWidth(2, 350)
        self.table.setColumnWidth(3, 70)
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
        self.button_back.setGeometry(50, 600, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone che consente di aggiungere un orario per
        # le prenotazioni.
        self.button_new_prenotazione = QPushButton(self)
        self.button_new_prenotazione.setText("Aggiungi orari")
        self.font_button = QFont("Times", 11)
        self.button_new_prenotazione.setFont(self.font_button)
        self.button_new_prenotazione.setGeometry(780, 620, 140, 50)
        self.button_new_prenotazione.setStyleSheet(self.stylesheet)
        self.button_new_prenotazione.clicked.connect(self.go_aggiungi_orari)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative alla prenotazione e contenute nel file
    # 'lista_prenotazioni.pickle' nella tabella della VistaListaPrenotazioni.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_prenotazioni)
        self.table.setRowCount(n_righe + 1)
        for prenotazione in self.lista_prenotazioni:
            controller_prenotazione = ControllerPrenotazione(prenotazione)

            self.table.setItem(i, 0, QTableWidgetItem(controller_prenotazione.get_id()))
            self.table.setItem(i, 1, QTableWidgetItem(controller_prenotazione.get_tipo()))
            self.table.setItem(i, 2, QTableWidgetItem(controller_prenotazione.get_data()))

            delete = QPushButton()
            delete.setIcon(self.cancella_icon)
            delete.setIconSize(QSize(35, 35))
            self.button_group_elimina.addButton(delete, i)
            self.table.setCellWidget(i, 3, delete)
            i += 1

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_prenotazioni = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_prenotazioni.show()
        self.close()

    # == go_aggiungi_orari ==
    # La funzione si occupa di aprire la VistaAggiungiOrari.
    def go_aggiungi_orari(self):
        self.aggiungi_orari = VistaAggiungiOrari(self.tipo)
        self.aggiungi_orari.show()
        self.close()

    def go_elimina(self, i):
        conferma = QMessageBox.question(self, "Attenzione", "Sei sicuro di voler eliminare questo orario?",
                                        QMessageBox.No, QMessageBox.Yes)
        if conferma == QMessageBox.Yes:
            self.controller.rimuovi_prenotazione_by_index(i-1)
            self.controller.save_data()
            self.refresh()
        else:
            return

    def refresh(self):
        self.go_lista = VistaListaPrenotazioni(self.tipo)
        self.go_lista.show()
        self.close()

    def on_selection_elimina(self, selected):
        self.go_elimina(self.button_group_elimina.id(selected))
