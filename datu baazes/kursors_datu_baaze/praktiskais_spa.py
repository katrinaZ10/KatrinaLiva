import sqlite3
savienojums = sqlite3.connect('spa_sistema.db')

cursor = savienojums.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS klienti(
        klientI_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        pakalpojums_id TEXT NOT NULL,
        datums TEXT NOT NULL,
        FOREIGN KEY (klients_id) REFERENCES klienti(klienti_id),
        FOREIGN KEY (pakalpojums_id) REFERENCES pakalpojumi(pakalpojumi_id)
    )
""")

print('Dautbāze un tabulas izveidotas!')
'''
print('--Pievienot klientu:')
vards = input('Ievadiet vārdu: ')
uzvards = input('Ievadiet uzvārdu: ')
telefons = input('Ievadiet telefona numuru: ')

cursor.execute("""
    INSERT INTO klienti(vards, uzvards, telefons) VALUES (?,?,?)""",
    (vards, uzvards, telefons))
savienojums.commit()
print('Klients pievienots!')

#tabula pakalpojumi
print('\n--Pieveinot pakalpojumu:')
nosaukums = input('Ievadiet  nosaukumu: ')
ilgums = int(input('Ievadiet ilgumu: '))
cena = float(input('Ievadiet cenu: '))

cursor.execute("""
    INSERT INTO pakalpojumi(nosaukums, ilgums, cena) VALUES (?,?,?)""",
    (nosaukums, ilgums, cena))
savienojums.commit()
print('Pakalpojums pieveinots!')

print('\n--Pievienot pierakstu:')
klients_id = int(input('Ievadiet  klienta ID: '))
pakalpojums_id = int(input('Ievadiet pakalpojuma ID: '))
datums = input('Ievadiet datumu piraksta (YYYY-MM-DD): ')

cursor.execute("""
    INSERT INTO pieraksti (klients_id, pakalpojums_id, datums) VALUES (?,?,?)""",
    (klients_id, pakalpojums_id, datums))
savienojums.commit()
print('Pieraksts pievienots!')'''

#parāfīt tabulā esošos datus
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



