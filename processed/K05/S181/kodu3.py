def moos(s,v,m):
    kasutatud_karbid = 0
    while s>0:
        if m-5 < 0:
            break
        m-=5
        s-=1
        kasutatud_karbid += 1
    while v>0:
        if m-1 < 0:
            break
        m-=1
        v-=1
        kasutatud_karbid += 1
    if (s*5+v) < m:
        return -1
    elif m != 0:
        return -1
    return kasutatud_karbid
    

