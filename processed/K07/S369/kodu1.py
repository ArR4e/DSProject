def poisse_ja_tüdrukuid(inimesed):
    poisse = 0
    tydrukuid = 0
    
    for inimene in inimesed:
        if inimene[-1] == 'P':
            poisse +=1
        else:
            tydrukuid +=1
    return(poisse, tydrukuid)
    
poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander T', 'Jüri T', 'Veronika T'])