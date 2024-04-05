import datetime 
iziet = ['stop', 'beigt', 'iziet', 'exit']#veido saraktu, lai lietotājs var ievadīt jebkuru no vārdiem un programma apstāsies
def iegutDatus(): #funkcija iegūs datus no lietotāja
    while True:
        global nosaukums, laiks, vards, vieta
        
        nosaukums = input('Eksperimenta nosaukums: ')
        laiks = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vards = input('Eksperimenta vadītājs: ')
        vieta = input('Eksperimenta vieta: ')    
        beigt = input('Vai jūs vēlaties turpināt? (j/n)')
        
        '''if nosaukums or vards or vieta == iziet:
            print('Uzredzēšanos! \nLai jums jauka diena! :).')
            break
        else:
            ()'''
            
        if beigt == 'n': 
            print('Uzredzēšanos! \nLai jums jauka diena! :)')
            break
        elif beigt == 'j':
            ()
            
def saglabatDatus(): #funkcija saglabās datus eksperimentaDati.txt failā
    try:
        print()             
        with open("eksperimentaDati.txt", "a", encoding='utf8') as fails:
            fails.write(f"Nosaukums - {nosaukums} : Vārds - {vards} : Vieta - {vieta} : Laiks - {laiks}\n")
    except FileNotFoundError:
        print('Fails neeksitē')
        
def galvenais():
    print('Laipni lūgti eksmperimenta programmā!', '\n- - - - -')
    iegutDatus()
    saglabatDatus()

galvenais()