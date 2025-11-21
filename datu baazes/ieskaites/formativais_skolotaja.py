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
        FOREIGN KEY (sportisti_id) REFERENCES sportisti(sportisti_id) ON DELETE CASCADE
    )
""") #ilgums minūtēs

#papild funkcijas datu pārbaude(lai nav tukss teksts, lai ir skaitlis un lai eksistē id)
#neļauj atstāt tukšu lauku pie tekasta ievades
def ievadi_tekstu(teksts):
    while True:
        ievade = input(teksts).strip()
        if ievade == "":
            print('Kļūda: nevar būt tukšs!')
        else:
            return ievade

#ja nav ievadīts vesles skaitlis pie vecums, ilgumms, id, tad prasīt vēlreiz
def ievadi_skaitli(teksts):
    while True:
        try:
            skaitlis = int(input(teksts))
            return skaitlis
        except ValueError:
            print('Kļūda: jāievada vesels skaitlis!')

#pārbauda, vai eksistā sportista_id
def id_parbaude(sportisti_id):
    cursor.execute("""
            SELECT COUNT(*) FROM sportisti WHERE sportisti_id = ?
            """, (sportisti_id,))
    return cursor.fetchone()[0]>0
'''
#sportistu pievienošana (5 ieraksti)
sportistu_skaits = 0
while sportistu_skaits <5: #max atļautais sportistu skaits ir 5
    vards = ievadi_tekstu('Ievadi sportista vārdu: ')
    uzvards = ievadi_tekstu('Ievadi sportista uzvārdu: ')
    vecums = ievadi_skaitli('Ievadi sportista vecumu: ')

    cursor.execute("""
                INSERT INTO sportisti (vards, uzvards, vecums) 
                VALUES (?,?,?)""", (vards, uzvards, vecums))
    savienojums.commit()

    sportistu_skaits +=1
    print('Sportists pievientos!\n')

nodarbibu_skaits = 0
while nodarbibu_skaits <=5:
    while True:
        sportisti_id = ievadi_skaitli('Ievadiet sportista ID: ')

        if id_parbaude(sportisti_id):
            break
        else:
            print('Kļūda: tāda sportista ID nav!')

    veids = ievadi_tekstu('Ievadiet nodarbības veidu: ')
    ilgums = ievadi_skaitli('Ievadiet nodarbības ilgumu: ')

    cursor.execute("""
                INSERT INTO nodarbibas (sportisti_id, veids, ilgums)
                VALUES (?,?,?)""", (sportisti_id, veids, ilgums))
    savienojums.commit()

    nodarbibu_skaits +=1
    print('Nodarbība pievienota!\n')'''

#vaicājumi
#parādīt katra sportista kopīgo nodarbību skaitu
print('\nSportistu kopējais nodarbību skaits:')
cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, COUNT(nodarbibas.nodarbibas_id) AS 'Skaits'
    FROM sportisti
    LEFT JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    GROUP BY sportisti.sportisti_id""") #left join jo atgriezīs arī ja sportistam nav neviena nodarbība
for rinda in cursor.fetchall():
    print(f"{rinda[0]} {rinda[1]} - nodarbībus skaits: {rinda[2]}")

#parādīt itkai sportistus kuri trenējušis >120min
print('\nSportisti kuru treniņu ilgums > 120 min')
cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, SUM(nodarbibas.ilgums) AS kopa_min
    FROM sportisti
    JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    GROUP BY sportisti.sportisti_id
    HAVING kopa_min > 120""")
for rinda in cursor.fetchall():
    print(f"{rinda[0]} {rinda[1]} - nodarbību kopējais ilgums: {rinda[2]}")

print('\nTOP 3 sportisti: ')
cursor.execute("""
    SELECT sportisti.vards, sportisti.uzvards, SUM(nodarbibas.ilgums) AS kopa_min
    FROM sportisti
    LEFT JOIN nodarbibas ON nodarbibas.sportisti_id = sportisti.sportisti_id
    GROUP BY sportisti.sportisti_id
    ORDER BY kopa_min DESC
    LIMIT 3""")


for rinda in cursor.fetchall():
    print(f" {rinda[0]} {rinda[1]} - nodarbību kopējais ilgums: {rinda[2]}")


