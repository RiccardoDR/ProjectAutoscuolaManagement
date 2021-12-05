from ProgettoAutoscuola.ListaDipendenti.Model.ListaDipendenti import ListaDipendenti


class ControllerListaDipendenti:  # Gestisce e attua i comandi relativi alla lista dei dipendenti.
    def __init__(self):
        self.model = ListaDipendenti()

    def set_data(self):
        self.model.set_data()

    def add_dipendente(self, dipendente):
        self.model.add_dipendente(dipendente)

    def rimuovi_dipendente_by_index(self, i):
        self.model.rimuovi_dipendente_by_index(i)

    def get_lista_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def save_data(self):
        self.model.save_data()
