from ProgettoAutoscuola.ListaPagamenti.Model.ListePagamenti import ListaPagamenti


class ControllerListaPagamenti:  # Gestisce e attua i comandi relativi alla lista dei pagamenti.
    def __init__(self):
        self.model = ListaPagamenti()

    def set_data(self):
        self.model.set_data()

    def aggiungi_pagamento(self, pagamento):
        self.model.aggiungi_pagamento(pagamento)

    def elimina_pagamento_by_cliente(self, i):
        self.model.elimina_pagamenti_by_cliente(i)

    def get_lista_pagamenti(self):
        return self.model.get_lista_pagamenti()

    def save_data(self):
        self.model.save_data()
