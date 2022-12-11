def poisse_ja_tüdrukuid(järjend):
    m = 0
    n = 0
    for i in järjend:
        if i.count(' P') != 0:
            m += 1
        elif i.count(' T') != 0:
            n += 1
    sugu = (m, n)
    return(sugu)

poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])