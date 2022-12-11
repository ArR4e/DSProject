# Poiste ja tüdrukute arv

def poisse_ja_tüdrukuid(nimed):
    P = 0
    T = 0
    for i in nimed:
        if i[-1] == "P":
            P += 1
        elif i[-1] == "T":
            T += 1
    return (P, T)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))