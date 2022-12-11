def moos(suured, väikesed, moosi_kogus):
    if moosi_kogus - suured * 5 - väikesed > 0 or moosi_kogus % 5 > väikesed:
        return -1
    
    kasutatud_karbid = 0
    
    while moosi_kogus > 0: #Tänu eelnevale kontrollile saame siin tsüklis naiivselt eeldada, et ülesanne on lahenduv
        if moosi_kogus < 5:
            kasutatud_karbid += moosi_kogus
            break
        elif suured > 0:
            if moosi_kogus >= 5:
                suured -= 1
                kasutatud_karbid += 1
                moosi_kogus -= 5
        else:
            kasutatud_karbid += moosi_kogus
            break
            
    return kasutatud_karbid
             
            
                