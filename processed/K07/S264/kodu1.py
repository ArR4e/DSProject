
järjend = ["Mati P", "Kati T", "Siim Aleksander P", "Jüri P", "Veronika T"]


def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        pikkus = len(uus_järjend)
        for rida in uus_järjend:
            if rida == "P":
                poisse += 1
            elif rida == "T":
                tüdrukuid += 1
    arvud = (poisse, tüdrukuid)
    return arvud
print(poisse_ja_tüdrukuid(järjend))
