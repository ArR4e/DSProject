def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for i in järjend:
        sisend = i.split(' ')[-1]
        if sisend == "P":
            m += 1
        elif sisend == "T":
            n += 1
    return(m, n)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))