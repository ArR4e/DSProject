def poisse_ja_tüdrukuid(järjend):
    
    poisse = 0
    tüdrukuid = 0
    
    for i in järjend:
        PvT = i[len(i) - 1] #võtab alati sõne viimase tähe, kus on sugu P või T
        if PvT == "P":
            poisse += 1
        elif PvT == "T":
            tüdrukuid += 1
            
    if poisse == 0 and tüdrukuid == 0:
        return (0, 0)
    else:
        return (poisse, tüdrukuid)
    
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))