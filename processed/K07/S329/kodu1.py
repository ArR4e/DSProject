# 1. Poiste ja tüdrukute arv

def poisse_ja_tüdrukuid(järjend):
    tüdrukute_arv = 0
    poiste_arv = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        if 'T' in uus_järjend:
            tüdrukute_arv += 1
        elif 'P' in uus_järjend:
            poiste_arv += 1
        else:
            poiste_arv += 0
            tüdrukute_arv += 0
    return(poiste_arv, tüdrukute_arv)
            
        
    
järjend = ['Mati P', 'Kati T', ' ', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
poisse_ja_tüdrukuid(järjend)


