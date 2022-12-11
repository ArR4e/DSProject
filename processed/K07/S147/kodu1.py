def poisse_ja_tüdrukuid(järjend):
    Poisid,Tüdrukud = 0,0
    for i in järjend:
        if i[-1] == "P":
            Poisid += 1
        elif i[-1] == "T":
            Tüdrukud += 1
    return (Poisid, Tüdrukud)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))