def poisse_ja_tüdrukuid(nimed):
    poisid = 0
    tydrukud = 0
    for el in nimed:
        sugu = el[-1]
        if sugu == "P":
            poisid += 1
            continue
        if sugu == "T":
            tydrukud += 1
            continue
    return poisid, tydrukud
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])