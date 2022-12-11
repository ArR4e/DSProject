def moos(x, y, z):
    m=z
    karpide_arv=0
    suur_arv=x
    väike_arv=y
    while m>=5 and suur_arv>0:
        m-=5
        suur_arv-=1
        karpide_arv+=1
    while m>0 and väike_arv>0:
        m-=1
        väike_arv-=1
        karpide_arv+=1
    if m==0:
        return(karpide_arv)
    else:
        return(-1)
        
    
