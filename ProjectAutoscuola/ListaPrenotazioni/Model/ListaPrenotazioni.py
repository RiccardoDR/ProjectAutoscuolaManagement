import os
import pickle


class ListaPrenotazioni:  # Gestisce i dati e le operazioni relative alla lista prenotazioni.
    def __init__(self):
        self.lista_prenotazioni = []
        self.sorted = []

    # Il seguente blocco carica nella variabile lista_pagamenti la lista
    # dei pagamenti contenuta nel file 'lista-pagamenti.pickle'.
    def set_data(self):
        if os.stat('ListaPrenotazioni/Data/lista_prenotazioni.pickle').st_size != 0:
            if os.path.isfile('ListaPrenotazioni/Data/lista_prenotazioni.pickle'):
                with open('ListaPrenotazioni/Data/lista_prenotazioni.pickle', 'rb') as f:
                    self.lista_prenotazioni = pickle.load(f)
                    self.sorted = sorted(self.lista_prenotazioni, key=lambda x: (x.get_tipo()))

    # == aggiungi_prenotazione ==
    # La funzione si occupa di aggiungere le informazioni relative alla nuova prenotazione
    # nel file 'lista_prenotazioni.pickle' in append.
    def aggiungi_prenotazione(self, prenotazione):
        self.sorted.append(prenotazione)
        self.sorted = sorted(self.sorted, key=lambda x: (x.get_tipo()))

    # == get_lista_prenotazioni ==
    # La funzione ritorna la lista_prenotazioni.
    def get_lista_prenotazioni(self):
        return self.sorted

    # == rimuovi_prenotazione_by_id ==
    # La funzione ha il compito di eliminare dal file 'lista_prenotazioni.pickle' tutte le
    # informazioni relative alla prenotazione con l'id corrispondente a quello preso in input.
    def rimuovi_prenotazione_by_id(self, i):
        prenotazione = self.sorted[i]
        self.sorted.remove(prenotazione)

    # == save_data ==
    # La funzione si occupa di salvare eventuali modifiche dei
    # dati relativi alle prenotazioni e contenuti nella lista_prenotazioni.
    def save_data(self):
        with open('ListaPrenotazioni/Data/lista_prenotazioni.pickle', 'wb') as handle:
            pickle.dump(self.sorted, handle, pickle.HIGHEST_PROTOCOL)
