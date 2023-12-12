temperaturas = {'Datums' : [], 'Gradi' : []} #veidota vārdnīca, lai varētu piekļūt temeratūrām vieglāk
temperaturas['Datums'] = ['1.decembris', '2.decembris', '3.decembris', '4.decembris', '5.decembris', '6.decembris', '7.decembris']
temperaturas['Gradi'] = [-6, -2, 7, 3,-2,-5,6]

while True:
    lietotajs = input('Ievadiet datumu (piemēram "1.decembris"): ')
    print(lietotajs, 'temperatūra Celsija skalā ir: ', temperaturas[lietotajs], '\n*****') #parāda cik būs celsija skalā
    print(lietotajs, 'tempretūra Fārenheita skalā ir:', temperaturas[lietotajs]*(9/5)+32) #parāda cik būs fārenheita skalā

    skaititajs = 1
    
    while lietotajs != temperaturas['Datums']:
        skaititajs =+1
        print(lietotajs, 'temperatūra Celsija skalā ir: ', temperaturas[lietotajs], '\n*****') #parādi cik būs celsija skalā
        print(lietotajs, 'tempretūra Fārenheita skalā ir:', temperaturas[lietotajs]*(9/5)+32) #parāda cik būs fārenheita skalā
        lietotajs = input('Nepareiz atslēga. Lūdzu ievadiet datumu no 1. līdz 7.decembrim')
        
    if skaititajs == 3:
        print('Nepareiz iformācija. Jums vairs nav piekļuves.')
        exit()
    