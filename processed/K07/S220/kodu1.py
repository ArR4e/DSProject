def poisse_ja_tüdrukuid(a: list):
    T =0
    P = 0
    for i in a :
        täht = i.split(" ")[-1]
        if täht == "P":
            P += 1
        elif täht == "T":
            T += 1
    return(P,T)
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))   