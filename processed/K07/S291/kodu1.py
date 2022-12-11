def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    poiste_tüdrukute_arv = []
    for sõne in järjend:
        uus_järjend = sõne.split()
        if uus_järjend[-1] == "P":
            poiste_arv += 1
        else:
            tüdrukute_arv += 1
    poiste_tüdrukute_arv.append(poiste_arv)
    poiste_tüdrukute_arv.append(tüdrukute_arv)
    ennik = (poiste_tüdrukute_arv[0], poiste_tüdrukute_arv[1])
    return ennik
        
    
järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']