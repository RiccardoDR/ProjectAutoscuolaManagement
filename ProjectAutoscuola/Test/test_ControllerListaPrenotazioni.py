import pickle
from unittest import TestCase
import os

from ProgettoAutoscuola.ListaPrenotazioni.Controller.ControllerListaPrenotazioni import ControllerListaPrenotazioni
from ProgettoAutoscuola.Prenotazione.Model.Prenotazione import Prenotazione


class TestControllerListaPrenotazioni(TestCase):

    def test_aggiungi_prenotazione(self):
        self.controller = ControllerListaPrenotazioni()
        self.prenotazione = Prenotazione("lezione teorica", "27/07/2021")
        self.controller.aggiungi_prenotazione(self.prenotazione)

    def test_rimuovi_prenotazione_by_id(self):
        self.test_aggiungi_prenotazione()
        if os.path.isfile('Data/lista_prenotazioni.pickle'):
            with open('Data/lista_prenotazioni.pickle', 'r') as f:
                self.lista_prenotazioni = pickle.load(f)
                a = self.lista_prenotazioni.index(self.prenotazione)
                self.assertTrue(self.controller.rimuovi_prenotazione_by_index(a))
                self.assertFalse(self.controller.rimuovi_prenotazione_by_index(10000))

    def test_get_lista_prenotazioni(self):
        self.test_aggiungi_prenotazione()
        self.assertNotEqual(self.controller.get_lista_prenotazioni(), [])