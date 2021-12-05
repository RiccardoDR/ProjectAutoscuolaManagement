from os import listdir


class ListaDocumenti:  # Gestisce i dati e le operazioni relative alla lista documenti
    def __init__(self):
        self.lista_documenti = []
        self.lista_documenti = listdir("ListaDocumenti/Documents")
        self.lista_documenti.sort()

    def get_lista_documenti(self):
        return self.lista_documenti

    def get_documento_by_index(self, index):
        return self.lista_documenti[index - 1]
