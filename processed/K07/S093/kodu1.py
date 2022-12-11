def poisse_ja_tüdrukuid(järjend):
    tüdrukud = 0
    poisid = 0
    for i in järjend:
        järjend_1 = i.split(' ')
        if 'T' in järjend_1:
            tüdrukud += 1
        elif 'P' in järjend_1:
            poisid += 1
        else:
            poisid +=  0
            tüdrukud += 0
        return(poisid, tüdrukud)
    
järjend = (['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])

