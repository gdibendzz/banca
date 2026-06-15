import random
from datetime import datetime


class ContoCorrente:

    def __init__(self, intestatario, numeroConto):
        self.saldo = 0
        self.pin = random.randint(1111, 9999)
        print(f" per info Conto: {numeroConto}: {self.pin}")
        self.bloccato = False
        self.intestatario = intestatario
        self.numeroConto = numeroConto
        self.movimenti = []
        self.fido = 200
        self.commissione = 1
        self.prelievo_giornaliero = 500

    def deposita(self, importo):
        if importo <= 0:
            print("Non si può depositare un importo negativo o zero")
        else:
            self.saldo += importo
            self.movimenti.append(
                {
                    "tipo": "deposito",
                    "importo": importo,
                    "descrizione": "Versamento Contanti",
                    "data": datetime.now(),
                }
            )

    def preleva(self, importo):
        if self.bloccato == True:
            print("Conto bloccato. Impossibile prelevare")
        else:
            differenza = self.saldo - importo
            if importo > self.prelievo_giornaliero:
                print(
                    "Importo supera il limite giornaliero. Hai ancora a disposizione",
                    self.prelievo_giornaliero,
                )
            elif differenza < -self.fido:
                print("Non puoi prelevare più del fido")
            elif importo % 10 == 0 or importo % 20 == 0:
                self.saldo -= importo + self.commissione
                self.prelievo_giornaliero -= importo
                self.movimenti.append(
                    {
                        "tipo": "prelievo",
                        "importo": importo,
                        "descrizione": "Prelievo Contanti",
                        "data": datetime.now(),
                    }
                )
                self.movimenti.append(
                    {
                        "tipo": "commissione",
                        "importo": self.commissione,
                        "descrizione": "Commissione applicata",
                        "data": datetime.now(),
                    }
                )
            else:
                print("Impossibile effettuare la seguente operazione")

    def mostra_saldo(self):
        print("Saldo attuale:", self.saldo)

    def mostra_movimenti(self):
        if len(self.movimenti) > 0:
            print(f"Lista movimenti di {self.numeroConto}:")
            for m in self.movimenti:
                print(
                    f"{m["descrizione"]} -  importo: {m["importo"]} - data : {m["data"].strftime('%d-%m-%Y %H:%M:%S')} "
                )
        else:
            print("Nessun movimento da visualizzare")

    def bonifico(self, conto_destinazione, importo, causale):
        if self.bloccato == True:
            print("Conto bloccato. Impossibile effettuare il bonifico")
        elif self.saldo - importo < -self.fido:
            print("Non puoi prelevare più del fido")
        else:
            self.movimenti.append(
                {
                    "tipo": "bonifico",
                    "importo": importo,
                    "descrizione": f"Bonifico effettuato - causale:  {causale}",
                    "data": datetime.now(),
                }
            )
            conto_destinazione.saldo += importo
            conto_destinazione.movimenti.append(
                {
                    "tipo": "bonifico",
                    "importo": importo,
                    "descrizione": f"Bonifico ricevuto - causale:  {causale}",
                    "data": datetime.now(),
                }
            )

    def cerca_da_numero(self, numero):
        return True if numero == self.numeroConto else False

    def mostra_riepilogo(self):
        blocked = "Sì" if self.bloccato else "No"
        print(
            f"Intestatario: {self.intestatario}; Numero conto: {self.numeroConto} Saldo: {self.saldo}; Fido: {self.saldo}, Bloccato: {blocked}"
        )
        self.mostra_movimenti()
        print(
            f"Numero totale di movimenti di {self.numeroConto}: {len(self.movimenti)}"
        )

    def blocca_conto(self):
        self.bloccato = True

    def sblocca_conto(self):
        self.bloccato = False

    def reset_limite_giornaliero(self):
        self.prelievo_giornaliero = 500

    def conta_depositi(self):
        cd = 0
        if len(self.movimenti) > 0:
            for m in self.movimenti:
                if m["tipo"] == "deposito":
                    cd += 1
        return cd

    def conta_prelievi(self):
        cp = 0
        if len(self.movimenti) > 0:
            for m in self.movimenti:
                if m["tipo"] == "prelievo":
                    cp += 1
        return cp

    def findByWord(self, word):
        return list(
            filter(lambda x: word.lower() in x["descrizione"].lower(), self.movimenti)
        )

    def totale_operazione(self, operazione):
        total = 0
        m_validi = list(filter(lambda m: m["tipo"] == operazione, self.movimenti))
        if len(m_validi) > 0:
            total = sum([m["importo"] for m in m_validi] )
        return total

    def max_movimento(self):
        max_op = 0
        op = None
        m_validi = list(
            filter(
                lambda m: (
                    m["tipo"] == "deposito"
                    or m["tipo"] == "prelievo"
                    or m["tipo"] == "bonifico"
                    or m["tipo"] == "addebito"
                ),
                self.movimenti,
            )
        )
        if len(m_validi) > 0:
            for m in m_validi:

                if m["importo"] > max_op:
                    max_op = m["importo"]
                    op = f"{m["descrizione"]} -  importo: {m["importo"]} - data : {m["data"].strftime('%d-%m-%Y %H:%M:%S')} "
        return op

    def addebito_automatico(self, importo, descrizione):
        self.saldo -= importo
        self.movimenti.append(
            {
                "tipo": "addebito",
                "importo": importo,
                "descrizione": f"Addebito automatico per {descrizione}",
                "data": datetime.now(),
            }
        )

    def __str__(self):
        blocked = "true" if self.bloccato else "false"

        return f"Intestatario: {self.intestatario}; Numero conto: {self.numeroConto} Saldo: {self.saldo}; Fido: {self.saldo}, Bloccato: {blocked}"
