import models.conto_corrente as cc
import models.cliente as cl
import utils.method_utils as mu

def main():
    numeroc=mu.generatore_numero_conto()
    cc1=cc.ContoCorrente("Gianmarco Di Benedetto", next(numeroc))
    cc2=cc.ContoCorrente("Alberto Rossi", next(numeroc))
    cc3=cc.ContoCorrente("Marco Verdi", next(numeroc))
    c1=cl.Cliente("Gianmarco", "Di Benedetto", cc1)
    c2=cl.Cliente("Alberto", "Rossi", cc2)
    c3=cl.Cliente("Marco", "Rossi", cc3)
    clienti=[c1, c2, c3]
    search=input("Inserire cognome da ricercare: ")
    clienti_filtered=list(filter(lambda x : x.cognome.lower() == search.lower(), clienti))
    if len(clienti_filtered) > 0:
        print("Risultati trovati:", len(clienti_filtered))
        for c in clienti_filtered:
            print(c.get_nome_completo())
    else:
        print("Nessun cliente trovato")

if __name__ == "__main__":
    main()