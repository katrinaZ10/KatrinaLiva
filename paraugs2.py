krasas = ['rozā', 'dzeltens', 'balts', 'zils' ]
jaunsSaraksts = []
for i in krasas:
    burti = 0
    for burts in i:
        burti +=1
    pagaiduSaraksts = [i, burti]
    jaunsSaraksts.append(pagaiduSaraksts)
print(jaunsSaraksts)

for krasa in krasas:
    print(len(krasa))#len atrod vārda garumu
    print(krasa,len(krasa))