def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for rida in järjend:
        if rida[-1] == "P":
            poisse += 1
        elif rida[-1] == "T":
            tüdrukuid += 1
        else:
            poisse = 0
            tüdrukuid = 0
    järjend2 = [poisse, tüdrukuid]
    return(tuple(järjend2))
poisse_ja_tüdrukuid(['Mati P', 'Siim Aleksander P', 'Jüri P'])
poisse_ja_tüdrukuid(['Kati T', 'Veronika T'])
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
poisse_ja_tüdrukuid([])