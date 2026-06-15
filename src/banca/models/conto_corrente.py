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
            self.movimenti.append(f"Deposito di {importo} euro, data movimento: {datetime.now()}")

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
                self.movimenti.append(f"Prelievo di {importo} euro")
                self.movimenti.append(
                    f"Commissione applicata di {self.commissione} euro"
                )
            else:
                print("Impossibile effettuare la seguente operazione")

    def mostra_saldo(self):
        print("Saldo attuale:", self.saldo)

    def mostra_movimenti(self):
        if len(self.movimenti) > 0:
            print(f"Lista movimenti di {self.numeroConto}:")
            for m in self.movimenti:
                print(m)
        else:
            print("Nessun movimento da visualizzare")

    def bonifico(self, conto_destinazione, importo, causale):
        if self.bloccato == True:
            print("Conto bloccato. Impossibile effettuare il bonifico")
        else:
            self.preleva(importo)
            self.movimenti.append(
                f"Bonifico di {importo} euro effettuato a {conto_destinazione.numeroConto} - Causale: {causale}, data movimento: {datetime.now()}"
            )
            conto_destinazione.deposita(importo)
            conto_destinazione.movimenti.append(
                f"Bonifico di {importo} euro ricevuto da {self.numeroConto} - Causale: {causale}, data movimento: {datetime.now()}"
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
                if m.startswith("Deposito"):
                    cd += 1
        return cd

    def conta_prelievi(self):
        cp = 0
        if len(self.movimenti) > 0:
            for m in self.movimenti:
                if m.startswith("Prelievo"):
                    cp += 1
        return cp

    def findByWord(self, word):
        return list(filter(lambda x: word.lower() in x.lower(), self.movimenti))

    def totale_operazione(self, operazione):
        total = 0
        m_validi = list(filter( lambda  m : m.startswith(operazione) ,  self.movimenti))
        if len(m_validi) > 0:
            for m in m_validi:
                words = m.split(" ")
                print(f"words: {words[2]}")
                total += float(words[2])
        return total

    def max_movimento(self):
        max_op = 0
        op = None
        m_validi = list(filter( lambda  m : (m.startswith("Deposito") or m.startswith("Prelievo")), self.movimenti))
        if len(m_validi) > 0:
            for m in m_validi:
                words = m.split(" ")
                op_sum = float(words[2])
                if op_sum > max_op:
                    max_op = op_sum
                    op = m
        return op

    def addebito_automatico(self,importo, descrizione):
        self.saldo -= importo
        self.movimenti.append(f"Addebito automatico di {importo} euro per {descrizione}, data movimento: {datetime.now()}")


    def __str__(self):
        blocked = "true" if self.bloccato else "false"

        return f"Intestatario: {self.intestatario}; Numero conto: {self.numeroConto} Saldo: {self.saldo}; Fido: {self.saldo}, Bloccato: {blocked}"
