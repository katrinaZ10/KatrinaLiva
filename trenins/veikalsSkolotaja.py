stop = '0'
ceks = 'Iepirkšanās čeks:' #izveidots lai nebūtu katru reizi jāraksta teksts
summaBezAtlaides = 0.0
kopsumma = 0.0 #galējā summa

while stop == '0':
    ceks

    precuSkaits = int(input("Ievadiet preču skaitu:"))
    if precuSkaits < 0: #ja mazāk par 0, tad iziet
        exit()
    produkts = input("Ievadiet preces nosaukumu:")
    produktaCena = round(float(input("Ievadiet cenu 1. gab. cenu:")), 2)

    #atlaides var izvēlēties, ierakstot skaitli no 1-5
    print("\n\t1.-Maxima: 30% atlaide\n\t2-Elvi:40%, ja ir klienta karte\n\t3-Rimi: 20%, ja ir klienta karte\n\t4-Mego: 30%, ja pērk 3 un vairāk preces \n\t5-Aibe: katra 2.prece par brīvu.")
    atlaidesVeids = input("Izvēlieties kurā veikalā iepirksieties: (rakstiet ciparu no 1-5)")

    cenaBezAtlaides = produktaCena*precuSkaits#iegūst cenu bez atlaidēm
    pirkumaCena = cenaBezAtlaides #no pirkumaCenas reiķinās atlaides

    #sākas atlaižu apreiķināšana
    if atlaidesVeids == '1': #atlaide maximā
        #pirkumaCena = pirkumaCena*0.7
        pirkumaCena*=0.7 #izmanto salikto operatoru

    elif atlaidesVeids == '2':#atlaide Elvi
        klietnaKarte= input("Ievadiet 1, ja ir klienta karte, 0, ja nav")
        if klietnaKarte == '1':
            pirkumaCena*=0.6 #atlaide 40%

    elif atlaidesVeids == '3': #rimi atlaide
        klietnaKarte = input("Ievadiet 1, ja ir klienta karte, 0, ja nav")
        if klietnaKarte == '1':
            pirkumaCena*=0.5
        else:
            pirkumaCena*=0.8

    elif atlaidesVeids == '4':
        if precuSkaits >=3:
            pirkumaCena*=0.7

    elif atlaidesVeids == '5':
        if precuSkaits%2 == 0:
            pirkumaCena/=2
        else:
            #atņem 1 gabala cenu no kopējās cenas
            pirkumaCena -= produktaCena
            pirkumaCena/=2
            pirkumaCena+= produktaCena

    cenaBezAtlaides = round(cenaBezAtlaides,2)
    pirkumaCena = round(pirkumaCena,2) #noappaļo ar 2 cipariem aiz komata

    summaBezAtlaides+= cenaBezAtlaides #iegūst summu
    kopsumma+=pirkumaCena

    ceks+= produkts+ '\n' +str(produktaCena)+' X '+ str(precuSkaits)+ '\t'+str(cenaBezAtlaides)+ '\nAr atlaidi:'+ '\t'+str(pirkumaCena)
    stop = input("Viss nopirkts? Jā-1, nē-0")
ceks += '\n-------------------------------------'
ceks += f'\nKopā bez atlaides(EUR):\t\t{summaBezAtlaides}\nKopā ar atlaidēm(EUR):\t\t{kopsumma}\n\n'

print(ceks)