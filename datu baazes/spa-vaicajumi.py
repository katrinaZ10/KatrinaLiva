import sqlite3

#pieslēgties esošajai datubāzei
#jāuzraksta programma, kur lietotājs var izvēlēties ocpijas no 0-5
#katra opcija atgriež vaicājuma rezultātus,bet 0-iziet no programmas
#nevar ievadīt neko citu kā tikai 0-5
#1-visi klienti
#2-visi pakalpojumi
#3-visi pieraksti(ar klienta vārdu un pakalpojuma nos)
#4-tuvāko 7 dienu pieraksti
#5-lietotājs norāda cenu.parādīt pakalpojumus, kas ir dārgāki par norādīto cenu

savienojums = sqlite3.connect("spa_sistema.db")
cursor = savienojums.cursor()

while True: 
    izvele=int(input("Izvēlies no 0-5:"))
    if izvele<0 or izvele>5:
        print("Ievadi no 0-5")
    else:
        break
    
if izvele==1:
    print("Visi klienti: ")
    cursor.execute("""
        SELECT * FROM klienti
        ORDER BY klienti.uzvards ASC     
                    """)
    dati=cursor.fetchall()
    if dati:
        for rinda in dati:
            print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]},telefona nr.:{rinda[3]}")
    else:
        print("Datubāzē nav klientu!")
        
#uzd2 ir tāds pats kā uzd1
elif izvele==3:
    print("Klientu pieraksti: ")
    cursor.execute(""" 
        SELECT pieraksti.pieraksti_id,
               klienti.vards ||' '|| klienti.uzvards AS klients,
               pakalpojumi.nosaukums AS Pakalpojums,
               pakalpojumi.cena,
               pieraksti.datums          
        FROM pieraksti
        JOIN klienti ON pieraksti.klients_id=klienti.klienti_id
        JOIN pakalpojumi ON pieraksti.pakalpojums_id=pakalpojumi.pakalpojumi_id
        ORDER BY pieraksti.datums ASC
        """)
    dati=cursor.fetchall()
    if dati:
        for rinda in dati:
            print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]},{rinda[3]},{rinda[4]}")
    else:
        print("Datubāzē nav klientu!")        