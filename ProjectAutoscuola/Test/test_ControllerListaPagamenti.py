import os
import pickle
from unittest import TestCase

from ProgettoAutoscuola.ListaPagamenti.Controller.ControllerListaPagamenti import ControllerListaPagamenti
from ProgettoAutoscuola.Pagamento.Model.Pagamento import Pagamento


class TestControllerListaPagamenti(TestCase):

    def test_aggiungi_pagamento(self):
        self.controller = ControllerListaPagamenti()
        self.pagamento = Pagamento("50", "esame teorico", "giuseppe")
        self.controller.aggiungi_pagamento(self.pagamento)

    def test_elimina_pagamenty_by_cliente(self):
        self.test_aggiungi_pagamento()
        if os.path.isfile('Data/lista_pagamenti.pickle'):
            with open('Data/lista_pagamenti.pickle', 'rb') as f:
                self.lista_pagamenti = pickle.load(f)
                self.assertTrue(self.controller.elimina_pagamento_by_cliente(self.pagamento.get_cliente()))
                self.assertFalse(self.controller.elimina_pagamento_by_cliente("aaaaaaa"))

    def test_get_lista_pagamenti(self):
        self.test_aggiungi_pagamento()
        self.assertNotEqual(self.controller.get_lista_pagamenti(), [])
