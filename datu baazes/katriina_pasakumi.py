import sqlite3
from datetime import datetime
savienojums = sqlite3.connect('katriina_datubaze_pasakumi.db')

cursor = savienojums.cursor()

#tabulu izveide
#PASAKUMI
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pasakumi(
        pasakumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        datums TEXT NOT NULL,
        vieta TEXT NOT NULL
    )
""")
#DALIBNIEKI
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dalibnieki(
        dalibnieki_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")
#REGISTRACIJAS
cursor.execute("""
    CREATE TABLE IF NOT EXISTS registracijas(
        registracijas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pasakumi_id INTEGER NOT NULL,
        dalibnieki_id INTEGER NOT NULL,
        statuss TEXT NOT NULL,
        FOREIGN KEY (pasakumi_id) REFERENCES pasakumi(pasakumi_id) ON DELETE CASCADE,
        FOREIGN KEY (dalibnieki_id) REFERENCES dalibnieki(dalibnieki_id) ON DELETE CASCADE
    )
""") 

def skaitla_ievade(teksts): #funkcija pārbaudīs vai sakitļu ieraksti ir pareizi
    while True:
        try:
            skaitlis = int(input(teksts))
            return skaitlis
        except ValueError:
            print('Kļūda: jāievada vesels skaitlis!')
            
def id_pasakumi_parbaude(ievade): #fukcija pārbauda vai pasākumu ID eksistē
    cursor.execute("""
            SELECT COUNT(*) FROM pasakumi WHERE pasakumi_id = ?
            """, (ievade,))
    return cursor.fetchone()[0]>0

def id_dalibnieki_parbaude(ievade): #fukcija pārbauda vai dalībnieka ID eksistē
    cursor.execute("""
            SELECT COUNT(*) FROM dalibnieki WHERE dalibnieki_id = ?
            """, (ievade,))
    return cursor.fetchone()[0]>0


#ierakstu veikšana
while True: #Ieraksti pasākumiem
    pasakumu_sk = 0 #iestata uz 0, lai var veikt 2 ierakstus pēc prasīšanas
    print('\n--- Pasākumu pievienošana:')
    while pasakumu_sk <2:
        nosaukums = input('Pasākuma nosaukums: ')
        
        while True:
            datums = input('Pasākuma datums (YYYY-MM-DD): ')
            try: #pārbaude vai datums ir nākotnē, un vai ir pareizs formatējums
                datums_sdn = datetime.strptime(datums, "%Y-%m-%d").date()
                if datums_sdn<datetime.now().date():
                    print('Datums neavr būt pagātnē!')
                else:
                    break
            except ValueError:
                print('Nepareizs formāts! Izmanto YYYY-MM-DD') 

        vieta = input('Pasākuma atrašanās vieta: ')

        cursor.execute("""
                    INSERT INTO pasakumi (nosaukums, datums, vieta)
                    VALUES (?,?,?)""", (nosaukums, datums, vieta))
        savienojums.commit()#ievieto lietotāja doto informāciju datubāzē

        pasakumu_sk +=1
        print('Pasākums pievienots!\n')

    velreiz = input('\nVai vēlaties pievienot vēl pasākumus(ja/ne): ')
    if velreiz == 'ne':
        break
       
while True: #ieraskti dalibniekiem
    dalibnieku_sk = 0 #iestata uz 0, lai var veikt 2 ierakstus pēc prasīšanas
    print('\n--- Dalībnieka pievienošana:')
    while dalibnieku_sk <2:
        vards = input('Dalībnieka vārds: ')
        uzvards = input('Dalībnieka uzvārds: ') 
        vecums = skaitla_ievade('Dalībnieka vecums: ')

        cursor.execute("""
                    INSERT INTO dalibnieki (vards, uzvards, vecums)
                    VALUES (?,?,?)""", (vards, uzvards, vecums))
        savienojums.commit() #ievieto lietotāja doto informāciju datubāzē

        dalibnieku_sk +=1
        print('Dalībnieks pievienots!')

    velreiz = input('\nVai vēlaties pievienot vēl dalībniekus(ja/ne): ')
    if velreiz == 'ne':
        break

while True: #ieraskti reģistrācijām
    registraciju_sk = 0
    print('\n--- Reģistrācijas pievienošana:')
    while registraciju_sk <2:
        while True: #cikls ies līdz tiks pareizi ievadīts reģistrācijas ID
            pasakumi_id = input('Pasākuma ID: ')
            if id_pasakumi_parbaude(pasakumi_id): #ID pārbaude ar funkciju
                break
            else:
                print('Kļūda: ID neeksistē!')

        while True: #cikls ies līdz tiks pareizi ievadīts dalībnieka ID
            dalibnieki_id = input('Dalībnieka ID: ')
            if id_dalibnieki_parbaude(dalibnieki_id):#ID pārbaude ar funkciju
                    break
            else:
                print('Kļūda: ID neeksistē!')

        while True: #cikls beigsies pie pareizas ievades
            statuss = input('Reģistrācija statuss (Ja/Ne): ').lower()
            if statuss != 'ja' or 'ne':
                print('Neparaieza ievade!')
            else:
                break

        cursor.execute("""
                    INSERT INTO registracijas (pasakumi_id, dalibnieki_id, statuss)
                    VALUES (?,?,?)""", (pasakumi_id, dalibnieki_id, statuss))
        savienojums.commit()#ievieto lietotāja doto informāciju datubāzē

        registraciju_sk +=1
        print('Reģistrācija pievienota!')

    velreiz = input('\nVai vēlaties pievienot vēl dalībniekus(ja/ne): ')
    if velreiz == 'ne':
        break

#vaicājumi

print('\n--- Visi pasākumi:')
cursor.execute("""
            SELECT*FROM pasakumi""")
for rinda in cursor.fetchall():
    print(f"ID {rinda[0]}.  {rinda[1]} : {rinda[2]}")

print('\n--- Dalībnieki, kas vecāki par 17: ')
cursor.execute("""
            SELECT*FROM dalibnieki
            WHERE vecums >17""")
for rinda in cursor.fetchall():
    print(f"ID: {rinda[0]} - {rinda[1]} {rinda[2]} {rinda[3]}")      


print('\n--- Dalībnieku reģistrācija: ')
cursor.execute("""
        SELECT dalibnieki.vards, 
            dalibnieki.uzvards, 
            pasakumi.nosaukums
        FROM registracijas
        JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
        JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
        GROUP BY registracijas.dalibnieki_id""")
for rinda in cursor.fetchall():
    print(f"{rinda[0]} {rinda[1]}: {rinda[2]}") 


print('\n--- Dalībnieku skaits katrā pasākumā:')
for rinda in cursor.execute("""
    SELECT pasakumi.nosaukums,
        COUNT(registracijas.dalibnieki_id) AS Skaits
    FROM pasakumi
    LEFT JOIN registracijas ON pasakumi.pasakumi_id=registracijas.pasakumi_id
    GROUP BY pasakumi.pasakumi_id"""): #left join jo atgriezīs arī ja sportistam nav neviena nodarbība
    print(f"{rinda[0]} : {rinda[1]}")


print('\n--- Pasākumi kur ir pieteikušies vairāk par 3 cilvēkiem: ')
cursor.execute("""
        SELECT pasakumi.nosaukums,
            COUNT(registracijas.dalibnieki_id) AS Skaits
        FROM pasakumi 
        LEFT JOIN registracijas ON pasakumi.pasakumi_id=registracijas.pasakumi_id
        GROUP BY pasakumi.pasakumi_id
        HAVING Skaits >= 3""") #ja ieliktu >3 tad neiesaktītu pasākumus kur ir tiaki 3 dalbinieki

for rinda in cursor.fetchall():
    print(f"{rinda[0]} : {rinda[1]}")


print('\n--- Parādīt uz kuru pilsētu un kad brauc dalībnieks')
cursor.execute("""
            SELECT dalibnieki.vards,
                dalibnieki.uzvards,
                pasakumi.vieta,
                pasakumi.datums
            FROM registracijas
            JOIN pasakumi ON pasakumi.pasakumi_id = registracijas.pasakumi_id
            JOIN dalibnieki ON dalibnieki.dalibnieki_id = registracijas.dalibnieki_id
            GROUP BY dalibnieki.dalibnieki_id""")

for rinda in cursor.fetchall():
    print(f"{rinda[0]} {rinda[1]} brauc uz: {rinda[2]} {rinda[3]}")