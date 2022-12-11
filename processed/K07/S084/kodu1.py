def poisse_ja_tüdrukuid(andmed):
    poisse = 0
    tüdrukuid = 0
    for nimi in andmed:
        if nimi[len(nimi)-1] == "P":
            poisse += 1
        else:
            tüdrukuid += 1
    return (poisse, tüdrukuid)
#print(poisse_ja_tüdrukuid(["Mati P", "Kati T", "Teet Tuut P", "Jüri P", "Veronika T"]))