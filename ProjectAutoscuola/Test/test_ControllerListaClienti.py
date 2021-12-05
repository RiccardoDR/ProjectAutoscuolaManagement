import os
import pickle
from unittest import TestCase

from ProgettoAutoscuola.Cliente.Model.Cliente import Cliente
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class TestControllerListaClienti(TestCase):

    def test_aggiungi_cliente(self):
        self.controller = ControllerListaClienti()
        self.cliente = Cliente("Luca", "dambro", "2345", "via ciao", "email@ciao.it", "2134", "23/03/2000", "maschio")
        self.controller.aggiungi_cliente(self.cliente)

    def test_rimuovi_cliente_by_index(self):
        self.test_aggiungi_cliente()
        if os.path.isfile('Data/lista_clienti.pickle'):
            with open('Data/lista_clienti.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)
                a = self.lista_clienti.index(self.cliente)
                self.assertFalse(self.controller.rimuovi_cliente_by_index(10000))
                self.assertTrue(self.controller.rimuovi_cliente_by_index(a))

    def test_get_lista_clienti(self):
        self.test_aggiungi_cliente()
        self.assertNotEqual(self.controller.get_lista_clienti(), [])
