def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        el = el[-1]
        if el == "P":
            m += 1
        elif el == "T":
            n += 1
        else:
            return 0
    return (m,n)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati P', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
        