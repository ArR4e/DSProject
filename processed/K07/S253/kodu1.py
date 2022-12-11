def poisse_ja_tüdrukuid(jarjend):
    poiste_arv = 0
    tydrukute_arv = 0
    for i in jarjend:
        temp = i.split()
        if temp[-1] == "P":
            poiste_arv += 1
        else:
            tydrukute_arv += 1
    return poiste_arv, tydrukute_arv
        




print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
