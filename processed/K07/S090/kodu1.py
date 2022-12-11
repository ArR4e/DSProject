def poisse_ja_tüdrukuid(x):
    n = 0
    m = 0
    for el in x:
        if " P" in el:
            n += 1
        if " T" in el:
            m += 1
    return (n , m)
        
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))