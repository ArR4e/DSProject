def poisse_ja_tüdrukuid(slist):
    poisse = 0
    tüdrukuid = 0
    for el in slist:
        if el[-1] == "P":
            poisse += 1
        elif el[-1] == "T":
            tüdrukuid += 1
    return poisse, tüdrukuid

