import os
import pickle
from unittest import TestCase

from ProgettoAutoscuola.ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti
from ProgettoAutoscuola.Dipendente.Model.Dipendente import Dipendente


class TestControllerListaDipendenti(TestCase):

    def test_add_dipendente(self):
        self.controller = ControllerListaDipendenti()
        self.dipendente = Dipendente("test", "test", "234", "13/05/1999", "pescara", "ciao@ciao.com", "23435", "segretario", "indeterminato", "maschio")
        self.controller.add_dipendente(self.dipendente)

    def test_elimina_dipendente_by_index(self):
        self.test_add_dipendente()
        if os.path.isfile('Data/lista_dipendenti.pickle'):
            with open('Data/lista_dipendenti.pickle', 'r') as f:
                self.lista_dipendenti = pickle.load(f)
                a = self.lista_dipendenti.index(self.dipendente)
                self.assertFalse(self.controller.rimuovi_dipendente_by_index(10000))
                self.assertTrue(self.controller.rimuovi_dipendente_by_index(a))

    def test_get_lista_dipendenti(self):
        self.test_add_dipendente()
        self.assertNotEqual(self.controller.get_lista_dipendenti(), [])
