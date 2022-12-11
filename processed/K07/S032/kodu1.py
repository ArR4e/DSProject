def poisse_ja_tüdrukuid(nimed):
    p = 0
    t = 0
    for nimi in nimed:
        if nimi[-1] == 'P':
            p += 1
        elif nimi[-1] == 'T':
            t += 1
    return (p, t)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
#print(n, s)
