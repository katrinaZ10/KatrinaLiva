import sqlite3
savienojums = sqlite3.connect('katriina_sports.db')

cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sportisti(
        sportisti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nodarbibas(
        nodarbibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sportisti_id INTEGER NOT NULL,
        veids TEXT NOT NULL,
        ilgums INTEGER NOT NULL,
        FOREIGN KEY (sportisti_id) REFERENCES sportisti(sportisti_id)
    )
""") #ilgums minūtēs

def ievade_jn(teksts): #funkciju lieto lai pārbaudītu lietotāja ievadi uz turpināt jautājumu
    while True:
        atbilde = input(teksts).lower()
        if atbilde in ['j', 'n']:
            return atbilde
        print("Ievadi tikai 'j' vai 'n'!")

def tuksa_ievade(teksts): #funkciju lieto, lai pārbaudītu vai lietotājs nav atstājis tukšu
    while True:
        ievade = input(teksts).lower()
        if ievade != "":
            return ievade
        print('Nav ievade veikta!')


while True: #sportistu pievienošana
    print('--Pievienot sportistu:')
    vards = tuksa_ievade('Ievadiet vārdu: ')
    uzvards = tuksa_ievade('Ievadiet uzvārdu: ')

    while True:
        try:
            vecums = int(tuksa_ievade('Ievadiet vecumu: '))
            if vecums > 0:
                break
            else:
                print('Ievadiet pozitīvu skaitli!')
        except ValueError:
            print("Ievadiet skaitli!")

    cursor.execute(""" 
        INSERT INTO sportisti(vards,uzvards, vecums) VALUES (?,?,?)""",
        (vards,uzvards, vecums))
    savienojums.commit()
    print('Pakalpojums pievienots!')

    turpinat = ievade_jn('Vai pievienot vēl vienu sportistu?(j/n): '. lower())
    if turpinat == 'n':
        break


print('Sportists pievienots!')

while True: #nodarbības pievinošana

    print('\n--Pieveinot nodarbību:')
    while True:#sportistu id atkārtoti
        try:
            sportisti_id = tuksa_ievade('\nIevadiet sportista ID: ')
            #pārbaudīt, vai sportista id tabulā eksistē
            cursor.execute("SELECT COUNT(*) FROM sportisti WHERE sportisti_id = ?", (sportisti_id,))
            if cursor.fetchone()[0] > 0:
                break #id pareizs - turpina
            else:
                print('\nSportists ar šādu ID neeksistē!')
        except ValueError:
            print('\nIevadiet skaitli, jo ID ir cipars!')

    veids = tuksa_ievade('Ievadiet veidu: ')
    while True: #ilguma ievades pārbaude
        try:
            ilgums = int(tuksa_ievade('Ievadiet ilgumu: '))
            if ilgums>0:
                break
            else:
                print('Ievadiet pozitīvu skaitli!')
        except ValueError:
            print('Ievadiet skaitli!')

    cursor.execute(""" 
        INSERT INTO nodarbibas(sportisti_id,veids, ilgums) VALUES (?,?,?)""",
        (sportisti_id,veids, ilgums))
    savienojums.commit()
    print('Pakalpojums pievienots!')

    turpinat = tuksa_ievade('Vai pievienot vēl vienu nodarbību?(j/n): '. lower())
    if turpinat == 'n':
        break


#vaicājumi
print('\nSportistu kopējais treniņu skaits:')
cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, COUNT(nodarbibas.nodarbibas_id) AS 'Skaits'
    FROM sportisti
    JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    GROUP BY sportisti.sportisti_id""")
for rinda in cursor.fetchall():
    print(rinda)


#parādīt itkai sportistus kuri trenējušis >120min
print('\nSportisti kuru treniņu ilgums >120 min')
cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, nodarbibas.ilgums
    FROM sportisti
    JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    WHERE nodarbibas.ilgums >120""")
for rinda in cursor.fetchall():
    print(rinda)

print('\nTOP 3 sportisti: ')
'''cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, COUNT(nodarbibas.ilgums)
    FROM sportisti
    JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    WHERE nodarbibas.ilgums = SELECT(MAX(ilgums) FROM nodarbibas)""")
for i in range(4):
    for rinda in cursor.fetchall():
        print(i,'. ' ,rinda)'''

