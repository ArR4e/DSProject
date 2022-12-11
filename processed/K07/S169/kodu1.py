def poisse_ja_tüdrukuid(list):
    poisid = 0
    tüdrukud = 0
    for a in list:
        if a[-1] == "P":
            poisid += 1
        else:
            tüdrukud += 1
    x = (poisid,tüdrukud)
    return x
            
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])