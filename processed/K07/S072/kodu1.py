def poisse_ja_tüdrukuid(sisend):
    poisse = 0
    tüdrukuid = 0
    
    for inimene in sisend:
        if inimene[-1] == 'P':
            poisse += 1
        else:
            tüdrukuid += 1
            
    return (poisse, tüdrukuid)

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))