class ControllerCliente:  # Gestisce e attua i comandi relativi al cliente.
    def __init__(self, cliente):
        self.model = cliente

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

    def get_cf(self):
        return self.model.get_cf()

    def set_cf(self, cf):
        self.model.set_cf(cf)

    def get_indirizzo(self):
        return self.model.get_indirizzo()

    def set_indirizzo(self, indirizzo):
        self.model.set_indirizzo(indirizzo)

    def get_email(self):
        return self.model.get_email()

    def set_email(self, email):
        self.model.set_email(email)

    def get_telefono(self):
        return self.model.get_telefono()

    def set_telefono(self, telefono):
        self.model.set_telefono(telefono)

    def get_tipo_patente(self):
        return self.model.get_tipo_patente()

    def set_tipo_patente(self, tipo_patente):
        self.model.set_tipo_patente(tipo_patente)

    def get_data_nascita(self):
        return self.model.get_data_nascita()

    def set_data_nascita(self, data_nascita):
        self.model.set_data_nascita(data_nascita)

    def get_sesso(self):
        return self.model.get_sesso()

    def set_sesso(self, sesso):
        self.model.set_sesso(sesso)

    def get_visita_medica(self):
        return self.model.get_visita_medica()

    def set_visita_medica(self, visita_medica):
        self.model.set_visita_medica(visita_medica)

    def get_esame_teorico(self):
        return self.model.get_esame_teorico()

    def set_esame_teorico(self, esame_teorico):
        self.model.set_esame_teorico(esame_teorico)

    def get_esame_pratico(self):
        return self.model.get_esame_pratico()

    def set_esame_pratico(self, esame_pratico):
        self.model.set_esame_pratico(esame_pratico)

    def get_pagamento_iniziale(self):
        return self.model.get_pagamento_iniziale()

    def set_pagamento_iniziale(self, pagamento_iniziale):
        self.model.set_pagamento_iniziale(pagamento_iniziale)

    def get_pagamento_esame_teorico(self):
        return self.model.get_pagamento_esame_teorico()

    def set_pagamento_esame_teorico(self, pagamento_esame_teorico):
        self.model.set_pagamento_esame_teorico(pagamento_esame_teorico)

    def get_pagamento_lezioni_guida(self):
        return self.model.get_pagamento_lezioni_guida()

    def set_pagamento_lezioni_guida(self, pagamento_lezioni_guida):
        self.model.set_pagamento_lezioni_guida(pagamento_lezioni_guida)

    def get_pagamento_esame_pratico(self):
        return self.model.get_pagamento_esame_pratico()

    def set_pagamento_esame_pratico(self, pagamento_esame_pratico):
        self.model.set_pagamento_esame_pratico(pagamento_esame_pratico)

    def get_prenotazione(self):
        return self.model.get_prenotazione()

    def set_prenotazione(self, prenotazione):
        self.model.set_prenotazione(prenotazione)

    def get_path(self):
        return self.model.get_path()

    def set_path(self, path):
        self.model.set_path(path)
