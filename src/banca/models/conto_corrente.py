class ContoCorrente:

    def __init__(self, intestatario, numeroConto):
        self.saldo = 0
        self.bloccato = False
        self.intestatario = intestatario
        self.numeroConto = numeroConto
        self.movimenti=[]
        self.fido=200
        self.commissione=1

    def deposita(self, importo):
        if importo <=0:
            print("Non si può depositare un importo negativo o zero")
        else:
            self.saldo+=importo
            self.movimenti.append(f"Deposito di {importo} euro")
    
    def preleva(self, importo):
        differenza=self.saldo-importo
        if differenza < -self.fido:
            print("Non puoi prelevare più del fido")
        else:
            self.saldo-=importo+self.commissione
            self.movimenti.append(f"Prelievo di {importo} euro")
            self.movimenti.append(f"Commissione applicata di {self.commissione} euro")
    
    def mostra_saldo(self):
        print("Saldo attuale:", self.saldo)

    def mostra_movimenti(self):
        if len(self.movimenti) > 0:
            print(f"Lista movimenti di {self.numeroConto}:")
            for m in self.movimenti:
                print(m)
        else:
            print("Nessun movimento da visualizzare")
    
    def bonifico(self, conto_destinazione, importo):
        self.preleva(importo)
        conto_destinazione.deposita(importo)
    
    def cerca_da_numero(self, numero):
        return True if numero == self.numeroConto else False