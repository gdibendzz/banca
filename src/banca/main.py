import models.conto_corrente as cc
import models.conto_cointestato as cci
import utils.file_utils as fu
import utils.method_utils as mu



numeroc=mu.generatore_numero_conto()
cc1=cc.ContoCorrente("Gianmarco Di Benedetto", next(numeroc))
cc2=cc.ContoCorrente("Alberto Rossi", next(numeroc))
d={
        f"{cc1.numeroConto}": cc1,
        f"{cc2.numeroConto}": cc2
    }
try:
    num=int(input("Inserire il numero conto da cercare: "))
    if num < 0:
        raise ValueError

    cc_founded=None
    for x,y in d.items():
        if y.cerca_da_numero(num) == True:
            cc_founded=y
    if cc_founded is None:
        print("Non esiste alcun conto con questo numero")
    else:

        op=""
        list_cc=[]
        
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
            

        while op != 12 and not cc_founded.bloccato:
            try:
                op=int(input("Seleziona l'operazione che vuoi effettuare \n" \
                "1. Per depositare \n" \
                "2. Per prelevare \n" \
                "3. Per mostrare il saldo \n" \
                "4. Per mostrare i movimenti \n" \
                "5. Per creare altri conti \n"  \
                "6. Per cercare i movimenti \n"  \
                "7. Salva i movimenti \n"  \
                "8. Classifica dei saldi \n"  \
                "9. Statistiche conto \n"  \
                "10. Elimina un conto \n"  \
                "11. Scala addebiti automatici \n"  \
                "12. Per uscire\n"))

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
                        numero=int(input("Inserire numero di conti da creare: "))
                        for x in range(numero):
                            ni=str(input("\nInserire il nome intestatario: "))
                            nc=int(input("Inserire il numero conto: "))
                            if len(list_cc) > 0:
                                for lcc in list_cc:
                                    if lcc.cerca_da_numero(nc):
                                        raise Exception("Esiste già questo numero conto.")
                            di=float(input("Inserire il deposito iniziale: "))
                            is_cointestato = input("Il conto è cointestato? S/N: ")
                            if is_cointestato.upper() == "S":
                                list_coint = []
                                numero=int(input("Inserire numero di cointestatari: "))
                                for x in range(numero):
                                    nci=str(input("Inserire il nome del cointestatario: "))
                                    list_coint.append(nci)
                                conto_c=cci.ContoCointestato(ni, nc, list_coint)
                            else:
                                conto_c=cc.ContoCorrente(ni, nc)
                            fu.write(conto_c.__str__(), f"{conto_c.numeroConto}.txt", "a")
                            conto_c.deposita(di)
                            print("\n")
                            conto_c.mostra_riepilogo()
                            list_cc.append(conto_c)
                    case 6:
                        search = input("Inserire la parola chiave: ")
                        mov_list = cc_founded.findByWord(search)
                        if len(mov_list) == 0:
                            print("La lista è vuota")
                        else:
                            print("Elenco: ")
                            for x in mov_list:
                                print(x)
                    case 7:
                        fu.write(cc_founded.__str__(), f"{cc_founded.numeroConto}.txt", "a")
                        lista_mov = cc_founded.movimenti
                        for m in lista_mov:
                            fu.write(m+"\n", f"{cc_founded.numeroConto}.txt", "a")
                        print("File Stampato\n----------------\n")
                        print(fu.read(f"{cc_founded.numeroConto}.txt"))
                    case 8:
                        print ("Lista di conti non ordinati: ")
                        for x in list_cc:
                            print(x.__str__())
                        list_cc.sort(key=lambda x: x.saldo, reverse=True)
                        print ("**************************************\n")
                        print ("Lista di conti ora ordinati: ")
                        for x in list_cc:
                            print(x.__str__())
                    case 9:
                        print("\n\n")
                        print(f"Totale prelevato: {cc_founded.totale_operazione("Prelievo")}")
                        print(f"Totale depositato: {cc_founded.totale_operazione("Deposito")}")
                        mm = cc_founded.max_movimento()
                        print(f"Movimento più alto: {mm if mm is not None else "Nessun Movimento Effettuato"}")
                        print(f"Numero totale di operazioni : {cc_founded.conta_depositi() + cc_founded.conta_prelievi()}")
                        print("\n\n")

                    case 10:
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
                    case 11: 
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

                        print ("SALDO DOPO tentativo diaddebito automatico:  \n\n")
                        print(cc_founded.__str__())
                    case _:
                        print("USCITA DAL SOFTWARE")
                        pass
            except ValueError:    
                print("Il numero del conto deve essere un numero positivo\n \n")
except ValueError:    
    print("Il numero del conto deve essere un numero positivo \n \n")