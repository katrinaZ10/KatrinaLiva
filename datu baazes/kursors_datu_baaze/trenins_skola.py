import sqlite3
savienojumus = sqlite3.connect('skola_trenins.db') #automātiski izveido ja tāda nav

#cursor objekts
cursor = savienojumus.cursor()
cursor.execute('DROP TABLE IF EXISTS skoleni') #lia teksts dati nedublētos

#izveidot tabulu skolēni ar kollonām id, vards, vecums
cursor.execute("""
    CREATE TABLE IF NOT EXISTS skoleni(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")

cursor.execute('INSERT INTO skoleni(vards, vecums) VALUES (?,?)', ('Amanda', 24))
cursor.execute('INSERT INTO skoleni(vards, vecums) VALUES (?,?)', ('Tommijs',16))
cursor.execute('INSERT INTO skoleni(vards, vecums) VALUES (?,?)', ('Uvis',20))

savienojumus.commit() #ievieto datus datubāzē

print('Visi skolēni:')
cursor.execute('SELECT*FROM skoleni')
#print(cursor.fetchall()) #parāda nesmuki
visi = cursor.fetchall()

for i in visi:
    print(f"ID: {i[0]} | Vārds {i[1]} | Vecums: {i[2]}")

print('\nSkolēni, kas jaunāki par 18:')
cursor.execute('SELECT*FROM skoleni WHERE vecums < 18')
jaunie = cursor.fetchall()
for i in jaunie:
    print(f"{i[1]} ({i[2]} gadi)")


print('\nVecākais skolēns:')
cursor.execute('SELECT*FROM skoleni ORDER BY vecums DESC LIMIT 1')
vecakais = cursor.fetchone()
print(f"Vārds: {vecakais[1]} ({vecakais[2]} gadi)")

#saskaitīt skolēnus kuri jaunāki par 17 gadiem
cursor.execute('SELECT COUNT(*) FROM skoleni WHERE vecums < 18')
rez = cursor.fetchone()[0] #jo vajag vienu konkrētu vērtību
print(f"\nJaunāki par 18 gadiem: {rez}")

