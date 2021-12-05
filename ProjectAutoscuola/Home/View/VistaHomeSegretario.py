from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QAction, QToolButton, QWidget, QPushButton, QMessageBox

from ProgettoAutoscuola.Home.View import VistaAccesso, VistaHomeIstruttore
from ProgettoAutoscuola.ListaClienti.View.VistaListaClienti import VistaListaClienti
from ProgettoAutoscuola.ListaDipendenti.View.VistaListaDipendenti import VistaListaDipendenti
from ProgettoAutoscuola.ListaDocumenti.View.VistaListaDocumenti import VistaListaDocumenti
from ProgettoAutoscuola.ListaPagamenti.View.VistaListaPagamenti import VistaListaPagamenti
from ProgettoAutoscuola.RinnovoPatente.View.VistaRinnovoPatente import VistaRinnovoPatente


class VistaHomeSegretario(QWidget):  # Apre e visualizza la vista home con le funzioni consentite al segretario.
    def __init__(self, parent=None):
        super(VistaHomeSegretario, self).__init__(parent)

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Home Segretario")
        self.resize(800, 600)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Il seguente blocco crea le azioni che saranno svolte dai bottoni, i bottoni
        # che saranno presenti sulla schermata e i collegamenti tra i due.
        self.action_home = QAction()
        self.action_clienti = QAction()
        self.action_dipendenti = QAction()
        self.action_prenotazioni = QAction()
        self.action_rinnovo = QAction()
        self.action_pagamenti = QAction()
        self.action_documenti = QAction()

        self.create_button1('Image/clienti.png', 'Clienti', 110, self.action_clienti)
        self.create_button1('Image/dipendenti.png', 'Dipendenti', 310, self.action_dipendenti)
        self.create_button1('Image/prenotazione.png', 'Prenotazioni', 510, self.action_prenotazioni)

        self.create_button2('Image/rinnovo.png', 'Rinnovo', 110, self.action_rinnovo)
        self.create_button2('Image/pagamenti.png', 'Pagamenti', 310, self.action_pagamenti)
        self.create_button2('Image/documenti.png', 'Documenti', 510, self.action_documenti)

        self.action_clienti.triggered.connect(self.go_clienti)
        self.action_dipendenti.triggered.connect(self.go_dipendenti)
        self.action_prenotazioni.triggered.connect(self.go_prenotazioni)
        self.action_rinnovo.triggered.connect(self.go_rinnovo)
        self.action_pagamenti.triggered.connect(self.go_pagamenti)
        self.action_documenti.triggered.connect(self.go_documenti)

        self.button_logout = QPushButton(self)
        self.button_logout.setIcon(QIcon('Image/logout.png'))
        self.button_logout.setIconSize(QSize(90, 90))
        self.button_logout.setGeometry(80, 480, 90, 90)
        self.button_logout.clicked.connect(self.logout)

    # == create_button ==
    # La funzione crea i bottoni che saranno presenti sulla schermata nella prima colonna prendendo per input
    # il path dell immagine che rappresenterà il bottone, il suo nome, la posizione che avrà nella
    # schermata e quale azione dovrà compiere una volta premuto.
    # La funzione si occupa dei bottoni anche dal punto di vista grafico.
    def create_button1(self, path_img, nome, posizione, action):
        button = QToolButton(self)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        font_button = QFont("Times", 11)
        button.setFont(font_button)
        button.setGeometry(posizione, 200, 180, 80)
        action.setIcon(QIcon(path_img))
        action.setText(nome)
        button.setIconSize(QSize(50, 50))
        button.setDefaultAction(action)
        button.setStyleSheet('QToolButton{background-color: black; border: 1px solid #ababab; border-radius: 10px;}'
                             'QToolButton::Hover { background-color: white }')

    # == create_button2 ==
    # La funzione crea i bottoni che saranno presenti sulla schermata nella seconda colonna prendendo per input
    # il path dell immagine che rappresenterà il bottone, il suo nome, la posizione che avrà nella
    # schermata e quale azione dovrà compiere una volta premuto.
    # La funzione si occupa dei bottoni anche dal punto di vista grafico.
    def create_button2(self, path_img, nome, posizione, action):
        button = QToolButton(self)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        font_button = QFont("Times", 11)
        button.setFont(font_button)
        button.setGeometry(posizione, 300, 180, 80)
        action.setIcon(QIcon(path_img))
        action.setText(nome)
        button.setIconSize(QSize(50, 50))
        button.setDefaultAction(action)
        button.setStyleSheet('QToolButton{background-color: white; border: 1px solid #ababab; border-radius: 10px;}'
                             'QToolButton::Hover{background-color: #00afff}')

    # == go_clienti ==
    # La funzione si occupa di aprire la VistaListaClienti.
    def go_clienti(self):
        self.vista_clienti = VistaListaClienti()
        self.vista_clienti.show()
        self.close()

    # == go_dipendenti ==
    # La funzione si occupa di aprire la VistaListaDipendenti.
    def go_dipendenti(self):
        self.vista_dipendenti = VistaListaDipendenti()
        self.vista_dipendenti.show()
        self.close()

    # == go_prenotazioni ==
    # La funzione si occupa di aprire la vista che permette al segretario di gestire
    # le prenotazioni. La vista è la stessa dell'istruttore: la VistaHomeIstruttore.
    def go_prenotazioni(self):
        self.vista_prenotazioni = VistaHomeIstruttore.VistaHomeIstruttore("Segretario")
        self.vista_prenotazioni.show()
        self.close()

    # == go_rinnovo ==
    # La funzione si occupa di aprire la VistaRinnovoPatente.
    def go_rinnovo(self):
        self.rinnovo = VistaRinnovoPatente()
        self.rinnovo.show()
        self.close()

    # == go_pagamenti ==
    # La funzione si occupa di aprire la VistaListaPagamenti.
    def go_pagamenti(self):
        self.vista_pagamento = VistaListaPagamenti()
        self.vista_pagamento.show()
        self.close()

    # == go_documenti ==
    # La funzione si occupa di aprire la VistaListaDocumenti.
    def go_documenti(self):
        self.vista_documenti = VistaListaDocumenti()
        self.vista_documenti.show()
        self.close()

    def logout(self):
        QMessageBox.information(self, "Arrivederci", "Sessione terminata")
        self.vista_accesso = VistaAccesso.VistaAccesso()
        self.vista_accesso.show()
        self.close()
