def poisse_ja_tüdrukuid(järjend):
    poiste_count = 0
    tüdrukute_count = 0
    for rida in järjend:
        if rida[-1] == "P":
            poiste_count += 1
        elif rida[-1] == "T":
            tüdrukute_count += 1
        else:
            poiste_count = 0
            tüdrukute_count = 0
    return(poiste_count, tüdrukute_count)
