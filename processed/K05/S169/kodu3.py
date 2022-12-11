def moos(suured_karbid,väiksed_karbid,moosi_kogus):
    kasutatud_karbid = 0
    while moosi_kogus > 0:
        while moosi_kogus >= 5 and suured_karbid >0:
            suured_karbid -= 1
            kasutatud_karbid += 1
            moosi_kogus -= 5
        while moosi_kogus >= 1 and väiksed_karbid >0:
            väiksed_karbid -= 1
            kasutatud_karbid += 1
            moosi_kogus -= 1
        if suured_karbid == 0 or väiksed_karbid == 0:
            break
    if moosi_kogus == 0:
        return kasutatud_karbid
    else:
        return -1

print(moos(2,6,14))
            
        