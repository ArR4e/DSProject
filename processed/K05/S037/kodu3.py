def moos(suuri_karpe, väikeseid_karpe, moosi_kogus):
    arv = 0
    while 0 < moosi_kogus >= 5 and suuri_karpe > 0:
        moosi_kogus >= 5
        moosi_kogus -= 5
        suuri_karpe -= 1
        arv += 1
    while  moosi_kogus > 0 and väikeseid_karpe > 0:
        moosi_kogus -= 1
        väikeseid_karpe -= 1
        arv += 1
    while moosi_kogus > 0 and väikeseid_karpe == 0:
        arv = -1
        break
    
    return arv