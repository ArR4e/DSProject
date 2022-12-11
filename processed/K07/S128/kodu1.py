def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    for i in range(len(järjend)):
        sõne = järjend[i]
        if sõne[len(järjend[i])-1] == "P":
            poisid += 1
        elif sõne[len(järjend[i])-1] == "T":
            tüdrukud += 1
    ennik = (poisid, tüdrukud)
    return ennik
sisend = input("Sisesta järjend: ")
poisse_ja_tüdrukuid(sisend)