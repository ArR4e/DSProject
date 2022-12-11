# näiteks: a = (['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])

def poisse_ja_tüdrukuid(a):
    m = 0
    n = 0
    for el in a:
        nimi_ja_sugu = el.split(" ")
        sugu = nimi_ja_sugu[-1]
        if sugu == "P" :
            m += 1
        if sugu == "T" :
            n += 1
    return (m,n)