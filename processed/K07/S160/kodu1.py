def poisid_ja_tydrukud(a, b, c, d ,e):
    isik = 0
    sugu = 0
    p = 0
    t = 0
    nimekiri = []
    for name in sõne:
        isik = name.split(" ")
        sugu = (isik[-1])
        
        if sugu == "P" :
            p += 1
            x = (p, t)
        elif sugu == "T" :
            t += 1
            x = (p, t)
    return (p,t)
        
sõne = 'Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'
print(poisid_ja_tydrukud('Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'))