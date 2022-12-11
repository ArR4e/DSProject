def moos(s,v,m):
    k=0
    while s>0 and m>4:
        k+=1
        s-=1
        m-=5
    while v>0 and m>0:
        k+=1
        v-=1
        m-=1
    if m==0:
        return k
    else:
        return(-1)