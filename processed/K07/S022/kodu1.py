def poisse_ja_tüdrukuid(järjend):
    tüdrukud = 0
    poisid = 0
    for el in järjend:
        if el[-1] == 'P':
            poisid += 1
        if el[-1] == "T":
            tüdrukud = tüdrukud + 1
    arv = (poisid, tüdrukud)
    return arv
    
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])