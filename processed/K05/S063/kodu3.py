'''Kirjuta funktsioon moos, mis võtab argumendiks kolm täisarvulist väärtust:

suurte karpide arvu;
väikeste karpide arvu;
keedetava moosi koguse kilogrammides.
Funktsioon tagastab karpide arvu, mida Emma moosi keetmiseks kasutab. 
Kui moosikogus antud karpidesse ei mahu, tagastab funktsioon arvu -1.'''

import math

def moos(suurte_arv, vaikeste_arv, kogus):
    karpi_kokku = 0
    ulejaanud_kogus = 0
    
    # arvutame, kas mahub suurtesse karpidesse
    
    suurte_karpide_arv = math.floor(kogus/5) # on vaja suurt karpi
    
    # kui suurt karpi on piisav arv
    if suurte_arv >= suurte_karpide_arv:
        karpi_kokku += suurte_karpide_arv # loendame need karbid
        ulejaanud_kogus = kogus%5 # mis on jäänud väikestesse karpidesse
    
    # kui suuri karpe ei ole piisavalt
    else:
        karpi_kokku += suurte_arv # loendame need, mis olemas
        ulejaanud_kogus = kogus - (suurte_arv*5) # mis on jäänud väikestesse karpidesse
    
    # arvutame, kas mahub väikestesse karpidesse
    
    # kui väikest karpi on piisav arv
    if vaikeste_arv >= ulejaanud_kogus:
        karpi_kokku += ulejaanud_kogus # loendame need karbid
    
    # kui väikest karpi ei ole piisav arv
    else:
        return -1
        
    return karpi_kokku