def moos(suur, vaike, kogus):
    if suur * 5 > kogus:
        s_purgid = kogus // 5
        
    else:
        s_purgid = suur
        
    if vaike >= kogus - s_purgid * 5:
        v_purgid = kogus - s_purgid * 5
        return(s_purgid + v_purgid)
    else:
        return(-1)
        
        