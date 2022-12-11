def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
    for rida in järjend:
        uus_järjend = rida.split(" ")
        sugu = uus_järjend[-1]
        if sugu == "P":
            poiste_arv += 1
        elif sugu == "T":
            tüdrukute_arv += 1
        else:
            poiste_arv = 0
            tüdrukute_arv = 0
    return(poiste_arv, tüdrukute_arv)

print(poiste_arv, tüdrukute_arv)