import os
import pickle

from ProgettoAutoscuola.Cliente.Controller.ControllerCliente import ControllerCliente
from ProgettoAutoscuola.ListaClienti.Controller.ControllerListaClienti import ControllerListaClienti


class ListaVisiteMediche:  # Gestisce i dati e le operazioni relative alla lista viste mediche.
    def __init__(self):
        self.lista_visite = []
        self.sorted = []

    # Il seguente blocco carica nella variabile lista_visite la lista
    # delle visite mediche contenuta nel file 'lista-visite.pickle'.
    def set_data(self):
        if os.stat('ListaVisiteMediche/Data/lista_visite.pickle').st_size != 0:
            if os.path.isfile('ListaVisiteMediche/Data/lista_visite.pickle'):
                with open('ListaVisiteMediche/Data/lista_visite.pickle', 'rb') as f:
                    self.lista_visite = pickle.load(f)
                    self.sorted = sorted(self.lista_visite, key=lambda x: (x.get_cliente()))

    # == aggiungi_visita ==
    # La funzione si occupa di aggiungere le informazioni relative alla nuova visita medica
    # nel file 'lista_visite.pickle' in append.
    def aggiungi_visita(self, visita):
        self.sorted.append(visita)
        self.sorted = sorted(self.sorted, key=lambda x: (x.get_cliente()))

    def elimina_visite_by_cliente(self, i):
        start = 0
        end = 0
        trovato_inizio = False
        trovato_fine = False
        self.controller_clienti = ControllerListaClienti()
        self.controller_clienti.set_data()
        self.cliente = self.controller_clienti.get_lista_clienti()[i]
        print(self.cliente)
        self.controller_cliente = ControllerCliente(self.cliente)
        self.set_data()
        for visita in self.sorted:
            if visita.get_cliente() == self.controller_cliente.get_nome()+" "+self.controller_cliente.get_cognome():
                if not trovato_inizio:
                    trovato_inizio = True
                    start = self.sorted.index(visita)
            if trovato_inizio:
                if visita.get_cliente() != self.controller_cliente.get_nome()+" "+self.controller_cliente.get_cognome():
                    if not trovato_fine:
                        trovato_fine = True
                        end = self.sorted.index(visita)

        if not trovato_fine:
            del self.lista_visite[start:]
        else:
            del self.lista_visite[start:end]
        self.sorted = sorted(self.lista_visite, key=lambda x: (x.get_cliente()))

    # == get_lista_visite ==
    # La funzione ritorna la lista_visite.
    def get_lista_visite(self):
        return self.sorted

    # == rimuovi_visita_by_id ==
    # La funzione ha il compito di eliminare dal file 'lista_visite.pickle' tutte le
    # informazioni relative alla visita con l'id corrispondente a quello preso in input.
    def rimuovi_visita_by_id(self, visita):
        self.sorted.remove(visita)

    # == save_data ==
    # La funzione si occupa di salvare eventuali modifiche dei
    # dati relativi alle visite e contenuti nella lista_visite.
    def save_data(self):
        with open('ListaVisiteMediche/Data/lista_visite.pickle', 'wb') as handle:
            pickle.dump(self.sorted, handle, pickle.HIGHEST_PROTOCOL)
