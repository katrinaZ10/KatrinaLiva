'''
-izvaidot 3 sarakstus: lietotājs pats norādīs, 
 cik elementu likt sarakstā
-pirmā un otrā saraksta vērtības ievada lietotājs
-trešā saraksta vērtības iegūst apvienojot pirmos divus
-katra saraksta saturu glīti parādīt uzz ekrāna.
'''
'''pirmaisSaraksts = []
otraisSaraksts = []

pirmais = int(input('Cik elementu būs 1. Sarakstā? '))

for i in range(pirmais) :
    pirmaisSarakstsDivi = input('Ievadiet 1. saraksta elemetus: ')
    pirmaisSaraksts.append(pirmaisSarakstsDivi)
    print('1. saraksts: ',pirmaisSaraksts)#varētu strādāt

otrais = int(input('Cik elementu būs 2. sarakstā?'))
for otraisSaraksts in range(otrais) :
    otraisSarakstsDivi = input('Ievadiet 2. saraksta elemetus: ')
    print('2. saraksts: ', otraisSarakstsDivi)

tresaisSaraksts = [pirmaisSarakstsDivi+otraisSarakstsDivi]
print('3. saraksts: ', tresaisSaraksts)'''


saraksts1 = []
saraksts2 = []
#pirmais saraksts
print('Ievadi saraksta garumu: ')
garums = int(input()) #lietotājs pats ievada saraksta garumu

for i in range(garums):
    lieta1 = input("Ievadiet saraksta elementu:")
    saraksts1.append(lieta1)
print("Pirmā saraksta elementi:",saraksts1)

print('Ievadi saraksta garumu: ')
garums2 = int(input()) #lietotājs pats ievada saraksta garumu
for j in range(garums2):
    lieta2 = input("Ievadiet saraksta elementu:")
    saraksts2.append(lieta2)
print("Pirmā saraksta elementi:",saraksts2)

jauns_saraksts = [saraksts1+saraksts2]
print(jauns_saraksts)