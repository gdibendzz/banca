import models.conto_corrente as c


class ContoCointestato(c.ContoCorrente):

    def __init__(self, intestatario, numeroConto, cointestatari):
        super().__init__(intestatario, numeroConto)
        self.cointestatari = cointestatari

    def __str__(self):
        blocked = "true" if self.bloccato else "false"

        return f"Intestatari: {self.intestatario}, {', '.join(self.cointestatari)}; Numero conto: {self.numeroConto} Saldo: {self.saldo}; Fido: {self.saldo}, Bloccato: {blocked}"

    def mostra_riepilogo(self):
        blocked = "Sì" if self.bloccato else "No"
        int_list = self.cointestatari.copy()
        int_list.append(self.intestatario)

        print(
            f"Intestatari: {self.intestatario}, {', '.join(self.cointestatari)}; Numero conto: {self.numeroConto} Saldo: {self.saldo}; Fido: {self.saldo}, Bloccato: {blocked}"
        )
        self.mostra_movimenti()
        print(
            f"Numero totale di movimenti di {self.numeroConto}: {len(self.movimenti)}"
        )
