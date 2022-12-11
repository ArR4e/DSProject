def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for rida in järjend:
        if rida[-1] == "T":
            tüdrukute_arv +=1
        if rida[-1] == "P":
            poiste_arv+=1
    return (poiste_arv, tüdrukute_arv)

            
        