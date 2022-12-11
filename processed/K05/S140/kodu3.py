from math import floor

def suur_karp(suur, kogus):
    suhe = kogus / 5
    #suhe näitab mitu suur karpi läheks vaja
    if suur < suhe:
        suhe = suur
    #ei saa kasutada rohkem karpe, kui antud on
    return floor(suhe)
    #floor näitab, mitu tervet karpi ära kasutatakse
    
def moos(suur, väike, kogus):
    uus_kogus = kogus - 5 * suur_karp(suur, kogus)
    #uus_kogus näitab mitu väikest karpi on vaja
    if uus_kogus <= väike:
        väike = uus_kogus
        #kui väikseid karpe on piisavalt, siis võetakse
        #kasutusele nii palju kui vaja
    else:
        return -1
    #kui väikseid karpe pole piisavalt,
    #ei saa nii palju moosi keeta
    return suur_karp(suur, kogus) + väike
