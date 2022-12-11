nimed = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid(nimed):
    t = 0
    p = 0
    for rida in nimed:
        elemendid = rida.split()
        for element in elemendid:
            if element == "P":
                p += 1
            if element == "T":
                t += 1
    arvud = (p, t)
    return arvud

print(poisse_ja_tüdrukuid(nimed))