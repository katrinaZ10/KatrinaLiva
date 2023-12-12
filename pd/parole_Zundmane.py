password = 'pieci'
vards = 'kamielis'

lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
parole = input('Lūdzu, ievadiet savu paroli:')
beigas = 'stop'
trys = 1
#while trys<6:
if lietotajs == vards and parole ==password: #ja gan lietotāj vārds ir pariez un arī parole sāk jautāt paar skaitļu ievadi. Programma turipnās
    print('Pieslēgšanās veiksmīga!')
    pirmais = int(input('Ievadiet 1. veselo skaitli: '))
    otrais = int(input('Ievadiet 2. veselo skaitli: '))
    summa = 0
    while pirmais <= otrais: #pirmā u otrā skaitļa apreiķinu sākums
        summa = summa+pirmais
        pirmais= pirmais+1
        print('Veselu secīgi pieaugošu skaitļu no ',pirmais,'līdz ', otrais,'summa ir:',summa)
        if pirmais or otrais <0:
            print('Skaitļi nevar būt negatīvi!')
else: #nepareizas paroles ievade
    print('Nepareiza ievade.')
    while trys <= 5:
        print('Jums ir vēl 5 meiģinājumi') #garais ceļš pieldīt šo uzdevumu
        lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        parole = input('Lūdzu, ievadiet savu paroli:')

        print('Jums ir vēl 4 meiģinājumi')
        lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        parole = input('Lūdzu, ievadiet savu paroli:')

        print('Jums ir vēl 3 meiģinājumi')
        lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        parole = input('Lūdzu, ievadiet savu paroli:')

        print('Jums ir vēl 2 meiģinājumi')
        lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        parole = input('Lūdzu, ievadiet savu paroli:')

        print('Jums ir vēl 1 meiģinājums')
        lietotajs = input('Lūdzu, ievadiet savu lietotājvārdu:')
        parole = input('Lūdzu, ievadiet savu paroli:')
        
        print('Jums neizdevās pieslēgties.')
        break
    #elif beigas == 'stop':
        print('Programmas beigas!')
        exit()
