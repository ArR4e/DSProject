def moos(s,v,m):
    arv=0
    if m==0:
        return 0
    if s!=0:
        for el in range(s):
            arv+=1
            m-=5
            s-=1
            if m==0:
                return arv
            if m<5 or s==0:
                break
    if v!=0:    
        for el in range(v):
            arv+=1
            m-=1
            v-=1
            if m==0:
                return arv
            if v<=0:
                return -1
    else:
        return -1
                
