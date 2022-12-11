def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    i = 0
    for el in järjend:
        if järjend[i].endswith("P"):
            poisse += 1
            i += 1
        elif järjend[i].endswith("T"):
            tüdrukuid += 1
            i += 1
    
    return(poisse,tüdrukuid)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))