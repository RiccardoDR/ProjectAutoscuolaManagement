from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QLabel, QFrame, QComboBox

from ProgettoAutoscuola.VisitaMedica.Controller.ControllerVisitaMedica import ControllerVisitaMedica
from ProgettoAutoscuola.Home.View import VistaHomeMedico
from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche


class VistaDisdiciVisitaMedica(QWidget):  # Apre la vista che permette di disdire una visita col medico dell'autoscuola.
    def __init__(self, parent=None):
        super(VistaDisdiciVisitaMedica, self).__init__(parent)

        self.controller = ControllerListaVisiteMediche()
        self.controller.set_data()
        self.lista_visite = self.controller.get_lista_visite()

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
        self.setWindowTitle("Disdici Visita")
        self.resize(700, 500)
        self.setFixedSize(self.size())

        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Disdici Visita'.
        self.label_titolo = QLabel(self)
        self.font_titolo = QFont("Arial", 18, QFont.Bold)
        self.label_titolo.setText("Disdici Visita")
        self.label_titolo.setFont(self.font_titolo)
        self.label_titolo.setGeometry(50, 55, 300, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 600, 250)

        # Inserimento e impostazioni grafiche dell'etichetta 'Selezionare la visita'.
        self.label_id = QLabel(self)
        self.font_id = QFont("Times", 9)
        self.label_id.setFont(self.font_id)
        self.label_id.setText("Selezionare la visita")
        self.label_id.setGeometry(60, 190, 160, 30)

        # Inserimento e impostazioni grafiche del menù a tendina contenente le visite contenute nella
        # lista_visite. Inoltre la visita selezionata nel menù viene salvata nella variabile
        # 'visita_da_eliminare'.
        self.selezione_visita = QComboBox(self)
        for visita in self.lista_visite:
            controller_visita = ControllerVisitaMedica(visita)

            if controller_visita.get_esito() == "None":
                self.selezione_visita.addItem(controller_visita.get_cliente() + " - " + controller_visita.get_data())
        nome = self.selezione_visita.currentText().split("-")

        for visita in self.lista_visite:
            controller_visita = ControllerVisitaMedica(visita)

            if nome[0].strip() == controller_visita.get_cliente() and controller_visita.get_esito() == "None":
                self.visita_da_eliminare = visita
        self.selezione_visita.setGeometry(250, 190, 300, 30)

        # Inserimento e impostazioni grafiche del bottone per confermare la rimozione della visita.
        self.button_rimuovi = QPushButton(self)
        self.button_rimuovi.setText("Rimuovi")
        self.font_button = QFont("Times", 11)
        self.button_rimuovi.setFont(self.font_button)
        self.button_rimuovi.setGeometry(525, 410, 120, 50)
        self.button_rimuovi.setStyleSheet(self.stylesheet)
        self.button_rimuovi.clicked.connect(self.disdici_visita)

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(60, 60))
        self.button_back.setGeometry(50, 390, 90, 90)
        self.button_back.clicked.connect(self.go_back)

    # == disdici_visita ==
    # La funzione seguente per prima cosa chiede all'utente se vuole confermare l'eliminazione corrente e,
    # in caso di risposta affermativa, cancella la visita selezionata grazie all'id salvato nella variabile
    # 'visita_da_eliminare'.
    def disdici_visita(self):
        conferma = QMessageBox.question(self, "Conferma", "Sei sicuro di voler disdire?", QMessageBox.Yes,
                                        QMessageBox.No)
        if conferma == QMessageBox.Yes:
            self.controller.disdici_visita(self.visita_da_eliminare)
            self.controller.save_data()
            self.home = VistaHomeMedico.VistaHomeMedico()
            self.home.show()
            self.close()
        else:
            return

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_home = VistaHomeMedico.VistaHomeMedico()
        self.go_home.show()
        self.close()