nimed = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']

def poisse_ja_tüdrukuid (x):
    poisid = 0
    tüdrukud = 0
    for inimene in x:
        sugu = inimene[-1]
        if sugu == "P":
            poisid += 1
        elif sugu == "T":
            tüdrukud += 1
    return (poisid, tüdrukud)

print(poisse_ja_tüdrukuid (nimed))