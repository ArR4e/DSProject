def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    kulunud_karbid = 0
    while True:
        if suured_karbid + väikesed_karbid == 0:
            return -1
        
        if moosi_kogus >= 5 and suured_karbid > 0:
            moosi_kogus -= 5
            suured_karbid -= 1
            kulunud_karbid += 1
        
        elif väikesed_karbid > 0:
            moosi_kogus -= 1
            väikesed_karbid -= 1
            kulunud_karbid += 1
        
        if moosi_kogus == 0:
            return kulunud_karbid
        
        if 0 < moosi_kogus < 5 and väikesed_karbid == 0:
            return -1

print(moos(3,3,4))
            