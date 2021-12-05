# from PyPDF2 import PdfFileReader
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QTextEdit

from ProgettoAutoscuola.ListaDocumenti.Controller.ControllerListaDocumenti import ControllerListaDocumenti
from ProgettoAutoscuola.ListaDocumenti.View import VistaListaDocumenti
from ProgettoAutoscuola.ListaDocumenti.View.VistaStampa import VistaStampa


class VistaDocumento(QWidget):  # Apre la vista che visualizza il contenuto del documento.
    def __init__(self, documento):
        super(VistaDocumento, self).__init__()
        self.documento = documento

        self.controller = ControllerListaDocumenti()
        self.lista_documenti = self.controller.get_lista_documenti()

        self.stylesheet_button = """
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
        self.resize(900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle(documento)

        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.font = QFont("Times", 18)
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(10, 30, 880, 350)

        # Inserimento e impostazioni grafiche del testo del documento.
        self.file_pdf = "ListaDocumenti/Documents/" + documento
        self.textedit = QTextEdit(self)
        self.textedit.setReadOnly(True)
        self.textedit.setGeometry(10, 30, 880, 350)
        # self.pdf = PdfFileReader(self.file_pdf)
        self.page = self.pdf.getPage(0)
        self.page_content = self.page.extractText()
        self.textedit.setText(self.page_content)

        # Inserimento e impostazioni grafiche del bottone che permette di stampare il documento.
        self.button_print_document = QPushButton(self)
        self.button_print_document.setIcon(QIcon('Image/stampante'))
        self.button_print_document.setIconSize(QSize(90, 70))
        self.button_print_document.setGeometry(700, 400, 140, 70)
        self.button_print_document.clicked.connect(self.print_document)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 70))
        self.button_back.setGeometry(60, 410, 140, 70)
        self.button_back.clicked.connect(self.go_back)

    # == print_documento ==
    # La funzione si occupa di aprire la VistaStampa.
    def print_document(self):
        self.avanzamento_stampa = VistaStampa()
        self.avanzamento_stampa.show()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_documenti = VistaListaDocumenti.VistaListaDocumenti()
        self.go_lista_documenti.show()
        self.close()
