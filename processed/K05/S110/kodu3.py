def moos(s,v,kg):
    s_vaja = kg // 5
    s_kasutada = min(s_vaja,s)
    v_vaja = kg - 5*s_kasutada
    
    if v_vaja <= v:
        return s_kasutada + v_vaja
    else:
        return -1