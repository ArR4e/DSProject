def moos(suured,väiksed,moosi_kogus):
    jääk = moosi_kogus%5
    s_karbid = (moosi_kogus-jääk)/5
    s_kasutame_karbid = min(s_karbid, suured)
    moosi_alles = moosi_kogus-s_kasutame_karbid*5
    
    
    if väiksed < moosi_alles/1:
        return -1
    if väiksed >= moosi_alles/1:
        return int(moosi_alles+s_kasutame_karbid)
    
    
