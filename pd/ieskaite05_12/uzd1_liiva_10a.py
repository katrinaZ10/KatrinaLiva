#garais vai īsais gads
gads = int(input('Ievadiet gadu: '))

if gads % 4 == 0: #dalot ar 4 ir jāsanāk 0, savādāk tas ir īsai gads
    if gads % 100 == 0: #dalot ar 100 ir jāsanāk 'evenly' 0, jo garie gadi daloteis
        if gads % 400 == 0: #tas pats kas dalot ar 100
            print(gads, 'ir garais gads.')
        else:
            print(gads, 'nav garais gads.')
    else: 
        print(gads, 'ir garais gads.')
else: 
    print(gads, 'nav garais gads.')
