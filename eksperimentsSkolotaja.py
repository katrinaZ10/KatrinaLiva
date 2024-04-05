from datetime import datetime

iziesana = ['stop', 'exit', 'iziesana'] #pārbaudes tiek ieliktas sarakstā

def pareizsVards(vards):
    simboli = []# tukšs saraksts, kur saglabās burtus
    for i in vards:
        simboli.append(i) #iziet cauri katram simbolam 'vards' un pievieno to sarakstam
    fiksets = "" #šeit glabā pārveidoto/pareizo vārdu
    while True:
        if " " in simboli:
            simboli.remove(" ") #noņem nevajadzīgā atstarpes
        else:
            break
        #pārliecinās, ka pirmais burts ir lielais
    simboli[0]=simboli[0].upper()
    for i in simboli:
        fiksets= fiksets+i
    return fiksets #atgriež virkni ar lielo burtu un bez atstarpēm
    
''' vards= vards.replace(" ","")
vards = vards.capitalize() #nomaina pirmo burt uz lielo'''

def iegutDatus(): #šī ir funkcija kas iegūs datus no lietotāja(nosaukumu, vards, laiks), un pārbauda iziešanu
    nosaukums = input('Ievadiet eksperimenta nosaukumu: ')
    if nosaukums in iziesana:
        print('Lai jums jauka diena!')
        exit() #iziet, ja nosaukums ir sarakstā 'iziesana'
        
        
    laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vards = input('Ievadiet savu vārdu: ')
    if vards in iziesana:
        print('Lai jums jauka diena!')
        exit()
    
    vieta = input('Ievadiet eksperimenta vietu: ')
    if vieta in iziesana:
        print('Lai jums jauka diena!')
        exit() 
        
    return[nosaukums, laiks, pareizsVards(vards), vieta]

def saglabatDatus(dati):
    pilns = f"\nVārds: {dati[2]}-eksperiments:{dati[0]}-Vieta: {dati[3]}-Laiks:{dati[1]}" #indeksi no retur[...]
    file = open("eksperimenta_Dati.txt", "a", encoding="utf8")
    file.write(pilns)
    file.close()
    
def galvena():
    print('Sveicināti eksperimenta progammā! \n- - - - -')
    while True: #nodrošina atkārtošanos
        saglabatDatus(iegutDatus())
        while True:
            izvele = input('Vai vēlaties turpināt? (j/n) ').lower()
            if izvele == 'n':
                print('Uzredzēšanos! ')
                exit()
            elif izvele not in ['j', 'n']: #jāievada vēlreiz
                print('Nepareiz ievade!')
            else:
                break

galvena()

