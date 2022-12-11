def moos(a, b, jääk):
    vaja = 0
    while a>0 and jääk>=5:
        jääk += -5
        vaja += 1
        a += -1
    while b>0 and jääk>0:
        jääk += -1
        vaja += 1
        b += -1
    if jääk>0:
        return(-1)
    return(vaja)