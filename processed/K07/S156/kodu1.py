def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for i in range(len(järjend)):
        #print(len(järjend))
        if järjend [i][-1] == "P":
            poisse += 1
        elif järjend [i][-1] == "T":
            tüdrukuid += 1
    return(poisse, tüdrukuid)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
