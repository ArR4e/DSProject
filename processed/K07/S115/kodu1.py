def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for i in järjend:
        uus_järjend = i.split(" ")
        for i in uus_järjend:
            if i == "P":
                poiste_arv += 1
            elif i == "T":
                tüdrukute_arv += 1         
    return (poiste_arv, tüdrukute_arv)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))