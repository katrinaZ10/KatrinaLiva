#lietotājs ievada virkni
saraksts = []
lietotajs = int(input('Ievadiet skaitļu skaitu(ne mazāk kā 3): '))

while True:
    if lietotajs <= 2 or 0 : #neļauj ievadīt mazāk par 2 vai 0
        ievade = int(input('Ievadiet skaitļu skaitu(ne mazāk kā 3): '))

    for i in range(lietotajs): #jautā ievadīt saraksta elementus
        skaitli = int(input('Ievadiet skaitli '))
        saraksts.append(skaitli)
        
    print('Saraksts ar skaitļiem' ,saraksts)
    sarakstsKartots = saraksts.sort() #izmantoju lai atrastu lielāko vērtību
    #print('Lielākais ievadītais skaitlis: ', sarakstsKartots[-1])
    exit()    