def poisse_ja_tüdrukuid(a):
    poisid = 0
    tüdrukud = 0
    for el in a:
        täht = el.split()
        for t in täht:
            if t == "P":
                poisid += 1
            elif t == "T":
                tüdrukud += 1
    return (poisid, tüdrukud)

jrj = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

print(poisse_ja_tüdrukuid(jrj))
