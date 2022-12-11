def poisse_ja_tüdrukuid(x):
    poisid = 0
    tüdrukud = 0
    for el in x:
        if el[-1] == 'T':
            tüdrukud += 1
        elif el[-1] == 'P':
            poisid += 1
    return (poisid, tüdrukud)

poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])