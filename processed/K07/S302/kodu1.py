def poisse_ja_tüdrukuid(jär):
    poiss = 0
    tydruk = 0
    ennik = ()
    for el in jär:
        if el[-1] == "P":
            poiss +=1
        else:
            tydruk +=1
    ennik =(poiss, tydruk)
    return ennik
    
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))