from ProgettoAutoscuola.ListaVisiteMediche.Model.ListaVisiteMediche import ListaVisiteMediche


class ControllerListaVisiteMediche:  # Gestisce e attua i comandi relativi alla lista delle visite mediche.
    def __init__(self):
        self.model = ListaVisiteMediche()

    def set_data(self):
        self.model.set_data()

    def elimina_visite_by_cliente(self, i):
        self.model.elimina_visite_by_cliente(i)

    def aggiungi_visita(self, visita):
        self.model.aggiungi_visita(visita)

    def get_lista_visite(self):
        return self.model.get_lista_visite()

    def disdici_visita(self, visita):
        self.model.rimuovi_visita_by_id(visita)

    def save_data(self):
        self.model.save_data()
