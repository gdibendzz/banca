import utils.account_utils as au


def find_by_numero(list, num):
    list = [x for x in list if x["numero_conto"] == num]
    return None if len(list) == 0 else list[0]

def main():
    account_list = []

    op = 0


    while op != 4:
        try:
            op = int(
                input(
                    "\nSeleziona l'operazione che vuoi effettuare \n"
                    "1. Crea Conto \n"
                    "2. Lista Conti \n"
                    "3. Accedi \n"
                    "4. Esci\n"
                )
            )
            
            if op < 0:
                raise ValueError
            
            match op:

                case 1:
                    try:
                        ni = str(input("\nInserire il nome intestatario: "))
                        nc = int(input("Inserire il numero conto: "))
                        if nc < 0:
                            raise ValueError
                        c = find_by_numero(account_list, nc)
                        if c is None:
                            new_c = {
                                "intestatario": ni,
                                "numero_conto": nc,
                                "saldo": 0,
                                "movimenti": [],
                            }
                            account_list.append(new_c)
                            print("Conto creato con successo!")
                        else:
                            print("Numero conto già esistente")
                    except ValueError:
                        print("Il numero del conto deve essere un numero positivo \n \n")
                case 2:
                    if len(account_list) == 0:
                        print("Nessun conto creato")
                    else:
                        for c in account_list:
                            au.mostra_conto(c)
                case 3:
                    try:
                        nc = int(input("Inserire il numero conto: "))
                        if nc < 0:
                            raise ValueError
                        c = find_by_numero(account_list, nc)
                        if c is None:
                            print("Conto non esistente")
                        else:
                            op1 = 0
                            while op1 != 5:
                                try:
                                    op1 = int(
                                        input(
                                            "\nSeleziona l'operazione che vuoi effettuare \n"
                                            "1. Per depositare \n"
                                            "2. Per prelevare \n"
                                            "3. Per mostrare il saldo \n"
                                            "4. Per mostrare i movimenti \n"
                                            "5. Per uscire\n"
                                        )
                                    )
                                    if op1 < 0:
                                        raise ValueError
                                    match op1:
                                        case 1:
                                            try:
                                                importo = int(
                                                    input(
                                                        "Inserire in valore da depositare: "
                                                    )
                                                )
                                                au.deposita(c, importo)
                                            except ValueError as e:
                                                print(e)
                                        case 2:
                                            try:
                                                importo = int(
                                                    input(
                                                        "Inserire in valore da prelevare: "
                                                    )
                                                )
                                                au.preleva(c, importo)
                                            except ValueError as e:
                                                print(e)          
                                        case 3:
                                            print(f"Saldo disponibile: {c["saldo"]}€")                       
                                        case 4:
                                            au.mostra_movimenti(c)
                                        case _:
                                            pass

                                except ValueError:
                                    print("Inserire un intero")
                    except ValueError:
                        print("Il numero del conto deve essere un numero positivo \n \n")
                case _:
                    pass

        except ValueError:
            print("Inserire un intero")

if __name__ == "__main__":
    main()


