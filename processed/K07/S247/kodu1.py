# kirj funktsioon, argumendiks järjend
# funktsioon peab tagastama 2elemdiga enniku
# 1 element P ar, 2element T arv
#for tsükkel

def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for el in järjend:
        uus_järjend = el[-1]
        for täht in uus_järjend:
            if täht == "P":
                m += 1
            else:
                n += 1
    return (m, n)

inimesed = poisse_ja_tüdrukuid(["Mati P", "Kati T", "Siim Aleksander P", "Jüri P", "Veronika T"])
print(inimesed)



