def poisse_ja_tüdrukuid(järjend):
    poiste_arv = 0
    tüdrukute_arv = 0
    for x in järjend:
        if x[-1] == 'P':
            poiste_arv += 1
        if x[-1] == 'T':
            tüdrukute_arv += 1
        if poiste_arv == 0 and tüdrukute_arv == 0:
            return 0
    return(poiste_arv, tüdrukute_arv)
            
        
        
järjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
print(poisse_ja_tüdrukuid(järjend))