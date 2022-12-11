def poisse_ja_tüdrukuid(l):
    poisid = 0
    tüdrukud = 0
    for m in range(len(l)):
        if l[m][-1].lower() == "p":
            poisid += 1
        elif l[m][-1].lower() == "t":
            tüdrukud += 1
    return poisid,tüdrukud

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))