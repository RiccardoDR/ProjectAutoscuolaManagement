import pickle
import os

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class ListaPagamenti:  # Gestisce i dati e le operazioni relative alla lsita pagamenti.
    def __init__(self):
        self.lista_pagamenti = []
        self.sorted = []

    # Il seguente blocco carica nella variabile lista_pagamenti la lista
    # dei pagamenti contenuta nel file 'lista-pagamenti.json'.
    def set_data(self):
        if os.stat('ListaPagamenti/Data/lista_pagamenti.pickle').st_size != 0:
            if os.path.isfile('ListaPagamenti/Data/lista_pagamenti.pickle'):
                with open('ListaPagamenti/Data/lista_pagamenti.pickle', 'rb') as f:
                    self.lista_pagamenti = pickle.load(f)
                    self.sorted = sorted(self.lista_pagamenti, key=lambda x: (x.get_cliente()))

    # == aggiungi_pagamento ==
    # La funzione si occupa di aggiungere le informazioni relative al nuovo pagamento
    # nel file 'lista_pagamenti.pickle' in append.
    def aggiungi_pagamento(self, pagamento):
        self.sorted.append(pagamento)
        self.sorted = sorted(self.sorted, key=lambda x: (x.get_cliente()))

    def elimina_pagamenti_by_cliente(self, i):
        start = 0
        end = 0
        trovato_inizio = False
        trovato_fine = False
        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()
        self.cliente = self.controller_clienti.get_lista_clienti()[i]
        self.controller_cliente = ControllerCliente(self.cliente)
        self.set_data()
        for pagamento in self.sorted:
            if pagamento.get_cliente() == self.controller_cliente.get_nome()+" "+self.controller_cliente.get_cognome():
                if not trovato_inizio:
                    trovato_inizio = True
                    start = self.sorted.index(pagamento)
            if trovato_inizio:
                if pagamento.get_cliente() != self.controller_cliente.get_nome()+" "+self.controller_cliente.get_cognome():
                    if not trovato_fine:
                        trovato_fine = True
                        end = self.sorted.index(pagamento)

        if not trovato_fine:
            del self.lista_pagamenti[start:]
        else:
            del self.lista_pagamenti[start:end]
        self.sorted = sorted(self.lista_pagamenti, key=lambda x: (x.get_cliente()))

    # == get_lista_pagamenti ==
    # La funzione ritorna la lista_pagamenti.
    def get_lista_pagamenti(self):
        return self.sorted

    # == save_data ==
    # La funzione si occupa di salvare eventuali modifiche dei
    # dati relativi ai pagamenti e contenuti nella lista_pagamenti.
    def save_data(self):
        with open('ListaPagamenti/Data/lista_pagamenti.pickle', 'wb') as handle:
            pickle.dump(self.sorted, handle, pickle.HIGHEST_PROTOCOL)
