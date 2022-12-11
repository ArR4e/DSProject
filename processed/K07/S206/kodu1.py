def poisse_ja_tüdrukuid(järjend):
    poisse= 0
    tüdrukuid= 0
    for nimi in järjend:
        if nimi[-1] == "P":
            poisse += 1
        elif nimi[-1] == "T":
            tüdrukuid += 1
    return (poisse, tüdrukuid)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati ', 'Siim Aleksander P', 'Jüri P', 'Veronika ']))