class Cliente:  # Gestisce i dati e le operazioni relative al cliente.
    def __init__(self, nome, cognome, cf, indirizzo, email, telefono, tipo_patente, data_di_nascita, sesso):
        self.id = "None"
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono
        self.tipo_patente = tipo_patente
        self.data_di_nascita = data_di_nascita
        self.sesso = sesso
        self.visita_medica = "None"
        self.esame_teorico = "None"
        self.esame_pratico = "None"
        self.pagamento_iniziale = "None"
        self.pagamento_esame_teorico = "None"
        self.pagamento_lezioni_guida = "None"
        self.pagamento_esame_pratico = "None"
        self.prenotazione = "None"
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

    def get_cf(self):
        return self.cf

    def set_cf(self, cf):
        self.cf = cf

    def get_indirizzo(self):
        return self.indirizzo

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_tipo_patente(self):
        return self.tipo_patente

    def set_tipo_patente(self, tipo_patente):
        self.tipo_patente = tipo_patente

    def get_data_nascita(self):
        return self.data_di_nascita

    def set_data_nascita(self, data_nascita):
        self.data_di_nascita = data_nascita

    def get_sesso(self):
        return self.sesso

    def set_sesso(self, sesso):
        self.sesso = sesso

    def get_visita_medica(self):
        return self.visita_medica

    def set_visita_medica(self, visita_medica):
        self.visita_medica = visita_medica

    def get_esame_teorico(self):
        return self.esame_teorico

    def set_esame_teorico(self, esame_teorico):
        self.esame_teorico = esame_teorico

    def get_esame_pratico(self):
        return self.esame_pratico

    def set_esame_pratico(self, esame_pratico):
        self.esame_pratico = esame_pratico

    def get_pagamento_iniziale(self):
        return self.pagamento_iniziale

    def set_pagamento_iniziale(self, pagamento_iniziale):
        self.pagamento_iniziale = pagamento_iniziale

    def get_pagamento_esame_teorico(self):
        return self.pagamento_esame_teorico

    def set_pagamento_esame_teorico(self, pagamento_esame_teorico):
        self.pagamento_esame_teorico = pagamento_esame_teorico

    def get_pagamento_lezioni_guida(self):
        return self.pagamento_lezioni_guida

    def set_pagamento_lezioni_guida(self, pagamento_lezioni_guida):
        self.pagamento_lezioni_guida = pagamento_lezioni_guida

    def get_pagamento_esame_pratico(self):
        return self.pagamento_esame_pratico

    def set_pagamento_esame_pratico(self, pagamento_esame_pratico):
        self.pagamento_esame_pratico = pagamento_esame_pratico

    def get_prenotazione(self):
        return self.prenotazione

    def set_prenotazione(self, prenotazione):
        self.prenotazione = prenotazione

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
