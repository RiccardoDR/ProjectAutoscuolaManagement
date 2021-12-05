class ControllerPagamento:  # Gestisce e attua i comandi relativi al pagamento.
    def __init__(self, pagamento):
        self.model = pagamento

    def get_id(self):
        return self.model.get_id()

    def get_prezzo(self):
        return self.model.get_prezzo()

    def set_prezzo(self, prezzo):
        self.model.set_prezzo(prezzo)

    def get_descrizione(self):
        return self.model.get_descrizione()

    def set_descrizione(self, descrizione):
        self.model.set_descrizione(descrizione)

    def get_cliente(self):
        return self.model.get_cliente()

    def set_cliente(self, cliente):
        self.model.set_cliente(cliente)
