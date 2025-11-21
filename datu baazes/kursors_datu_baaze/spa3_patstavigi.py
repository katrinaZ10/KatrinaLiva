#pieslēgties esošjai datubāzei(5 ieraksti) IR
#jāuraksta programma, kur ietotājs var izvēlētites opcijas no 0 - 5
#katra opcija atgriež vaicājuma rezultātus, bet 0 - iziet no programmas
#nevar ievadīt neko citu kā 0-5
#1 - visi klienti
#2 - visi pakalpojumi
#3- visi pieraksti(ar klientu vārdu un pakalpojuma nosaukumu)
#4 - tuvāko 7 dienu pieraksti
#5- lietotājs norāda cenu. Parādīt pakalpojumus, kas ir dārgāki par norādīto cenu 
import sqlite3
from datetime import datetime

savienojums = sqlite3.connect('spa_sistema.db')
cursor = savienojums.cursor()

print('Laipni lūgti Siguldas SPA!')
while True:
    print('\nDarbības izvēlne:\n0 - iziet no programmas\n1 - Visi klienti\n2 - Visi pieejamie pakalpojumi\n3 - Visi pieraksti\n4 - Tuvākie pieraksti\n5 - Minimālā cenas ievade')

    liet_izvele = int(input('\nIevadiet savu izvēli (0-5): '))
    try:
        if liet_izvele == 0:
            print('\nTiekamies nākošreiz!')
            exit()

        elif liet_izvele == 1:
            print('\nVisi SPA klienti: ')

            cursor.execute("""SELECT*FROM klienti
            ORDER BY klienti.uzvards ASC""")
            #for rinda in cursor.fetchall():
            #    print(rinda)

            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]} : {rinda[1]}  {rinda[2]}, Telefona nr: {rinda[3]}")
            else:
                print('Datubāzē nav klientu!')
                
        elif liet_izvele == 2:
            print('\nVisi pieejamie pakalpojumi: ')

            cursor.execute("SELECT*FROM pakalpojumi")
            #for rinda in cursor.fetchall():
                #print(rinda)
            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]} : {rinda[1]},  {rinda[2]}H, {rinda[3]} EUR")
            else:
                print('Datubāzē nav pakalpojumu!')


        elif liet_izvele == 3:
            print('\nVisi SPA pieraksti: ')

            cursor.execute(""" 
                SELECT pieraksti.pieraksts_id,
                    klienti.vards ||' '|| klienti.uzvards AS klients,
                    pakalpojumi.nosaukums AS Pakalpojums,
                    pakalpojumi.cena,
                    pieraksti.datums          
                FROM pieraksti
                JOIN klienti ON pieraksti.klients_id=klienti.klients_id
                JOIN pakalpojumi ON pieraksti.pakalpojumi_id=pakalpojumi.pakalpojumi_id
                ORDER BY pieraksti.datums ASC
                """)
            dati=cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]} : {rinda[1]}, Pakalpojums: {rinda[2]} {rinda[3]} EUR, {rinda[4]}")
            else:
                print("Datubāzē nav klientu!")        
            

        elif liet_izvele == 4:
            print('\nTuvākie pieraksti nedēļas laikā: ')
            cursor.execute("""
            SELECT klienti.vards ||' '|| klienti.uzvards AS Klients,
                pakalpojumi.nosaukums AS Pakalpojums,
                pieraksti.datums
            FROM pieraksti
                JOIN klienti ON pieraksti.klients_id = klienti.klients_id
                JOIN pakalpojumi ON pieraksti.pakalpojumi_id = pakalpojumi.pakalpojumi_id
                WHERE pieraksti.datums BETWEEN date('now') AND date('now', '+7 days')
                ORDER BY pieraksti.datums ASC""")
            dati=cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"Vārds {rinda[0]}, {rinda[1]}, {rinda[2]}")
            else:
                print("Datubāzē nav klientu!") 

        elif liet_izvele == 5:
            print('\nMinimālās cenas uzstādīšana: ')
            while True:
                try:
                    liet_min = float(input('Ievadiet minimālo vērtību: '))
                    if liet_min <=0:
                        print('Ievadiet pareizi!')
                        continue
                    break
                except ValueError:
                    print('Lūdzu, ievadiet skaitli!')

            cursor.execute("""
            SELECT pakalpojumi.nosaukums, pakalpojumi.ilgums, pakalpojumi.cena
            FROM pakalpojumi
            WHERE pakalpojumi.cena > ?
            ORDER BY pakalpojumi.cena DESC""", (liet_min,))
            dati=cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID: {rinda[0]} - {rinda[1]}H, {rinda[2]}EUR")
            else:
                print("Datubāzē nav klientu!") 

        else:
            print('Jāievada skaitlis no 0 līdz 5!')
    except ValueError:
        print('Jāievada sakitlis!')




