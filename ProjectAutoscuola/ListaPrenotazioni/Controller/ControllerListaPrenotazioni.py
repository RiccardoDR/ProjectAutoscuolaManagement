from ProgettoAutoscuola.ListaPrenotazioni.Model.ListaPrenotazioni import ListaPrenotazioni


class ControllerListaPrenotazioni:  # Gestisce e attua i comandi relativi alla lista delle prenotazioni.
    def __init__(self):
        self.model = ListaPrenotazioni()

    def set_data(self):
        self.model.set_data()

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def disdici_prenotazione(self, prenotazione):
        self.model.rimuovi_prenotazione_by_id(prenotazione)

    def rimuovi_prenotazione_by_index(self, i):
        self.model.rimuovi_prenotazione_by_id(i)

    def save_data(self):
        self.model.save_data()

