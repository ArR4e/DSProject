def moos(s_karp, v_karp, kogus):
    if s_karp == 0:
        s_vaja = 0
        v_vaja = kogus 
        if v_vaja <= v_karp:
            return v_vaja
        else:
            return -1
    elif (s_karp * 5 + v_karp) < kogus:
        return -1
    else:
        s_vaja = (kogus // 5)
        v_vaja = kogus - s_vaja * 5
        if s_vaja > s_karp:
            v_vaja = kogus - s_karp * 5
            karpide_arv = s_karp + v_vaja
            return karpide_arv
        elif s_vaja <= s_karp and v_vaja <= v_karp:
            karpide_arv = s_vaja + v_vaja
            return karpide_arv
        else:
            return -1
    
#print(moos(1,2,10))