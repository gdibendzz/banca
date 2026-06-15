from unittest import case

import models.conto_corrente as cc
import models.conto_cointestato as cci
import models.cliente as cl
import utils.file_utils as fu

'''
numeroc=mu.generatore_numero_conto()
cc1=cc.ContoCorrente("Gianmarco Di Benedetto", next(numeroc))
cc2=cc.ContoCorrente("Alberto Rossi", next(numeroc))
d={
        f"{cc1.numeroConto}": cc1,
        f"{cc2.numeroConto}": cc2
   }
'''

def cerca_conto(numero, lista: list[cc.ContoCorrente]):
    conto_trovato=None
    for l in lista:
        if l.cerca_da_numero(numero):
            conto_trovato=l
    return conto_trovato

list_cc=[]
clienti=[]
op = 0
while op != 6:
    try:
        op = int(
              input(
                 "\nSeleziona l'operazione che vuoi effettuare \n"
                 "1. Crea Conto \n"
                 "2. Lista Conti \n"
                 "3. Accedi per operazioni \n"
                 "4. Elimina Conto \n"
                 "5. Ricerca cliente \n"
                 "6. Esci\n"
                )
            )
        if op < 0:
            raise ValueError
         
        match op:
            case 1:
                numero=int(input("Inserire numero di conti da creare: "))
                for x in range(numero):
                            nome_cliente=input("Inserire nome del cliente: ")
                            cognome_cliente=input("Inserire cognome del cliente: ")
                            nc = None
                            contodiverso = False
                            while contodiverso == False:
                                nc = int(input("Inserire il numero conto: "))
                                if len(list_cc) > 0:
                                    nuova_lista = list(filter(lambda x : x.cerca_da_numero(nc), list_cc))
                                    if len(nuova_lista) > 0:
                                        print("Esiste già questo numero conto.")
                                    else:
                                        contodiverso = True
                                else:
                                    contodiverso = True

                            di=float(input("Inserire il deposito iniziale: "))
                            is_cointestato = input("Il conto è cointestato? S/N: ")
                            if is_cointestato.upper() == "S":
                                list_coint = []
                                numero=int(input("Inserire numero di cointestatari: "))
                                for x in range(numero):
                                    nci=str(input("Inserire il nome del cointestatario: "))
                                    list_coint.append(nci)
                                conto_c=cci.ContoCointestato(nome_cliente + " " + cognome_cliente, nc, list_coint)
                            else:
                                conto_c=cc.ContoCorrente(nome_cliente + " " + cognome_cliente, nc)
                            fu.write(conto_c.__str__(), f"{conto_c.numeroConto}.txt", "a")
                            conto_c.deposita(di)
                            print("\n")
                            conto_c.mostra_riepilogo()
                            list_cc.append(conto_c)
                            cliente=cl.Cliente(nome_cliente, cognome_cliente, conto_c)
                            clienti.append(cliente)
            case 2:
                print ("Lista di conti non ordinati: ")
                for x in list_cc:
                            print(x.__str__())
                            list_cc.sort(key=lambda x: x.saldo, reverse=True)
                print ("**************************************\n")
                print ("Lista di conti ora ordinati: ")
                for x in list_cc:
                    print(x.__str__())
                
            case 3:
                try:
                    num=int(input("Inserire il numero conto da cercare: "))
                    if num < 0:
                        raise ValueError

                    cc_founded = cerca_conto(num, list_cc)
                    if cc_founded is None:
                        print("Non esiste alcun conto con questo numero")
                    else:

                        # poi la puliamo op=""
                        # poila puliamo >> list_cc=[]
                        
                        i = 1
                        while i <= 3:
                            try:  
                                pin = int(input("Inserire il pin del conto: "))
                                if pin < 0:
                                    raise ValueError
                            except ValueError:    
                                print("Il numero del conto deve essere un numero positivo")
                            if pin == cc_founded.pin:
                                
                                break
                            
                            else:
                                print(f"Hai ancora  {3 - i} tentativi")
                                i += 1
                            if(i == 4):
                                print("Conto bloccato")
                                cc_founded.blocca_conto()
                

                        while op != 10 and not cc_founded.bloccato:
                            try:
                                op=int(input("\nSeleziona l'operazione che vuoi effettuare \n" \
                                "1. Per depositare \n" \
                                "2. Per prelevare \n" \
                                "3. Per mostrare il saldo \n" \
                                "4. Per mostrare i movimenti \n" \
                                "5. Per cercare i movimenti \n"  \
                                "6. Salva i movimenti \n"  \
                                "7. Statistiche conto \n"  \
                                "8. Scala addebiti automatici \n"  \
                                "9. Effettua un bonifico \n"  \
                                "10. Per uscire\n"))

                                if op < 0:
                                        raise ValueError
                                match op:
                                    case 1:
                                        s=int(input("Inserire la somma da depositare: "))
                                        cc_founded.deposita(s)
                                    case 2:
                                        p=int(input("Inserire la somma da prelevare: "))
                                        cc_founded.preleva(p)
                                    case 3:
                                        cc_founded.mostra_saldo()
                                    case 4:
                                        cc_founded.mostra_movimenti()
                                        numDepositi=cc_founded.conta_depositi()
                                        numPrelievi=cc_founded.conta_prelievi()
                                        print("Numero depositi:", numDepositi)
                                        print("Numero prelievi:", numPrelievi)
                                    case 5:
                                        search = input("Inserire la parola chiave: ")
                                        mov_list = cc_founded.findByWord(search)
                                        if len(mov_list) == 0:
                                            print("La lista è vuota")
                                        else:
                                            print("Elenco: ")
                                            for m in mov_list:
                                                print( f"{m['descrizione']} -  importo: {m['importo']} - data : {m['data'].strftime('%d-%m-%Y %H:%M:%S')} ")
                                    case 6:
                                        fu.write(cc_founded.__str__() + "\n", f"{cc_founded.numeroConto}.txt", "a")
                                        lista_mov = cc_founded.movimenti
                                        for m in lista_mov:
                                            fu.write(f"{m['descrizione']} -  importo: {m['importo']} - data : {m['data'].strftime('%d-%m-%Y %H:%M:%S')}\n", f"{cc_founded.numeroConto}.txt", "a")
                                        print("File Stampato\n----------------\n")
                                        print(fu.read(f"{cc_founded.numeroConto}.txt"))
                                
                                    case 7:
                                        print("\n\n")
                                        print(f"Totale prelevato: {cc_founded.totale_operazione('prelievo')}")
                                        print(f"Totale depositato: {cc_founded.totale_operazione('deposito')}")
                                        mm = cc_founded.max_movimento()
                                        print(f"Movimento più alto: {mm if mm is not None else 'Nessun Movimento Effettuato'}")
                                        print(f"Numero totale di operazioni : {cc_founded.conta_depositi() + cc_founded.conta_prelievi()}")
                                        print("\n\n")

                                    case 8: 
                                        print ("SALDO PRIMA del tentativo di addebito automatico:  \n\n")
                                        print(cc_founded.__str__())
                                        print("\n\n")
                                        importo = float(input("Inserire l'importo dell'addebito automatico: "))
                                        descrizione = input("Inserire la descrizione dell'addebito automatico: ")
                                        if importo < 0:
                                            raise ValueError
                                        if cc_founded.saldo < importo:
                                            print("Saldo insufficiente per effettuare l'addebito automatico")
                                            cc_founded.blocca_conto()
                                            print("Conto bloccato")
                                        else:                            
                                            cc_founded.addebito_automatico(importo, descrizione)
                                            print("Addebito automatico effettuato con successo")

                                        print ("SALDO DOPO tentativo di addebito automatico:  \n\n")
                                        print(cc_founded.__str__())
                                    case 9:
                                        conto2 = None
                                        while conto2 is None:
                                            numero_conto=int(input("Inserire numero da cercare: "))
                                            conto2=cerca_conto(numero_conto, list_cc)
                                            if conto2 is None:
                                                print("Non esiste un conto con il seguente numero conto.")
                                            else:
                                                importo=int(input("Inserire importo: "))
                                                causale=input("Inserire la causale: ")
                                                cc_founded.bonifico(conto2, importo, causale)
                                                cc_founded.mostra_movimenti()
                                                conto2.mostra_movimenti()
                                    case 10:
                                        print("USCITA DAL SOFTWARE")
                                    case _:
                                        pass
                            except ValueError:    
                                print("Il numero del conto deve essere un numero positivo\n \n")
                except ValueError:    
                    print("Il numero del conto deve essere un numero positivo\n \n")

            case 4:
                print ("Lista conti iniziali:\n\n")
                for x in list_cc:
                    print(x.__str__())
                    control = 0
                    input_num = int(input("Inserire il numero del conto da eliminare: "))
                    if input_num < 0:
                        raise ValueError 
                    for x in list_cc:
                        if input_num == x.numeroConto:
                            if x.saldo != 0:
                                list_cc.remove(x)
                                control=1
                                print("Conto eliminato")
                            else:
                                print("Impossibile eliminare un conto con saldo diverso da 0")  
                                control == 1 
                        if control == 0:
                            print("Non esiste alcun conto con questo numero")

                    print ("Lista conti dopo tentativo  di elimninazione:\n\n")

                    for x in list_cc:
                        print(x.__str__())
            case 5:
                search=input("Inserire cognome da ricercare: ")
                clienti_filtered=list(filter(lambda x : x.cognome.lower() == search.lower(), clienti))
                if len(clienti_filtered) > 0:
                    print("Risultati trovati:", len(clienti_filtered))
                    for c in clienti_filtered:
                        print(c.get_nome_completo())
                else:
                    print("Nessun cliente trovato")
            case __:
                print("USCITA DAL SOFTWARE")

    except ValueError:
      print("Inserire un intero")
           


