def poisse_ja_tüdrukuid (järjend):
    poistearv = 0
    tüdrukutearv = 0
    
    for inimene in järjend:
        if inimene[len (inimene) - 1] == "P":
            poistearv += 1
        
        else:
            tüdrukutearv += 1
    
    return (poistearv, tüdrukutearv)

print (poisse_ja_tüdrukuid (['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))