from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QPushButton, QComboBox, QMessageBox

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.Prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazione
from ProgettoAutoscuola.Home.View import VistaHomeIstruttore
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti
from ProgettoAutoscuola.ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni


class VistaPrenotazione(QWidget):  # Apre la vista che permette di effettuare una prenotazione.
    def __init__(self, tipo):
        super(VistaPrenotazione, self).__init__()
        self.tipo = tipo

        self.controller = ControllerListaPrenotazioni()
        self.controller.set_data()
        self.lista_prenotazioni = self.controller.get_lista_prenotazioni()

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
        self.setWindowTitle("Nuova Prenotazione")
        self.resize(1000, 550)
        self.setFixedSize(self.size())

        # Inserimento e impostazioni grafiche dell'immagine dello sfondo della finestra.
        self.imagePath = "Image/foto.png"
        self.image = QImage(self.imagePath)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)
        self.label.resize(self.size())

        # Inserimento e impostazioni grafiche dell'etichetta 'Nuova Prenotazione'.
        self.label = QLabel(self)
        self.font = QFont("Arial", 18, QFont.Bold)
        self.label.setText("Nuova Prenotazione")
        self.label.setFont(self.font)
        self.label.setGeometry(50, 55, 350, 40)

        # Inserimento e impostazioni grafiche del frame nella finestra.
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: white; border: 1px solid; border-radius: 10px;')
        self.frame.setGeometry(50, 100, 900, 280)

        # Usa la funzione 'create_label1' per creare due etichette.
        self.create_label1("Cliente", 150)
        self.create_label1("Tipo", 250)

        # Inserimento e impostazioni grafiche dell'etichetta 'Data'.
        self.label_edit = QLabel(self)
        self.label_edit.setText("Data")
        self.label_edit.setGeometry(500, 150, 100, 20)
        self.font_label1 = QFont("Times", 9)
        self.label_edit.setFont(self.font_label1)

        # Inserimento e impostazioni grafiche del menù a tendina contenente la lista dei cliente
        # che non hanno effettuato alcuna prenotazione.
        self.edit_cliente = QComboBox(self)
        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if controller_cliente.get_esame_teorico() == "None" or controller_cliente.get_esame_pratico() == "None":
                if controller_cliente.get_id() != "None":
                    self.edit_cliente.addItem(controller_cliente.get_nome() + " " + controller_cliente.get_cognome())
        self.edit_cliente.setGeometry(250, 150, 200, 30)

        # Inserimento e impostazioni grafiche del menù a tendina contenente la lista dei servizi
        # per cui è possibile effettuare un pagamento.
        self.edit_tipo = QComboBox(self)
        self.edit_tipo.addItem("Lezione", self.get_data("Lezione"))
        self.edit_tipo.addItem("Esame teorico", self.get_data("Esame teorico"))
        self.edit_tipo.addItem("Lezione guida", self.get_data("Lezione guida"))
        self.edit_tipo.addItem("Esame pratico", self.get_data("Esame pratico"))
        self.edit_tipo.setGeometry(250, 250, 200, 30)

        # Inserimento e impostazioni grafiche del menù a tendina contenente le dati per cui
        # è possibile prenotarsi.
        self.edit_data = QComboBox(self)
        self.edit_data.setGeometry(600, 150, 200, 30)

        # In base al servizio scelto vengono cambiate le dati per cui è possibile prenotarsi.
        self.edit_tipo.currentIndexChanged.connect(self.update_data)
        self.update_data(self.edit_tipo.currentIndex())

        # Inserimento e impostazioni grafiche del bottone per tornare alla vista precedente.
        self.button_back = QPushButton(self)
        self.button_back.setIcon(QIcon('Image/back.png'))
        self.button_back.setIconSize(QSize(90, 90))
        self.button_back.setGeometry(50, 420, 90, 90)
        self.button_back.clicked.connect(self.go_back)

        # Inserimento e impostazioni grafiche del bottone che permette di confermare la prenotazione.
        self.button_new_prenotazione = QPushButton(self)
        self.button_new_prenotazione.setText("Salva")
        self.font_button = QFont("Arial", 11)
        self.button_new_prenotazione.setFont(self.font_button)
        self.button_new_prenotazione.setGeometry(800, 440, 120, 50)
        self.button_new_prenotazione.setStyleSheet(self.stylesheet)
        self.button_new_prenotazione.clicked.connect(self.salva_prenotazione)

    # == create_label1 ==
    # La funzione crea un etichetta con nome inserito in input alla funzione e posizione nella finestra
    # presa anch'essa in input. La funzione gestisce anche le impostazioni grafiche dell'etichetta.
    def create_label1(self, nome, posizione):
        label_edit = QLabel(self)
        label_edit.setText(nome)
        label_edit.setGeometry(80, posizione, 100, 20)
        font_label = QFont("Arial", 9)
        label_edit.setFont(font_label)

    # == get_data ==
    # La funzione aggiunge alla lista 'lezioni' gli orari per cui è possibile prenotarsi ad un determinato
    # servizio. La lista 'lezioni' verrà poi ritornata dalla funzione.
    def get_data(self, nome):
        lezioni = []
        count = 0
        for prenotazione in self.lista_prenotazioni:
            controller_prenotazione = ControllerPrenotazione(prenotazione)
            count += 1
            if controller_prenotazione.get_tipo() == nome:
                lezioni.append(controller_prenotazione.get_data())
        return lezioni

    # == update_data ==
    # La funzione aggiunge al menù a tendina relativo alle date le date del servizio selezionato.
    def update_data(self, index):
        self.edit_data.clear()
        date = self.edit_tipo.itemData(index)
        if date:
            self.edit_data.addItems(date)

    # == salva_prenotazione ==
    # La funzione permette di salvare la prenotazione scelta. Prima si controlla che il cliente sia presente a sistema e se
    # abbia effettuato il pagamento iniziale: nel caso in cui non fosse stato effettuato viene inviato
    # un messaggio di errore. Vengono poi effettuati ulteriori controller per verificare che
    # il client abbia pagato i servizi per cui sta effettuando le prenotazioni. Inoltre, se il cliente ha già effettuato
    # una prenotazione viene inviato un messaggio all'utente chiedendogli se desidera cancellare la prenotazione
    # effettuare sostituendola con una nuova. Infine le modifiche vengono salvate e l'utente è riportato
    # alla VistaHomeIstruttore.
    def salva_prenotazione(self):
        if self.edit_data.currentText() == '' or self.edit_tipo.currentText() == '':
            QMessageBox.critical(self, "Attenzione", "Inserisci tutti i dati")

        for cliente in self.lista_clienti:
            controller_cliente = ControllerCliente(cliente)

            if self.edit_cliente.currentText() == controller_cliente.get_nome() + " " + controller_cliente.get_cognome():
                if self.edit_tipo.currentIndex() == 0:
                    if controller_cliente.get_esame_teorico() == "Effettuato":
                        QMessageBox.critical(self, "Attenzione", "Il cliente ha già svolto l'esame teorico")
                        return

                    if controller_cliente.get_pagamento_iniziale() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha pagato l'iscrizione")
                        return

                    if controller_cliente.get_visita_medica() == "None":
                        QMessageBox.critical(self, "Errore", "Il cliente non ha fatto la visita medica")
                        return

                if self.edit_tipo.currentIndex() == 1:
                    if controller_cliente.get_esame_teorico() == "Effettuato":
                        QMessageBox.critical(self, "Attenzione", "Il cliente ha già svolto l'esame teorico")
                        return

                    if controller_cliente.get_pagamento_iniziale() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha pagato l'iscrizione")
                        return

                    if controller_cliente.get_visita_medica() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha fatto la visita medica")
                        return

                    if controller_cliente.get_pagamento_esame_teorico() == "None":
                        QMessageBox.critical(self, "Attenzione",
                                             "Il cliente non ha pagato l'iscrizione per l'esame teorico")
                        return

                if self.edit_tipo.currentIndex() == 2:
                    if controller_cliente.get_esame_pratico() == "Effettuato":
                        QMessageBox.critical(self, "Attenzione", "Il cliente ha già svolto l'esame pratico")
                        return

                    if controller_cliente.get_pagamento_iniziale() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha pagato l'iscrizione")
                        return

                    if controller_cliente.get_visita_medica() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha fatto la visita medica")
                        return

                    if controller_cliente.get_pagamento_esame_teorico() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha ancora fatto l'esame teorico")
                        return

                    if controller_cliente.get_pagamento_lezioni_guida() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha ancora pagato le lezioni di guida")
                        return

                if self.edit_tipo.currentIndex() == 3:
                    if controller_cliente.get_esame_pratico() == "Effettuato":
                        QMessageBox.critical(self, "Attenzione", "Il cliente ha già svolto l'esame pratico")
                        return

                    if controller_cliente.get_pagamento_iniziale() == "None":
                        QMessageBox.critical(self, "Attenzione", "Il cliente non ha pagato l'iscrizione")
                        return

                    if controller_cliente.get_visita_medica() == "None":
                        QMessageBox.critical(self, "Errore", "Il cliente non ha fatto la visita medica")
                        return

                    if controller_cliente.get_pagamento_esame_teorico() == "None":
                        QMessageBox.critical(self, "Errore", "Il cliente non ha ancora fatto l'esame teorico")
                        return

                    if controller_cliente.get_pagamento_lezioni_guida() == "None":
                        QMessageBox.critical(self, "Errore", "Il cliente non ha ancora pagato le lezioni di guida")
                        return

                    if controller_cliente.get_pagamento_esame_pratico() == "None":
                        QMessageBox.critical(self, "Errore",
                                             "Il cliente non ha pagato l'iscrizione per l'esame pratico")
                        return

                if controller_cliente.get_prenotazione() == "None":
                    controller_cliente.set_prenotazione(
                        self.edit_data.currentText() + " - " + self.edit_tipo.currentText())
                else:
                    conferma = QMessageBox.question(self, "Attenzione", "Il cliente si è già prenotato,"
                                                                        "vuoi annullare la data precedente?",
                                                    QMessageBox.Yes, QMessageBox.No)
                    if conferma == QMessageBox.Yes:
                        controller_cliente.set_prenotazione(self.edit_data.currentText() + " - "
                                                            + self.edit_tipo.currentText())
                    else:
                        return
        self.controller_clienti.save_data()
        self.go_lista_prenotazioni = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_lista_prenotazioni.show()
        self.close()

    # == go_back ==
    # La funzione si occupa di aprire la finestra precedente.
    def go_back(self):
        self.go_lista_prenotazioni = VistaHomeIstruttore.VistaHomeIstruttore(self.tipo)
        self.go_lista_prenotazioni.show()
        self.close()
