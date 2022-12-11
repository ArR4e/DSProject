def moos(s_karbid, v_karbid, moosi_kogus):
    kasutatud_karbid = 0
    while moosi_kogus >= 5 and s_karbid > 0:
        s_karbid -= 1
        moosi_kogus -= 5
        kasutatud_karbid += 1
    while moosi_kogus >= 1 and v_karbid > 0:
        v_karbid -= 1
        moosi_kogus -= 1
        kasutatud_karbid += 1
    if moosi_kogus > 0:
        return -1
    else:
        return kasutatud_karbid    
