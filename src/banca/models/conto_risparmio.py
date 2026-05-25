import conto_corrente as cc
class ContoRisparmio(cc.ContoCorrente):
    def __init__(self, intestatario, numeroConto, tasso_interesse):
        super().__init__(intestatario, numeroConto)
        self.tasso_interesse=tasso_interesse
    
    def applica_interessi(self):
        self.saldo+=(self.saldo * self.tasso_interesse) / 100