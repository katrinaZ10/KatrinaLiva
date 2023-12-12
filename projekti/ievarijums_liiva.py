#ziemas krājumu veidošana
cukursSumma = 0
udensSumma = 0
citronsSumma = 0
mandeluEks = 0
kanelis = 0

pluss = input("Vai jūsu mazbērnu sauc Marmelāde? ja/ne?")
if pluss == 'ja':
    print("Šī ir diemžēl ievārījumu ģimene, jūs ar savu mazmeitu Marmelādi varat doties meklēt citu recepti.")
    exit()
elif pluss == 'ne':
    aboli = int(input("Cik daudz ir ābolu? (raksti kilogramos)"))
    if aboli <2:
        print("Vajag vairāk ābolus.")
        exit() #programma beidzās ar pārāk maz āboliem
    elif aboli >3:
        print("Vai jums mājās ir viss vajadzīgais?")
        list = print('3kg Aboli', "\n1kg Cukurs", "\n500ml Udens", "\n1gab Citrons", "\n5ml Mandelu ekstraksts", "\n10g Kanēlis")
        atb = input("Ja/ne? Raksti šeit: ")
    if atb == 'ne':
        print("Šīs ir cenas receptes sastāvdaļām 'Rimi' veikalā:") #cenas ir piemērotas Vienai ievārijumu receptei
        print('1. Cukurs: 1,35 €', '\n2. Ūdens: 0,58€', '\n3. Citrons (vajadzīgs būs tikai viens): 0,90 € /gab', '\n4. Mandeļu ekstraksts: 2,55 € /l', '\n5. Kanēlis: 0,39€')
        produkti = input('Lūdzu ieraksti atbilstošo skaili kas tev trūksts:')
        if produkti == '1':
            cukurs = int(input('Cik daudz paciņas cukura jums vajadzēs?(Ievadi skaitli)')) #int, jo savādāk nereizinā ar float (1,35)
            cukursSumma = cukurs*1.35
            print('Par cukuru jāmaksā: ', cukursSumma)
        elif produkti == '2':
            udens = int(input('Cik daudz porcijām ūdeni jums vajadzēs?'))
            udensSumma = udens*0.58
            print('Par ūdeni jāmaksā: ', udensSumma)
        elif produkti == '3':
            citrons = int(input('Cik daudz citroni jums trūkst?'))
            citronsSumma = citrons*0.9
            print('Kopā par citroniem jāmaksā: ', citronsSumma)


    elif atb == 'ja':
      print('Jūs varat iet gatavot savu ābolu ievārījumu') 
