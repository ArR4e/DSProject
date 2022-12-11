def poisse_ja_tüdrukuid(jär):
    p = 0
    t = 0
    for i in jär:
        n = len(i) - 1
        if i[n] == "P":
            p += 1
        else:
            t += 1
    return(p, t)
            
        
järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
poisse_ja_tüdrukuid(järjend)