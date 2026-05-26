import models.conto_corrente as cc
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
    while op != 6:
        op=int(input("Seleziona l'operazione che vuoi effettuare \n" \
        "1. Per depositare \n" \
        "2. Per prelevare \n" \
        "3. Per mostrare il saldo \n" \
        "4. Per mostrare i movimenti \n" \
        "5. Per creare altri conti \n"  \
        "6. Per uscire\n"))
        match op:
            case 1:
                s=int(input("Inserire la somma da depositare: "))
                cc1.deposita(s)
            case 2:
                p=int(input("Inserire la somma da prelevare: "))
                cc1.preleva(p)
            case 3:
                cc1.mostra_saldo()
            case 4:
                cc1.mostra_movimenti()
                numDepositi=cc1.conta_depositi()
                numPrelievi=cc1.conta_prelievi()
                print("Numero depositi:", numDepositi)
                print("Numero prelievi:", numPrelievi)
            case 5:
                numero=int(input("Inserire numero di conti da creare: "))
                list_cc=[]
                for x in range(numero):
                    ni=str(input("Inserire il nome intestatario: "))
                    nc=int(input("Inserire il numero conto: "))
                    di=float(input("Inserire il deposito iniziale: "))
                    conto_c=cc.ContoCorrente(ni, nc)
                    conto_c.deposita(di)
                    conto_c.mostra_riepilogo()
                    list_cc.append(conto_c)
                break
            case _:
                pass