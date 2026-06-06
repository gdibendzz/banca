def deposita(conto, importo):
    if importo < 0:
        raise ValueError("Impossibile depositare importi negativi")
  
    conto["saldo"] += importo

    mov = {
        "tipo": "DEPOSITO", 
        "importo": importo, 
        "descrizione": "Versamento Contanti"
           }
    
    conto["movimenti"].append(mov)

def preleva(conto, importo):
    if importo < 0:
        raise ValueError("Impossibile prelevare importi negativi")
    
    if conto["saldo"] - importo < 0:
         raise ValueError("Saldo insufficiente")
    
    conto["saldo"] -= importo

    mov = {
        "tipo": "PRELIEVO", 
        "importo": importo, 
        "descrizione": "Prelievo Contanti"
           }
    
    conto["movimenti"].append(mov)

def mostra_movimenti(cc):
        if len(cc["movimenti"]) > 0:
            print(f"Lista movimenti di {cc["numero_conto"]} - {cc["intestatario"]}")
            for m in cc["movimenti"]:
                print(f"{m["tipo"]}  - {m["importo"]}€ - {m["descrizione"]}")
        else:
            print("Nessun movimento da visualizzare")

def mostra_conto(cc):
            print(f"Intestatario: {cc["intestatario"]}; Numero conto: {cc["numero_conto"]}; Saldo: {cc["saldo"]}")


