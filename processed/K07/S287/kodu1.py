def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for f in järjend:
        if f[len(f)-1] == "T":
            tüdrukuid += 1
        elif f[len(f)-1] == "P":
            poisse += 1
        else:
            print("error")
    return(poisse, tüdrukuid)
            
#poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
