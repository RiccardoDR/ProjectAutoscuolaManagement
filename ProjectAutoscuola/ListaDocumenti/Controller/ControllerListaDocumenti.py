import os

from ProgettoAutoscuola.ListaDocumenti.Model.ListaDocumenti import ListaDocumenti


class ControllerListaDocumenti: # Gestisce e attua i comandi relativi alla lista dei documenti.
    def __init__(self):
        self.model = ListaDocumenti()

    def get_lista_documenti(self):
        return self.model.get_lista_documenti()

    def get_documento_by_index(self, index):
        return self.model.get_documento_by_index(index)

    def rimuovi_documento(self, doc):
        os.remove('ListaDocumenti/Documents/' + doc)
