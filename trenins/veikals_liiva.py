simts = 100
vards = input("Kā jūs sauc? (lūdzu rakstīt bez garumzīmēm)")


preces_daudzums = int(input("Cik daudz preces jūs plānojat iegādāties?"))

if preces_daudzums>0:   
    veikalu_nosaukumi = ["\nRimi", "\nMaxima", "\nElvi", "\nLidl", "\nCamelum"]
    atlaide_kur = input("Vai jūs iepieksieties kādā no minētajiem veikaliem? (ja/ne)")
    #"\nRimi", "\nMaxima", "\nElvi", "\nLidl", "\nCamelum"#kamieļii!!! un jautā lai varētu zināt par atlaidēm
    if atlaide_kur == 'ja': #šiet sākas atlaižu jautāšana
        jautajums = input("Kurā no veikaliem jūs plānojat iepirkties?(rakstīt bez garumzīmēm)")
        if jautajums == 'rimi': #rimi atlaides
            rimi_atlaide = 30
            print("Atlaide veikalā Rimi ir 30%")
            rimi_preces = input("Ko jūs pirksiet?(Raksti bez garumzimem)")
            rimi_preces_cena = input("Cik tas maksās?")
            rimi_summa = rimi_preces*simts/rimi_atlaide
            print(rimi_summa)
        if jautajums == 'maxima': #maxima atlaides
            maxima_atlaide = 40
            maxima_jautajums = input("Vai jūs maksāsiet ar karti?(ja/ne)")
            if maxima_jautajums == 'ja':
                print("Jūsu atlaide būs 40%")
            elif maxima_jautajums == 'ne':
                print("Jums,", vards, "diemžēl nebūs atlaide.")
        if jautajums == 'elvi': #elvi atlaides
            elvi_mazs = 20
            elvi_liels = 50
            elvi_jautajums = input("Vai jūs maksāsiet ar karti?(ja/ne)")
            if elvi_jautajums == 'ja':
                print("Jūsu atlaide būs 50%")
            elif elvi_jautajums == 'ne':
                print("Jūsu atlaide būs 20%")
        if jautajums == 'Lidl': #!!!
            lidl_mazs = 30
            if preces_daudzums>3:
                print("Jūsus atlaide būs 30%")
            elif preces_daudzums<3:
                print("Jums,", vards, "nebūs atlaide.")
        if jautajums == 'camelon': #!!!
            print() 
        elif atlaide_kur == 'ne':
         print("Jums,", vards, " diemžēl nebūs atlaide.")
elif preces_daudzums<0:
    print("Kļūda! Jūs,", vards, "nevarat iepirkties.")

for preces in range(preces_daudzums):
    print(preces)
    if preces_daudzums<0:
        print("Kļūda! Jūs,", vards, "nevarat iepirkties.")
