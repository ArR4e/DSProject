from math import floor
def moos(suur_k, väike_k, kg):
    #kasutame kõigepealt suured karbid ära:
    max_5 = floor(kg / 5)
    karbid = 0
    for i in range(suur_k):
        if i <= max_5 and kg >= 5:
            karbid += 1
            kg -= 5
        
    #nüüd kasutame väikseid karpe
    for i in range(väike_k):
        if kg != 0:
            karbid +=1
            kg -= 1
    
    if kg == 0:
        return karbid
    else:
        return -1