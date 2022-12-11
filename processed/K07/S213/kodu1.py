def poisse_ja_tüdrukuid(jarjend):
    m = 0
    n = 0
    for x in jarjend:
        if " P" in x:
            m += 1
        elif " T" in x:
            n += 1
    return m, n

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))