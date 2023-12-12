#pāra un nepāra skaitļu saskiatīšana
ievadeSaraksts = input('Ievadiet vismaz 10 elmentus(starp viņiem liekat atstarpi): ')
lietSaraksts = ievadeSaraksts.split() #saraksta izveide
print('Saraksts: ', lietSaraksts)
paraSk = []
neparaSk = []

def find(lietSaraksts):
    if lietSaraksts%2 == 0:
        numTips = 'Pāra'
    else:
        numTips = 'Nepāra'

'''for i in range(lietSaraksts) :
    if i%2 == 0:
        paraSk.append(i)
    else:
        neparaSk.append(i)

print(paraSk, '/n', neparaSk)'''