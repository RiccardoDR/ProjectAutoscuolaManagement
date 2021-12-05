import shutil

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, \
    QFileDialog, QLabel, QButtonGroup

from ProgettoAutoscuola.Home.View import VistaHomeSegretario
from ProgettoAutoscuola.ListaDocumenti.Controller.ControllerListaDocumenti import ControllerListaDocumenti
from ProgettoAutoscuola.ListaDocumenti.View.VistaDocumento import VistaDocumento


class VistaListaDocumenti(QWidget):  # Apre la vista che visualizza la lista dei documenti.
    def __init__(self, parent=None):
        super(VistaListaDocumenti, self). __init__(parent)

        self.controller = ControllerListaDocumenti()
        self.lista_documenti = self.controller.get_lista_documenti()

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
        self.setWindowTitle("Lista Documenti")
        self.resize(1000, 600)
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
        self.table.setColumnCount(3)
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("Apri"))
        self.table.setItem(0, 1, QTableWidgetItem("Nome"))
        self.table.setItem(0, 2, QTableWidgetItem("Elimina"))

        self.button_group_apri = QButtonGroup()
        self.button_group_elimina = QButtonGroup()
        self.apri_icon = QIcon("Image/Visualizza.png")
        self.cancella_icon = QIcon("Image/delete.png")
        self.button_group_apri.buttonClicked.connect(self.on_selection_apri)
        self.button_group_elimina.buttonClicked.connect(self.on_selection_elimina)

        self.set_data()  # Inserisce nella tabella i dati contenuti nella lista_documenti.

        # Impostazioni grafiche della tabella.
        self.table.setGeometry(70, 50, 850, 400)
        self.table.setColumnWidth(0, 75)
        self.table.setColumnWidth(1, 700)
        self.table.setColumnWidth(2, 75)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().hide()
        self.table.horizontalScrollBar().setDisabled(True)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().hide()
        self.table.setSelectionMode(self.table.NoSelection)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)

        # Inserimento e impostazioni grafiche del bottone che consente di caricare un nuovo documento
        # nel sistema.
        self.button_upload_document = QPushButton(self)
        self.button_upload_document.setText("Carica")
        self.font_button = QFont("Times", 11)
        self.button_upload_document.setFont(self.font_button)
        self.button_upload_document.setGeometry(800, 500, 120, 50)
        self.button_upload_document.setStyleSheet(self.stylesheet)
        self.button_upload_document.clicked.connect(self.upload_document)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(80, 80))
        self.button_back.setGeometry(70, 490, 80, 80)
        self.button_back.clicked.connect(self.go_back)

    # == set_data ==
    # La funzione si occupa di salvare le informazioni relative al documento e contenute nel file
    # 'lista_documenti.json' nella tabella della VistaListaDocumenti.
    def set_data(self):
        i = 1
        n_righe = len(self.lista_documenti)
        self.table.setRowCount(n_righe+1)
        for documento in self.lista_documenti:
            apri = QPushButton()
            apri.setIcon(self.apri_icon)
            apri.setIconSize(QSize(25, 25))
            self.button_group_apri.addButton(apri, i)
            self.table.setCellWidget(i, 0, apri)

            self.table.setItem(i, 1, QTableWidgetItem(documento))

            delete = QPushButton()
            delete.setIcon(self.cancella_icon)
            delete.setIconSize(QSize(35, 35))
            self.button_group_elimina.addButton(delete, i)
            self.table.setCellWidget(i, 2, delete)
            i += 1

    # == open_document ==
    # La funzione, dopo che è stato selezionato un documento dalla lista,
    # apre la VistaDocumento.
    def open_document(self, i):
        documento = self.lista_documenti[i-1]
        self.vista_documento = VistaDocumento(documento)
        self.vista_documento.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_documenti = VistaHomeSegretario.VistaHomeSegretario()
        self.go_lista_documenti.show()
        self.close()

    # == upload_document ==
    # La funzione permette di caricare nel sistema un file .pdf scelto dai file
    # contenuti nel computer del dipendente.
    def upload_document(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', '/home', 'Images(*.pdf)')
        if filename[0]:
            f = open(filename[0], 'r')
            src = f.name
            des = 'ListaDocumenti/Documents/'
            shutil.copy2(src, des)
            self.refresh()
        else:
            return

    # == remove_document ==
    # La funzione, dopo aver inviato un messaggio di conferma all'utente, effettua
    # l'eliminazione del documento dalla lista. La finestra viene poi refreshata per aggiornare
    # la lista.
    def remove_document(self, i):
        conferma = QMessageBox.question(self, "Attenzione", "Sei sicuro di voler eliminare questo documento?",
                                        QMessageBox.No, QMessageBox.Yes)
        if conferma == QMessageBox.Yes:
            documento = self.lista_documenti[i-1]
            self.controller.rimuovi_documento(documento)
            self.refresh()
        else:
            return

    # == refresh ==
    # La funzione si occupa di riaprire la VistaListaDocumenti per aggiornarla dopo
    # che sono state effettuate modifiche.
    def refresh(self):
        self.go_vista_documenti = VistaListaDocumenti()
        self.go_vista_documenti.show()
        self.close()

    def on_selection_apri(self, selected):
        self.open_document(self.button_group_apri.id(selected))

    def on_selection_elimina(self, selected):
        self.remove_document(self.button_group_elimina.id(selected))
