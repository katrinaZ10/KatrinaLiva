augumi = {  'vards' : [], 'garums' : []}
augumi['vards'] = ['Elizabete','Adriāns','Ance','Maija','Amanda','Paula','Renārs','Uldis','Ernests','Karlīna','Elvis','Zigfrīds']
augumi['garums'] = [172, 185, 164, 184, 162, 164, 165, 167, 177, 184, 165, 180]

while True:
    print('Šie ir šobrīdējie dati:', '\n',augumi)
    parsteigums = int(input('Cik jūs esat garš? (cm)'))
    if parsteigums <= 200: #pārsteigum, papildus jautājums
        print('😭😭😭TU ESI ĪSĀKS PAR KAMIELI😭😭😭')
    else:
        print('🐪🐪🐪🐪🐪Tu esi kamielis🐪🐪🐪🐪🐪')
    beigt = input('Vai jūs vēlaties beigt? (ja/ne) ')
    if beigt == 'ja':
        exit()
    else:
        ()   
     
    lietotajs= input('Vai jūs vēlētos pievienot datus? (ja/ne)')
    if lietotajs == 'ja':
        print('Lūdzu, ievadiet jauno informāciju: ') #ļauj lietotājam ievadīt jaunu informāciju, kas tiek pielikta pie 'augumi'
        jaunsVards = input('Ievadiet vārdu: ')
        jaunsGarums = input('Ievadiet garums: ')
        augumi['vards'].append(jaunsVards) #ieliek jauno kontakta atslēgu
        augumi['garums'].append (jaunsGarums) #ieliek jauno kontakta numuru
        print(augumi)
        print('Jūs pievienojāt: ', jaunsVards, jaunsGarums)
        #print('Jūs pievienojāt ', augumi[jaunsVards],augumi[jaunsGarums])
    elif lietotajs == 'ne':
        ()
    
    dzest = input('Vai jūs vēlātos ko dzēst? (ja/ne) ')
    if dzest == 'ja':
        vards = input('Ievadi vārdu: ')
        index = augumi['vards'].index(vards)  #metode index paņem mainīgo name un atrod atbilstošo
        #remove metode nestrādās, jo izdzēsīs tikai vienu
        augumi['vards'].pop(index) #pop prasa konkrēto indeksu 
        augumi['garums'].pop(index)
        print('Jūs izdzēsāt: ', vards , index)
