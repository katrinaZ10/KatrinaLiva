kontakti = {'vards' : [], 'numurs' : []}
kontakti['vards']= ['Alise','Pēterītis','Ēriks', 'Markuss']
kontakti['numurs'] ={'24546982','23469578','28445697','24777698'}

print('Ko vēlaties darīt?')
print('\t1-drukāt','\n\t2-Pievienot','\n\t3-izdzēst','\n\t4-iziet','\n\t5-pārsteigums')

while True:
    atbilde = int(input('Ievadiet skaitli: '))

    if atbilde == 1:
        print('Jūs ievadījāt 1, šie ir jūsu konakti: ', kontakti)

    if atbilde == 2:
        print('Jūs ievadījāt 2, pievienojiet jaunu konaktu')
        jaunsAtsl = input('Ievadiet vārdu: ')
        jaunsNum = input('Ievadiet numuru: ')
        kontakti['vards'].append(jaunsAtsl) #ieliek jauno kontakta atslēgu
        kontakti['numurs'].append (jaunsNum) #ieliek jauno kontakta numuru
        print(kontakti)
    '''if jaunsAtsl in kontakti:
        kontakti[jaunsAtsl] = jaunsNum
        print('Vārdnīca tika atjaunināta!')
    else:
        kontakti[jaunsAtsl] = jaunsNum
        print('Jauns kontakts tika pievienot vārdnīcai!')'''

    if atbilde == 3: #.remove
        print('Jūs ievadījāt 3, izdzēt konaktu')
        dzest = input('Kuru kontaktu jūs vēlaties izdzēst: ')
        

    if atbilde == 4:
        print('Jūs ievadījāt 4: Paldies, ka izmantojāt šo programmu!')
        exit()

    if atbilde == 5:
        print('🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪 KAMIEĻU BALLĪTE! 🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪🐪')