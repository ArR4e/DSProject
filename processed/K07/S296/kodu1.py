def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for nimi in järjend:
        lahku = nimi.split()
        if lahku[-1] == 'P':
            m += 1
        if lahku[-1] == 'T':
            n += 1
    return(m,n)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
