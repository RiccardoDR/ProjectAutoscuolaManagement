import random


class VisitaMedica:  # Gestisce i dati e le operazioni relative alla prenotazione della visita medica.
    def __init__(self, cliente, data):
        self.id = str(random.randint(10000, 99999))
        self.cliente = cliente
        self.descrizione = "None"
        self.data = data
        self.esito = "None"

    def get_id(self):
        return self.id

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_descrizione(self):
        return self.descrizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_esito(self):
        return self.esito

    def set_esito(self, esito):
        self.esito = esito
