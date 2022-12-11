def poisse_ja_tüdrukuid(järjend):
    p = 0
    t = 0
    for el in järjend:
        if el[-1] == "P":
            p += 1
        if el[-1] == "T":
            t += 1
    return (p, t)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))