import random


class Prenotazione:  # Gestisce i dati e le operazioni relative alla prenotazione.
    def __init__(self, tipo, data):
        self.id = str(random.randint(10000, 99999))
        self.tipo = tipo
        self.data = data

    def get_id(self):
        return self.id

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data