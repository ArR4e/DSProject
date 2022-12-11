def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for rida in järjend:
        rida = rida[-1]
        if rida == "P":
            poiste_arv = poiste_arv + 1
        elif rida == "T":
            tüdrukute_arv = tüdrukute_arv + 1
            
    return(poiste_arv, tüdrukute_arv)