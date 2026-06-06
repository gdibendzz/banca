import models.conto_corrente as cc
import models.conto_cointestato as cci

def cerca_conto(numero, lista: list[cc.ContoCorrente]):
    conto_trovato=None
    for l in lista:
        if l.cerca_da_numero(numero):
            conto_trovato=l
    return conto_trovato

def esegui_operazioni(lista):
    if len(lista) > 0:
        try:
            numero=int(input("Inserire numero da cercare: "))
            conto=cerca_conto(numero, lista)
            if conto is None:
                print("Non esiste un conto con il seguente numero conto.")
            else:
                op=""
                i = 1
                while i <= 3:
                    try:  
                        pin = int(input("Inserire il pin del conto: "))
                        if pin < 0:
                            raise ValueError
                    except ValueError:    
                        print("Il numero del conto deve essere un numero positivo")
                    if pin == conto.pin:
                        break
                    else:
                        print(f"Hai ancora  {3 - i} tentativi")
                        i += 1
                if(i == 4):
                    print("Accesso negato.")
                    conto.blocca_conto()

                while op != 8 and not conto.bloccato:
                    op=int(input("Seleziona l'operazione che vuoi effettuare \n" \
                        "1. Per depositare \n" \
                        "2. Per prelevare \n" \
                        "3. Per mostrare il saldo \n" \
                        "4. Per mostrare i movimenti \n" \
                        "5. Per cercare i movimenti \n"  \
                        "6. Per effettuare bonifico \n"  \
                        "7. Statistiche conto \n"  \
                        "8. Per uscire\n"))
                    if op < 0:
                        raise ValueError
                    match op:
                        case 1:
                            s=int(input("Inserire la somma da depositare: "))
                            conto.deposita(s)
                        case 2:
                            p=int(input("Inserire la somma da prelevare: "))
                            conto.preleva(p)
                        case 3:
                            conto.mostra_saldo()
                        case 4:
                            conto.mostra_movimenti()
                        case 5:
                            search=input("Inserire la parola chiave: ")
                            lmovimenti=conto.findByWord(search)
                            if len(lmovimenti) == 0:
                                print("Nessun movimento trovato")
                            else:
                                print("Elenco movimenti del conto", conto.numeroConto)
                                for m in lmovimenti:
                                    print(m)
                        case 6:
                            numero_conto=int(input("Inserire numero da cercare: "))
                            conto2=cerca_conto(numero_conto, lista)
                            if conto2 is None:
                                print("Non esiste un conto con il seguente numero conto.")
                            else:
                                importo=int(input("Inserire importo: "))
                                causale=input("Inserire la causale: ")
                                conto.bonifico(conto2, importo, causale)
                                conto.mostra_movimenti()
                                conto2.mostra_movimenti()
                        case 7:
                            print(f"Totale prelevato: {conto.totale_operazione('Prelievo')}")
                            print(f"Totale depositato: {conto.totale_operazione('Deposito')}")
                            mm = conto.max_movimento()
                            print(f"Movimento più alto: {mm if mm is not None else 'Nessun Movimento Effettuato'}")
                            print(f"Numero totale di operazioni : {conto.conta_depositi() + conto.conta_prelievi()}")
                        case _:
                            pass
        except ValueError:
            print("Il numero deve essere positivo.")
        for l in lista:
            pass
    else:
        print("Non è presente alcun conto.")

def main():
    lista_conti=[]
    list_coint = []
    numero=int(input("Inserire numero di conti da creare: "))
    for x in range(numero):
        ni=str(input("\nInserire il nome intestatario: "))
        nc=int(input("Inserire il numero conto: "))
        if len(lista_conti) > 0:
            for lcc in lista_conti:
                if lcc.cerca_da_numero(nc):
                    raise Exception("Esiste già questo numero conto.")
        di=float(input("Inserire il deposito iniziale: "))
        is_cointestato = input("Il conto è cointestato? S/N: ")
        if is_cointestato.upper() == "S":
            numero=int(input("Inserire numero di cointestatari: "))
            for x in range(numero):
                nci=str(input("Inserire il nome del cointestatario: "))
                list_coint.append(nci)
            conto_c=cci.ContoCointestato(ni, nc, list_coint)
        else:
            conto_c=cc.ContoCorrente(ni, nc)
        conto_c.deposita(di)
        print("\n")
        conto_c.mostra_riepilogo()
        lista_conti.append(conto_c)
    esegui_operazioni(lista_conti)

if __name__ == "__main__":
    main()