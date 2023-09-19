import math
import random

radiuss = float(input('Ievadiet riņķa līnijas rādiusu:'))
print(radiuss)
RL = math.pi*2*radiuss #formula aprēķina rl garumu
print('Riņķa līnijas garums:',RL)
RLlaukums = math.pi*math.pow(radiuss,2) #formula apreiķina laukumu
print('Riņķa līnijas laukums:', RLlaukums)

katete1 = int(input('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:')) #sākās taisnleņķa trijstūra apreiķini
print(katete1)
katete2 = int(input('Ievadiet trijstūta otrās katetes garumu:'))
print(katete2)

h = math.pow(katete1,2)+math.pow(katete2,2) #apreiķina to kas būs ZEM kvadrātsaknes
h2 = math.sqrt(h) #paliek to kvādrātsaknē
print('Taisnleņķa trijstūra hipotenūzas garums:',h2, "%.2f"%h2) 

print("Gadījuma sakitlis no 0-1:", random.random()) # izvēlās random ciparu
