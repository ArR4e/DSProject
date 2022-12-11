def poisse_ja_tüdrukuid(nimi):
    poiss = 0
    tudruk = 0
    for i in nimi:
        if i[-1] == "P":
            poiss +=1
        else:
            tudruk +=1
            
    arv = (poiss, tudruk)
    return arv

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))