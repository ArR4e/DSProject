def poisse_ja_tüdrukuid(järjend):
    elementide_arv = len(järjend)
    if elementide_arv == 0:
        return (0, 0)
    tüdrukud = 0
    poisid = 0
    
    for nimi in järjend:
        if len(nimi) > 0:
            if nimi[-1] == "T":
                tüdrukud += 1
            else:
                poisid += 1
    return (poisid, tüdrukud) 

