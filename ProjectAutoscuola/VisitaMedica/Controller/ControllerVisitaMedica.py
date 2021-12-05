class ControllerVisitaMedica:  # Gestisce e attua i comandi relativi alle visite mediche.
    def __init__(self, visita):
        self.model = visita

    def get_id(self):
        return self.model.get_id()

    def get_cliente(self):
        return self.model.get_cliente()

    def set_cliente(self, cliente):
        self.model.set_cliente(cliente)

    def get_descrizione(self):
        return self.model.get_descrizione()

    def set_descrizione(self, descrizione):
        self.model.set_descrizione(descrizione)

    def get_data(self):
        return self.model.get_data()

    def set_data(self, data):
        self.model.set_data(data)

    def get_esito(self):
        return self.model.get_esito()

    def set_esito(self, esito):
        self.model.set_esito(esito)
