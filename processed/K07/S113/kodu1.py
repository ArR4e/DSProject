def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for rida in järjend:
        if rida[-1] == "P":
            poisse += 1
        if rida[-1] == "T":
            tüdrukuid += 1
        
    return (poisse, tüdrukuid)