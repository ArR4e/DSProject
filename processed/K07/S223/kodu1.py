def poisse_ja_tüdrukuid(jada):
    poisse = 0
    tüdrukuid = 0
    for x in jada:
        if x[-1] == "P":
            poisse += 1
        elif x[-1] == "T":
            tüdrukuid += 1
    return (poisse, tüdrukuid)