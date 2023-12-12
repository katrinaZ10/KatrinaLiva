'''atbilde = 'j'
while atbilde =='j':
    print("Nekusties!")
    atbilde = input("Vai breismonis ir draudzīgs?(j/n)")
print("Bēdz prom!")'''

#pārbaudīt vai lietotājs prot reizināt ar 7
#pragramma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi

reiz = int(input("Ievadi reizinātāju:"))
for i in range(1,13):#cikla mainīgais no 1-12
    print("Cik ir", i, "x", reiz, "?")
    minejums = input()
    if minejums == 'stop':#apstādina programmu, ja lietotājs ievada stop
        break
    if minejums == 'izlaist':
        print("Tiek izlaists")
        continue #izlaiž vienu jautājumu
    atbilde = i * reiz
    if atbilde == int(minejums):
        print("Pareizi!")
    else:
        print("Nē tas ir", atbilde)
        #ja ir nepareizi, tad atrgriežas pie jautājuma
        #if minejums
