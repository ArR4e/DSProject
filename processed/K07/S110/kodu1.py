def poisse_ja_tüdrukuid(järjend):
    poisse = 0
    tüdrukuid = 0
    for rida in järjend:
        uus = rida.split(' ')
        if 'P' in uus:
            poisse += 1
        if 'T' in uus:
            tüdrukuid += 1    
    return(poisse,tüdrukuid)
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])