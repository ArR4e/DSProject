def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for rida in järjend:
        if rida == "":
            return (poiste_arv, tüdrukute_arv)
        else:
            nimi_ja_täht = rida
            nimi_ja_täht_järjend = list(nimi_ja_täht.split())
            täht = nimi_ja_täht_järjend[-1]
            if täht == "P":
                poiste_arv += 1
            else:
                tüdrukute_arv += 1
    return (poiste_arv, tüdrukute_arv)