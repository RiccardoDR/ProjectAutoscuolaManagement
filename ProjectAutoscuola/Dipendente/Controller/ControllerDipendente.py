class ControllerDipendente:  # Gestisce e attua i comandi relativi al dipendente.
    def __init__(self, dipendente):
        self.model = dipendente

    def get_id(self):
        return self.model.get_id()

    def set_id(self, id):
        self.model.set_id(id)

    def get_nome(self):
        return self.model.get_nome()

    def set_nome(self, nome):
        self.model.set_nome(nome)

    def get_cognome(self):
        return self.model.get_cognome()

    def set_cognome(self, cognome):
        self.model.set_cognome(cognome)

    def get_username(self):
        return self.model.get_username()

    def set_username(self, username):
        self.model.set_username(username)

    def get_password(self):
        return self.model.get_password()

    def set_password(self, password):
        self.model.set_password(password)

    def get_cf(self):
        return self.model.get_cf()

    def set_cf(self, cf):
        self.model.set_cf(cf)

    def get_data_nascita(self):
        return self.model.get_data_nascita()

    def set_data_nascita(self, data_nascita):
        self.model.set_data_nascita(data_nascita)

    def get_luogo_nascita(self):
        return self.model.get_luogo_nascita()

    def set_luogo_nascita(self, luogo_nascita):
        self.model.set_luogo_nascita(luogo_nascita)

    def get_email(self):
        return self.model.get_email()

    def set_email(self, email):
        self.model.set_email(email)

    def get_telefono(self):
        return self.model.get_telefono()

    def set_telefono(self, telefono):
        self.model.set_telefono(telefono)

    def get_mansione(self):
        return self.model.get_mansione()

    def set_mansione(self, mansione):
        self.model.set_mansione(mansione)

    def get_contratto(self):
        return self.model.get_contratto()

    def set_contratto(self, contratto):
        self.model.set_contratto(contratto)

    def get_sesso(self):
        return self.model.get_sesso()

    def set_sesso(self, sesso):
        self.model.set_sesso(sesso)

    def get_path(self):
        return self.model.get_path()

    def set_path(self, path):
        self.model.set_path(path)
