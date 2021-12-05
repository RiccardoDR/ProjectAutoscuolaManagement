class ControllerPrenotazione:  # Gestisce e attua i comandi relativi alle prenotazioni.
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id(self):
        return self.model.get_id()

    def get_tipo(self):
        return self.model.get_tipo()

    def set_tipo(self, tipo):
        self.model.set_tipo(tipo)

    def get_data(self):
        return self.model.get_data()

    def set_data(self, data):
        self.model.set_data(data)
