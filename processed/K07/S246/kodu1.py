def poisse_ja_tüdrukuid(nimed):
    tüdrukuid = 0
    poisse = 0
    for nimi in nimed:
        sugu = nimi[-1]
        if sugu == "P":
            poisse += 1
        else:
            tüdrukuid += 1
    return (poisse, tüdrukuid)