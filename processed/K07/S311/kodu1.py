def poisse_ja_tüdrukuid(j):
    poisse = 0
    tüdrukuid = 0
    for i in j:
        u = i.split(" ")
        tüdrukuid += u.count("T")
        poisse += u.count("P")
    return (poisse , tüdrukuid)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))