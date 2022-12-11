def moos(suur, vaike, moosikogus):
    karpidearv=0
    if moosikogus>=5:
        karpidearv+=min(moosikogus//5, suur)
        moosikogus-=5*(karpidearv)
    if moosikogus<=vaike:
        karpidearv+=moosikogus
        moosikogus-=moosikogus
    if moosikogus!=0:
        return(-1)
    return(karpidearv)
