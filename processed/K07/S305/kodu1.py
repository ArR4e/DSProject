def poisse_ja_tüdrukuid(a):
    p = 0
    t = 0
    for i in a:
        if i[-1] == "P":
            p += 1
        elif i[-1] == "T":
            t += 1
    return (p, t)
    
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))