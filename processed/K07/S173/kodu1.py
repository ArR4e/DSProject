nimed = ["", 'Mati P', 'Kati T', 'Siim Aleksander P',"" , 'Jüri P', 'Veronika T', ""]
tühi = []
kokku = tuple()
def poisse_ja_tüdrukuid(nimed):
    t = 0
    p = 0
    for i in nimed:
        if i == "":
            continue
        a = ((i.split())[-1])
        if a == "T":
            t += 1
        elif a == "P":
            p += 1
    return (p, t)
print(poisse_ja_tüdrukuid(nimed))