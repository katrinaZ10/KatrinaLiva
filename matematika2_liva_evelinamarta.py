cipars = int(input('Ievadiet divciparu skaitli:'))
dviOtr = cipars%10
dviPir = cipars/10
print('Pirmais cipars:', end='')
print (int(dviPir))
print('Otrais cipars:', end='')
print(dviOtr)
print(int(dviPir) + int(dviOtr))