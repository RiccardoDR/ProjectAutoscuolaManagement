from ProgettoAutoscuola.ListaClienti.Model.ListaClienti import ListaClienti


class ControllerListaClienti:  # Gestisce e attua i comandi relativi alla lista dei clienti.
    def __init__(self):
        self.model = ListaClienti()

    def set_data(self):
        self.model.set_data()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def rimuovi_cliente_by_index(self, i):
        self.model.rimuovi_cliente_by_index(i)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def save_data(self):
        self.model.save_data()
