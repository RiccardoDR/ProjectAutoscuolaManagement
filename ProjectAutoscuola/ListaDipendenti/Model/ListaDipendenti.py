import os
import pickle


class ListaDipendenti:  # Gestisce i dati e le operazioni relative alla lista dipendenti.
    def __init__(self):
        self.lista_dipendenti = []
        self.sorted = []

    # Il seguente blocco carica nella variabile lista_dipendenti la lista
    # dei dipendenti contenuta nel file 'lista-dipendenti.pickle'.
    def set_data(self):
        if os.stat('ListaDipendenti/Data/lista_dipendenti.pickle').st_size != 0:
            if os.path.isfile('ListaDipendenti/Data/lista_dipendenti.pickle'):
                with open('ListaDipendenti/Data/lista_dipendenti.pickle', 'rb') as f:
                    self.lista_dipendenti = pickle.load(f)
                    self.sorted = sorted(self.lista_dipendenti, key=lambda x: (x.get_cognome()))

    # == add_dipendente ==
    # La funzione si occupa di aggiungere le informazioni relative al nuovo dipendente
    # nel file 'lista_dipendenti.pickle' in append.
    def add_dipendente(self, dipendente):
        self.sorted.append(dipendente)
        self.sorted = sorted(self.sorted, key=lambda x: (x.get_cognome()))

    # == rimuovi_dipendente_by_id ==
    # La funzione ha il compito di eliminare dal file 'lista_dipendenti.pickle' tutte le
    # informazioni relative al dipendente con l'id corrispondente a quello preso in input.
    def rimuovi_dipendente_by_index(self, i):
        dipendente = self.sorted[i]
        self.sorted.remove(dipendente)

    # == get_lista_dipendenti ==
    # La funzione ritorna la lista_dipendenti.
    def get_lista_dipendenti(self):
        return self.sorted

    # == save_data ==
    # La funzione si occupa di salvare eventuali modifiche dei
    # dati relativi ai dipendenti e contenuti nella lista_dipendenti.
    def save_data(self):
        with open('ListaDipendenti/Data/lista_dipendenti.pickle', 'wb') as handle:
            pickle.dump(self.sorted, handle, pickle.HIGHEST_PROTOCOL)
