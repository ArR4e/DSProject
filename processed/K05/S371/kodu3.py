def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    kasutatud_karbid = 0
    while True:
        if suured_karbid == 0:
            break
        if moosi_kogus >= 5:
            moosi_kogus -= 5
            suured_karbid -= 1
            kasutatud_karbid += 1
        if moosi_kogus < 5:
            break
    
    if moosi_kogus == 0:
        return kasutatud_karbid
    if väikesed_karbid >= moosi_kogus:
        kasutatud_karbid += moosi_kogus
        return kasutatud_karbid
    else:
        return -1
    
print(moos(0, 10, 7))