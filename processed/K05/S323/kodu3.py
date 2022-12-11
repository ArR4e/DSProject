# suur karp = 5kg
# väike karp = 1kg

def moos(s_karbid, v_karbid, moos_kg):
    kasutatud_karbid = 0
    
    #kasutame ära s_karbid:
    while s_karbid > 0 and moos_kg >= 5:
        s_karbid -= 1
        moos_kg -= 5
        kasutatud_karbid += 1
        
    #kui moos ei mahu karpidesse täpselt ära ehk s_karbid jääb üle ja v_karbid tuleb puudu
    if moos_kg > v_karbid:
        return -1
    
    #kasutame ära v_karbid:
    while v_karbid > 0 and moos_kg > 0:
        v_karbid -= 1
        moos_kg -= 1
        kasutatud_karbid += 1
        
    return(kasutatud_karbid)

print(moos(5, 1, 9))