def  poisse_ja_tüdrukuid(nimekiri):
    poisse = 0
    tydrukuid = 0
    for nimi in nimekiri:
        if nimi[-1] == "P":
            poisse+= 1
        else:
            tydrukuid+= 1
    return (poisse, tydrukuid)