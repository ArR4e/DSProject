def poisse_ja_tüdrukuid(a):
    poisse=0
    tüdrukuid=0
    for nimi in a:
        if nimi[-1] == "P":
            poisse += 1
        else:
            tüdrukuid+=1
    return(poisse, tüdrukuid)