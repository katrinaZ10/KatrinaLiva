import math
cilveki = input("Vai brauc vairāk nekā 4 cilvēki? (ja/ne)")
if cilveki == 'ja':
    print("Jūs nevarat braukt.")
elif cilveki == 'ne':
    #bonuss kamieļi!
    kamielis = input("Vai jūs plānojat pārvadāt kamieli/kamieļus? (ja/ne)")
    if kamielis == 'ja':
        print("Atvainojiet, bet jūs nevarat braukt.")
        exit()
    elif kamielis == 'ne':
        print("Super! Varēsiet braukt.") 
    pulkstens = int(input("Cik šobrīd ir pulkstens (lūdzu ievadīt veselu skaili)? ")) #jautā lai zinātu cik būs jāmaksā par kilometru, jo cenas atšķiras
    if pulkstens >6 and pulkstens<22:
        print("Jūsu tarifs būs 0,47€ par kilometru.")
        tarifsDienas = 0.47
    else: 
        print("Jūsu tarifs būs 0,87€ par kilometru.")
        tarifsNakts = 0.87
    
        #nolīgšana un izsaukšana
    noligt = input("Vai pie dzelzceļa autostāvientas ir firmas taksometra stāvieta? (ja/ne)")
    noligtCena = 2.40
    if noligt == 'ja': #šeit sāk pārbaudīt vai būs arī jāizsauc taksis vai tikai jānolīgst
        noligtTwo = input("Vai tur ir taksometrs stāvietā?(ja/ne)")
        if noligtTwo == 'ja':
            print("Jums nebūs jāmaksā izsaukšanas cena.")
        elif noligtTwo == 'ne':
            print("Papildus maksa par izsaukumu ir 2,40€.")
    elif noligt == 'ne':
        print("Papildus maksa par izsaukumu ir 2,40€.")
        #vai būs taksim jāgaida
    gaidit = input("Vai jūs vēlēsieties paceļam kautkur piestāt? (ja/ne)")
    gaiditCena = 0.15
    if gaidit == 'ne':
        print()
    elif gaidit == 'ja':
        gaiditTime = float(input("Cik ilgi jūs vajadzēs pagaidīt? (lūdzu, ievadiet veselu skaitli)"))
        gaiditSum = gaiditTime*gaiditCena
        print(gaiditSum)
        #ceļa apreiķini
    cels = int(input("Cik tālu jūs brauksiet?"))
    #čeks
    print("Jūsu čeks par šo braucienu.")
    print("Kopējā summa:", '\nGaidīšanas cena:', gaiditSum, "€")
    if pulkstens >6 and pulkstens<22:
        diena= print("Ceļa cena:",round(cels*tarifsDienas), "€")
    else:
       nakts= print("Ceļa cena:", cels*tarifsNakts, "€")
    if noligt == 'ja':
        jum =print("Papildus maksa par izsaukšanu:", noligtCena, "€")
    '''summa = gaiditSum+diena or nakts+ jum
    print("Kopējā summa:", summa )  '''