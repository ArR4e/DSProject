def moos(suur,väike,kg):
    purgid=0
    if kg==0:
        return 0
    while suur>0 and kg>=5:
        kg-=5
        purgid+=1
        if kg==0:
            return purgid       
        suur-=1
    while väike>0 and kg>=1:
        kg-=1
        purgid+=1
        if kg==0:
            return purgid
        väike-=1
    else:
        return-1
