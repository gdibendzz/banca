import models.conto_corrente as cc
import utils.file_utils as fu
import utils.method_utils as mu



numeroc=mu.generatore_numero_conto()
cc1=cc.ContoCorrente("Gianmarco Di Benedetto", next(numeroc))
cc2=cc.ContoCorrente("Alberto Rossi", next(numeroc))
d={
    f"{cc1.numeroConto}": cc1,
    f"{cc2.numeroConto}": cc2
}
num=int(input("Inserire il numero conto da cercare: "))
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
        pin = int(input("Inserire il pin del conto: "))
        if pin == cc_founded.pin:
            
            break
        
        else:
            print(f"Hai ancora  {3 - i} tentativi")
            i += 1


    if(i == 4):
        print("Conto bloccato")
        cc_founded.blocca_conto()
        

    while op != 8 and not cc_founded.bloccato:
        op=int(input("Seleziona l'operazione che vuoi effettuare \n" \
        "1. Per depositare \n" \
        "2. Per prelevare \n" \
        "3. Per mostrare il saldo \n" \
        "4. Per mostrare i movimenti \n" \
        "5. Per creare altri conti \n"  \
        "6. Per cercare i movimenti \n"  \
        "7. Salva i movimenti \n"  \
        "8. Per uscire\n"))
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
                    ni=str(input("Inserire il nome intestatario: "))
                    nc=int(input("Inserire il numero conto: "))
                    di=float(input("Inserire il deposito iniziale: "))
                    conto_c=cc.ContoCorrente(ni, nc)
                    fu.write(conto_c.__str__(), f"{conto_c.numeroConto}.txt", "a")
                    conto_c.deposita(di)
                    conto_c.mostra_riepilogo()
                    list_cc.append(conto_c)
                break
            case 6:
                search = input("Inserire la parola chiave: ")
                mov_list = cc_founded.findByWord(search)

                if(len(mov_list) == 0):
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
            case _:
                pass