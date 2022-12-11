def poisse_ja_tüdrukuid(lapsed):
    tüdruk = 0
    poiss = 0
    poiste_arv = []
    tüdrukute_arv = []
    
    for lapse_info in lapsed:
        lapse_info = lapsed.split(' ')
        sugu = lapse_info[1]
        for tüdruk in sugu:
            #count ei toimi siin, sest pole number, muud moodi vaja tuvastada mitu T või P on
            tüdruk = len(sugu[:'T'])
            tüdruk += 1
            tüdrukute_arv = tüdrukute_arv + [tüdruk]
        elif poiss in sugu:
            poiss = len(sugu[:'P'])
            poiss += 1
            poiste_arv = poiste_arv + [poiss]
    return (poiste_arv, tüdrukute_arv)
            #ei tea kuhu edasi joosta sellega, kõik tundub vale

    laste_arv = (poiste_arv, tüdrukute_arv)
    print(laste_arv)

poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
    
