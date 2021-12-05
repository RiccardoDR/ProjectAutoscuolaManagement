from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QLabel, \
    QButtonGroup

from ProgettoAutoscuola.Dipendente.Controller.ControllerDipendente import ControllerDipendente
from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti
from ProgettoAutoscuola.Dipendente.View.VistaDipendente import VistaDipendente
from ProgettoAutoscuola.ListaDipendenti.View.VistaNuovoDipendente import VistaNuovoDipendente


class VistaListaDipendenti(QWidget):  # Apre la vista che visualizza la lista dei dipendenti.
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

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
        self.setWindowTitle("Lista Dipendenti")
        self.resize(1250, 700)
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
        self.table.setColumnCount(6)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("Apri"))
        self.table.setItem(0, 1, QTableWidgetItem("ID"))
        self.table.setItem(0, 2, QTableWidgetItem("Nome"))
        self.table.setItem(0, 3, QTableWidgetItem("Cognome"))
        self.table.setItem(0, 4, QTableWidgetItem("Mansione"))
        self.table.setItem(0, 5, QTableWidgetItem("Elimina"))

        self.button_group_apri = QButtonGroup()
        self.button_group_elimina = QButtonGroup()
        self.apri_icon = QIcon("Image/apri_icon.png")
        self.cancella_icon = QIcon("Image/delete.png")
        self.button_group_apri.buttonClicked.connect(self.on_selection_apri)
        self.button_group_elimina.buttonClicked.connect(self.on_selection_elimina)

        self.set_data()  # Inserisce nella tabella i dati contenuti nella lista_dipendenti.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(25, 30, 1200, 550)
        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 300)
        self.table.setColumnWidth(3, 300)
        self.table.setColumnWidth(4, 300)
        self.table.setColumnWidth(5, 90)
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
        self.button_back.setGeometry(70, 600, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone per inserire un nuovo dipendente nella lista.
        self.button_new_dipendente = QPushButton(self)
        self.button_new_dipendente.setText("Nuovo Dipendente")
        self.font_button = QFont("Times", 11)
        self.button_new_dipendente.setFont(self.font_button)
        self.button_new_dipendente.setGeometry(1000, 620, 190, 50)
        self.button_new_dipendente.setStyleSheet(self.stylesheet)
        self.button_new_dipendente.clicked.connect(self.go_new_dipendente)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative al dipendente e contenute nel file
    # 'lista_dipendenti.pickle' nella tabella della VistaListaDipendenti.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_dipendenti)
        self.table.setRowCount(n_righe + 1)
        for dipendente in self.lista_dipendenti:
            controller_dipendente = ControllerDipendente(dipendente)

            apri = QPushButton()
            apri.setIcon(self.apri_icon)
            apri.setIconSize(QSize(30, 30))
            self.button_group_apri.addButton(apri, i)
            self.table.setCellWidget(i, 0, apri)

            self.table.setItem(i, 1, QTableWidgetItem(controller_dipendente.get_id()))
            self.table.setItem(i, 2, QTableWidgetItem(controller_dipendente.get_nome()))
            self.table.setItem(i, 3, QTableWidgetItem(controller_dipendente.get_cognome()))
            self.table.setItem(i, 4, QTableWidgetItem(controller_dipendente.get_mansione()))

            delete = QPushButton()
            delete.setIcon(self.cancella_icon)
            delete.setIconSize(QSize(35, 35))
            self.button_group_elimina.addButton(delete, i)
            self.table.setCellWidget(i, 5, delete)
            i += 1

    # == go_new_dipendente ==
    # La funzione si occupa di aprire la VistaNuovoDipendente.
    def go_new_dipendente(self):
        self.vista_nuovo_dipendente = VistaNuovoDipendente()
        self.vista_nuovo_dipendente.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeSegretario.VistaHomeSegretario()
        self.go_home.show()
        self.close()

    # == go_apri ==
    # La funzione si occupa di aprire la VistaCliente corrispondente al cliente scelto.
    def go_apri(self, i):
        dipendente = self.lista_dipendenti[i - 1]
        self.go_dipendente = VistaDipendente(dipendente, False)
        self.go_dipendente.show()
        self.close()

    # == go_elimina ==
    # La funzione, dopo aver chiesto conferma all'utente, cancella le informazioni relative al
    # cliente scelto.
    def go_elimina(self, i):
        conferma = QMessageBox.question(self, "Attenzione", "Sei sicuro di voler eliminare questo dipendente?",
                                        QMessageBox.No, QMessageBox.Yes)
        if conferma == QMessageBox.Yes:
            self.controller.rimuovi_dipendente_by_index(i - 1)
            self.controller.save_data()
            self.refresh()
        else:
            return

    def refresh(self):
        self.go_lista = VistaListaDipendenti()
        self.go_lista.show()
        self.close()

    def on_selection_apri(self, selected):
        self.go_apri(self.button_group_apri.id(selected))

    def on_selection_elimina(self, selected):
        self.go_elimina(self.button_group_elimina.id(selected))
