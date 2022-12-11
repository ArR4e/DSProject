def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    kasutatud_karbid = 0
    while moosi_kogus > 0:
        if moosi_kogus >= 5 and suured_karbid != 0:
            moosi_kogus -= 5
            suured_karbid -= 1
            kasutatud_karbid += 1
        elif väikesed_karbid != 0:
            moosi_kogus -= 1
            väikesed_karbid -= 1
            kasutatud_karbid += 1
        else:
            break
    if moosi_kogus == 0:
        return kasutatud_karbid
    else:
        return -1
        
