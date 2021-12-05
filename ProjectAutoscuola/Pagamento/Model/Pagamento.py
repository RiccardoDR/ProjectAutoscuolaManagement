import random


class Pagamento:  # Gestisce i dati e le operazioni relative al pagamento.
    def __init__(self, prezzo, descrizione, cliente):
        self.id = str(random.randint(10000, 99999))
        self.prezzo = prezzo
        self.descrizione = descrizione
        self.cliente = cliente

    def get_id(self):
        return self.id

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_descrizione(self):
        return self.descrizione

    def set_descrizione(self, descrizione):
        self.descrizione = descrizione

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente
