import os
import pickle
from unittest import TestCase

from ProgettoAutoscuola.ListaVisiteMediche.Controller.ControllerListaVisiteMediche import ControllerListaVisiteMediche
from ProgettoAutoscuola.Model.VisitaMedica import VisitaMedica


class TestControllerListaVisiteMediche(TestCase):

    def test_aggiungi_visita(self):
        self.controller = ControllerListaVisiteMediche()
        self.visita = VisitaMedica("giuseppe", "30/07/2021")
        self.controller.aggiungi_visita(self.visita)

    def test_disdici_visita(self):
        self.test_aggiungi_visita()
        if os.path.isfile('Data/lista_visite.pickle'):
            with open('Data/lista_visite.pickle', 'r') as f:
                self.lista_visite = pickle.load(f)
                self.visita_da_eliminare = self.visita.get_cliente() + self.visita.get_data()
                self.assertFalse(self.controller.disdici_visita("aaaaa"))
                self.assertTrue(self.controller.disdici_visita(self.visita_da_eliminare))

    def test_get_lista_visite(self):
        self.test_aggiungi_visita()
        self.assertNotEqual(self.controller.get_lista_visite(), [])
