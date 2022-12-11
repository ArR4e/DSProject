def poisse_ja_tüdrukuid(eesnimi_ja_sugu):
    poiste_arv = 0
    tüdrukute_arv = 0
    for element in eesnimi_ja_sugu:
        if element[-1] == "P":
            poiste_arv += 1
        else:
            tüdrukute_arv += 1
    return poiste_arv, tüdrukute_arv