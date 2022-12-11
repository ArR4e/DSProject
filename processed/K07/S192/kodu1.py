def poisse_ja_tüdrukuid(järjend):
    p = 0
    t = 0
    for rida in järjend:
        if ' P' in rida:
            p += 1
        if ' T' in rida:
            t += 1
    return(p, t)
x = poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
print(x)