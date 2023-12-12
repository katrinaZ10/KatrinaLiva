import math
#Andra Ziediņa maģiskā rēķināšana
rullaCena = float(input('Ievadiet linoleja cenu kvadrātmetrā :'))
rullaPlatums= float(input('Ievadiet ruļļa platumu metros :'))
telpa = float(input('Ievadiet telpas platumu kvadrātmetros :'))
paklajaCena = 0 #vajaga 0, jo ja negrib, lai var pieskaitīt

while True:


    parsteigums= input('Vai tev patīk kamieļi? (ja/ne)')
    if parsteigums == 'ja':
        print('Super! Vari turpināt.')
        linolejaDaudz = telpa*rullaPlatums
        linolejaDaudzMaksa = linolejaDaudz*rullaCena #šiet sāk maksas reiķinu lai pēctam būtu vieglāk
        print('Jums vajadzēs ', round(linolejaDaudz), 'kvadrātmerus linoleja', '\nTas izmaksās :', round(linolejaDaudzMaksa), '€') 
        izmontotLinolejs = float(input('Cik daudz linoleja tu izmantoji?'))
        atlikums= linolejaDaudz-izmontotLinolejs
        print('Tev palika pāri ', atlikums, 'kvadrātmetri linoleja.')
        
        paklajs = input('Vai jūsu klients grib paklāju? (ja/ne)')
        if paklajs == 'ja':
            
            paklajaCena = float(input('Cik maksā paklājs kvardātmetrā? '))
            paklajaSumma = paklajaCena*telpa
            print('Andrīt, tev paklājs izmaksās :',paklajaSumma, '€')   
        else:
            ()
    else:
        print('Uzredzēšanos, Andri!🐪🐪')
        break
    
    
    iziet = input('Vai tu vēlies turpināt rēķināt? (ja/ne) ')
    if iziet == 'ja':
        kopsumma = linolejaDaudzMaksa+paklajaSumma
        print('Super! Tava šobrīdēja kopsumma ir :', kopsumma, '€')
        print('-----------------------------------')
    elif iziet == 'ne':
        kopsumma = linolejaDaudzMaksa+paklajaSumma
        print('Kopsumma ir :', kopsumma, '€')
        print('Atā, Andrīt!')
        exit()
