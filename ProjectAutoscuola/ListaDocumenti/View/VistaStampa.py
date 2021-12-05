from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QProgressBar, QMessageBox

from ProgettoAutoscuola.ListaDocumenti.Controller.ControllerListaDocumenti import ControllerListaDocumenti


class VistaStampa(QWidget):  # Apre la vista che consente di verificare lo stato di avanzamento della stampa.
    def __init__(self, parent=None):
        super(VistaStampa, self).__init__(parent)
        self.controller_documenti = ControllerListaDocumenti()
        self.lista_documenti = self.controller_documenti.get_lista_documenti()

        # Impostazioni grafiche generali della finestra del programma.
        self.setWindowTitle("Stampa in corso...")
        self.resize(300, 100)

        # Inserimento e impostazioni grafiche della barra per visualizzare lo stato di avanzamento.
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(40, 40, 220, 20)
        self.timer = QBasicTimer()

        self.step = 0
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(10, self)

    # == timerEvent ==
    # La funzione controlla che, quando la variabile 'step' arriva a 100 e quindi la stampa è completata,
    # viene fermato il timer e viene aperta una finestra che comunica l'avvenuta stampa
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.close()
            msg = QMessageBox()
            msg.setWindowTitle("stampa")
            msg.setText("Stampa avvenuta con successo")
            msg.exec()
            return

        self.step += 1
        self.progressBar.setValue(self.step)
