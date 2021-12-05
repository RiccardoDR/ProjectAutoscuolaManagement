import random


class Dipendente:  # Gestisce i dati e le operazioni relative al dipendente.
    def __init__(self, nome, cognome, username, password, cf, data_di_nascita, luogo_di_nascita, email, telefono, mansione,
                 tipo_contratto, sesso):
        self.id = str(random.randint(10000, 99999))
        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.password = password
        self.cf = cf
        self.data_di_nascita = data_di_nascita
        self.luogo_di_nascita = luogo_di_nascita
        self.email = email
        self.telefono = telefono
        self.mansione = mansione
        self.tipo_contratto = tipo_contratto
        self.sesso = sesso
        self.path = "None"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cognome(self):
        return self.cognome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_cf(self):
        return self.cf

    def set_cf(self, cf):
        self.cf = cf

    def get_data_nascita(self):
        return self.data_di_nascita

    def set_data_nascita(self, data_nascita):
        self.data_di_nascita = data_nascita

    def get_luogo_nascita(self):
        return self.luogo_di_nascita

    def set_luogo_nascita(self, luogo_nascita):
        self.luogo_di_nascita = luogo_nascita

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_mansione(self):
        return self.mansione

    def set_mansione(self, mansione):
        self.mansione = mansione

    def get_contratto(self):
        return self.tipo_contratto

    def set_contratto(self, contratto):
        self.tipo_contratto = contratto

    def get_sesso(self):
        return self.sesso

    def set_sesso(self, sesso):
        self.sesso = sesso

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path



