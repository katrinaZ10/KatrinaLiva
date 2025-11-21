import sqlite3
from datetime import datetime

savienojums = sqlite3.connect('spa_sistema.db')
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klienti(
        klients_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        telefons TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pakalpojumi(
        pakalpojumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        ilgums INTREGER NOT NULL, --minūtēs
        cena REAL NOT NULL
    )
""")
#ilgums ir minūtēs

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pieraksti(
        pieraksts_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klients_id TEXT NOT NULL,
        pakalpojumi_id TEXT NOT NULL,
        datums TEXT NOT NULL,
        FOREIGN KEY (klients_id) REFERENCES klienti(klients_id),
        FOREIGN KEY (pakalpojumi_id) REFERENCES pakalpojumi(pakalpojumi_id)
    )
""")

print('Dautbāze un tabulas izveidotas!')

def ievade_jn(teksts): #funkciju lieto la pārbaudītu teksta ievadi
    while True:
        atbilde = input(teksts).lower()
        if atbilde in ['j', 'n']:
            return atbilde
        print("Ievadi tikai 'j' vai 'n'!")

while True: #KLIENTI
    print('--Pievienot klientu:')
    vards = input('Ievadiet vārdu: ')
    uzvards = input('Ievadiet uzvārdu: ')
    telefons = input('Ievadiet telefona numuru: ')

    cursor.execute("""
        INSERT INTO klienti(vards, uzvards, telefons) VALUES (?,?,?)""",
        (vards, uzvards, telefons))
    savienojums.commit()

    turpinat = ievade_jn('Vai pievienot vēl vienu klietu(j/n): '. lower())
    if turpinat == 'n':
        break
print('Klients pievienots!')

while True: #PAKALPOJUMI
    print('\n--Pieveinot pakalpojumu:')
    nosaukums = input('Ievadiet  nosaukumu: ')
    while True: #ILGUMA ievades pārbaude
        try:
            ilgums = int(input('Ievadiet ilgumu: '))
            if ilgums>0:
                break
            else:
                print('Ievadiet pozitīvu skaitli!')
        except ValueError:
            print('Ievadiet skaitli!')

    while True:
        try: #CENAS ievades pārbaude
            cena = float(input('Ievadiet cenu: '))
            if cena>0:
                break
            else:
                print('Ievadiet pozitīvu skaitli!')
        except ValueError:
            print('Ievadiet skaitli!')

    cursor.execute("""
        INSERT INTO pakalpojumi(nosaukums, ilgums, cena) VALUES (?,?,?)""",
        (nosaukums, ilgums, cena))
    savienojums.commit()
    print('Pakalpojums pievienots!')

    turpinat = ievade_jn('Vai pievienot vēl vienu pakalpojmu(j/n): '. lower())
    if turpinat == 'n':
        break

#pārbaudīt kādi klienti(un id) jau eksistē
while True:
    print('Pieajammie klienti: ')
    cursor.execute("SELECT klients_id, vards, uzvards FROM klienti")
    for klients in cursor.fetchall():
        print(f"ID: {klients[0]} - {klients[1]} - {klients[2]}")

    #klienta ievade ar ID pārvaudi
    while True:#KLIENTa id atkārtoti
        try:
            klients_id = input('\nIevadiet klienta ID: ')
            #pārbaudīt, vai klienta id tabulā eksistē
            cursor.execute("SELECT COUNT(*) FROM klienti WHERE klients_id = ?", (klients_id,)) #neaimirsir komateu 2trajās iekavās
            if cursor.fetchone()[0] > 0:
                break #id pareizs - turpina
            else:
                print('\nKients ar šādu ID neeksistē!')
        except ValueError:
            print('\nIevadiet sakitli, jo ID ir cipars!')

 #PAKALPOJUMI
    print('\nPieejamie pakalpojumi: ')
    cursor.execute("SELECT pakalpojumi_id, nosaukums, cena FROM pakalpojumi")
    for p in cursor.fetchall():
        print(f"ID - {p[0]} - {p[1]} - {p[2]} EUR")

    while True:  #līdz ievada pareizu pakalpojumu id
        try:
            pakalpojumi_id = input('\nIevadiet pakalpojuma ID: ')
            #pārbaudīt, vai klienta id tabulā eksistē
            cursor.execute("SELECT COUNT(*) FROM pakalpojumi WHERE pakalpojumi_id = ?", (pakalpojumi_id,)) #neaimirsir komateu 2trajās iekavās
            
            if cursor.fetchone()[0] > 0:
                break #id pareizs - turpina
            else:
                print('\nPakalpojums ar šādu ID neeksistē!')
        except ValueError:
            print('\nIevadiet sakitli, jo ID ir cipars!')

    #ja abi ir pariezi, tad jautā fatumu un ieraksta datus tabulā
    while True:
        datums_txt = input('Ievadi pieraksta datumu (YYYY-MM-DD): ')
        try:
            datums = datetime.strptime(datums_txt, "%Y-%m-%d").date()
            if datums<datetime.now().date():
                print('Datums neavr būt pagātnē!')
            else:
                break
        except ValueError:
            print('Nepareizs formāts! Izmanto YYYY-MM-DD')

    cursor.execute("""
        INSERT INTO pieraksti (klients_id, pakalpojumi_id, datums) VALUES (?, ?, ?)""",
        (klients_id, pakalpojumi_id, str(datums)))
    savienojums.commit()

    turpinat = ievade_jn('Vai pievienot vēl vienu pierakstu(j/n): '. lower())
    if turpinat == 'n':
        break

    
'''while True: #PIERAKSTI
    print('\n--Pievienot pierakstu:')
    klients_id = int(input('Ievadiet  klienta ID: '))
    pakalpojums_id = int(input('Ievadiet pakalpojuma ID: '))
    datums = input('Ievadiet datumu piraksta (YYYY-MM-DD): ')

    cursor.execute("""
        INSERT INTO pieraksti (klients_id, pakalpojums_id, datums) VALUES (?,?,?)""",
        (klients_id, pakalpojums_id, datums))
    savienojums.commit()
    print('Pieraksts pievienots!')

    turpinat = input('Vai pievienot vēl vienu pierakstu(j/n): '. lower())
    if turpinat != 'j':
        break'''


#parādīt tabulā esošos datus
print('\nVisi klienti: ')
cursor.execute("SELECT*FROM klienti")
for rinda in cursor.fetchall():
    print(rinda)

print('\nVisi pakalpojumi: ')
cursor.execute("SELECT*FROM pakalpojumi")
for rinda in cursor.fetchall():
    print(rinda)

print('\nVisi pieraksti: ')
cursor.execute("SELECT*FROM pieraksti")
for rinda in cursor.fetchall():
    print(rinda)



