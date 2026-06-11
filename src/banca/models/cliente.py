import models.conto_corrente as cc
class Cliente:
    def __init__(self, nome: str, cognome: str, conto: cc.ContoCorrente):
        self.nome=nome
        self.cognome=cognome
        self.conto=conto

    def get_nome_completo(self):
        return self.nome + " " + self.cognome