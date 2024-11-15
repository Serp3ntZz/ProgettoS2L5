import datetime 
def assistente_virtuale(comando):    
    if comando == "1":        
        oggi = datetime.datetime.today()          
        risposta = "\nLa data di oggi è " + oggi.strftime("%d/%m/%Y\n")    
    elif comando == "2":        
        ora_attuale = datetime.datetime.now().time()          
        risposta = "\nL'ora attuale è " + ora_attuale.strftime("%H:%M\n")    
    elif comando == "3":        
        risposta = "\nMi chiamo Assistente Virtuale\n"         
    return risposta 
while True:    
    print("Cosa vuoi sapere? ") 
    print("1. Qual è la data di Oggi?")
    print("2. Che ore sono?")
    print("3. Come ti chiami?")
    print("Per uscire digita 'esci' ")
    comando_utente = input("Cosa vuoi sapere? (inserisci un numero da 1 a 3): ") 
    if comando_utente.lower() == "esci":        
        print("\nArrivederci!")        
        break    
    elif comando_utente == "1" or comando_utente == "2" or comando_utente == "3":        
        print(assistente_virtuale(comando_utente)) 
    else:
        print("\nInserisci un numero da 1 a 3 oppure digita 'esci'\n")
