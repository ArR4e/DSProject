def poisse_ja_tüdrukuid(järjend):
    P = 0
    T = 0
    for inimene in järjend:
        if inimene[-1] == "P":
            P += 1
        elif inimene[-1] == "T":
            T += 1
    return (P, T)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))