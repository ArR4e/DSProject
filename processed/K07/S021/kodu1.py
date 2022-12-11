def poisse_ja_tüdrukuid(järjend):
    p=0
    t=0
    for sõne in järjend:
        sugu = sõne[-1]
        if sugu == "P":
            p += 1
            continue
        elif sugu == "T":
            t += 1
            continue
    return(p, t)  
poisse_ja_tüdrukuid(["Mati P", "Kati T", "Siim Aleksander P", "Jüri P", "Veronika T"])