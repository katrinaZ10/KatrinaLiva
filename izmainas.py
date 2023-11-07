saraksts = [2, 4, 6, 8, 10, 12, 14, 16]
saraksts.append('Cepums') #pievieno saraksta beigās
print(saraksts)

#izmet no beigām
saraksts.pop()
print(saraksts)

saraksts.insert(3,'Hello')#ievieto  3. no kreisās
print(saraksts)

saraksts.remove(4) #izmet norādīto vērību
print(saraksts)

#funkcijas del(delete) pielietojumns
tests = [1, 2, 3, 4, 5, 6, 7, 8]
del tests[3] #izdzēš vienu elementu
print(tests)

del tests[3:6]
print(tests)#izdzēš intervālu

cipari = [1, 2, 3, 4, 5, 6, 7, 8]
del cipari[2:7:2] #no 2-7 dzēš ārā katru otro
print(cipari)


